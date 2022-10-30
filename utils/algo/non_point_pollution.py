from pydoc import pager
import pandas as pd
import numpy as np
from collections import namedtuple
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene
from utils.algo.rain_generate import rain_generate
from utils.algo.figure_function import fig_rainfall, fig_runoff, fig_pollution
from utils.algo.general_functions import check_datetime_setting


class Struct(object):
    def __new__(cls, data):
        if isinstance(data, dict):
            return namedtuple(
                'struct', data.keys()
            )(
                *(Struct(val) for val in data.values())
            )
        elif isinstance(data, (tuple, list, set, frozenset)):
            return type(data)(Struct(_) for _ in data)
        else:
            return data


class NonPointPollution:
    def __init__(self, weather_file_path="") -> None:
        default_params_file_path = 'data/non_point_pollution/non_point_pollution_params.xlsx'
        pollutantdata, ludata, usdata = self.load_block_default_params(
            default_params_file_path)
        lutype, ustype, pltype, usloss, usinfil, P, struct_P = self.preprocess_block_params(
            ludata, usdata, pollutantdata)

        self.landuse_type_list = lutype
        self.underlyingsurface_type_list = ustype
        self.pollution_type_list = pltype

        self.underlyingsurface_loss_list = usloss
        self.underlyingsurface_infil_list = usinfil

        self.Pollution_dict = P
        self.Pollution = struct_P

        # 仿真起止时间，及时间步长
        self.start_dt_str = "2022-08-21 00:00"
        self.end_dt_str = "2024-08-21 00:00"
        self.Tstep = 1               # time step (hr)
        self.ADP = -1  # 雨前干旱时长（day）

        self.rainfall = None  # 降雨量，mm/hr
        # 设置循环长度
        self.LoopCount = 0

        # 文件路径
        self.weather_file_path = ''
        # self.weather_file_path = weather_file_path

    @property
    def get_weather_data(self):
        # 输入计算蒸散发所需的气象数据
        data = np.loadtxt(self.weather_file_path)
        self.rainfall = data[:]  # 降雨量，mm/hr

        # 设置循环长度
        self.LoopCount = len(data)

    def change_landuse_params(self, block_Dialog):
        """根据 landuse_type 改变显示的参数值"""
        landuse_type = block_Dialog.comboBox_landuse.currentText()
        if landuse_type == "请选择":
            QMessageBox.critical(
                block_Dialog,
                '错误',
                "请选择土地利用类型！")
            return
        # 获取土地利用类型对应的索引
        lu_ind = np.where(self.landuse_type_list == landuse_type)[0][0]

        # Bmax
        block_Dialog.doubleSpinBox_Bmax_SS.setValue(
            self.Pollution.SS.Bmax[lu_ind])
        block_Dialog.doubleSpinBox_Bmax_COD.setValue(
            self.Pollution.COD.Bmax[lu_ind])
        block_Dialog.doubleSpinBox_Bmax_TP.setValue(
            self.Pollution.TP.Bmax[lu_ind])
        block_Dialog.doubleSpinBox_Bmax_TN.setValue(
            self.Pollution.TN.Bmax[lu_ind])
        block_Dialog.doubleSpinBox_Bmax_NH3N.setValue(
            self.Pollution.NH3N.Bmax[lu_ind])
        # bt
        block_Dialog.doubleSpinBox_bt_SS.setValue(self.Pollution.SS.bt[lu_ind])
        block_Dialog.doubleSpinBox_bt_COD.setValue(
            self.Pollution.COD.bt[lu_ind])
        block_Dialog.doubleSpinBox_bt_TP.setValue(self.Pollution.TP.bt[lu_ind])
        block_Dialog.doubleSpinBox_bt_TN.setValue(self.Pollution.TN.bt[lu_ind])
        block_Dialog.doubleSpinBox_bt_NH3N.setValue(
            self.Pollution.NH3N.bt[lu_ind])

        # return block_Dialog

    def change_underlyingsurface_params(self, block_Dialog):
        """根据 underlyingsurface_type 改变显示的参数值"""
        # 获取下垫面类型对应的索引
        underlyingsurface_type = block_Dialog.comboBox_underlyingsurface.currentText()
        if underlyingsurface_type == "请选择":
            QMessageBox.critical(
                block_Dialog,
                '错误',
                "请选择下垫面类型！")
            return

        us_ind = np.where(self.underlyingsurface_type_list ==
                          underlyingsurface_type)[0][0]

        # C1
        block_Dialog.doubleSpinBox_C1_SS.setValue(self.Pollution.SS.C1[us_ind])
        block_Dialog.doubleSpinBox_C1_COD.setValue(
            self.Pollution.COD.C1[us_ind])
        block_Dialog.doubleSpinBox_C1_TP.setValue(self.Pollution.TP.C1[us_ind])
        block_Dialog.doubleSpinBox_C1_TN.setValue(self.Pollution.TN.C1[us_ind])
        block_Dialog.doubleSpinBox_C1_NH3N.setValue(
            self.Pollution.NH3N.C1[us_ind])
        # C2
        block_Dialog.doubleSpinBox_C2_SS.setValue(self.Pollution.SS.C2[us_ind])
        block_Dialog.doubleSpinBox_C2_COD.setValue(
            self.Pollution.COD.C2[us_ind])
        block_Dialog.doubleSpinBox_C2_TP.setValue(self.Pollution.TP.C2[us_ind])
        block_Dialog.doubleSpinBox_C2_TN.setValue(self.Pollution.TN.C2[us_ind])
        block_Dialog.doubleSpinBox_C2_NH3N.setValue(
            self.Pollution.NH3N.C2[us_ind])
        # EMC
        block_Dialog.doubleSpinBox_EMC_SS.setValue(
            self.Pollution.SS.EMC[us_ind])
        block_Dialog.doubleSpinBox_EMC_COD.setValue(
            self.Pollution.COD.EMC[us_ind])
        block_Dialog.doubleSpinBox_EMC_TP.setValue(
            self.Pollution.TP.EMC[us_ind])
        block_Dialog.doubleSpinBox_EMC_TN.setValue(
            self.Pollution.TN.EMC[us_ind])
        block_Dialog.doubleSpinBox_EMC_NH3N.setValue(
            self.Pollution.NH3N.EMC[us_ind])
        # other
        block_Dialog.doubleSpinBox_max_init_loss.setValue(
            self.underlyingsurface_loss_list[us_ind])
        block_Dialog.doubleSpinBox_infiltration_rate.setValue(
            self.underlyingsurface_infil_list[us_ind])

        # return block_Dialog
    @property
    def pack_params(self):
        # 斑块类型
        params_dict = {
            "面源斑块类型": {
                "土地利用类型": self.landuse_type,
                "下垫面类型": self.underlyingsurface_type
            },
        }
        # 污染物参数
        lu_ind = np.where(self.landuse_type_list == self.landuse_type)[0][0]
        us_ind = np.where(self.underlyingsurface_type_list ==
                          self.underlyingsurface_type)[0][0]
        params_dict["污染物参数"] = {}
        for p_name, param in self.Pollution_dict.items():
            params_dict["污染物参数"][p_name] = {}
            for p, v in param.items():
                if p in ["Bmax", "bt"]:
                    params_dict["污染物参数"][p_name][p] = v[lu_ind]
                else:
                    params_dict["污染物参数"][p_name][p] = v[us_ind]

        return params_dict

    def update_params(self, block_Dialog):
        """更新模型参数
        将界面显示的参数值更新到模型参数中

        Args:
            block_Dialog (_type_): _description_

        Returns:
            _type_: _description_
        """
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

        # 获取 土地利用类型 和下垫面 类型
        self.landuse_type = block_Dialog.comboBox_landuse.currentText()
        self.underlyingsurface_type = block_Dialog.comboBox_underlyingsurface.currentText()
        lu_ind = np.where(self.landuse_type_list == self.landuse_type)[0][0]
        us_ind = np.where(self.underlyingsurface_type_list ==
                          self.underlyingsurface_type)[0][0]

        # 更新土地利用类型参数
        # Bmax
        self.Pollution.SS.Bmax[lu_ind] = block_Dialog.doubleSpinBox_Bmax_SS.value(
        )
        self.Pollution.COD.Bmax[lu_ind] = block_Dialog.doubleSpinBox_Bmax_COD.value(
        )
        self.Pollution.TP.Bmax[lu_ind] = block_Dialog.doubleSpinBox_Bmax_TP.value(
        )
        self.Pollution.TN.Bmax[lu_ind] = block_Dialog.doubleSpinBox_Bmax_TN.value(
        )
        self.Pollution.NH3N.Bmax[lu_ind] = block_Dialog.doubleSpinBox_Bmax_NH3N.value(
        )
        # bt
        self.Pollution.SS.bt[lu_ind] = block_Dialog.doubleSpinBox_bt_SS.value()
        self.Pollution.COD.bt[lu_ind] = block_Dialog.doubleSpinBox_bt_COD.value(
        )
        self.Pollution.TP.bt[lu_ind] = block_Dialog.doubleSpinBox_bt_TP.value()
        self.Pollution.TN.bt[lu_ind] = block_Dialog.doubleSpinBox_bt_TN.value()
        self.Pollution.NH3N.bt[lu_ind] = block_Dialog.doubleSpinBox_bt_NH3N.value(
        )

        # 下垫面参数
        # C1
        self.Pollution.SS.C1[us_ind] = block_Dialog.doubleSpinBox_C1_SS.value()
        self.Pollution.COD.C1[us_ind] = block_Dialog.doubleSpinBox_C1_COD.value(
        )
        self.Pollution.TP.C1[us_ind] = block_Dialog.doubleSpinBox_C1_TP.value()
        self.Pollution.TN.C1[us_ind] = block_Dialog.doubleSpinBox_C1_TN.value()
        self.Pollution.NH3N.C1[us_ind] = block_Dialog.doubleSpinBox_C1_NH3N.value(
        )
        # C2
        self.Pollution.SS.C2[us_ind] = block_Dialog.doubleSpinBox_C2_SS.value()
        self.Pollution.COD.C2[us_ind] = block_Dialog.doubleSpinBox_C2_COD.value(
        )
        self.Pollution.TP.C2[us_ind] = block_Dialog.doubleSpinBox_C2_TP.value()
        self.Pollution.TN.C2[us_ind] = block_Dialog.doubleSpinBox_C2_TN.value()
        self.Pollution.NH3N.C2[us_ind] = block_Dialog.doubleSpinBox_C2_NH3N.value(
        )
        # EMC
        self.Pollution.SS.EMC[us_ind] = block_Dialog.doubleSpinBox_EMC_SS.value(
        )
        self.Pollution.COD.EMC[us_ind] = block_Dialog.doubleSpinBox_EMC_COD.value(
        )
        self.Pollution.TP.EMC[us_ind] = block_Dialog.doubleSpinBox_EMC_TP.value(
        )
        self.Pollution.TN.EMC[us_ind] = block_Dialog.doubleSpinBox_EMC_TN.value(
        )
        self.Pollution.NH3N.EMC[us_ind] = block_Dialog.doubleSpinBox_EMC_NH3N.value(
        )
        # other
        self.underlyingsurface_loss_list[us_ind] = block_Dialog.doubleSpinBox_max_init_loss.value(
        )
        self.underlyingsurface_infil_list[us_ind] = block_Dialog.doubleSpinBox_infiltration_rate.value(
        )

    def reset_params(self, block_Dialog, temp_block_params):
        """把 temp_block_Dialog 的所有参数赋给 block_Dialog"""

        # 重置 土地利用类型 和 下垫面类型
        block_Dialog.comboBox_landuse.setCurrentText(temp_block_params.landuse)
        block_Dialog.comboBox_underlyingsurface.setCurrentText(
            temp_block_params.underlyingsurface)

        # 重置 土地利用类型参数
        # Bmax
        block_Dialog.doubleSpinBox_Bmax_SS.setValue(temp_block_params.Bmax_SS)
        block_Dialog.doubleSpinBox_Bmax_COD.setValue(
            temp_block_params.Bmax_COD)
        block_Dialog.doubleSpinBox_Bmax_TP.setValue(temp_block_params.Bmax_TP)
        block_Dialog.doubleSpinBox_Bmax_TN.setValue(temp_block_params.Bmax_TN)
        block_Dialog.doubleSpinBox_Bmax_NH3N.setValue(
            temp_block_params.Bmax_NH3N)
        # bt
        block_Dialog.doubleSpinBox_bt_SS.setValue(temp_block_params.bt_SS)
        block_Dialog.doubleSpinBox_bt_COD.setValue(temp_block_params.bt_COD)
        block_Dialog.doubleSpinBox_bt_TP.setValue(temp_block_params.bt_TP)
        block_Dialog.doubleSpinBox_bt_TN.setValue(temp_block_params.bt_TN)
        block_Dialog.doubleSpinBox_bt_NH3N.setValue(temp_block_params.bt_NH3N)

        # 重置 下垫面类型参数
        # C1
        block_Dialog.doubleSpinBox_C1_SS.setValue(temp_block_params.C1_SS)
        block_Dialog.doubleSpinBox_C1_COD.setValue(temp_block_params.C1_COD)
        block_Dialog.doubleSpinBox_C1_TP.setValue(temp_block_params.C1_TP)
        block_Dialog.doubleSpinBox_C1_TN.setValue(temp_block_params.C1_TN)
        block_Dialog.doubleSpinBox_C1_NH3N.setValue(temp_block_params.C1_NH3N)
        # C2
        block_Dialog.doubleSpinBox_C2_SS.setValue(temp_block_params.C2_SS)
        block_Dialog.doubleSpinBox_C2_COD.setValue(temp_block_params.C2_COD)
        block_Dialog.doubleSpinBox_C2_TP.setValue(temp_block_params.C2_TP)
        block_Dialog.doubleSpinBox_C2_TN.setValue(temp_block_params.C2_TN)
        block_Dialog.doubleSpinBox_C2_NH3N.setValue(temp_block_params.C2_NH3N)
        # EMC
        block_Dialog.doubleSpinBox_EMC_SS.setValue(temp_block_params.EMC_SS)
        block_Dialog.doubleSpinBox_EMC_COD.setValue(temp_block_params.EMC_COD)
        block_Dialog.doubleSpinBox_EMC_TP.setValue(temp_block_params.EMC_TP)
        block_Dialog.doubleSpinBox_EMC_TN.setValue(temp_block_params.EMC_TN)
        block_Dialog.doubleSpinBox_EMC_NH3N.setValue(
            temp_block_params.EMC_NH3N)

        # other
        block_Dialog.doubleSpinBox_max_init_loss.setValue(
            temp_block_params.max_init_loss)
        block_Dialog.doubleSpinBox_infiltration_rate.setValue(
            temp_block_params.infiltration_rate)

        return block_Dialog

    def Temp_assign_params(self, block_Dialog):
        """临时保存前一次操作的参数"""
        temp_block_params = dict()

        # 面源斑块（土地利用、下垫面）类型
        temp_block_params["landuse"] = block_Dialog.comboBox_landuse.currentText()
        temp_block_params["underlyingsurface"] = block_Dialog.comboBox_underlyingsurface.currentText()

        # 土地利用参数
        # Bmax
        temp_block_params["Bmax_SS"] = block_Dialog.doubleSpinBox_Bmax_SS.value()
        temp_block_params["Bmax_COD"] = block_Dialog.doubleSpinBox_Bmax_COD.value()
        temp_block_params["Bmax_TP"] = block_Dialog.doubleSpinBox_Bmax_TP.value()
        temp_block_params["Bmax_TN"] = block_Dialog.doubleSpinBox_Bmax_TN.value()
        temp_block_params["Bmax_NH3N"] = block_Dialog.doubleSpinBox_Bmax_NH3N.value(
        )
        # bt
        temp_block_params["bt_SS"] = block_Dialog.doubleSpinBox_bt_SS.value()
        temp_block_params["bt_COD"] = block_Dialog.doubleSpinBox_bt_COD.value()
        temp_block_params["bt_TP"] = block_Dialog.doubleSpinBox_bt_TP.value()
        temp_block_params["bt_TN"] = block_Dialog.doubleSpinBox_bt_TN.value()
        temp_block_params["bt_NH3N"] = block_Dialog.doubleSpinBox_bt_NH3N.value()

        # 下垫面参数
        # C1
        temp_block_params["C1_SS"] = block_Dialog.doubleSpinBox_C1_SS.value()
        temp_block_params["C1_COD"] = block_Dialog.doubleSpinBox_C1_COD.value()
        temp_block_params["C1_TP"] = block_Dialog.doubleSpinBox_C1_TP.value()
        temp_block_params["C1_TN"] = block_Dialog.doubleSpinBox_C1_TN.value()
        temp_block_params["C1_NH3N"] = block_Dialog.doubleSpinBox_C1_NH3N.value()
        # C2
        temp_block_params["C2_SS"] = block_Dialog.doubleSpinBox_C2_SS.value()
        temp_block_params["C2_COD"] = block_Dialog.doubleSpinBox_C2_COD.value()
        temp_block_params["C2_TP"] = block_Dialog.doubleSpinBox_C2_TP.value()
        temp_block_params["C2_TN"] = block_Dialog.doubleSpinBox_C2_TN.value()
        temp_block_params["C2_NH3N"] = block_Dialog.doubleSpinBox_C2_NH3N.value()
        # EMC
        temp_block_params["EMC_SS"] = block_Dialog.doubleSpinBox_EMC_SS.value()
        temp_block_params["EMC_COD"] = block_Dialog.doubleSpinBox_EMC_COD.value()
        temp_block_params["EMC_TP"] = block_Dialog.doubleSpinBox_EMC_TP.value()
        temp_block_params["EMC_TN"] = block_Dialog.doubleSpinBox_EMC_TN.value()
        temp_block_params["EMC_NH3N"] = block_Dialog.doubleSpinBox_EMC_NH3N.value()
        # other
        temp_block_params["max_init_loss"] = block_Dialog.doubleSpinBox_max_init_loss.value(
        )
        temp_block_params["infiltration_rate"] = block_Dialog.doubleSpinBox_infiltration_rate.value()

        return Struct(temp_block_params)

    def load_block_default_params(self, file_path):
        """加载主要参数"""
        io = pd.io.excel.ExcelFile(file_path)
        # timeseriesdata = pd.read_excel(io,sheet_name="TimeSeries").values
        # patchdata = pd.read_excel(io,sheet_name="Patch").values
        pollutantdata = pd.read_excel(io, sheet_name="Pollutant").values
        # controlunitdata = pd.read_excel(io,sheet_name="ControlUnit").values
        ludata = pd.read_excel(io, sheet_name="LandUse").values
        usdata = pd.read_excel(io, sheet_name="UnderlyingSurface").values
        io.close()

        return pollutantdata, ludata, usdata

    def preprocess_block_params(self, ludata, usdata, pollutantdata):
        """预处理主要参数"""
        # 读取土地利用类型的id
        lutype = ludata[:, 1]
        # nlu = len(ludata[:, 0])

        # 读取下垫面类型的id以及对应的最大初损、下渗率
        ustype = usdata[:, 1]
        usloss = usdata[:, 2]
        usinfil = usdata[:, 3]
        # nus = len(usdata[:, 0])

        # 读取污染指标及其对应的id
        npl = len(pollutantdata[:, 0])
        pltype = pollutantdata[:, 1]
        # 读取所有土地利用类型和下垫面类型对应的水质参数
        P = {p: {"Bmax": None,
                 "bt": None,
                 "C1": None,
                 "C2": None,
                 "EMC": None, }
             for p in pltype}
        for p, ptype in enumerate(pltype):
            P[ptype]["Bmax"] = ludata[:, 2+p]  # ok<*SAGROW>
            P[ptype]["bt"] = ludata[:, 2+npl+p]
            P[ptype]["C1"] = usdata[:, 4+p]
            P[ptype]["C2"] = usdata[:, 4+npl+p]
            P[ptype]["EMC"] = usdata[:, 4+2*npl+p]

        return lutype, ustype, pltype, usloss, usinfil, P, Struct(P)

    @property
    def sim(self):
        """单位面积的径流污染产生过程线模型"""
        """初始化"""
        expand_time = 5*60  # 延长5小时
        n_min = self.LoopCount + expand_time
        npl = len(self.Pollution)

        rain = np.concatenate(
            (self.rainfall, np.zeros(expand_time)), axis=0) / 60  # 单位转换：mm/hr -> mm/min
        evap = np.zeros_like(rain) + 0.2/60  # mm/min

        # 获取 土地利用类型 和下垫面 类型
        lu_ind = np.where(self.landuse_type_list == self.landuse_type)[0][0]
        us_ind = np.where(self.underlyingsurface_type_list ==
                          self.underlyingsurface_type)[0][0]

        usloss = self.underlyingsurface_loss_list[us_ind] / 60  # min级别的
        usinfil = self.underlyingsurface_infil_list[us_ind] / 60  # min级别的

        storage = np.zeros((n_min, 1))
        runoff = np.zeros((n_min, 1))
        storage[0, 0] = usloss

        """径流计算"""
        # 每个时刻不同`下垫面`的剩余蓄水能力和径流量动态变化
        for t in range(1, n_min):
            storage[t, 0] = min(usloss,
                                storage[t-1, 0] - rain[t] + evap[t] + usinfil)
            if storage[t, 0] < 0:
                # 当蓄水能力小于0时，产生径流
                runoff[t, 0] = max(0, 0 - storage[t, 0])
                storage[t, 0] = 0
        # 获取下雨至雨停后径流为0前的数据
        dry_period = runoff[self.LoopCount:]
        zero_runoff = np.where(dry_period == 0)[0][0]
        useful_period = self.LoopCount + int(zero_runoff)
        # 与用户定义的仿真周期对比
        dates = pd.date_range(start=self.start_dt_str,
                              end=self.end_dt_str, freq="1min")
        useful_period = min(useful_period, len(dates))
        useful_runoff = runoff[:useful_period] * 60  # 单位转换：mm/min -> mm/hr

        """污染物浓度计算"""
        # 每个时刻每一种污染物含量动态变化
        P = self.Pollution_dict
        B = np.zeros((useful_period, npl))  # 污染物累积量
        W = np.zeros((useful_period, npl))  # 污染物冲刷量
        concentration = dict()

        # 计算雨前污染物累积量
        for p, name in enumerate(self.pollution_type_list):  # 污染物类型
            if P[name]["EMC"][us_ind] == 0:  # 计算道路、硬地、水体的污染物累积和冲刷
                if self.ADP == -1:  # 默认污染物累积量为Bmax
                    B[0, p] = P[name]["Bmax"][lu_ind]
                else:
                    """计算污染物累积量
                    B[0] = min(Bmax, bt * ADP * 24)
                    """
                    B[0, p] = \
                        min(P[name]["Bmax"][lu_ind],
                            P[name]["bt"][lu_ind] * self.ADP * 24)

                W[0, p] = B[0, p]  # 初始化

        # 计算下雨至雨停后径流为0期间的污染物负荷
        for t in range(1, useful_period):  # 时间
            for p, name in enumerate(self.pollution_type_list):  # 污染物类型
                if P[name]["EMC"][us_ind] == 0:  # 计算道路、硬地、水体的污染物累积和冲刷
                    """计算污染物负荷
                    W[t] = C1 * runoff[t]^{C2} * B[t-1]
                    """
                    W[t, p] = P[name]["C1"][us_ind] * \
                        runoff[t, 0]**P[name]["C2"][us_ind] * B[t-1, p]

                    """更新污染物累积量
                    B[t] = max(0, B[t-1] - W[t])
                    """
                    B[t, p] = max(0, B[t-1, p] - W[t, p])
                else:  # 计算屋顶和绿地的冲刷
                    """计算污染物负荷
                    W[t] = runoff[t] * EMC
                    """
                    W[t, p] = runoff[t, 0] * P[name]["EMC"][us_ind]

        # 计算每个时刻的径流污染物浓度
        for p, name in enumerate(self.pollution_type_list):
            if P[name]["EMC"][us_ind] > 0:  # 计算道路、硬地、水体的污染物累积和冲刷
                concentration[name] = np.array(
                    [P[name]["EMC"][us_ind]]*useful_period)
            else:
                """污染物浓度计算
                C[t] = W[t] / runoff[t]
                """
                concentration[name] = np.divide(W[:, p], runoff[:useful_period, 0],
                                                out=np.zeros_like(W[:, p]),
                                                where=runoff[:useful_period, 0] != 0)

        return rain[:useful_period], useful_runoff, concentration

    def block_sim(self, main, rain_generate_Dialog, block_Dialog):
        # 面源斑块赋值
        self.start_dt_str = main.start_dt_str
        self.end_dt_str = main.end_dt_str
        self.Tstep = main.time_step
        self.ADP = main.ADP

        # 判断是否选择了路径，若无，则要弹窗
        if hasattr(main, 'weather_file_path'):
            # 天气文件赋值
            self.weather_file_path = main.weather_file_path
            self.get_weather_data

            # 检查仿真时间是否正确
            if not check_datetime_setting(main, self.LoopCount, self.start_dt_str, self.end_dt_str, self.Tstep):
                return
        else:
            # 用默认的雨型
            peak = rain_generate_Dialog.doubleSpinBox_peak.value()
            return_period = rain_generate_Dialog.spinBox_return_period.value()
            duration = rain_generate_Dialog.spinBox_duration.value()
            rain = rain_generate(peak, return_period, duration)
            # 赋值
            if rain is None:
                QMessageBox.critical(
                    block_Dialog,
                    '错误',
                    "请提供降雨数据（输入时序文件 或 生成雨型）！")
                return
            else:
                self.rainfall = rain
                self.LoopCount = len(rain)

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

        """仿真，并返回结果"""
        rain, runoff, pollution = self.sim

        """结果可视化"""
        self.show_block(rain, runoff, pollution, main)

        self.result = {"降雨强度(mm/min)": rain,
                       "径流量(mm/min)": runoff[:, 0]}
        for name, val in pollution.items():
            self.result[name+"浓度"] = val

        QMessageBox.information(main, '运行完毕', '仿真已完成！')

        main.block_sim_flag = True

    def show_block(self, rain, runoff, pollution, main):
        # rainfall
        F_rain = fig_rainfall(rain,
                              width=main.block_rainfall_sim_res_rainfall.width(),
                              height=main.block_rainfall_sim_res_rainfall.height(),
                              start_dt_str=self.start_dt_str,
                              freq="1min")

        # runoff
        F_runoff = fig_runoff(runoff, name_list=["斑块"],
                              width=main.block_rainfall_sim_res_runoff.width(),
                              height=main.block_rainfall_sim_res_runoff.height(),
                              start_dt_str=self.start_dt_str,
                              freq="1min")

        # pollution
        F_pollution = fig_pollution(pollution,
                                    width=main.block_rainfall_sim_res_pollution.width(),
                                    height=main.block_rainfall_sim_res_pollution.height(),
                                    start_dt_str=self.start_dt_str,
                                    freq="1min")

        # rain
        main.scene_rain = QGraphicsScene()
        main.scene_rain.addWidget(F_rain)  # 将图形元素添加到场景中
        main.block_rainfall_sim_res_rainfall.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.block_rainfall_sim_res_rainfall.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.block_rainfall_sim_res_rainfall.setScene(
            main.scene_rain)  # 将创建添加到图形视图显示窗口

        # runoff
        main.scene_runoff = QGraphicsScene()
        main.scene_runoff.addWidget(F_runoff)  # 将图形元素添加到场景中
        main.block_rainfall_sim_res_runoff.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.block_rainfall_sim_res_runoff.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.block_rainfall_sim_res_runoff.setScene(
            main.scene_runoff)  # 将创建添加到图形视图显示窗口

        # pollution
        main.scene_pollution = QGraphicsScene()
        main.scene_pollution.addWidget(F_pollution)  # 将图形元素添加到场景中
        main.block_rainfall_sim_res_pollution.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.block_rainfall_sim_res_pollution.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.block_rainfall_sim_res_pollution.setScene(
            main.scene_pollution)  # 将创建添加到图形视图显示窗口


def get_month(begin, end):
    begin_year, end_year = begin.year, end.year
    begin_month, end_month = begin.month, end.month
    if begin_year == end_year:
        months = end_month-begin_month
    else:
        months = (end_year-begin_year)*12+end_month-begin_month
    return months + 1

# if __name__ == '__main__':
    # npp =()
    # npp.change_landuse_params(1)
    # pass
