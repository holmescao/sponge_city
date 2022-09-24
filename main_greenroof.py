# TODO: 有些无法在qt designer完成的事情，需要写代码完成，所以最终还是全靠写代码来设计吧！
import copy
import json
import yaml
import numpy as np
import pandas as pd
import datetime
import os 
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox,QGraphicsScene,QDialog
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
"""================= 导入窗口================="""
from utils.ui.sponge_city import Ui_MainWindow # 导入主窗口
from utils.ui_class.SimdateOptions import SimdateOptions
from utils.ui_class.GreenroofInput import GreenroofInput
from utils.ui_class.Block import Block
from utils.ui_class.SpongeBlock import SpongeBlock
from utils.ui_class.RainGenerate import RainGenerate

"""================= 导入函数================="""
from utils.algo.green_roof_single import GreenRoof as SingleGreenRoof                   # 导入要执行的算法
from utils.algo.non_point_pollution import NonPointPollution
from utils.algo.bioretention_ponds import BioretentionPonds
from utils.algo.green_roof import GreenRoof
from utils.algo.permeable_pavement import PermeablePavement
from utils.algo.concave_herbaceous_field import ConcaveHerbaceousField
from utils.algo.rain_generate import rain_generate

from utils.algo.sponge_block import sponge_block_pollution, sponge_block_runoff, available,forbidden
from utils.algo.general_functions import save_dict_to_yaml
from utils.algo.figure_function import MyFigure, fig_rainfall,fig_runoff,fig_pollution,fig_sponge_pie,fig_rainfall_runoff,fig_vs_single_pollution,fig_rain_generate




# 新建类继承于UI类，方便进一步书写逻辑
class Application(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)             # 创建界面
        
        """实例化"""
        # %%%%%%%%%%%%%%%%%%%%%%%%单体%%%%%%%%%%%%%%%%%%%%%%%%
        # 绿色屋顶模型
        self.SingleGreenRoof = SingleGreenRoof()
        
        # %%%%%%%%%%%%%%%%%%%%%%%%地块%%%%%%%%%%%%%%%%%%%%%%%%
        # 面源污染模型
        self.NonPointPollution = NonPointPollution()
        # 海绵模型
        self.BioretentionPonds = BioretentionPonds()
        self.GreenRoof = GreenRoof()
        self.PermeablePavement = PermeablePavement()
        self.ConcaveHerbaceousField = ConcaveHerbaceousField()
        
        # 实例化输入界面 !得把self传进去，否则不会保持窗口
        self.block_Dialog = Block(self)
        self.sponge_block_Dialog = SpongeBlock(self)
        self.sim_datetime_Dialog = SimdateOptions(self)
        self.rain_generate_Dialog = RainGenerate(self)
        
        """信号和槽函数部分"""
        # 选择观测数据文件
        self.action_open_observed_file.triggered.connect(self.open_observed_file)
        self.action_open_weather_file.triggered.connect(self.open_weather_file)
        self.action_block_rainfall_file.triggered.connect(self.open_weather_file)
        
        """海绵单体选择"""
        self.listView.clicked.connect(self.select_haimian) # 点击选择海绵体，弹窗选择参数
        
        """工具栏-选择"""
        # 仿真起止日期和步长
        self.actionDates.triggered.connect(self.open_sim_datetime_dialog) 
        # 面源斑块
        self.action_Block.triggered.connect(self.open_block_dialog)
        # 海绵地块
        self.action_SpongeBlock.triggered.connect(self.open_sponge_block_dialog)
        # 雨型生成
        self.action_rain_generate.triggered.connect(self.open_rain_generate_dialog)
        """工具栏-运行"""
        # 绿色屋顶仿真
        self.action_sim_green_roof.triggered.connect(self.green_roof_sim)
        self.action_sim_and_val_green_roof.triggered.connect(self.green_roof_sim_and_val) # 仿真&验证 TODO：可以去除
        # 面源斑块仿真
        self.action_sim_block.triggered.connect(self.block_sim)
        # 海绵地块仿真
        self.action_sim_sponge_block.triggered.connect(self.sponge_block_sim)
        
        
        # self.action_sim_green_roof.clicked.connect(
        #     lambda: self.test(self.test_button,))
        
        """全局参数"""
        self.tmp_landuse_type = "请选择"
        self.tmp_underlyingsurface_type = "请选择"
    
    def open_rain_generate_dialog(self):
        self.reject = False
        
        # 临时保存当前选项值
        peak=self.rain_generate_Dialog.doubleSpinBox_peak.value()
        return_period=self.rain_generate_Dialog.spinBox_return_period.value()
        duration=self.rain_generate_Dialog.spinBox_duration.value()
        params_dict = self.Temp_assign_rain_generate_params(peak,return_period,duration)
        
        # 生成雨型
        rain = rain_generate(peak,return_period,duration)
        # 画图
        self.show_rain_generate(rain)
        # 监测参数更新
        self.rain_generate_Dialog.doubleSpinBox_peak.valueChanged.connect(self.Dynamic_update_rain_generate_params)
        self.rain_generate_Dialog.spinBox_return_period.valueChanged.connect(self.Dynamic_update_rain_generate_params)
        self.rain_generate_Dialog.spinBox_duration.valueChanged.connect(self.Dynamic_update_rain_generate_params)
        
        # 退出
        # self.rain_generate_Dialog.accepted.connect(
        #     lambda: self.reset_rain_generate_params(params_dict))
        self.rain_generate_Dialog.rejected.connect(
            lambda: self.reset_rain_generate_params(params_dict))
        
        # 打开、保持窗口
        self.rain_generate_Dialog.show()
    
    def Dynamic_update_rain_generate_params(self):
        # 生成新雨型
        peak=self.rain_generate_Dialog.doubleSpinBox_peak.value()
        return_period=self.rain_generate_Dialog.spinBox_return_period.value()
        duration=self.rain_generate_Dialog.spinBox_duration.value()
        rain = rain_generate(peak,return_period,duration)
        # 画图
        self.show_rain_generate(rain)
    
    
    def show_rain_generate(self,rain):
        F_rain = fig_rain_generate(rain,
                                   width=self.rain_generate_Dialog.graphicsView_rain_generate.width(),
                                   height=self.rain_generate_Dialog.graphicsView_rain_generate.height())
        # 将图形元素添加到场景中
        self.scene_rain_generate = QGraphicsScene()  
        self.scene_rain_generate.addWidget(F_rain)  
        self.rain_generate_Dialog.graphicsView_rain_generate.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rain_generate_Dialog.graphicsView_rain_generate.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rain_generate_Dialog.graphicsView_rain_generate.setScene(self.scene_rain_generate)  # 将创建添加到图形视图显示窗口
    
    def Temp_assign_rain_generate_params(self,peak,return_period,duration):
        return {"peak":peak,"return_period":return_period,"duration":duration}
    
    def reset_rain_generate_params(self,params_dict):
        self.reject = True
        self.rain_generate_Dialog.doubleSpinBox_peak.setValue(params_dict["peak"])
        self.rain_generate_Dialog.spinBox_return_period.setValue(params_dict["return_period"])
        self.rain_generate_Dialog.spinBox_duration.setValue(params_dict["duration"])
    
    def open_sponge_block_dialog(self):
        self.reject = False
        # %%%%%%%%%%%%%%%%这里开始%%%%%%%%%%%%%%%%
        """界面初始化"""
        landuse_type = self.block_Dialog.comboBox_landuse.currentText()
        underlyingsurface_type = self.block_Dialog.comboBox_underlyingsurface.currentText()
        
        if (self.tmp_landuse_type == landuse_type) and (self.tmp_underlyingsurface_type == underlyingsurface_type):
            no_change_block_type = True
        else:
            no_change_block_type = False
        
        self.tmp_landuse_type = landuse_type
        self.tmp_underlyingsurface_type = underlyingsurface_type
        
        non_def_block = "请选择"
        if (landuse_type == non_def_block) or (underlyingsurface_type == non_def_block):
            QMessageBox.critical(
            self,
            '错误',
            "请先在面源斑块窗口定义面源斑块类型")
            return

        # 显示面源斑块（土地利用类型、下垫面类型）
        self.sponge_block_Dialog.lineEdit_landuse.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.sponge_block_Dialog.lineEdit_underlying.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.sponge_block_Dialog.lineEdit_landuse.setText(landuse_type)
        self.sponge_block_Dialog.lineEdit_underlying.setText(underlyingsurface_type)
        self.sponge_block_Dialog.lineEdit_landuse.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sponge_block_Dialog.lineEdit_underlying.setFocusPolicy(QtCore.Qt.NoFocus)
        
        # 临时保存当前选项值
        params_dict = self.Temp_assign_sponge_block_params(
            self.sponge_block_Dialog.tableWidget_sponge_setting,
            self.sponge_block_Dialog.spinBox_area.value())
        # 设置海绵可用设施
        if not no_change_block_type:
            self.sponge_block_Dialog.tableWidget_sponge_setting =\
                self.Unedit_sponge(self.sponge_block_Dialog.tableWidget_sponge_setting,
                            underlyingsurface_type)
        
        """界面参数实时更新"""
        # 监测参数实时更新: 判断参数值是否越界、显示饼图
        self.sponge_block_Dialog.tableWidget_sponge_setting.itemChanged.connect(
            self.Dynamic_update_sponge_block_params)
        # 面积参数更新
        self.sponge_block_Dialog.spinBox_area.valueChanged.connect(self.Dynamic_update_sponge_block_area)
        
        # 更新：参数改变
        # self.sponge_block_Dialog.accepted.connect()
        self.sponge_block_Dialog.rejected.connect(
            lambda: self.reset_sponge_block_params(params_dict))
        
        # 打开、保持窗口
        self.sponge_block_Dialog.show()
    
    def Dynamic_update_sponge_block_area(self):
        if self.reject == True:
            return
        
        self.Dynamic_update_sponge_block_params()
        
        
    def Dynamic_update_sponge_block_params(self, item=None):
        if self.reject == True or (item is not None and item.column()==1):
            return
        # 判断参数值是否越界、显示饼图
        
        """判断参数是否越界"""
        # # 计算海绵总比例
        # Sponge_Sum = 0
        # max_sum = 100
        # tableWidget = self.sponge_block_Dialog.tableWidget_sponge_setting
        # row = tableWidget.rowCount()
        # values = [int(tableWidget.item(i,0).text()) for i in range(row)]
        # Sponge_Sum = sum(values)
        # # 对越界的处理
        # if Sponge_Sum > max_sum:
        #     over = Sponge_Sum - max_sum
        #     origin_val = int(tableWidget.item(item.row(),item.column()).text())
        #     changed_val = max(0, origin_val - over)
        #     tableWidget.item(item.row(),item.column()).setText(str(changed_val))
        #     values[item.row()] = changed_val
        # 计算总面积
        block_area = self.sponge_block_Dialog.spinBox_area.value()
        block_assign = np.zeros(5,dtype=int)
        Sponge_Sum = 0
        tableWidget = self.sponge_block_Dialog.tableWidget_sponge_setting
        row = tableWidget.rowCount()
        # 获取比例
        values = np.array([int(tableWidget.item(i,0).text()) for i in range(row)])
        # 计算面积
        block_assign[:4] = values * block_area //100
        block_assign[1] *= 10 # 生物滞留池
        block_assign[3] *= 10 # 下凹式绿地
        
        Sponge_Sum = sum(block_assign)
        # 对越界的处理
        if Sponge_Sum > block_area:
            over_area = Sponge_Sum - block_area # 4w
            if (item.row() == 1 and item.column()==0) or (item.row() == 3 and item.column()==0):
                origin_area = int(int(tableWidget.item(item.row(),item.column()).text())*block_area*10/100)
                changed_area = max(0, origin_area - over_area)
                changed_val = int(changed_area/block_area/10*100)
            else:
                origin_area = int(int(tableWidget.item(item.row(),item.column()).text())*block_area/100)
                changed_area = max(0, origin_area - over_area)
                changed_val = int(changed_area/block_area*100)
            # 自动调整ui界面的值
            tableWidget.item(item.row(),item.column()).setText(str(changed_val))
            # 调整面积
            block_assign[item.row()] = changed_area
            
        # 更新ui界面的海绵面积，且列为禁动
        for i in range(row):
            tableWidget = available(tableWidget,i,[1])
            tableWidget.item(i,1).setText(str(block_assign[i]))
            tableWidget = forbidden(tableWidget,i,[1],zero_flag=False)
        
        """画饼图"""
        labels = [tableWidget.verticalHeaderItem(i).text() for i in range(row)]
        labels.append("非海绵区域")
        block_assign[-1] = max(0,block_area-Sponge_Sum)
        
        labels = np.array(labels,dtype=object)
        
        zero_inds = np.where(block_assign==0,True,False)
        block_assign = block_assign[~zero_inds]
        labels = labels[~zero_inds]
        
        F_sponge = fig_sponge_pie(block_assign, labels, 
                       width=self.sponge_block_Dialog.graphicsView_sponge_setting_show.width(),
                       height=self.sponge_block_Dialog.graphicsView_sponge_setting_show.height())
        # sponge
        self.scene_sponge = QGraphicsScene()  
        self.scene_sponge.addWidget(F_sponge)  # 将图形元素添加到场景中
        self.sponge_block_Dialog.graphicsView_sponge_setting_show.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sponge_block_Dialog.graphicsView_sponge_setting_show.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sponge_block_Dialog.graphicsView_sponge_setting_show.setScene(self.scene_sponge)  # 将创建添加到图形视图显示窗口
        
    def Unedit_sponge(self, tableWidget, underlying_surface):
        # 初始化表格
        row = tableWidget.rowCount()
        for i in range(row):
            tableWidget = available(tableWidget,i,[0])
            tableWidget = forbidden(tableWidget,i,[1])
        
        # 禁用部分设施
        if underlying_surface in "绿地, 水体":
            # 全部海绵设施均不可用
            for i in range(row):
                tableWidget = forbidden(tableWidget,i,[0])
        elif underlying_surface in "道路, 硬地":
            # 绿色屋顶不可用
            tableWidget = forbidden(tableWidget,0,[0])
        elif underlying_surface in "屋顶":
            # 只有绿色屋顶可用
            for i in range(1, row):
                tableWidget = forbidden(tableWidget,i,[0])
        else:
            pass
        
        
        return tableWidget
    
    def Temp_assign_sponge_block_params(self,tableWidget,area_value):
        col = 2
        temp_sponge_block_params = np.zeros(
            (tableWidget.rowCount(),col),dtype=object)
        
        for i in range(tableWidget.rowCount()):
            for j in range(col):
                temp_sponge_block_params[i,j] = tableWidget.item(i,j).text()
        
        block_area = area_value
        
        return {"block_area":block_area,"sponge_params":temp_sponge_block_params}
    
    def reset_sponge_block_params(self,params_dict):
        self.reject = True
        self.sponge_block_Dialog.spinBox_area.setValue(params_dict["block_area"])
        
        temp_sponge_block_params = params_dict["sponge_params"]
        row,col = temp_sponge_block_params.shape
        for i in range (row):
            for j in range(col):
                self.sponge_block_Dialog.tableWidget_sponge_setting.item(i,j).setText(
                    temp_sponge_block_params[i,j])
    
    def open_block_dialog(self):
        # 临时保存当前选项值
        temp_block_params = self.NonPointPollution.Temp_assign_params(self.block_Dialog)
        
        self.reject = False
        
        # 选择面源斑块类型
        self.block_Dialog.comboBox_landuse.currentIndexChanged.connect(self.get_landuse_type)
        self.block_Dialog.comboBox_underlyingsurface.currentIndexChanged.connect(self.get_underlyingsurface_type)
        
        # 更新：参数改变（真的）
        self.block_Dialog.accepted.connect(lambda: self.NonPointPollution.update_params(self.block_Dialog))
        
        # 恢复到此次打开窗口时的初始值
        self.block_Dialog.rejected.connect(lambda: self.reset_block_params(temp_block_params))
        
        # 打开、保持窗口
        self.block_Dialog.show()
        
    def reset_block_params(self, temp_block_params):
        self.reject = True
        self.block_Dialog = self.NonPointPollution.reset_params(self.block_Dialog, temp_block_params)
        
    def get_landuse_type(self):
        # 如果是因为退出而引发的利用类型变化则跳过
        if self.reject: return
        
        # 只显示土地利用类型对应的参数值，但不更新模型的参数值
        self.block_Dialog = self.NonPointPollution.change_landuse_params(self.block_Dialog)
    
    def get_underlyingsurface_type(self):
        # 如果是因为退出而引发的利用类型变化则跳过
        if self.reject: return
        
        # 只显示下垫面类型对应的参数值，但不更新模型的参数值
        self.block_Dialog = self.NonPointPollution.change_underlyingsurface_params(self.block_Dialog)
    
    def open_sim_datetime_dialog(self):
        
        # 收到确认信号后，更新参数
        self.dateTime_start_edit = self.sim_datetime_Dialog.dateTime_start_edit
        self.dateTime_end_edit = self.sim_datetime_Dialog.dateTime_end_edit
        self.time_step = self.sim_datetime_Dialog.spinBox_timestep
        self.sim_datetime_Dialog.accepted.connect(self.update_sim_datetime)
        # 打开窗口
        self.sim_datetime_Dialog.show() 
    
    def update_sim_datetime(self):
        # 获取更新后的时间
        # 起始时间
        self.dateTime_start_edit.setDisplayFormat("yyyy-MM-dd hh:mm")
        start_dt = self.dateTime_start_edit.dateTime()
        start_dt_str = start_dt.toString(self.dateTime_start_edit.displayFormat())
        # 结束时间
        self.dateTime_end_edit.setDisplayFormat("yyyy-MM-dd hh:mm")
        end_dt = self.dateTime_end_edit.dateTime()
        end_dt_str = end_dt.toString(self.dateTime_end_edit.displayFormat())
        # 时间步长hour
        time_step = self.time_step.value() / 60
        
        # 赋值
        self.assign_sim_datetime(start_dt_str,end_dt_str,time_step)
        
    
    def assign_sim_datetime(self,start_dt_str,end_dt_str,time_step):
        # 给绿色屋顶赋值
        self.SingleGreenRoof.start_dt_str = start_dt_str
        self.SingleGreenRoof.end_dt_str = end_dt_str
        self.SingleGreenRoof.Tstep = time_step
        
        
        # 面源斑块赋值
        self.NonPointPollution.start_dt_str = start_dt_str
        self.NonPointPollution.end_dt_str = end_dt_str
        self.NonPointPollution.Tstep = time_step
        
        # TODO：其他的也一样赋值吧；
        # 或者放到具体海绵单体的仿真函数里面
        
    def check_datetime(self,data_num, start_dt_str,end_dt_str,time_step):
        start_dt = datetime.datetime.strptime(start_dt_str,"%Y-%m-%d %H:%M")
        end_dt = datetime.datetime.strptime(end_dt_str,"%Y-%m-%d %H:%M")
        
        # 计算日期之间的点数
        time_delta = end_dt - start_dt
        total_min = time_delta.days *24 *60 + time_delta.seconds // 60
        step_per_min = 1/time_step/60
        time_num = int(total_min *step_per_min) + 1

        return True if data_num == time_num else False
            
    def select_haimian(self, item):
        # ["绿色屋顶","渗透铺装", "下凹式绿地", "生物滞留池"]
        if self.haimain_list[item.row()] == "绿色屋顶":
            self.open_green_roof_Dialog()
            # QMessageBox.information(self,"QListView","测试")
        else:
            pass
    
    def open_green_roof_Dialog(self):
        # 实例化输入界面
        green_roof_Dialog = GreenroofInput(self) # !得把self传进去，否则不会保持窗口
        # 收到确认信号后，更新参数
        # green_roof_Dialog.pushButton_greenroof_ok.clicked.connect(self.upate_params)
        green_roof_Dialog.accepted.connect(lambda: self.upate_params(green_roof_Dialog,))
        # green_roof_Dialog.pushButton_greenroof_ok.clicked.connect(lambda: self.upate_params(green_roof_Dialog,))
        # green_roof_Dialog.Signal_updateparams.connect(self.upate_params)
        green_roof_Dialog.show() # 打开窗口
    
        
    def open_observed_file(self):
        self.observed_file_path, filetype = QFileDialog.getOpenFileName(self,
                                    u"选取观测文件",
                                    "./",
                                    "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
        
        if ".txt" not in self.observed_file_path:
            QMessageBox.critical(
            self,
            '错误',
            "数据文件格式必须为'*.txt'！")
            return 
        
    def open_weather_file(self):
        self.weather_file_path, filetype = QFileDialog.getOpenFileName(self,
                                    u"选取气象文件",
                                    "./",
                                    "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
        if ".txt" not in self.weather_file_path:
            QMessageBox.critical(
            self,
            '错误',
            "数据文件格式必须为'*.txt'！")
            return 

    def upate_params(self,params):
        
        # TODO：分离到green_roof_config.py文件中
        # ***************** initialization ******************
        # self.SingleGreenRoof.d1_0 = self.d1_0.value()                # initial depth of water stored on the surface (mm)
        self.SingleGreenRoof.xita2_0 = params.xita2_0.value()           # soil layer initial moisture content (volume of water / total volume of soil)
        self.SingleGreenRoof.d3_0 = params.d3_0.value()    # initial depth of water in the storage layer (mm)
        # self.SingleGreenRoof.F_0 = self.F_0.value()   # initial accumulative infiltraion of surface water into the soil layer (mm),500(20200521)0500

        # =========== the Design parameters ============
        # self.SingleGreenRoof.chang = self.chang.value()                 # 绿色屋顶长度, mm
        # self.SingleGreenRoof.kuan = self.kuan.value()                   # 绿色屋顶宽度, mm
        self.SingleGreenRoof.D1 = params.D1.value()                       #溢流层深度，mm，注：论文里未注明溢流层深度
        self.SingleGreenRoof.D2 = params.D2.value()                       #基质层深度，mm
        self.SingleGreenRoof.D3 = params.D3.value()                       #蓄水层深度,mm
        self.SingleGreenRoof.D3D = params.D3D.value()                    #蓄水层最小可出流深度,mm

        #soilDensity = 1.4          # soil dry bulk density (g/cm**3)
        #storageDensity = 1.8       # stone dry bulk density (g/cm**3)
        self.SingleGreenRoof.phi1 = params.phi1.value() # void fraction of any surface volume (i.e., the fraction of freeboard above the surface not filled with vegetation)
        
        # ================ system setting ====================
        # self.Tstep = 1/60               # time step (hr),min

        #设置的常数
        # self.SingleGreenRoof.albedo = self.albedo.value()  #表面反射率
        # self.SingleGreenRoof.e0 = self.e0.value()     #0℃水的饱和蒸气压，kpa
        #z00 = 0.01   #地表有效粗糙长度，m
        #z = 2  #参考高度

        #已率定的水文参数,20220710
        self.SingleGreenRoof.xitaFC = params.xitaFC.value() #田间持水量
        self.SingleGreenRoof.xitaWP = params.xitaWP.value()  #凋萎点
        self.SingleGreenRoof.phi2 = params.phi2.value()     #土壤层孔隙率
        self.SingleGreenRoof.phi3 = params.phi3.value()    #砾石层孔隙率
        self.SingleGreenRoof.C3D = params.C3D.value()     #孔流系数0.105,0.148,5.65
        self.SingleGreenRoof.eta3D = params.eta3D.value()  #孔流指数，原1.865,1.93,0.9
        # self.SingleGreenRoof.C1 = self.C1.value() * 1e-8        #砾石层水分蒸发的空气动力学导率
        self.SingleGreenRoof.xitacb = params.xitacb.value()    #土壤含水量大于xitacb时，植物蒸腾不受水分限制,0.28#20211223
        self.SingleGreenRoof.Ksat = params.Ksat.value()     #土壤层基质流饱和导水率，mm/hr312.6044，231.72
        self.SingleGreenRoof.HCO = params.HCO.value()   #土壤层下部水分渗出公式中的导水衰减常数34.5439
        self.SingleGreenRoof.psi2 = params.psi2.value()   #土壤层表面水分入渗公式中的土壤层吸力水头44.1493
        # print("参数更新完毕")
        # print("self.SingleGreenRoof.xitaFC:,%.4f" % (self.SingleGreenRoof.xitaFC))
        
    def sponge_block_sim(self):
        # # 判断是否选择了路径，若无，则要弹窗
        # if not hasattr(self, 'weather_file_path'):
        #     QMessageBox.critical(
        #     self,
        #     '错误',
        #     '执行 仿真 前，请先选择数据文件，气象是必选的）！')
        #     return        
        if  hasattr(self, 'weather_file_path'):
            # 天气文件赋值
            self.NonPointPollution.weather_file_path = self.weather_file_path
            self.GreenRoof.weather_file_path = self.weather_file_path
            self.PermeablePavement.weather_file_path = self.weather_file_path
            self.BioretentionPonds.weather_file_path = self.weather_file_path
            self.ConcaveHerbaceousField.weather_file_path = self.weather_file_path
            
            self.NonPointPollution.get_weather_data
            # self.GreenRoof.get_weather_data
            # self.PermeablePavement.get_weather_data
            # self.BioretentionPonds.get_weather_data
            # self.ConcaveHerbaceousField.get_weather_data
            
            # 检查时间是否正确
            if not self.check_datetime(self.NonPointPollution.LoopCount,
                                start_dt_str=self.NonPointPollution.start_dt_str,
                                end_dt_str=self.NonPointPollution.end_dt_str,
                                time_step=self.NonPointPollution.Tstep):
                QMessageBox.critical(
                self,
                '错误',
                '仿真日期长度与真实数据长度不匹配！请检查仿真日期参数或真实数据文件')
                return 
        else:
            # 用默认的雨型
            peak= self.rain_generate_Dialog.doubleSpinBox_peak.value()
            return_period=self.rain_generate_Dialog.spinBox_return_period.value()
            duration=self.rain_generate_Dialog.spinBox_duration.value()
            rain = rain_generate(peak,return_period,duration)
            # 赋值
            self.NonPointPollution.rainfall = rain
            self.GreenRoof.rainfall = rain
            self.PermeablePavement.rainfall = rain
            self.BioretentionPonds.rainfall = rain
            self.ConcaveHerbaceousField.rainfall = rain
            
            self.NonPointPollution.LoopCount = len(rain)
            self.GreenRoof.LoopCount = len(rain)
            self.PermeablePavement.LoopCount = len(rain)
            self.BioretentionPonds.LoopCount = len(rain)
            self.ConcaveHerbaceousField.LoopCount = len(rain)
        
        # 是否选择下垫面类型
        if self.block_Dialog.comboBox_landuse.currentText() == "请选择":
            QMessageBox.critical(
            self.block_Dialog,
            '错误',
            "请选择土地利用类型！")
            return 
        if self.block_Dialog.comboBox_underlyingsurface.currentText() == "请选择":
            QMessageBox.critical(
            self.block_Dialog,
            '错误',
            "请选择下垫面类型！")
            return
        
        # 每个设施更新下垫面的水文参数
        self.GreenRoof.underlyingsurface_loss_list = self.NonPointPollution.underlyingsurface_loss_list
        self.GreenRoof.underlyingsurface_infil_list = self.NonPointPollution.underlyingsurface_infil_list
        self.PermeablePavement.underlyingsurface_loss_list = self.NonPointPollution.underlyingsurface_loss_list
        self.PermeablePavement.underlyingsurface_infil_list = self.NonPointPollution.underlyingsurface_infil_list
        self.BioretentionPonds.underlyingsurface_loss_list = self.NonPointPollution.underlyingsurface_loss_list
        self.BioretentionPonds.underlyingsurface_infil_list = self.NonPointPollution.underlyingsurface_infil_list
        self.ConcaveHerbaceousField.underlyingsurface_loss_list = self.NonPointPollution.underlyingsurface_loss_list
        self.ConcaveHerbaceousField.underlyingsurface_infil_list = self.NonPointPollution.underlyingsurface_infil_list
        
        # 每个设施、面源斑块模拟
        """单位面积过程仿真，并返回结果"""
        rain, runoff, pollution = self.NonPointPollution.sim
        GR_runoff, GR_pollution = self.GreenRoof.sim(runoff, pollution)
        PP_runoff, PP_pollution = self.PermeablePavement.sim(runoff, pollution)
        BRP_runoff, BRP_pollution = self.BioretentionPonds.sim(runoff, pollution)
        CHF_runoff, CHF_pollution = self.ConcaveHerbaceousField.sim(runoff, pollution)
        
        """面源斑块比例处理"""
        tableWidget = self.sponge_block_Dialog.tableWidget_sponge_setting
        sponge_type_list = ["GR","BRP","PP","CHF","TD"]
        sponge_area_list = [int(tableWidget.item(i,1).text())
                            for i in range(tableWidget.rowCount())]        
        block_area = self.sponge_block_Dialog.spinBox_area.value()
        traditional_area = block_area - sum(sponge_area_list)
        sponge_area_list.append(traditional_area)
        sponge_tpye_area_map = dict(zip(sponge_type_list,sponge_area_list))
        
        sponge_runoff = sponge_block_runoff(block_area,
                            sponge_tpye_area_map=sponge_tpye_area_map,
                            TD=runoff,
                               GR=GR_runoff,
                               PP=PP_runoff,
                               BRP=BRP_runoff,
                               CHF=CHF_runoff,
                               )
        sponge_pollution = sponge_block_pollution(block_area,
                            sponge_tpye_area_map=sponge_tpye_area_map,
                            TD=pollution,
                               GR=GR_pollution,
                               PP=PP_pollution,
                               BRP=BRP_pollution,
                               CHF=CHF_pollution,
                               )
        
        """结果可视化"""
        self.show_sponge_block(rain, runoff, pollution, sponge_runoff, sponge_pollution)
        
        
    def block_sim(self):
        # 判断是否选择了路径，若无，则要弹窗
        # if not hasattr(self, 'weather_file_path'):
        #     QMessageBox.critical(
        #     self,
        #     '错误',
        #     '执行 仿真 前，请先选择数据文件，气象是必选的）！')
        #     return 
        if  hasattr(self, 'weather_file_path'):
            # 天气文件赋值
            self.NonPointPollution.weather_file_path = self.weather_file_path
            self.NonPointPollution.get_weather_data
            
            # 检查仿真时间是否正确
            if not self.check_datetime(self.NonPointPollution.LoopCount,
                                start_dt_str=self.NonPointPollution.start_dt_str,
                                end_dt_str=self.NonPointPollution.end_dt_str,
                                time_step=self.NonPointPollution.Tstep):
                QMessageBox.critical(
                self,
                '错误',
                '仿真日期长度与真实数据长度不匹配！请检查仿真日期参数或真实数据文件')
                return 
        else:
            # 用默认的雨型
            peak= self.rain_generate_Dialog.doubleSpinBox_peak.value()
            return_period=self.rain_generate_Dialog.spinBox_return_period.value()
            duration=self.rain_generate_Dialog.spinBox_duration.value()
            rain = rain_generate(peak,return_period,duration)
            # 赋值
            self.NonPointPollution.rainfall = rain
            self.NonPointPollution.LoopCount = len(rain)
        
        if self.block_Dialog.comboBox_landuse.currentText() == "请选择":
            QMessageBox.critical(
            self.block_Dialog,
            '错误',
            "请选择土地利用类型！")
            return 
        if self.block_Dialog.comboBox_underlyingsurface.currentText() == "请选择":
            QMessageBox.critical(
            self.block_Dialog,
            '错误',
            "请选择下垫面类型！")
            return 
        
        """仿真，并返回结果"""
        rain, runoff, pollution = self.NonPointPollution.sim
        
        """结果可视化"""
        self.show_block(rain, runoff, pollution)
        
        # """结果自动保存"""
        # sim_results_save_dir,timestamp = self.save_single_sponge_sim_results(model_name="greenroof", 
        #                                     data=q3, 
        #                                     start_date=self.SingleGreenRoof.start_dt_str,
        #                                     end_date=self.SingleGreenRoof.end_dt_str,
        #                                     freq='1min')
        
        # self.save_single_sponge_sim_params(model_name="greenroof", 
        #                                    params_dict=self.SingleGreenRoof.pack_params,
        #                                    start_date=self.SingleGreenRoof.start_dt_str,
        #                                     end_date=self.SingleGreenRoof.end_dt_str,
        #                                     timestamp=timestamp,
        #                                     freq='1min')
        
        # QMessageBox.information(self,'运行完毕','完成！实验参数和结果保存在：\n%s' %(sim_results_save_dir))

    def show_sponge_block(self, rain, runoff, pollution, sponge_runoff, sponge_pollution):
        """rain_runoff"""
        runoff = np.concatenate((runoff.reshape(-1,1),sponge_runoff.reshape(-1,1)),axis=1)
        F_rain_runoff = fig_rainfall_runoff(rain,runoff, name_list=["斑块", "海绵"],
                            width=self.sponge_block_rainfallrunoff_sim_res_rainfall.width(),
                            height=self.sponge_block_rainfallrunoff_sim_res_rainfall.height(), 
                            start_dt_str=self.NonPointPollution.start_dt_str,
                            freq="1min")
        # 将图形元素添加到场景中
        self.scene_sponge_rain_runoff = QGraphicsScene()  
        self.scene_sponge_rain_runoff.addWidget(F_rain_runoff)  
        self.sponge_block_rainfallrunoff_sim_res_rainfall.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sponge_block_rainfallrunoff_sim_res_rainfall.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sponge_block_rainfallrunoff_sim_res_rainfall.setScene(self.scene_sponge_rain_runoff)  # 将创建添加到图形视图显示窗口
        
        """pollution"""
        # 创建与获取场景
        self.scene_sponge_pollution_SS = QGraphicsScene()
        self.scene_sponge_pollution_COD = QGraphicsScene()
        self.scene_sponge_pollution_TP = QGraphicsScene()  
        self.scene_sponge_pollution_TN = QGraphicsScene()
        self.scene_sponge_pollution_NH3N = QGraphicsScene()
        scene_list = [[self.sponge_block_pollution_sim_res_rainfall_SS,self.scene_sponge_pollution_SS],
                      [self.sponge_block_pollution_sim_res_rainfall_COD,self.scene_sponge_pollution_COD],
                      [self.sponge_block_pollution_sim_res_rainfall_TP,self.scene_sponge_pollution_TP],
                      [self.sponge_block_pollution_sim_res_rainfall_TN,self.scene_sponge_pollution_TN],
                      [self.sponge_block_pollution_sim_res_rainfall_NH3N,self.scene_sponge_pollution_NH3N],
                      ]
        
        # 获取污染物种类
        pp_metric = list(pollution.keys())
        # 逐个污染物画图
        for i, p in enumerate(pp_metric):
            if i >= len(scene_list):
                # TODO:给未来自定义污染物时用
                pass
            vs_pollution = np.concatenate((pollution[p].reshape(-1,1),sponge_pollution[p].reshape(-1,1)),axis=1)
            F_pollution = fig_vs_single_pollution(p, vs_pollution,name_list=["斑块", "海绵"],
                                width=scene_list[i][0].width(),
                                height=scene_list[i][0].height(), 
                                start_dt_str=self.NonPointPollution.start_dt_str,
                                freq="1min") 
            # 将图形元素添加到场景中
            scene_list[i][1].addWidget(F_pollution)  # 将图形元素添加到场景中
            scene_list[i][0].setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scene_list[i][0].setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scene_list[i][0].setScene(scene_list[i][1])  # 将创建添加到图形视图显示窗口
        
    def show_block(self, rain,runoff, pollution):
        # rainfall
        F_rain = fig_rainfall(rain, 
                              width=self.block_rainfall_sim_res_rainfall.width(),
                              height=self.block_rainfall_sim_res_rainfall.height(), 
            start_dt_str=self.NonPointPollution.start_dt_str,
            freq="1min")
        
        # runoff
        F_runoff = fig_runoff(runoff, name_list=["斑块"],
                              width=self.block_rainfall_sim_res_runoff.width(),
                              height=self.block_rainfall_sim_res_runoff.height(), 
            start_dt_str=self.NonPointPollution.start_dt_str,
            freq="1min")
        
        # pollution
        F_pollution = fig_pollution(pollution,
                              width=self.block_rainfall_sim_res_pollution.width(),
                              height=self.block_rainfall_sim_res_pollution.height(), 
            start_dt_str=self.NonPointPollution.start_dt_str,
            freq="1min")
        
        # rain
        self.scene_rain = QGraphicsScene()  
        self.scene_rain.addWidget(F_rain)  # 将图形元素添加到场景中
        self.block_rainfall_sim_res_rainfall.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.block_rainfall_sim_res_rainfall.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.block_rainfall_sim_res_rainfall.setScene(self.scene_rain)  # 将创建添加到图形视图显示窗口
        
        # runoff
        self.scene_runoff = QGraphicsScene()  
        self.scene_runoff.addWidget(F_runoff)  # 将图形元素添加到场景中
        self.block_rainfall_sim_res_runoff.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.block_rainfall_sim_res_runoff.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.block_rainfall_sim_res_runoff.setScene(self.scene_runoff)  # 将创建添加到图形视图显示窗口
        
        # pollution
        self.scene_pollution = QGraphicsScene()  
        self.scene_pollution.addWidget(F_pollution)  # 将图形元素添加到场景中
        self.block_rainfall_sim_res_pollution.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.block_rainfall_sim_res_pollution.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.block_rainfall_sim_res_pollution.setScene(self.scene_pollution)  # 将创建添加到图形视图显示窗口
        

    def green_roof_sim(self):
        # 判断是否选择了路径，若无，则要弹窗
        if not hasattr(self, 'weather_file_path'):
            QMessageBox.critical(
            self,
            '错误',
            '执行 仿真 前，请先选择数据文件，气象是必选的）！')
            return 
        
        # 天气文件赋值
        self.SingleGreenRoof.weather_file_path = self.weather_file_path
        self.SingleGreenRoof.get_weather_data
        # 检查仿真时间是否正确
        if not self.check_datetime(self.SingleGreenRoof.LoopCount,
                            start_dt_str=self.SingleGreenRoof.start_dt_str,
                            end_dt_str=self.SingleGreenRoof.end_dt_str,
                            time_step=self.SingleGreenRoof.Tstep):
            QMessageBox.critical(
            self,
            '错误',
            '仿真日期长度与真实数据长度不匹配！请检查仿真日期参数或真实数据文件')
            return 
        
        """仿真，并返回结果"""
        q3 = self.SingleGreenRoof.sim
        
        """结果可视化"""
        self.show_curve(q3,None,None)
        
        """结果自动保存"""
        sim_results_save_dir,timestamp = self.save_single_sponge_sim_results(model_name="greenroof", 
                                            data=q3, 
                                            start_date=self.SingleGreenRoof.start_dt_str,
                                            end_date=self.SingleGreenRoof.end_dt_str,
                                            freq='1min')
        
        self.save_single_sponge_sim_params(model_name="greenroof", 
                                           params_dict=self.SingleGreenRoof.pack_params,
                                           start_date=self.SingleGreenRoof.start_dt_str,
                                            end_date=self.SingleGreenRoof.end_dt_str,
                                            timestamp=timestamp,
                                            freq='1min')
        
        QMessageBox.information(self,'运行完毕','完成！实验参数和结果保存在：\n%s' %(sim_results_save_dir))
        
    def save_single_sponge_sim_results(self, model_name, data, start_date,end_date, freq='1min'):
            # 路径设置
            cur_path = os.path.split(os.path.realpath(__file__))[0]
            timestamp = str(datetime.datetime.now()).split(".")[0].replace(" ", "T").replace("-","").replace(":","")
            # save_dir = os.path.join(cur_path,"results", "single_sponge",timestamp)
            save_dir = os.path.join("results", "single_sponge",timestamp)
            if not os.path.exists(save_dir):
                os.makedirs(save_dir,exist_ok=True)
            
            # 仿真结果数据整合成df
            dates = pd.date_range(start=start_date,end=end_date,freq=freq)
            date_list = [x.strftime("%Y-%m-%d %H:%M") for x in dates]
            sim_results = pd.DataFrame(data={"仿真时间(min)":date_list,
                               "出流量 (mm/hr)":data})
            # 执行保存
            
            save_path = os.path.join(save_dir, "result_%s_sim.xlsx" % (model_name))
            sim_results.to_excel(save_path,index=False)
            
            return save_dir,timestamp
        
    def save_single_sponge_sim_params(self, model_name, params_dict,start_date,end_date, timestamp,freq='1min'):
        # 路径设置
        save_dir = os.path.join("results", "single_sponge",timestamp)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir,exist_ok=True)
        
        def merge_two_dicts(x, y):
            """Given two dicts, merge them into a new dict as a shallow copy."""
            x.update(y)
            return x
        
        other_cfg = {
            "基本信息":
                {
                "本次实验的时间戳":timestamp,
                "仿真海绵单体模型":model_name,
                "仿真起始日期+时间":start_date,
                "仿真结束日期+时间":end_date,
                "时间步长":freq,
                }
        }
        params_dict = merge_two_dicts(other_cfg, {"用户输入参数":params_dict})        
        
        save_path = os.path.join(save_dir, "result_%s_params.yaml" % (model_name))
        save_dict_to_yaml(params_dict,save_path)
        
        
        # params_json = json.dumps(params_dict)
        # with open('config.yaml','w',encoding='utf-8') as f:
        #     yaml.dump(params_dict,default_flow_style=True)
        #     yaml.safe_dump(yaml.load(params_dict,Loader=yaml.FullLoader),f,
        #                    allow_unicode=True,default_flow_style=False)
            # yaml.safe_dump(yaml.load(params_json,Loader=yaml.FullLoader),f,
            #                allow_unicode=True,default_flow_style=False)
            #allow_unicode=True在数据中存在中文时，解决编码问题
            
        # ***************** initialization ******************
        # self.SingleGreenRoof.d1_0 = self.d1_0.value()                # initial depth of water stored on the surface (mm)
        # self.SingleGreenRoof.F_0 = self.F_0.value()   # initial accumulative infiltraion of surface water into the soil layer (mm),500(20200521)0500

        # =========== the Design parameters ============
        # self.SingleGreenRoof.chang = self.chang.value()                 # 绿色屋顶长度, mm
        # self.SingleGreenRoof.kuan = self.kuan.value()                   # 绿色屋顶宽度, mm

        #soilDensity = 1.4          # soil dry bulk density (g/cm**3)
        #storageDensity = 1.8       # stone dry bulk density (g/cm**3)
        
        # ================ system setting ====================
        # self.Tstep = 1/60               # time step (hr),min

        #设置的常数
        # self.SingleGreenRoof.albedo = self.albedo.value()  #表面反射率
        # self.SingleGreenRoof.e0 = self.e0.value()     #0℃水的饱和蒸气压，kpa
        #z00 = 0.01   #地表有效粗糙长度，m
        #z = 2  #参考高度

        #已率定的水文参数,20220710
        
        # self.SingleGreenRoof.C1 = self.C1.value() * 1e-8        #砾石层水分蒸发的空气动力学导率

        # print("参数更新完毕")
        # print("self.SingleGreenRoof.xitaFC:,%.4f" % (self.SingleGreenRoof.xitaFC))
        # 输入参数整合成yaml格式
        # 执行保存
        return 
         
    def green_roof_sim_and_val(self):
        # 判断是否选择了路径，若无，则要弹窗
        if (not hasattr(self, 'weather_file_path')) or (not hasattr(self, 'observed_file_path')):
            QMessageBox.critical(
            self,
            '错误',
            '执行 仿真&验证 前，请先选择数据文件，气象和实测都是必选的）！')
            return 
        
        # 天气和观测文件赋值
        self.SingleGreenRoof.observed_file_path = self.observed_file_path
        self.SingleGreenRoof.weather_file_path = self.weather_file_path
        
        self.SingleGreenRoof.get_weather_data
        # 检查仿真时间是否正确
        if not self.check_datetime(self.SingleGreenRoof.LoopCount,
                            start_dt_str=self.SingleGreenRoof.start_dt_str,
                            end_dt_str=self.SingleGreenRoof.end_dt_str,
                            time_step=self.SingleGreenRoof.Tstep):
            QMessageBox.critical(
            self,
            '错误',
            '仿真日期长度与真实数据长度不匹配！请仿真日期参数或真实数据文件')
            return 
        
        """仿真，并返回结果"""
        q3 = self.SingleGreenRoof.sim
        
        """结果可视化"""
        NSE = self.SingleGreenRoof.outflow_NSE(q3)
        q3obs = self.SingleGreenRoof.q3obs
        q3sim = self.SingleGreenRoof.q3sim
        self.show_curve(q3sim,q3obs,NSE)
            
        QMessageBox.information(self,'运行完毕','仿真已完成！')
        
    def show_curve(self,pred, obs,NSE):        
        width,height = self.green_roof_sim_curve.width(),self.green_roof_sim_curve.height()
        F1 = MyFigure(width=width, height=height, 
                      dpi=150)
        F1.resize(width,height)
        F1.axes1 = F1.fig.add_subplot(111) 
        
        fs = 20
        xx_pred = range(len(pred))
        if obs is not None:
            xx_obs = range(len(obs))

        F1.axes1.plot(xx_pred,pred,color='r',lw=2,linestyle="-",label="仿真值")
        if obs is not None:
            # F1.axes1.plot(xx_obs,pred,color='g',lw=2,linestyle=".",label="观测值")
            F1.axes1.plot(xx_obs,pred,"o",color='g',lw=1,label="观测值")
        
        def get_xticklabels(start,end,num=6,freq='min'):
            dates = pd.date_range(start=start,end=end,freq=freq)
            date_list = [x.strftime("%Y-%m-%d %H:%M") for x in dates]
            show_dates = date_list[::len(dates)//num] + [date_list[-1]]
            
            xticks = list(range(0,len(dates),len(dates)//num)) + [len(dates)-1]
            xlabels = [show_dates[i] for i in range(len(show_dates))]
            
            return xticks, xlabels
        
        if obs is not None:
            xticks, xlabels = get_xticklabels(self.SingleGreenRoof.start_dt_str,self.SingleGreenRoof.end_dt_str,freq='1H')
        else:
            xticks, xlabels = get_xticklabels(self.SingleGreenRoof.start_dt_str,self.SingleGreenRoof.end_dt_str, freq='min')
        
        F1.axes1.legend(fontsize=fs-2)
        F1.axes1.set_xlabel(u"时间", fontsize=fs-2)
        F1.axes1.set_ylabel(u"出流量 (mm/hr)", fontsize=fs-5)
        F1.axes1.set_xticks(xticks)
        F1.axes1.set_xticklabels(labels=xlabels,rotation=90)
        # F1.axes1.set_yticklabels(fontsize=fs-2)
        F1.axes1.tick_params(axis='x',labelsize=fs-2)
        F1.axes1.tick_params(axis='y',labelsize=fs)
        if NSE is None:
            F1.axes1.set_title(u"NSE is None", fontsize=fs)
        else:
            F1.axes1.set_title(u"NSE=%.4f" % NSE, fontsize=fs)
            
        F1.axes1.grid(alpha=0.5,linestyle="-.")
        # F1.axes1.set_tight_layout()
        
        # save
        # fig_save_dir = "figs"
        # if not os.path.exists(fig_save_dir):
        #     os.makedirs(fig_save_dir,exist_ok=True)
        # fig_save_path = os.path.join(fig_save_dir,"outflow.jpg")
        # plt.savefig(fig_save_path)
        

        self.scene = QGraphicsScene()  # 创建一个场景
        self.scene.addWidget(F1)  # 将图形元素添加到场景中
        self.green_roof_sim_curve.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.green_roof_sim_curve.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.green_roof_sim_curve.setScene(self.scene)  # 将创建添加到图形视图显示窗口
        
        plt.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)                    # 创建应用程序对象
    mainWindow = Application()                      # 实例化界面    
    mainWindow.show()                               # 窗口显示
    sys.exit(app.exec_())                           # 主循环结束
