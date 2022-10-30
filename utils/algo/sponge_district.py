import json
from functools import reduce
import pandas as pd
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils.algo.rain_generate import rain_generate
from utils.algo.figure_function import fig_rainfall_runoff, fig_vs_single_pollution
from utils.algo.general_functions import check_district_file, check_datetime_setting
from utils.algo.sponge_block import sponge_block_pollution, sponge_block_runoff


class SpongeDistrict:
    def __init__(self) -> None:
        # 仿真起止时间，及时间步长
        self.start_dt_str = "2022-08-21 00:00"
        self.end_dt_str = "2024-08-21 00:00"
        self.Tstep = 1               # time step (hr)
        self.ADP = -1  # 雨前干旱时长（day）

    def assign_params_values():
        return

    def river_sim():
        """河流水文、水质模拟"""
        return

    def sponge_district_sim(self, main, NonPointPollution,
                            GreenRoof, PermeablePavement, BioretentionPonds, ConcaveHerbaceousField,
                            rain_generate_Dialog, block_Dialog, sponge_block_Dialog):
        # 检查城区文件是否导入
        if not check_district_file(main):
            return
        # 加载城区数据
        blocks_map, rivers_map, blocks_rivers_map = load_sponge_district_file(
            main.district_file_path)

        # 将excel文件内容赋值给相应模块的相关参数
        # self.assign_params_values()

        # 面源斑块赋值
        # TODO：这有什么用？
        self.start_dt_str = main.start_dt_str
        self.end_dt_str = main.end_dt_str
        self.Tstep = main.time_step
        # ADP
        # TODO：这有什么用？
        self.ADP = main.ADP
        NonPointPollution.ADP = main.ADP
        GreenRoof.ADP = main.ADP
        PermeablePavement.ADP = main.ADP
        BioretentionPonds.ADP = main.ADP
        ConcaveHerbaceousField.ADP = main.ADP

        # 获取降雨数据
        if hasattr(main, 'weather_file_path'):
            # 天气文件赋值
            NonPointPollution.weather_file_path = main.weather_file_path
            GreenRoof.weather_file_path = main.weather_file_path
            PermeablePavement.weather_file_path = main.weather_file_path
            BioretentionPonds.weather_file_path = main.weather_file_path
            ConcaveHerbaceousField.weather_file_path = main.weather_file_path
            # TODO：之后每个海绵都要加，因为现在只是用NonPointPollution来计算污染，其他海绵都是简化
            NonPointPollution.get_weather_data

            # 检查时间是否正确
            if not check_datetime_setting(main, NonPointPollution.LoopCount,
                                          self.start_dt_str, self.end_dt_str, self.Tstep):
                return
        else:
            # 用默认的雨型
            peak = rain_generate_Dialog.doubleSpinBox_peak.value()
            return_period = rain_generate_Dialog.spinBox_return_period.value()
            duration = rain_generate_Dialog.spinBox_duration.value()
            rain = rain_generate(peak, return_period, duration)
            # 赋值
            NonPointPollution.rainfall = rain
            GreenRoof.rainfall = rain
            PermeablePavement.rainfall = rain
            BioretentionPonds.rainfall = rain
            ConcaveHerbaceousField.rainfall = rain

            NonPointPollution.LoopCount = len(rain)
            GreenRoof.LoopCount = len(rain)
            PermeablePavement.LoopCount = len(rain)
            BioretentionPonds.LoopCount = len(rain)
            ConcaveHerbaceousField.LoopCount = len(rain)

        """每个设施更新下垫面的水文参数"""
        # TODO:这个有什么用？——等单体模型出来了，再用
        GreenRoof.underlyingsurface_loss_list = NonPointPollution.underlyingsurface_loss_list
        GreenRoof.underlyingsurface_infil_list = NonPointPollution.underlyingsurface_infil_list
        PermeablePavement.underlyingsurface_loss_list = NonPointPollution.underlyingsurface_loss_list
        PermeablePavement.underlyingsurface_infil_list = NonPointPollution.underlyingsurface_infil_list
        BioretentionPonds.underlyingsurface_loss_list = NonPointPollution.underlyingsurface_loss_list
        BioretentionPonds.underlyingsurface_infil_list = NonPointPollution.underlyingsurface_infil_list
        ConcaveHerbaceousField.underlyingsurface_loss_list = NonPointPollution.underlyingsurface_loss_list
        ConcaveHerbaceousField.underlyingsurface_infil_list = NonPointPollution.underlyingsurface_infil_list

        """
        城区模拟：
        挨个模拟各个斑块的径流、污染
        挨个模拟各个海绵地块的径流、污染
        """
        # 面源斑块比例处理
        blocks_area, confluence_ratio, sponges_area = self.cal_sponge_block_area(
            blocks_map)
        sponges_type = ["GR", "BRP", "PP", "CHF", "TD"]
        # 遍历地块
        series_len = NonPointPollution.LoopCount
        block_num = len(blocks_map)
        # 无海绵
        non_sponge_block = np.zeros(
            (block_num, series_len, 6))  # (Block, Time, Feature)
        sponge_block = np.zeros_like(non_sponge_block)
        # 有海绵
        blocks_type = blocks_map.values[:, 2:4]
        for b in range(blocks_area.shape[0]):
            sponge_tpye_area_map = dict(zip(sponges_type, sponges_area[b]))
            lu_ind, us_ind = int(blocks_type[b, 0]), int(blocks_type[b, 1])

            # 地块模拟：斑块 & 海绵
            # TODO：考虑self.result的最终模拟结果保存方式，现在只有单个地块的
            result = self.block_sim(
                NonPointPollution, GreenRoof, PermeablePavement, BioretentionPonds, ConcaveHerbaceousField,
                blocks_area[b], sponge_tpye_area_map, lu_ind, us_ind)

            # 模拟结果后处理
            non_sponge_block[b, :, 0] = result["无海绵"]["径流量(mm/min)"]
            non_sponge_block[b, :, 1] = result["无海绵"]["SS浓度"]
            non_sponge_block[b, :, 2] = result["无海绵"]["COD浓度"]
            non_sponge_block[b, :, 3] = result["无海绵"]["TP浓度"]
            non_sponge_block[b, :, 4] = result["无海绵"]["TN浓度"]
            non_sponge_block[b, :, 5] = result["无海绵"]["NH3N浓度"]
            sponge_block[b, :, 0] = result["海绵"]["径流量(mm/min)"]
            sponge_block[b, :, 1] = result["海绵"]["SS浓度"]
            sponge_block[b, :, 2] = result["海绵"]["COD浓度"]
            sponge_block[b, :, 3] = result["海绵"]["TP浓度"]
            sponge_block[b, :, 4] = result["海绵"]["TN浓度"]
            sponge_block[b, :, 5] = result["海绵"]["NH3N浓度"]

        """
        根据径流时间序列，迭代受纳河流的径流、污染变化情况
        一次迭代需要3步：
        1. 地块->河段（输入可以分两步吗？）
        2. 上河段->下河段（会横跨两个吗？）
        3. 支流->主干
        """
        non = non_sponge_block[4, 45, 0]
        have = sponge_block[4, 45, 0]
        non_sponge_rivers = self.init_rivers_info(rivers_map, series_len)
        sponge_rivers = self.init_rivers_info(rivers_map, series_len)
        non_sponge_rivers = self.sim_river(blocks_rivers_map, rivers_map,
                                           blocks_area, confluence_ratio,
                                           non_sponge_block, non_sponge_rivers)
        sponge_rivers = self.sim_river(blocks_rivers_map, rivers_map,
                                       blocks_area, confluence_ratio,
                                       sponge_block, sponge_rivers)

        # TODO：临时保存用于测试
        # Save
        np.save('non_sponge_rivers.npy', non_sponge_rivers)
        np.save('sponge_rivers.npy', sponge_rivers)

        """结果可视化"""
        # self.show_sponge_block(main, rain, runoff, pollution,
        #                        sponge_runoff, sponge_pollution, NonPointPollution.start_dt_str)

        QMessageBox.information(main, '运行完毕', '海绵城区仿真已完成！')
        main.sponge_district_sim_flag = True

    def sim_river(self, blocks_rivers_map, rivers_map,
                  blocks_area, confluence_ratio, blocks, rivers):
        rivers_np = rivers_map.values
        blocks_rivers_np = blocks_rivers_map.values
        # 按照block排序
        blocks_rivers_np = blocks_rivers_np[blocks_rivers_np[:, 0].argsort()]

        series_len = blocks.shape[1]
        seg_num = rivers_np.shape[0]
        for t in range(series_len):
            for s in range(seg_num):
                """
                获取地块的输入,Q_block(地块), Q_neighbor(上游), Q_branch(分支)
                """
                # 当前河流-河段的详细信息
                river_info = rivers_np[s, :]
                """考虑地块的影响"""
                # 定位行索引
                block_index = self.locate_index(
                    blocks_rivers_np[:, 1:], river_info[:4])
                # 判断是否有地块
                block_flag = True if len(block_index) else False
                if block_flag:
                    # 计算多个地块的输入
                    Q_block = []
                    C_block = []
                    for b_ind in block_index:
                        # TODO：block输入到河流的量是多少？
                        # 地块流量 mm/h -> m3/min
                        area = blocks_area[b_ind]
                        ratio = confluence_ratio[b_ind]
                        Q_b = blocks[b_ind, t, 0]
                        Q_block.append(Q_b / 1000/60 * area*ratio)
                        # 地块浓度
                        C_block.append(blocks[b_ind, t, 1:6])  # 地块5种污染物浓度
                else:

                    Q_block = 0
                    C_block = np.zeros(5)

                """考虑河流邻域(neighbor)、分支(branch)的影响"""
                main_id = int(river_info[0])
                main_seg_id = int(river_info[1])
                if river_info[3] == 0:  # 主干
                    if t == 0 or main_seg_id == 1:
                        Q_neighbor = river_info[8]  # 基流流量
                        C_neighbor = river_info[14:19]  # 5种污染物浓度
                    else:
                        Q_neighbor_pred = rivers[main_id]["流量"]["主干"][t -
                                                                      1, main_seg_id-1-1]
                        C_neighbor_pred = []
                        for k in rivers[main_id]["浓度"].keys():
                            C_neighbor_pred.append(
                                rivers[main_id]["浓度"][k]["主干"][t-1, main_seg_id-1-1])
                        C_neighbor_pred = np.array(C_neighbor_pred)

                        Q_neighbor = Q_neighbor_pred
                        C_neighbor = C_neighbor_pred

                    # branch
                    ids_list = [main_id, main_seg_id]
                    branch_index = self.locate_index(rivers_np, ids_list)
                    branch_len = len(branch_index) - 1  # 减掉1条主干河段
                    branch_flag = True if branch_len else False
                    if branch_flag:
                        branch_info = rivers_np[branch_index[-1], :]
                        if t == 0:
                            Q_branch = branch_info[8]  # 基流流量
                            C_branch = branch_info[14:19]  # 5种污染物浓度
                        else:
                            Q_branch_pred = rivers[main_id]["流量"]["支流%d" % (branch_info[2])][t -
                                                                                             1, -1]
                            C_branch_pred = []
                            for k in rivers[main_id]["浓度"].keys():
                                C_branch_pred.append(
                                    rivers[main_id]["浓度"][k]["支流%d" % (branch_info[2])][t -
                                                                                        1, -1])
                            C_branch_pred = np.array(C_branch_pred)

                            Q_branch = Q_branch_pred
                            C_branch = C_branch_pred
                    else:
                        Q_branch = 0
                        C_branch = np.zeros(5)

                else:  # 支流
                    branch_id = int(river_info[2])
                    branch_seg_id = int(river_info[3])

                    # 如果是初始时刻 或 初始河段，采用基础流量和浓度
                    if t == 0 or branch_seg_id == 1:
                        Q_neighbor = river_info[8]  # 基流流量
                        C_neighbor = river_info[14:19]  # 5种污染物浓度
                    else:
                        Q_neighbor_pred = rivers[main_id]["流量"]["支流%d" %
                                                                (branch_id)][t-1, branch_seg_id-1-1]
                        C_neighbor_pred = []
                        for k in rivers[main_id]["浓度"].keys():
                            C_neighbor_pred.append(
                                rivers[main_id]["浓度"][k]["支流%d" % (
                                    branch_id)][t-1, branch_seg_id-1-1])
                        C_neighbor_pred = np.array(C_neighbor_pred)

                        Q_neighbor = Q_neighbor_pred
                        C_neighbor = C_neighbor_pred

                    Q_branch = 0
                    C_branch = np.zeros(5)

                """一维水文、水质模型，计算浓度和流量"""
                # 河段参数
                X = river_info[4]  # 河长
                N = river_info[5]  # 粗糙系数
                J = river_info[6]  # 底坡
                B = river_info[7]  # 河宽
                K = river_info[9:14]  # 5种污染物降解系数

                C = one_dimensional_river_water_quality_model(
                    Q_neighbor, Q_block, Q_branch,
                    C_neighbor, C_block, C_branch,
                    N, J, B, K, X)
                Q = one_dimensional_river_hydrological_model(
                    Q_neighbor, Q_block, Q_branch)

                """更新：流量、浓度"""
                if river_info[3] == 0:  # 主干
                    rivers[main_id]["流量"]["主干"][t, main_seg_id-1] = Q

                    for i, k in enumerate(rivers[main_id]["浓度"].keys()):
                        rivers[main_id]["浓度"][k]["主干"][t, main_seg_id-1] = C[i]
                else:  # 支流
                    rivers[main_id]["流量"]["支流%d" %
                                          (branch_id)][t, branch_seg_id-1] = Q
                    polution_metrics = list(rivers[main_id]["浓度"].keys())
                    for i, k in enumerate(polution_metrics):
                        rivers[main_id]["浓度"][k]["支流%d" %
                                                 (branch_id)][t, branch_seg_id-1] = C[i]
        return rivers

    def sim_block_to_river(self, blocks_rivers_map, rivers_map, blocks, rivers):
        rivers_np = rivers_map.values
        blocks_rivers_np = blocks_rivers_map.values
        # 按照block排序
        blocks_rivers_np = blocks_rivers_np[blocks_rivers_np[:, 0].argsort()]
        # block排到河流的某个河段 (B,T,Feat)
        block_num = blocks.shape[0]
        series_len = blocks.shape[1]
        for t in range(series_len):
            for b in range(block_num):
                """
                获取地块的输入,Q_block(地块), Q_neighbor(上游), Q_branch(分支)
                """
                Q_block = blocks[b, t, 0]  # 地块流量
                C_block = blocks[b, t, 1:6]  # 地块5种污染物浓度
                # 获取地块-河段关系
                if blocks_rivers_np[b, 3] == 0:  # 主干
                    main_id = blocks_rivers_np[b, 1]
                    main_seg_id = blocks_rivers_np[b, 2]
                    branch_id = 0  # 非支流
                    ids_list = [main_id, main_seg_id, branch_id]
                    # 定位行索引
                    block_index = self.locate_index(rivers_np, ids_list)
                    # 获取基流
                    river_info = rivers_np[block_index[0], :]
                    if t == 0 or main_seg_id == 1:
                        Q_neighbor = river_info[8]  # 基流流量
                        C_neighbor = river_info[14:19]  # 5种污染物浓度
                    else:
                        Q_neighbor_pred = rivers[main_id]["流量"]["主干"][t -
                                                                      1, main_seg_id-1-1]
                        C_neighbor_pred = []
                        for k in rivers[main_id]["浓度"].keys():
                            C_neighbor_pred.append(
                                rivers[main_id]["浓度"][k]["主干"][t-1, main_seg_id-1-1])
                        C_neighbor_pred = np.array(C_neighbor_pred)

                        Q_neighbor = Q_neighbor_pred
                        C_neighbor = C_neighbor_pred

                    # branch
                    ids_list = [main_id, main_seg_id]
                    branch_index = self.locate_index(rivers_np, ids_list)
                    branch_len = len(branch_index) - 1
                    branch_flag = True if branch_len else False
                    if branch_flag:
                        if t == 0:
                            branch_info = rivers_np[branch_index[-1], :]
                            Q_branch = branch_info[8]  # 基流流量
                            C_branch = branch_info[14:19]  # 5种污染物浓度
                        else:
                            Q_branch_pred = rivers[main_id]["流量"]["支流%d" % (branch_index[-1])][t -
                                                                                               1, -1]
                            C_branch_pred = []
                            for k in rivers[main_id]["浓度"].keys():
                                C_branch_pred.append(
                                    rivers[main_id]["浓度"][k]["支流%d" % (branch_index[-1])][t -
                                                                                          1, -1])
                            C_branch_pred = np.array(C_branch_pred)

                            Q_branch = Q_branch_pred
                            C_branch = C_branch_pred
                    else:
                        Q_branch = 0
                        C_branch = 0
                else:  # 支流
                    main_id = blocks_rivers_np[b, 1]
                    main_seg_id = blocks_rivers_np[b, 2]
                    branch_id = blocks_rivers_np[b, 3]
                    branch_seg_id = blocks_rivers_np[b, 4]
                    ids_list = [main_id, main_seg_id, branch_id, branch_seg_id]
                    # 定位行索引
                    block_index = self.locate_index(rivers_np, ids_list)
                    # 获取基流
                    river_info = rivers_np[block_index[0], :]
                    # 如果是初始时刻 或 初始河段，采用基础流量和浓度
                    if t == 0 or branch_seg_id == 1:
                        Q_neighbor = river_info[8]  # 基流流量
                        C_neighbor = river_info[14:19]  # 5种污染物浓度
                    else:
                        Q_neighbor_pred = rivers[main_id]["流量"]["支流%d" %
                                                                (branch_id)][t-1, branch_seg_id-1-1]
                        C_neighbor_pred = []
                        for k in rivers[main_id]["浓度"].keys():
                            C_neighbor_pred.append(
                                rivers[main_id]["浓度"][k]["支流%d" % (
                                    branch_id)][t-1, branch_seg_id-1-1])
                        C_neighbor_pred = np.array(C_neighbor_pred)

                        Q_neighbor = Q_neighbor_pred
                        C_neighbor = C_neighbor_pred

                    Q_branch = 0
                    C_branch = np.zeros(5)

                """一维水文、水质模型，计算浓度和流量"""
                # 河段参数
                X = river_info[4]  # 河长
                N = river_info[5]  # 粗糙系数
                J = river_info[6]  # 底坡
                B = river_info[7]  # 河宽
                K = river_info[9:14]  # 5种污染物降解系数

                C = one_dimensional_river_water_quality_model(
                    Q_neighbor, Q_block, Q_branch,
                    C_neighbor, C_block, C_branch,
                    N, J, B, K, X)
                Q = one_dimensional_river_hydrological_model(
                    Q_neighbor, Q_block, Q_branch)

                """更新：流量、浓度"""
                if blocks_rivers_np[b, 3] == 0:  # 主干
                    rivers[main_id]["流量"]["主干"][t, main_seg_id-1] = Q

                    for i, k in enumerate(rivers[main_id]["浓度"].keys()):
                        rivers[main_id]["浓度"][k]["主干"][t, main_seg_id-1] = C[i]
                else:  # 支流
                    rivers[main_id]["流量"]["支流%d" %
                                          (branch_id)][t, branch_seg_id-1] = Q

                    for i, k in enumerate(rivers[main_id]["浓度"].keys()):
                        rivers[main_id]["浓度"][k]["支流%d" %
                                                 (branch_id)][t, branch_seg_id-1] = C[i]
        return rivers

    def locate_index(self, data, ids):
        """locate_index 获取满足多列条件的行索引

        _extended_summary_

        Args:
            data (_type_): _description_
            ids (_type_): _description_

        Returns:
            _type_: _description_
        """
        index_list = []
        for i, id in enumerate(ids):
            index_list.append(np.where(data[:, i] == id)[0])

        index = reduce(np.intersect1d, tuple(index_list))

        return index

    def init_rivers_info(self, rivers_map, series_len):
        """init_rivers_info 构建河流数据结构

        _extended_summary_

        Args:
            rivers_map (_type_): _description_
            series_len (_type_): _description_

        Returns:
            _type_: _description_
        """
        rivers_results = {}
        rivers_map_np = rivers_map.values
        river_ids = np.unique(rivers_map_np[:, 0]).astype(int)
        for river_i in river_ids:
            info_river_i = rivers_map_np[rivers_map_np[:, 0] == river_i, 1:4]
            # 河段数量
            seg_ids = np.unique(info_river_i[:, 0])
            seg_num = len(seg_ids)
            # 支流数量
            branch_num = len(np.unique(info_river_i[:, 1])) - 1

            # 初始化第i条河流信息
            rivers_results[river_i] = {}
            # ###主干
            # 流量
            rivers_results[river_i]["流量"] = {
                "主干": np.zeros((series_len, seg_num))}
            # 浓度
            rivers_results[river_i]["浓度"] = {}
            rivers_results[river_i]["浓度"]["SS"] = {
                "主干": np.zeros((series_len, seg_num))}
            rivers_results[river_i]["浓度"]["COD"] = {
                "主干": np.zeros((series_len, seg_num))}
            rivers_results[river_i]["浓度"]["TP"] = {
                "主干": np.zeros((series_len, seg_num))}
            rivers_results[river_i]["浓度"]["TN"] = {
                "主干": np.zeros((series_len, seg_num))}
            rivers_results[river_i]["浓度"]["NH3H"] = {
                "主干": np.zeros((series_len, seg_num))}

            # 每个支流的河段数量
            branch_seg = {}
            for branch_i in range(1, branch_num+1):
                info_seg_i = info_river_i[info_river_i[:, 1] == branch_i, 2]
                branch_seg_ids = np.unique(info_seg_i)
                branch_seg_num = len(branch_seg_ids)

                # ### 支流
                rivers_results[river_i]["流量"]["支流%d" % (branch_i)] = np.zeros(
                    (series_len, branch_seg_num))
                rivers_results[river_i]["浓度"]["SS"]["支流%d" % (branch_i)] = np.zeros(
                    (series_len, branch_seg_num))
                rivers_results[river_i]["浓度"]["COD"]["支流%d" % (branch_i)] = np.zeros(
                    (series_len, branch_seg_num))
                rivers_results[river_i]["浓度"]["TP"]["支流%d" % (branch_i)] = np.zeros(
                    (series_len, branch_seg_num))
                rivers_results[river_i]["浓度"]["TN"]["支流%d" % (branch_i)] = np.zeros(
                    (series_len, branch_seg_num))
                rivers_results[river_i]["浓度"]["NH3H"]["支流%d" % (branch_i)] = np.zeros(
                    (series_len, branch_seg_num))

        return rivers_results

    def cal_sponge_block_area(self, blocks_map):
        """将海绵组成比例转换为实际面积"""
        blocks_area = blocks_map["地块面积"].values
        confluence_ratio = blocks_map["汇流比例"].values
        sponges_ratio = blocks_map.values[:, -5:]

        sponges_area = blocks_area * sponges_ratio.T
        sponges_area = sponges_area.T / 100
        cover_times = 10.0
        sponges_area[:, 1] = sponges_area[:, 1] * cover_times
        sponges_area[:, 3] = sponges_area[:, 3] * cover_times

        return blocks_area, confluence_ratio, sponges_area

    def block_sim(self, NonPointPollution, GreenRoof, PermeablePavement, BioretentionPonds, ConcaveHerbaceousField,
                  block_area, sponge_tpye_area_map, lu_ind, us_ind):
        """单位面积过程仿真，并返回结果"""

        # 土地利用类型
        NonPointPollution.landuse_type = NonPointPollution.landuse_type_list[lu_ind-1]
        # 下垫面类型
        NonPointPollution.underlyingsurface_type = NonPointPollution.underlyingsurface_type_list[
            us_ind-1]

        # 每个设施、面源斑块模拟
        rain, runoff, pollution = NonPointPollution.sim
        # TODO：临时用这些sim，之后要改的
        GR_runoff, GR_pollution = GreenRoof.sim(runoff, pollution)
        PP_runoff, PP_pollution = PermeablePavement.sim(runoff, pollution)
        BRP_runoff, BRP_pollution = BioretentionPonds.sim(runoff, pollution)
        CHF_runoff, CHF_pollution = ConcaveHerbaceousField.sim(
            runoff, pollution)

        # 计算斑块径流
        sponge_runoff = sponge_block_runoff(block_area,
                                            sponge_tpye_area_map=sponge_tpye_area_map,
                                            TD=runoff,
                                            GR=GR_runoff,
                                            PP=PP_runoff,
                                            BRP=BRP_runoff,
                                            CHF=CHF_runoff,)
        # 计算斑块污染
        sponge_pollution = sponge_block_pollution(block_area,
                                                  sponge_tpye_area_map=sponge_tpye_area_map,
                                                  TD=pollution,
                                                  GR=GR_pollution,
                                                  PP=PP_pollution,
                                                  BRP=BRP_pollution,
                                                  CHF=CHF_pollution,
                                                  )
        result = {"降雨强度(mm/min)": rain,
                  "无海绵": {
                      "径流量(mm/min)": runoff[:, 0],
                  },
                  "海绵": {
                      "径流量(mm/min)": sponge_runoff,
                  },
                  }
        for name, val in sponge_pollution.items():
            result["海绵"][name+"浓度"] = val
        for name, val in pollution.items():
            result["无海绵"][name+"浓度"] = val

        return result


def load_sponge_district_file(file_path):
    io = pd.io.excel.ExcelFile(file_path)
    block_river_map = pd.read_excel(io, sheet_name='地块-河流')
    rivers_map = pd.read_excel(io, sheet_name='主干-支流')
    block_map = pd.read_excel(io, sheet_name='地块')
    io.close()

    return block_map, rivers_map, block_river_map


def river_velocity_model(n, R, J):
    u = 1 / n * np.power(R, 2/3) * np.power(J, 1/2)

    return u


def one_dimensional_river_water_quality_model(
        Q_neighbor, Q_block, Q_branch,
        C_neighbor, C_block, C_branch,
        n, J, b, k, x):

    # 流速计算
    Q = one_dimensional_river_hydrological_model(Q_neighbor, Q_block, Q_branch)
    h_t = Q / b
    R = h_t
    u = river_velocity_model(n, R, J)
    # 浓度计算
    if isinstance(Q_block, list):
        Q_block, C_block = np.array(Q_block), np.array(C_block)
        C_ = (Q_neighbor*C_neighbor
              + Q_block.dot(C_block)
              + Q_branch * C_branch) / Q
    else:
        C_ = (Q_neighbor*C_neighbor
              + Q_block*C_block
              + Q_branch * C_branch) / Q

    C = C_ * np.exp(-k*x/u)

    return C


def one_dimensional_river_hydrological_model(Q_neighbor, Q_block, Q_branch):
    if isinstance(Q_block, list):
        Q = Q_neighbor+sum(Q_block)+Q_branch
    else:
        Q = Q_neighbor+Q_block+Q_branch

    return Q
