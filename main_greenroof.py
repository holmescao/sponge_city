import os 
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt
from sponge_city import Ui_MainWindow # 导入主窗口
from utils.green_roof import GreenRoof                   # 导入要执行的算法

# matplotlib.use("Qt5Agg")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif']=['Microsoft Yahei'] # 设定字体为微软雅黑


# 新建类继承于UI类，方便进一步书写逻辑
class Application(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)             # 创建界面
        
        """信号和槽函数部分"""
        # 选择观测数据文件        
        self.action_open_observed_file.triggered.connect(self.open_observed_file)
        self.action_open_weather_file.triggered.connect(self.open_weather_file)
        
        self.action_sim_green_roof.triggered.connect(self.green_roof_sim) # 仿真
        self.action_sim_and_val_green_roof.triggered.connect(self.green_roof_sim_and_val) # 仿真&验证
        # self.action_sim_green_roof.clicked.connect(
        #     lambda: self.test(self.test_button,))
    
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

    @property
    def upate_params(self):
        # TODO：分离到green_roof_config.py文件中
        # ***************** initialization ******************
        self.GreenRoof.d1_0 = self.d1_0.value()                # initial depth of water stored on the surface (mm)
        self.GreenRoof.xita2_0 = self.xita2_0.value()           # soil layer initial moisture content (volume of water / total volume of soil)
        self.GreenRoof.d3_0 = self.d3_0.value()    # initial depth of water in the storage layer (mm)
        self.GreenRoof.F_0 = self.F_0.value()   # initial accumulative infiltraion of surface water into the soil layer (mm),500(20200521)0500

        # =========== the Design parameters ============
        self.GreenRoof.chang = self.chang.value()                 # 绿色屋顶长度, mm
        self.GreenRoof.kuan = self.kuan.value()                   # 绿色屋顶宽度, mm
        self.GreenRoof.D1 = self.D1.value()                       #溢流层深度，mm，注：论文里未注明溢流层深度
        self.GreenRoof.D2 = self.D2.value()                       #基质层深度，mm
        self.GreenRoof.D3 = self.D3.value()                       #蓄水层深度,mm
        self.GreenRoof.D3D = self.D3D.value()                    #蓄水层最小可出流深度,mm

        #soilDensity = 1.4          # soil dry bulk density (g/cm**3)
        #storageDensity = 1.8       # stone dry bulk density (g/cm**3)
        self.GreenRoof.phi1 = self.phi1.value() # void fraction of any surface volume (i.e., the fraction of freeboard above the surface not filled with vegetation)
        
        # ================ system setting ====================
        # self.Tstep = 1/60               # time step (hr),min

        #设置的常数
        self.GreenRoof.albedo = self.albedo.value()  #表面反射率
        self.GreenRoof.e0 = self.e0.value()     #0℃水的饱和蒸气压，kpa
        #z00 = 0.01   #地表有效粗糙长度，m
        #z = 2  #参考高度

        #已率定的水文参数,20220710
        self.GreenRoof.xitaFC = self.xitaFC.value() #田间持水量
        self.GreenRoof.xitaWP = self.xitaWP.value()  #凋萎点
        self.GreenRoof.phi2 = self.phi2.value()     #土壤层孔隙率
        self.GreenRoof.phi3 = self.phi3.value()    #砾石层孔隙率
        self.GreenRoof.C3D = self.C3D.value()     #孔流系数0.105,0.148,5.65
        self.GreenRoof.eta3D = self.eta3D.value()  #孔流指数，原1.865,1.93,0.9
        self.GreenRoof.C1 = self.C1.value() * 1e-8        #砾石层水分蒸发的空气动力学导率 # TODO:注意要x 1e-8
        self.GreenRoof.xitacb = self.xitacb.value()    #土壤含水量大于xitacb时，植物蒸腾不受水分限制,0.28#20211223
        self.GreenRoof.Ksat = self.Ksat.value()     #土壤层基质流饱和导水率，mm/hr312.6044，231.72
        self.GreenRoof.HCO = self.HCO.value()   #土壤层下部水分渗出公式中的导水衰减常数34.5439
        self.GreenRoof.psi2 = self.psi2.value()   #土壤层表面水分入渗公式中的土壤层吸力水头44.1493
        
    def green_roof_sim(self):
        # 判断是否选择了路径，若无，则要弹窗
        if not hasattr(self, 'weather_file_path'):
            QMessageBox.critical(
            self,
            '错误',
            '执行 仿真 前，请先选择数据文件，气象是必选的）！')
            return 
        
        # 实例化绿色屋顶模型
        self.GreenRoof = GreenRoof("",self.weather_file_path)
        
        """参数赋值"""
        self.upate_params
        """仿真，并返回结果"""
        q3 = self.GreenRoof.sim
        
        """结果可视化"""
        self.show_curve(q3,None,None)
            
        QMessageBox.information(self,'运行完毕','仿真已完成！')
        
    def green_roof_sim_and_val(self):
        # 判断是否选择了路径，若无，则要弹窗
        if (not hasattr(self, 'weather_file_path')) or (not hasattr(self, 'observed_file_path')):
            QMessageBox.critical(
            self,
            '错误',
            '执行 仿真&验证 前，请先选择数据文件，气象和实测都是必选的）！')
            return 
        # 实例化绿色屋顶模型
        self.GreenRoof = GreenRoof(self.observed_file_path,self.weather_file_path)
        
        """参数赋值"""
        self.upate_params
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
            F1.axes1.plot(xx_obs,pred,"o",color='g',lw=1.5,label="观测值")
            
        F1.axes1.legend(fontsize=fs-2)
        F1.axes1.set_xlabel(u"时间 (min)", fontsize=fs-2)
        F1.axes1.set_ylabel(u"出流量 (mm/hr)", fontsize=fs-5)
        # F1.axes1.set_xticklabels(fontsize=fs-2)
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
      
if __name__ == '__main__':
    app = QApplication(sys.argv)                    # 创建应用程序对象
    mainWindow = Application()                      # 实例化界面
    mainWindow.show()                               # 窗口显示
    sys.exit(app.exec_())                           # 主循环结束
