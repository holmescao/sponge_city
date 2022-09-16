## 面源污染负荷估算主程序
import os
from datetime import datetime
import pandas as pd
import xlrd
import numpy as np
from collections import namedtuple
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox


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
    def __init__(self, weather_file_path) -> None:
        default_params_file_path = 'utils/algo/non_point_pollution_params.xlsx'
        pollutantdata,ludata,usdata = self.load_block_default_params(default_params_file_path)
        lutype, ustype, pltype, usloss, usinfil, P, struct_P = self.preprocess_block_params(ludata,usdata,pollutantdata)

        self.landuse_type_list = lutype
        self.underlyingsurface_type_list = ustype
        self.pollution_type_list = pltype
        
        self.underlyingsurface_loss_list = usloss
        self.underlyingsurface_infil_list = usinfil
        
        self.Pollution_dict = P
        self.Pollution = struct_P

        # 仿真起止时间，及时间步长
        self.start_dt_str = "2022-08-21 00:00"
        self.end_dt_str = "2022-08-21 06:00"
        self.Tstep = 1               # time step (hr)
        
        # 文件路径
        self.weather_file_path = weather_file_path
        
    @property
    def get_weather_data(self):
        # 输入计算蒸散发所需的气象数据
        data = np.loadtxt(self.weather_file_path)
        self.rainfall = data[:]  # 降雨量，mm/hr

        #设置循环长度 
        self.LoopCount = len(data)

    def change_landuse_params(self,block_Dialog):
        """根据 landuse_type 改变显示的参数值"""
        
        # 获取土地利用类型对应的索引
        landuse_type = block_Dialog.comboBox_landuse.currentText()
        lu_ind = np.where(self.landuse_type_list ==landuse_type)[0][0]
        
        # Bmax
        block_Dialog.doubleSpinBox_Bmax_SS.setValue(self.Pollution.SS.Bmax[lu_ind])
        block_Dialog.doubleSpinBox_Bmax_COD.setValue(self.Pollution.COD.Bmax[lu_ind])
        block_Dialog.doubleSpinBox_Bmax_TP.setValue(self.Pollution.TP.Bmax[lu_ind])
        block_Dialog.doubleSpinBox_Bmax_TN.setValue(self.Pollution.TN.Bmax[lu_ind])
        block_Dialog.doubleSpinBox_Bmax_NH3N.setValue(self.Pollution.NH3N.Bmax[lu_ind])
        # bt
        block_Dialog.doubleSpinBox_bt_SS.setValue(self.Pollution.SS.bt[lu_ind])
        block_Dialog.doubleSpinBox_bt_COD.setValue(self.Pollution.COD.bt[lu_ind])
        block_Dialog.doubleSpinBox_bt_TP.setValue(self.Pollution.TP.bt[lu_ind])
        block_Dialog.doubleSpinBox_bt_TN.setValue(self.Pollution.TN.bt[lu_ind])
        block_Dialog.doubleSpinBox_bt_NH3N.setValue(self.Pollution.NH3N.bt[lu_ind])
        
        return block_Dialog
    
    def change_underlyingsurface_params(self,block_Dialog):
        """根据 underlyingsurface_type 改变显示的参数值"""
        
        # 获取下垫面类型对应的索引
        underlyingsurface_type = block_Dialog.comboBox_underlyingsurface.currentText()
        us_ind = np.where(self.underlyingsurface_type_list ==underlyingsurface_type)[0][0]
        
        # C1
        block_Dialog.doubleSpinBox_C1_SS.setValue(self.Pollution.SS.C1[us_ind])
        block_Dialog.doubleSpinBox_C1_COD.setValue(self.Pollution.COD.C1[us_ind])
        block_Dialog.doubleSpinBox_C1_TP.setValue(self.Pollution.TP.C1[us_ind])
        block_Dialog.doubleSpinBox_C1_TN.setValue(self.Pollution.TN.C1[us_ind])
        block_Dialog.doubleSpinBox_C1_NH3N.setValue(self.Pollution.NH3N.C1[us_ind])
        # C2
        block_Dialog.doubleSpinBox_C2_SS.setValue(self.Pollution.SS.C2[us_ind])
        block_Dialog.doubleSpinBox_C2_COD.setValue(self.Pollution.COD.C2[us_ind])
        block_Dialog.doubleSpinBox_C2_TP.setValue(self.Pollution.TP.C2[us_ind])
        block_Dialog.doubleSpinBox_C2_TN.setValue(self.Pollution.TN.C2[us_ind])
        block_Dialog.doubleSpinBox_C2_NH3N.setValue(self.Pollution.NH3N.C2[us_ind])
        # EMC
        block_Dialog.doubleSpinBox_EMC_SS.setValue(self.Pollution.SS.EMC[us_ind])
        block_Dialog.doubleSpinBox_EMC_COD.setValue(self.Pollution.COD.EMC[us_ind])
        block_Dialog.doubleSpinBox_EMC_TP.setValue(self.Pollution.TP.EMC[us_ind])
        block_Dialog.doubleSpinBox_EMC_TN.setValue(self.Pollution.TN.EMC[us_ind])
        block_Dialog.doubleSpinBox_EMC_NH3N.setValue(self.Pollution.NH3N.EMC[us_ind])
        # other
        block_Dialog.doubleSpinBox_max_init_loss.setValue(self.underlyingsurface_loss_list[us_ind])
        block_Dialog.doubleSpinBox_infiltration_rate.setValue(self.underlyingsurface_infil_list[us_ind])
        
        return block_Dialog
        
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
        lu_ind = np.where(self.landuse_type_list ==self.landuse_type)[0][0]
        us_ind = np.where(self.underlyingsurface_type_list ==self.underlyingsurface_type)[0][0]
        
        # 更新土地利用类型参数
        # Bmax
        self.Pollution.SS.Bmax[lu_ind] = block_Dialog.doubleSpinBox_Bmax_SS.value()
        self.Pollution.COD.Bmax[lu_ind] = block_Dialog.doubleSpinBox_Bmax_COD.value()
        self.Pollution.TP.Bmax[lu_ind] = block_Dialog.doubleSpinBox_Bmax_TP.value()
        self.Pollution.TN.Bmax[lu_ind] = block_Dialog.doubleSpinBox_Bmax_TN.value()
        self.Pollution.NH3N.Bmax[lu_ind] = block_Dialog.doubleSpinBox_Bmax_NH3N.value()
        # bt
        self.Pollution.SS.bt[lu_ind] = block_Dialog.doubleSpinBox_bt_SS.value()
        self.Pollution.COD.bt[lu_ind] = block_Dialog.doubleSpinBox_bt_COD.value()
        self.Pollution.TP.bt[lu_ind] = block_Dialog.doubleSpinBox_bt_TP.value()
        self.Pollution.TN.bt[lu_ind] = block_Dialog.doubleSpinBox_bt_TN.value()
        self.Pollution.NH3N.bt[lu_ind] = block_Dialog.doubleSpinBox_bt_NH3N.value()
        
        # 下垫面参数
        # C1
        self.Pollution.SS.C1[us_ind] = block_Dialog.doubleSpinBox_C1_SS.value()
        self.Pollution.COD.C1[us_ind] = block_Dialog.doubleSpinBox_C1_COD.value()
        self.Pollution.TP.C1[us_ind] = block_Dialog.doubleSpinBox_C1_TP.value()
        self.Pollution.TN.C1[us_ind] = block_Dialog.doubleSpinBox_C1_TN.value()
        self.Pollution.NH3N.C1[us_ind] = block_Dialog.doubleSpinBox_C1_NH3N.value()
        # C2
        self.Pollution.SS.C2[us_ind] = block_Dialog.doubleSpinBox_C2_SS.value()
        self.Pollution.COD.C2[us_ind] = block_Dialog.doubleSpinBox_C2_COD.value()
        self.Pollution.TP.C2[us_ind] = block_Dialog.doubleSpinBox_C2_TP.value()
        self.Pollution.TN.C2[us_ind] = block_Dialog.doubleSpinBox_C2_TN.value()
        self.Pollution.NH3N.C2[us_ind] = block_Dialog.doubleSpinBox_C2_NH3N.value()
        # EMC
        self.Pollution.SS.EMC[us_ind] = block_Dialog.doubleSpinBox_EMC_SS.value()
        self.Pollution.COD.EMC[us_ind] = block_Dialog.doubleSpinBox_EMC_COD.value()
        self.Pollution.TP.EMC[us_ind] = block_Dialog.doubleSpinBox_EMC_TP.value()
        self.Pollution.TN.EMC[us_ind] = block_Dialog.doubleSpinBox_EMC_TN.value()
        self.Pollution.NH3N.EMC[us_ind] = block_Dialog.doubleSpinBox_EMC_NH3N.value()
        # other
        self.underlyingsurface_loss_list[us_ind] = block_Dialog.doubleSpinBox_max_init_loss.value()
        self.underlyingsurface_infil_list[us_ind] = block_Dialog.doubleSpinBox_infiltration_rate.value()
    
    def reset_params(self, block_Dialog, temp_block_params):
        """把 temp_block_Dialog 的所有参数赋给 block_Dialog"""
        
        # 重置 土地利用类型 和 下垫面类型
        block_Dialog.comboBox_landuse.setCurrentText(temp_block_params.landuse)
        block_Dialog.comboBox_underlyingsurface.setCurrentText(temp_block_params.underlyingsurface)
        
        # 重置 土地利用类型参数
        # Bmax
        block_Dialog.doubleSpinBox_Bmax_SS.setValue(temp_block_params.Bmax_SS)
        block_Dialog.doubleSpinBox_Bmax_COD.setValue(temp_block_params.Bmax_COD)
        block_Dialog.doubleSpinBox_Bmax_TP.setValue(temp_block_params.Bmax_TP)
        block_Dialog.doubleSpinBox_Bmax_TN.setValue(temp_block_params.Bmax_TN)
        block_Dialog.doubleSpinBox_Bmax_NH3N.setValue(temp_block_params.Bmax_NH3N)
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
        block_Dialog.doubleSpinBox_EMC_NH3N.setValue(temp_block_params.EMC_NH3N)
        
        # other
        block_Dialog.doubleSpinBox_max_init_loss.setValue(temp_block_params.max_init_loss)
        block_Dialog.doubleSpinBox_infiltration_rate.setValue(temp_block_params.infiltration_rate)
        
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
        temp_block_params["Bmax_NH3N"] = block_Dialog.doubleSpinBox_Bmax_NH3N.value()
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
        temp_block_params["max_init_loss"] = block_Dialog.doubleSpinBox_max_init_loss.value()
        temp_block_params["infiltration_rate"] = block_Dialog.doubleSpinBox_infiltration_rate.value()
        
        return Struct(temp_block_params)
        
    def load_block_default_params(self,file_path):
        """加载主要参数"""
        io = pd.io.excel.ExcelFile(file_path)
        # timeseriesdata = pd.read_excel(io,sheet_name="TimeSeries").values
        # patchdata = pd.read_excel(io,sheet_name="Patch").values
        pollutantdata = pd.read_excel(io,sheet_name="Pollutant").values
        # controlunitdata = pd.read_excel(io,sheet_name="ControlUnit").values
        ludata = pd.read_excel(io,sheet_name="LandUse").values
        usdata = pd.read_excel(io,sheet_name="UnderlyingSurface").values
        io.close()

        return pollutantdata,ludata,usdata
        
    def preprocess_block_params(self, ludata,usdata, pollutantdata):
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
        P = {p:{"Bmax":None,
                "bt":None,
                "C1":None,
                "C2":None,
                "EMC":None,} 
            for p in pltype}
        for p, ptype in enumerate(pltype):
            P[ptype]["Bmax"] = ludata[:, 2+p] ##ok<*SAGROW>
            P[ptype]["bt"] = ludata[:, 2+npl+p]
            P[ptype]["C1"] = usdata[:, 4+p]
            P[ptype]["C2"] = usdata[:, 4+npl+p]
            P[ptype]["EMC"] = usdata[:, 4+2*npl+p]

        return lutype, ustype, pltype, usloss, usinfil, P, Struct(P)
    
    @property
    def sim(self):
        """2. 单位面积的径流污染产生过程线模型"""
        # self.get_weather_data
        # 2.1 rainfall runoff process simulation
        # 初始化
        nhour = self.LoopCount
        # nus = len(self.underlyingsurface_type_list)
        # nlu = len(self.landuse_type_list)
        nus = 1
        nlu = 1
        npl = len(self.Pollution)
        
        rain = self.rainfall
        evap = np.zeros_like(rain) + 0.2
        
        # 获取 土地利用类型 和下垫面 类型
        lu_ind = np.where(self.landuse_type_list ==self.landuse_type)[0][0]
        us_ind = np.where(self.underlyingsurface_type_list ==self.underlyingsurface_type)[0][0]
        
        usloss = np.array([self.underlyingsurface_loss_list[us_ind]])
        usinfil = np.array([self.underlyingsurface_infil_list[us_ind]])
        
        P = self.Pollution_dict
        
        storage = np.zeros((nhour, nus))
        runoff = np.zeros((nhour, nus))
        storage[0,:] = usloss.T
        B = np.zeros((nhour, nus*nlu*npl))
        W = np.zeros((nhour, nus*nlu*npl))

        pollution = dict()
        # 每个时刻不同下垫面的剩余蓄水能力和径流量动态变化
        for t in range(1, nhour):
            for u in range(nus):
                storage[t, u] = min(usloss[u], 
                                    storage[t-1, u] - rain[t] + evap[t] + usinfil[u])
                if storage[t, u] < 0:
                    # 当蓄水能力小于0时，产生径流
                    runoff[t, u] = 0 - storage[t, u]
                    storage[t, u] = 0
        
        # 每个时刻各个土地利用类型、下垫面类型的每一种污染物含量动态变化
        for t in range(1, nhour):
            for p, name in enumerate(self.pollution_type_list):
                for l in range(nlu):
                    for u in range(nus):
                        if P[name]["EMC"][u] == 0:
                            if rain[t] == 0:
                                B[t, p*nlu*nus + l*nus + u] = min(P[name]["Bmax"][l], 
                                                                        B[t-1, p*nlu*nus + l*nus + u] + P[name]["bt"][l])
                            else:
                                W[t, p*nlu*nus + l*nus + u] = P[name]["C1"][u] * runoff[t, u]**P[name]["C2"][u] \
                                    * B[t-1, p*nlu*nus + l*nus + u]
                                B[t, p*nlu*nus + l*nus + u] = max(0, B[t-1, p*nlu*nus + l*nus + u] \
                                    - W[t, p*nlu*nus + l*nus + u])
                        else:
                            W[t, p*nlu*nus + l*nus + u] = runoff[t, u] * P[name]["EMC"][u]

        for p, name in enumerate(self.pollution_type_list):
            pollution[name] = W[:,p]
        
        return rain, runoff, pollution
        
    
    
def get_month(begin,end):
    begin_year,end_year=begin.year,end.year
    begin_month,end_month=begin.month,end.month
    if begin_year==end_year:
        months=end_month-begin_month
    else:
        months=(end_year-begin_year)*12+end_month-begin_month
    return months + 1

# if __name__ == '__main__':
    # npp = NonPointPollution()
    # npp.change_landuse_params(1)
    # pass