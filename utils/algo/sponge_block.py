import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils.algo.rain_generate import rain_generate
from utils.algo.figure_function import fig_rainfall_runoff, fig_vs_single_pollution
from utils.algo.general_functions import check_datetime_setting


class NonPointControl:
    def __init__(self) -> None:
        # 仿真起止时间，及时间步长
        self.start_dt_str = "2022-08-21 00:00"
        self.end_dt_str = "2024-08-21 00:00"
        self.Tstep = 1               # time step (hr)
        self.ADP = -1  # 雨前干旱时长（day）

    def pack_params(self, sponge_block_Dialog, NonPointPollution):

        # 地块类型 与 降雨数据
        sponge_tpye_ratio_map = self.cal_sponge_block_ratio(
            sponge_block_Dialog)
        params_dict = {
            "地块类型": {
                "土地利用类型": sponge_block_Dialog.lineEdit_landuse.text(),
                "下垫面类型": sponge_block_Dialog.lineEdit_underlying.text(),
                "地块面积": sponge_block_Dialog.spinBox_area.value(),
            },
            # TODO："雨型生成"指标
        }
        # 海绵类型
        params_dict["海绵比例"] = {}
        for sponge, ratio in sponge_tpye_ratio_map.items():
            params_dict["海绵比例"][sponge] = ratio

        # 污染物参数
        lu_ind = np.where(NonPointPollution.landuse_type_list ==
                          NonPointPollution.landuse_type)[0][0]
        us_ind = np.where(NonPointPollution.underlyingsurface_type_list ==
                          NonPointPollution.underlyingsurface_type)[0][0]
        params_dict["污染物参数"] = {}
        for p_name, param in NonPointPollution.Pollution_dict.items():
            params_dict["污染物参数"][p_name] = {}
            for p, v in param.items():
                if p in ["Bmax", "bt"]:
                    params_dict["污染物参数"][p_name][p] = v[lu_ind]
                else:
                    params_dict["污染物参数"][p_name][p] = v[us_ind]

        return params_dict

    def sponge_block_sim(self, main, NonPointPollution,
                         GreenRoof, PermeablePavement, BioretentionPonds, ConcaveHerbaceousField,
                         rain_generate_Dialog, block_Dialog, sponge_block_Dialog):
        # 面源斑块赋值
        self.start_dt_str = main.start_dt_str
        self.end_dt_str = main.end_dt_str
        self.Tstep = main.time_step
        # ADP
        self.ADP = main.ADP
        NonPointPollution.ADP = main.ADP
        GreenRoof.ADP = main.ADP
        PermeablePavement.ADP = main.ADP
        BioretentionPonds.ADP = main.ADP
        ConcaveHerbaceousField.ADP = main.ADP

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

        # 判断是否选择下垫面类型
        if block_Dialog.comboBox_landuse.currentText() == "请选择":
            QMessageBox.critical(
                block_Dialog,
                '错误',
                "请选择土地利用类型！")
            return
        if block_Dialog.comboBox_underlyingsurface.currentText() == "请选择":
            QMessageBox.critical(
                block_Dialog,
                '错误',
                "请选择下垫面类型！")
            return

        """每个设施更新下垫面的水文参数"""
        GreenRoof.underlyingsurface_loss_list = NonPointPollution.underlyingsurface_loss_list
        GreenRoof.underlyingsurface_infil_list = NonPointPollution.underlyingsurface_infil_list
        PermeablePavement.underlyingsurface_loss_list = NonPointPollution.underlyingsurface_loss_list
        PermeablePavement.underlyingsurface_infil_list = NonPointPollution.underlyingsurface_infil_list
        BioretentionPonds.underlyingsurface_loss_list = NonPointPollution.underlyingsurface_loss_list
        BioretentionPonds.underlyingsurface_infil_list = NonPointPollution.underlyingsurface_infil_list
        ConcaveHerbaceousField.underlyingsurface_loss_list = NonPointPollution.underlyingsurface_loss_list
        ConcaveHerbaceousField.underlyingsurface_infil_list = NonPointPollution.underlyingsurface_infil_list

        # 面源斑块比例处理
        block_area, sponge_tpye_area_map = self.cal_sponge_block_area(
            sponge_block_Dialog)
        """地块模拟"""
        self.result,  runoff, pollution, sponge_runoff, sponge_pollution = self.sim(
            NonPointPollution, GreenRoof, PermeablePavement, BioretentionPonds, ConcaveHerbaceousField,
            block_area, sponge_tpye_area_map)
        """结果可视化"""
        self.show_sponge_block(main, rain, runoff, pollution,
                               sponge_runoff, sponge_pollution, NonPointPollution.start_dt_str)

        QMessageBox.information(main, '运行完毕', '仿真已完成！')
        main.sponge_block_sim_flag = True

    def sim(self, NonPointPollution, GreenRoof, PermeablePavement, BioretentionPonds, ConcaveHerbaceousField,
            block_area, sponge_tpye_area_map):
        # 单位面积过程仿真，并返回结果
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
                                            CHF=CHF_runoff,
                                            )
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
                  "无海绵径流量(mm/min)": runoff[:, 0],
                  "海绵径流量(mm/min)": sponge_runoff,
                  }
        for name, val in sponge_pollution.items():
            result[name+"浓度"] = val

        return result,  runoff, pollution, sponge_runoff, sponge_pollution

    def cal_sponge_block_area(self, sponge_block_Dialog):
        """面源斑块比例处理"""
        tableWidget = sponge_block_Dialog.tableWidget_sponge_setting
        sponge_type_list = ["GR", "BRP", "PP", "CHF", "TD"]
        sponge_area_list = [int(tableWidget.item(i, 1).text())
                            for i in range(tableWidget.rowCount())]
        block_area = sponge_block_Dialog.spinBox_area.value()
        traditional_area = block_area - sum(sponge_area_list)
        sponge_area_list.append(traditional_area)
        sponge_tpye_area_map = dict(
            zip(sponge_type_list, sponge_area_list))

        return block_area, sponge_tpye_area_map

    def cal_sponge_block_ratio(self, sponge_block_Dialog):
        """面源斑块比例处理"""
        tableWidget = sponge_block_Dialog.tableWidget_sponge_setting
        sponge_type_list = ["绿色屋顶", "生物滞留池", "渗透铺装", "下凹式绿地", "传统斑块"]
        sponge_ratio_list = [int(tableWidget.item(i, 0).text())
                             for i in range(tableWidget.rowCount())]

        traditional_ratio = 100 - sum(sponge_ratio_list)
        sponge_ratio_list.append(traditional_ratio)
        sponge_tpye_ratio_map = dict(
            zip(sponge_type_list, sponge_ratio_list))

        return sponge_tpye_ratio_map

    def show_sponge_block(self, main, rain, runoff, pollution, sponge_runoff, sponge_pollution, start_dt_str):
        """rain_runoff"""
        runoff = np.concatenate(
            (runoff.reshape(-1, 1), sponge_runoff.reshape(-1, 1)), axis=1)
        F_rain_runoff = fig_rainfall_runoff(rain, runoff, name_list=["斑块", "海绵"],
                                            width=main.sponge_block_rainfallrunoff_sim_res_rainfall.width(),
                                            height=main.sponge_block_rainfallrunoff_sim_res_rainfall.height(),
                                            start_dt_str=start_dt_str,
                                            freq="1min")
        # 将图形元素添加到场景中
        main.scene_sponge_rain_runoff = QGraphicsScene()
        main.scene_sponge_rain_runoff.addWidget(F_rain_runoff)
        main.sponge_block_rainfallrunoff_sim_res_rainfall.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.sponge_block_rainfallrunoff_sim_res_rainfall.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.sponge_block_rainfallrunoff_sim_res_rainfall.setScene(
            main.scene_sponge_rain_runoff)  # 将创建添加到图形视图显示窗口

        """pollution"""
        # 创建与获取场景
        main.scene_sponge_pollution_SS = QGraphicsScene()
        main.scene_sponge_pollution_COD = QGraphicsScene()
        main.scene_sponge_pollution_TP = QGraphicsScene()
        main.scene_sponge_pollution_TN = QGraphicsScene()
        main.scene_sponge_pollution_NH3N = QGraphicsScene()
        scene_list = [[main.sponge_block_pollution_sim_res_rainfall_SS, main.scene_sponge_pollution_SS],
                      [main.sponge_block_pollution_sim_res_rainfall_COD,
                          main.scene_sponge_pollution_COD],
                      [main.sponge_block_pollution_sim_res_rainfall_TP,
                          main.scene_sponge_pollution_TP],
                      [main.sponge_block_pollution_sim_res_rainfall_TN,
                          main.scene_sponge_pollution_TN],
                      [main.sponge_block_pollution_sim_res_rainfall_NH3N,
                          main.scene_sponge_pollution_NH3N],
                      ]

        # 获取污染物种类
        pp_metric = list(pollution.keys())
        # 逐个污染物画图
        for i, p in enumerate(pp_metric):
            if i >= len(scene_list):
                # TODO:给未来自定义污染物时用
                pass
            vs_pollution = np.concatenate(
                (pollution[p].reshape(-1, 1), sponge_pollution[p].reshape(-1, 1)), axis=1)
            F_pollution = fig_vs_single_pollution(p, vs_pollution, name_list=["斑块", "海绵"],
                                                  width=scene_list[i][0].width(
            ),
                height=scene_list[i][0].height(
            ),
                start_dt_str=start_dt_str,
                freq="1min")
            # 将图形元素添加到场景中
            scene_list[i][1].addWidget(F_pollution)  # 将图形元素添加到场景中
            scene_list[i][0].setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scene_list[i][0].setHorizontalScrollBarPolicy(
                Qt.ScrollBarAlwaysOff)
            scene_list[i][0].setScene(scene_list[i][1])  # 将创建添加到图形视图显示窗口


def sponge_block_pollution(area, sponge_tpye_area_map, **kwargs):
    first_type = list(kwargs.keys())[0]
    pollution_metric = list(kwargs[first_type].keys())
    series_step = kwargs[first_type][pollution_metric[0]].shape[0]
    pollution = dict(zip(pollution_metric, np.zeros(series_step)))

    for key, val in kwargs.items():
        w = sponge_tpye_area_map[key] / area  # 计算权重

        for p in pollution.keys():
            pollution[p] += w * val[p]

    return pollution


def sponge_block_runoff(area, sponge_tpye_area_map, **kwargs):
    first_type = list(kwargs.keys())[0]
    series_step = kwargs[first_type].shape[0]
    overall_runoff = np.zeros(series_step)

    for key, val in kwargs.items():
        w = sponge_tpye_area_map[key] / area  # 计算权重
        overall_runoff = overall_runoff + w * val[:, 0]

    return overall_runoff
