import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils.algo.rain_generate import rain_generate
from utils.algo.figure_function import fig_rainfall_runoff, fig_vs_single_pollution
from utils.algo.general_functions import check_datetime_setting


class NonPointControl:
    def __init__(self) -> None:
        pass

    def sponge_block_sim(self, main, NonPointPollution,
                         GreenRoof, PermeablePavement, BioretentionPonds, ConcaveHerbaceousField,
                         rain_generate_Dialog, block_Dialog, sponge_block_Dialog):
        # 面源斑块赋值
        self.start_dt_str = main.start_dt_str
        self.end_dt_str = main.end_dt_str
        self.Tstep = main.time_step

        if hasattr(main, 'weather_file_path'):
            # 天气文件赋值
            NonPointPollution.weather_file_path = main.weather_file_path
            GreenRoof.weather_file_path = main.weather_file_path
            PermeablePavement.weather_file_path = main.weather_file_path
            BioretentionPonds.weather_file_path = main.weather_file_path
            ConcaveHerbaceousField.weather_file_path = main.weather_file_path

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

        """单位面积过程仿真，并返回结果"""
        # 每个设施、面源斑块模拟
        rain, runoff, pollution = NonPointPollution.sim
        GR_runoff, GR_pollution = GreenRoof.sim(runoff, pollution)
        PP_runoff, PP_pollution = PermeablePavement.sim(runoff, pollution)
        BRP_runoff, BRP_pollution = BioretentionPonds.sim(runoff, pollution)
        CHF_runoff, CHF_pollution = ConcaveHerbaceousField.sim(
            runoff, pollution)

        # 面源斑块比例处理
        block_area, sponge_tpye_area_map = self.cal_sponge_block_area(
            sponge_block_Dialog)

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

        """结果可视化"""
        self.show_sponge_block(main, rain, runoff, pollution,
                               sponge_runoff, sponge_pollution, NonPointPollution.start_dt_str)

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
