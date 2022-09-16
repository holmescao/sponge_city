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
"""================= 导入窗口================="""
from utils.ui.sponge_city import Ui_MainWindow # 导入主窗口
from utils.ui_class.SimdateOptions import SimdateOptions
from utils.ui_class.GreenroofInput import GreenroofInput
from utils.ui_class.Block import Block

"""================= 导入函数================="""
from utils.algo.green_roof import GreenRoof                   # 导入要执行的算法
from utils.algo.non_point_pollution import NonPointPollution
from utils.algo.general_functions import save_dict_to_yaml
from utils.algo.figure_function import MyFigure, fig_rainfall,fig_runoff,fig_pollution



# 新建类继承于UI类，方便进一步书写逻辑
class Application(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)             # 创建界面
        
        """实例化"""
        # 绿色屋顶模型
        self.GreenRoof = GreenRoof("","")
        # 面源污染模型
        self.NonPointPollution = NonPointPollution("")
        # 实例化输入界面
        self.block_Dialog = Block(self) # !得把self传进去，否则不会保持窗口
        self.sim_datetime_Dialog = SimdateOptions(self) # !得把self传进去，否则不会保持窗口
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
        
        """工具栏-运行"""
        # 绿色屋顶
        self.action_sim_green_roof.triggered.connect(self.green_roof_sim) # 仿真
        self.action_sim_and_val_green_roof.triggered.connect(self.green_roof_sim_and_val) # 仿真&验证
        # 面源斑块
        self.action_sim_block.triggered.connect(self.block_sim) # 仿真
        
        
        # self.action_sim_green_roof.clicked.connect(
        #     lambda: self.test(self.test_button,))
        
    
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
        self.block_Dialog.rejected.connect(lambda: self.reset_params(temp_block_params))
        
        # 打开、保持窗口
        self.block_Dialog.show()
    
    def reset_params(self, temp_block_params):
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
        self.GreenRoof.start_dt_str = start_dt_str
        self.GreenRoof.end_dt_str = end_dt_str
        self.GreenRoof.Tstep = time_step
        
        
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
        # self.GreenRoof.d1_0 = self.d1_0.value()                # initial depth of water stored on the surface (mm)
        self.GreenRoof.xita2_0 = params.xita2_0.value()           # soil layer initial moisture content (volume of water / total volume of soil)
        self.GreenRoof.d3_0 = params.d3_0.value()    # initial depth of water in the storage layer (mm)
        # self.GreenRoof.F_0 = self.F_0.value()   # initial accumulative infiltraion of surface water into the soil layer (mm),500(20200521)0500

        # =========== the Design parameters ============
        # self.GreenRoof.chang = self.chang.value()                 # 绿色屋顶长度, mm
        # self.GreenRoof.kuan = self.kuan.value()                   # 绿色屋顶宽度, mm
        self.GreenRoof.D1 = params.D1.value()                       #溢流层深度，mm，注：论文里未注明溢流层深度
        self.GreenRoof.D2 = params.D2.value()                       #基质层深度，mm
        self.GreenRoof.D3 = params.D3.value()                       #蓄水层深度,mm
        self.GreenRoof.D3D = params.D3D.value()                    #蓄水层最小可出流深度,mm

        #soilDensity = 1.4          # soil dry bulk density (g/cm**3)
        #storageDensity = 1.8       # stone dry bulk density (g/cm**3)
        self.GreenRoof.phi1 = params.phi1.value() # void fraction of any surface volume (i.e., the fraction of freeboard above the surface not filled with vegetation)
        
        # ================ system setting ====================
        # self.Tstep = 1/60               # time step (hr),min

        #设置的常数
        # self.GreenRoof.albedo = self.albedo.value()  #表面反射率
        # self.GreenRoof.e0 = self.e0.value()     #0℃水的饱和蒸气压，kpa
        #z00 = 0.01   #地表有效粗糙长度，m
        #z = 2  #参考高度

        #已率定的水文参数,20220710
        self.GreenRoof.xitaFC = params.xitaFC.value() #田间持水量
        self.GreenRoof.xitaWP = params.xitaWP.value()  #凋萎点
        self.GreenRoof.phi2 = params.phi2.value()     #土壤层孔隙率
        self.GreenRoof.phi3 = params.phi3.value()    #砾石层孔隙率
        self.GreenRoof.C3D = params.C3D.value()     #孔流系数0.105,0.148,5.65
        self.GreenRoof.eta3D = params.eta3D.value()  #孔流指数，原1.865,1.93,0.9
        # self.GreenRoof.C1 = self.C1.value() * 1e-8        #砾石层水分蒸发的空气动力学导率
        self.GreenRoof.xitacb = params.xitacb.value()    #土壤含水量大于xitacb时，植物蒸腾不受水分限制,0.28#20211223
        self.GreenRoof.Ksat = params.Ksat.value()     #土壤层基质流饱和导水率，mm/hr312.6044，231.72
        self.GreenRoof.HCO = params.HCO.value()   #土壤层下部水分渗出公式中的导水衰减常数34.5439
        self.GreenRoof.psi2 = params.psi2.value()   #土壤层表面水分入渗公式中的土壤层吸力水头44.1493
        # print("参数更新完毕")
        # print("self.GreenRoof.xitaFC:,%.4f" % (self.GreenRoof.xitaFC))
        
        
    def block_sim(self):
        # 判断是否选择了路径，若无，则要弹窗
        if not hasattr(self, 'weather_file_path'):
            QMessageBox.critical(
            self,
            '错误',
            '执行 仿真 前，请先选择数据文件，气象是必选的）！')
            return 
        
        # 天气文件赋值
        self.NonPointPollution.weather_file_path = self.weather_file_path
        self.NonPointPollution.get_weather_data
        
        # self.update_sim_datetime()
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
        #                                     start_date=self.GreenRoof.start_dt_str,
        #                                     end_date=self.GreenRoof.end_dt_str,
        #                                     freq='1min')
        
        # self.save_single_sponge_sim_params(model_name="greenroof", 
        #                                    params_dict=self.GreenRoof.pack_params,
        #                                    start_date=self.GreenRoof.start_dt_str,
        #                                     end_date=self.GreenRoof.end_dt_str,
        #                                     timestamp=timestamp,
        #                                     freq='1min')
        
        # QMessageBox.information(self,'运行完毕','完成！实验参数和结果保存在：\n%s' %(sim_results_save_dir))

    def show_block(self, rain,runoff, pollution):
        # rainfall
        F_rain = fig_rainfall(rain, 
                              width=self.block_rainfall_sim_res_rainfall.width(),
                              height=self.block_rainfall_sim_res_rainfall.height(), 
            start_dt_str=self.NonPointPollution.start_dt_str,
            end_dt_str=self.NonPointPollution.end_dt_str,
            freq="1H")
        
        # runoff
        F_runoff = fig_runoff(runoff, 
                              width=self.block_rainfall_sim_res_runoff.width(),
                              height=self.block_rainfall_sim_res_runoff.height(), 
            start_dt_str=self.NonPointPollution.start_dt_str,
            end_dt_str=self.NonPointPollution.end_dt_str,
            freq="1H")
        
        # pollution
        F_pollution = fig_pollution(pollution,
                              width=self.block_rainfall_sim_res_pollution.width(),
                              height=self.block_rainfall_sim_res_pollution.height(), 
            start_dt_str=self.NonPointPollution.start_dt_str,
            end_dt_str=self.NonPointPollution.end_dt_str,
            freq="1H")
        
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
        self.GreenRoof.weather_file_path = self.weather_file_path
        self.GreenRoof.get_weather_data
        # 检查仿真时间是否正确
        if not self.check_datetime(self.GreenRoof.LoopCount,
                            start_dt_str=self.GreenRoof.start_dt_str,
                            end_dt_str=self.GreenRoof.end_dt_str,
                            time_step=self.GreenRoof.Tstep):
            QMessageBox.critical(
            self,
            '错误',
            '仿真日期长度与真实数据长度不匹配！请检查仿真日期参数或真实数据文件')
            return 
        
        """仿真，并返回结果"""
        q3 = self.GreenRoof.sim
        
        """结果可视化"""
        self.show_curve(q3,None,None)
        
        """结果自动保存"""
        sim_results_save_dir,timestamp = self.save_single_sponge_sim_results(model_name="greenroof", 
                                            data=q3, 
                                            start_date=self.GreenRoof.start_dt_str,
                                            end_date=self.GreenRoof.end_dt_str,
                                            freq='1min')
        
        self.save_single_sponge_sim_params(model_name="greenroof", 
                                           params_dict=self.GreenRoof.pack_params,
                                           start_date=self.GreenRoof.start_dt_str,
                                            end_date=self.GreenRoof.end_dt_str,
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
        # self.GreenRoof.d1_0 = self.d1_0.value()                # initial depth of water stored on the surface (mm)
        # self.GreenRoof.F_0 = self.F_0.value()   # initial accumulative infiltraion of surface water into the soil layer (mm),500(20200521)0500

        # =========== the Design parameters ============
        # self.GreenRoof.chang = self.chang.value()                 # 绿色屋顶长度, mm
        # self.GreenRoof.kuan = self.kuan.value()                   # 绿色屋顶宽度, mm

        #soilDensity = 1.4          # soil dry bulk density (g/cm**3)
        #storageDensity = 1.8       # stone dry bulk density (g/cm**3)
        
        # ================ system setting ====================
        # self.Tstep = 1/60               # time step (hr),min

        #设置的常数
        # self.GreenRoof.albedo = self.albedo.value()  #表面反射率
        # self.GreenRoof.e0 = self.e0.value()     #0℃水的饱和蒸气压，kpa
        #z00 = 0.01   #地表有效粗糙长度，m
        #z = 2  #参考高度

        #已率定的水文参数,20220710
        
        # self.GreenRoof.C1 = self.C1.value() * 1e-8        #砾石层水分蒸发的空气动力学导率

        # print("参数更新完毕")
        # print("self.GreenRoof.xitaFC:,%.4f" % (self.GreenRoof.xitaFC))
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
        self.GreenRoof.observed_file_path = self.observed_file_path
        self.GreenRoof.weather_file_path = self.weather_file_path
        
        self.GreenRoof.get_weather_data
        # 检查仿真时间是否正确
        if not self.check_datetime(self.GreenRoof.LoopCount,
                            start_dt_str=self.GreenRoof.start_dt_str,
                            end_dt_str=self.GreenRoof.end_dt_str,
                            time_step=self.GreenRoof.Tstep):
            QMessageBox.critical(
            self,
            '错误',
            '仿真日期长度与真实数据长度不匹配！请仿真日期参数或真实数据文件')
            return 
        
        """仿真，并返回结果"""
        q3 = self.GreenRoof.sim
        
        """结果可视化"""
        NSE = self.GreenRoof.outflow_NSE(q3)
        q3obs = self.GreenRoof.q3obs
        q3sim = self.GreenRoof.q3sim
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
            xticks, xlabels = get_xticklabels(self.GreenRoof.start_dt_str,self.GreenRoof.end_dt_str,freq='1H')
        else:
            xticks, xlabels = get_xticklabels(self.GreenRoof.start_dt_str,self.GreenRoof.end_dt_str, freq='min')
        
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
