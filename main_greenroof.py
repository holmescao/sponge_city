# TODO: 有些无法在qt designer完成的事情，需要写代码完成，所以最终还是全靠写代码来设计吧！
import json
import yaml
import numpy as np
import pandas as pd
import datetime
import os 
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox,QGraphicsScene,QDialog
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt
"""================= 导入窗口================="""
from sponge_city import Ui_MainWindow # 导入主窗口
from green_roof import Ui_Greenroof # 导入绿色屋顶输入界面
from sim_dates import Ui_SimDates # 导入时间选择界面
"""================= 导入窗口================="""
from utils.green_roof import GreenRoof                   # 导入要执行的算法
from utils.general_functions import save_dict_to_yaml

# matplotlib.use("Qt5Agg")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif']=['Microsoft Yahei'] # 设定字体为微软雅黑


# 重写一个matplotlib图像绘制类
class MyFigure(FigureCanvasQTAgg):
   def __init__(self,width=5,height=4,dpi = 100):
      # 1、创建一个绘制窗口Figure对象
      self.fig = Figure(figsize=(width,height),dpi=dpi,tight_layout=True)
      # 2、在父类中激活Figure窗口,同时继承父类属性
      super(MyFigure, self).__init__(self.fig)
 
   # 这里就是绘制图像、示例
   def plotSin(self,x,y):
      self.axes0 = self.fig.add_subplot(111)
      self.axes0.plot(x,y)


# 新建类继承于UI类，方便进一步书写逻辑
class Application(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)             # 创建界面
        
        """实例化"""
        # 实例化绿色屋顶模型
        self.GreenRoof = GreenRoof("","")
        
        """信号和槽函数部分"""
        # 选择观测数据文件        
        self.action_open_observed_file.triggered.connect(self.open_observed_file)
        self.action_open_weather_file.triggered.connect(self.open_weather_file)
        
        
        self.listView.clicked.connect(self.select_haimian) # 点击选择海绵体，弹窗选择参数
        
        self.actionDates.triggered.connect(self.open_sim_datetime_dialog) # 选择仿真起止日期和步长
        self.action_sim_green_roof.triggered.connect(self.green_roof_sim) # 仿真
        self.action_sim_and_val_green_roof.triggered.connect(self.green_roof_sim_and_val) # 仿真&验证
        # self.action_sim_green_roof.clicked.connect(
        #     lambda: self.test(self.test_button,))
        
        
    def open_sim_datetime_dialog(self):
        # 实例化输入界面
        sim_datetime_Dialog = SimdateOptions(self) # !得把self传进去，否则不会保持窗口
        # 收到确认信号后，更新参数
        self.dateTime_start_edit = sim_datetime_Dialog.dateTime_start_edit
        self.dateTime_end_edit = sim_datetime_Dialog.dateTime_end_edit
        self.time_step = sim_datetime_Dialog.spinBox_timestep
        sim_datetime_Dialog.accepted.connect(self.update_sim_datetime)
        # sim_datetime_Dialog.dateTime_start_edit.dateTimeChanged.connect(self.update_sim_datetime)
        # green_roof_Dialog.pushButton_greenroof_ok.clicked.connect(self.upate_params)
        # sim_datetime_Dialog.pushButton_greenroof_ok.clicked.connect(lambda: self.upate_params(green_roof_Dialog,))
        # green_roof_Dialog.Signal_updateparams.connect(self.upate_params)
        sim_datetime_Dialog.show() # 打开窗口
    
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
        
        # TODO：其他的也一样赋值吧；
        # 或者放到具体海绵单体的仿真函数里面
        
    def check_datetime(self,data_num, start_dt_str,end_dt_str,time_step):
        start_dt = datetime.datetime.strptime(start_dt_str,"%Y-%m-%d %H:%M")
        end_dt = datetime.datetime.strptime(end_dt_str,"%Y-%m-%d %H:%M")
        
        # 计算日期之间的点数
        time_delta = end_dt - start_dt
        total_min = time_delta.days *24 *60 + time_delta.seconds // 60 + 1
        step_per_min = 1/time_step/60
        time_num = total_min *step_per_min

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
            '仿真日期长度与真实数据长度不匹配！请仿真日期参数或真实数据文件')
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

class SimdateOptions(QDialog, Ui_SimDates):
    def __init__(self, parent=None):
        super(SimdateOptions, self).__init__(parent)
        self.setupUi(self)             # 创建界面

class GreenroofInput(QDialog, Ui_Greenroof):
    def __init__(self, parent=None):
        super(GreenroofInput, self).__init__(parent)
        self.setupUi(self)             # 创建界面

    
if __name__ == '__main__':
    app = QApplication(sys.argv)                    # 创建应用程序对象
    mainWindow = Application()                      # 实例化界面    
    mainWindow.show()                               # 窗口显示
    sys.exit(app.exec_())                           # 主循环结束
