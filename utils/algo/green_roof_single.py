from utils.algo.general_functions import (save_dict_to_yaml, check_datetime,
                                          save_sim_results,
                                          save_sim_params,
                                          check_datetime_setting,
                                          check_observed_file,
                                          check_weather_file)
from utils.algo.figure_function import fig_single_sponge_sim_curve
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene
from PyQt5.QtCore import Qt


class SingleGreenRoof:
    def __init__(self,
                 observed_file_path="",
                 weather_file_path="") -> None:
        """参数初始化"""
        # 设置绿色屋顶初始状态***************** initialization ******************
        # initial depth of water stored on the surface (mm)
        self.d1_0 = 0
        # soil layer initial moisture content (volume of water / total volume of soil)
        self.xita2_0 = 0.57
        self.d3_0 = 300    # initial depth of water in the storage layer (mm)
        # initial accumulative infiltraion of surface water into the soil layer (mm),500(20200521)0500
        self.F_0 = 0

        # =========== the Design parameters ============
        self.chang = 1000                   # 绿色屋顶长度, mm
        self.kuan = 1000                   # 绿色屋顶宽度, mm
        self.A = self.chang*self.kuan/10**6  # 绿色屋顶面积，m2
        self.D1 = 30  # 溢流层深度，mm，注：论文里未注明溢流层深度
        self.D2 = 100  # 基质层深度，mm
        self.D3 = 300  # 蓄水层深度,mm
        self.D3D = 280  # 蓄水层最小可出流深度,mm

        # soilDensity = 1.4          # soil dry bulk density (g/cm**3)
        # storageDensity = 1.8       # stone dry bulk density (g/cm**3)
        # void fraction of any surface volume (i.e., the fraction of freeboard above the surface not filled with vegetation)
        self.phi1 = 0.95

        # ================ system setting ====================
        # 设置的常数
        self.albedo = 0.23  # 表面反射率
        self.e0 = 0.6113  # 0℃水的饱和蒸气压，kpa
        # z00 = 0.01   #地表有效粗糙长度，m
        # z = 2  #参考高度

        # 已率定的水文参数,20220710
        self.xitaFC = 0.28  # 田间持水量
        self.xitaWP = 0.225  # 凋萎点
        self.phi2 = 0.5  # 土壤层孔隙率
        self.phi3 = 0.7369  # 砾石层孔隙率
        self.C3D = 6.6077  # 孔流系数0.105,0.148,5.65
        self.eta3D = 1  # 孔流指数，原1.865,1.93,0.9
        self.C1 = 0.000011675  # 砾石层水分蒸发的空气动力学导率 # TODO:注意要x 1e-8
        self.xitacb = 0.375  # 土壤含水量大于xitacb时，植物蒸腾不受水分限制,0.28#20211223
        self.Ksat = 178.57  # 土壤层基质流饱和导水率，mm/hr312.6044，231.72
        self.HCO = 4.8065  # 土壤层下部水分渗出公式中的导水衰减常数34.5439
        self.psi2 = 320.2869  # 土壤层表面水分入渗公式中的土壤层吸力水头44.1493

        # 仿真起止时间，及时间步长
        self.start_dt_str = "2021-05-25 00:01"
        self.end_dt_str = "2021-06-29 00:00"
        self.Tstep = 1/60               # time step (hr),min

        self.rainfall = None  # 降雨量，mm/hr
        # 设置循环长度
        self.LoopCount = 0
        # 文件路径
        self.observed_file_path = observed_file_path
        self.weather_file_path = weather_file_path

    def upate_params(self, params):
        # ***************** initialization ******************
        # self.d1_0 = self.d1_0.value()                # initial depth of water stored on the surface (mm)
        # soil layer initial moisture content (volume of water / total volume of soil)
        self.xita2_0 = params.xita2_0.value()
        # inater in the storage layer (mm)
        self.d3_0 = params.d3_0.value()
        # seof.F_0 = self.F_0.value()   # initial accumulative infiltraion of surface water into the soil layer (mm),500(20200521)0500

        # =sign parameters ============
        # seof.chang = self.chang.value()                 # 绿色屋顶长度, mm
        # seof.kuan = self.kuan.value()                   # 绿色屋顶宽度, mm
        self.D1 = params.D1.value()  # 溢流层深度，mm，注：论文里未注明溢流层深度
        self.D2 = params.D2.value()  # 基质层深度，mm
        self.D3 = params.D3.value()  # 蓄水层深度,mm
        self.D3D = params.D3D.value()  # 蓄水层最小可出流深度,mm

        # s         # soil dry bulk density (g/cm**3)
        # st.8       # stone dry bulk density (g/cm**3)
        # vony surface volume (i.e., the fraction of freeboard above the surface not filled with vegetation)
        self.phi1 = params.phi1.value()

        # =ystem setting ====================
        # se              # time step (hr),min
        # of.albedo = self.albedo.value()  #表面反射率
        # seof.e0 = self.e0.value()     #0℃水的饱和蒸气压，kpa
        # z0粗糙长度，m
        #    # 已        self.xitaFC = params.xitaFC.value()  # 田间持水量
        self.xitaWP = params.xitaWP.value()  # 凋萎点
        self.phi2 = params.phi2.value()  # 土壤层孔隙率
        self.phi3 = params.phi3.value()  # 砾石层孔隙率
        self.C3D = params.C3D.value()  # 孔流系数0.105,0.148,5.65
        self.eta3D = params.eta3D.value()  # 孔流指数，原1.865,1.93,0.9
        # seof.C1 = self.C1.value() * 1e-8        #砾石层水分蒸发的空气动力学导率
        # 土壤腾不受水分限制,0.28#20211223
        self.xitacb = params.xitacb.value()
        # 土壤12.6044，231.72
        self.Ksat = params.Ksat.value()
        self.HCO = params.HCO.value()  # 土壤层下部水分渗出公式中的导水衰减常数34.5439
        self.psi2 = params.psi2.value()  # 土壤层表面水分入渗公式中的土壤层吸力水头44.1493
        # p      # print("self.xitaFC:,%.4f" % (self.xitaFC))

    @property
    def pack_params(self):
        green_roof_params_dict = {
            "蓄水层": {
                "蓄水层水深": self.d3_0,
                "蓄水层深度": self.D3,
                "蓄水层最小可出流深度": self.D3D,
                "砾石层孔隙率": self.phi3,
                "孔流系数": self.C3D,
                "孔流指数": self.eta3D,
            },
            "土壤层": {
                "土层含水量": self.xita2_0,
                "基质层深度": self.D2,
                "田间持水量": self.xitaFC,
                "凋萎点": self.xitaWP,
                "土壤层孔隙率": self.phi2,
                "临界含水量": self.xitacb,
                "饱和导水率": self.Ksat,
                "衰减常数": self.HCO,
                "吸力水头": self.psi2,
            },
            "表层": {
                "溢流层深度": self.D1,
                "空隙率": self.phi1,
            }
        }

        #  green_roof_params_dict = {
        #     "蓄水层":{
        #         "蓄水层水深":self.GreenRoof.d3_0,
        #         "蓄水层深度":self.GreenRoof.D3,
        #         "蓄水层最小可出流深度":self.GreenRoof.D3D,
        #         "砾石层孔隙率":self.GreenRoof.phi3,
        #         "孔流系数":self.GreenRoof.C3D,
        #         "孔流指数":self.GreenRoof.eta3D,
        #     },
        #     "土壤层":{
        #         "土层含水量":self.GreenRoof.xita2_0,
        #         "基质层深度":self.GreenRoof.D2,
        #         "田间持水量":self.GreenRoof.xitaFC,
        #         "凋萎点":self.GreenRoof.xitaWP,
        #         "土壤层孔隙率":self.GreenRoof.phi2,
        #         "临界含水量":self.GreenRoof.xitacb,
        #         "饱和导水率":self.GreenRoof.Ksat,
        #         "衰减常数":self.GreenRoof.HCO,
        #         "吸力水头":self.GreenRoof.psi2,
        #     },
        #     "表层":{
        #         "溢流层深度":self.GreenRoof.D1,
        #         "空隙率":self.GreenRoof.phi1,
        #     }
        # }

        return green_roof_params_dict

    @property
    def get_observed_data(self):
        # 输入实测出流数据,仅包括出流量不为0的数据
        data = np.loadtxt(self.observed_file_path)
        self.Qnumberobs = data[:, 0]  # 实测出流流量的对应分钟序号
        self.q3obs = data[:, 1]  # 实测出流流量(仅包括不为0的数据），mm/hr

    @property
    def get_weather_data(self):
        # 输入计算蒸散发所需的气象数据
        data = np.loadtxt(self.weather_file_path)
        self.i0 = data[:, 0]  # 降雨量，mm/min
        self.Rsolar = data[:, 1]/3600*10**6  # 太阳辐射，MJ/(m2 h)转换成W/m2
        self.Tair = data[:, 2]  # 气温，℃
        self.gravelT = data[:, 2]  # 蓄水层水文，假定与气温相同，℃
        self.RH = data[:, 3]  # 空气湿度，#
        self.Uwind = data[:, 4]  # 风速，m/s
        # P = InputData8(:,6)  #大气压，kPa
        # 将大气压kpa转换为Psychrometric constant，kPa/℃
        self.y = 0.665*(10 ** (-3))*data[:, 5]
        # Ra_solar = data(:,8) #地外太阳辐射，W/m2 # 20211106

        # 设置循环长度
        self.LoopCount = len(data)

    @property
    def sim(self):
        self.get_weather_data
        # 设置向量
        # depth of water stored on the surface (mm)
        d1 = np.zeros(self.LoopCount)
        # soil layer moisture content (volume of water / total volume of soil)
        xita2 = self.xitaWP*np.ones(self.LoopCount)
        # depth of water in the storage layer (mm)
        d3 = np.zeros(self.LoopCount)
        # suction head of the storage drain (mm)
        h3 = np.zeros(self.LoopCount)
        # the effective rainfall, usually = i + q0 +d1 (mm/hr)
        ia = np.zeros(self.LoopCount)
        # surface layer runoff or overflow rate (mm/hr)
        q1 = np.zeros(self.LoopCount)
        # storage layer underdrain outflow rate (mm/hr)
        q3 = np.zeros(self.LoopCount)
        e1 = np.zeros(self.LoopCount)  # surface ET rate (mm/hr),PM公式
        # soil layer ET rate (mm/hr),PM公式,考虑水分胁迫系数的SW模型计算蒸散发量，mm/h
        e2 = np.zeros(self.LoopCount)
        e3 = np.zeros(self.LoopCount)  # storage layer ET rate (mm/hr)
        # infiltration rate of surface water into the soil layer (mm/hr)
        f1 = np.zeros(self.LoopCount)
        # accumulative infiltraion of surface water into the soil layer (mm)
        F1 = np.zeros(self.LoopCount)
        # percolation rate of water through the soil layer into the storage layer (mm/hr)
        f2 = np.zeros(self.LoopCount)
        es2 = np.zeros(self.LoopCount)  # 饱和水汽压，kPa
        ea2 = np.zeros(self.LoopCount)  # 实际水汽压，kPa
        D = np.zeros(self.LoopCount)  # 饱和水汽压差，kpa
        # Slope of saturation vapour pressure curve，kPa/℃
        delta = np.zeros(self.LoopCount)
        # G = np.zeros(LoopCount) #土壤热通量，W/m2,白天和夜间的数值不同
        Rn = np.zeros(self.LoopCount)  # 冠层净辐射量，W/m2,暂不考虑长波辐射的损失#
        # Rns = np.zeros(LoopCount) #土壤净辐射量，W/m2
        # Rso = np.zeros(LoopCount) #clear sky solar radiation，W/m2，#20211106
        # Rnl = np.zeros(LoopCount) #净长波辐射，W/m2，#20211106
        # d = np.zeros(LoopCount) #位移高度，m
        # z0= np.zeros(LoopCount) #地表粗糙度，m
        # pCp = np.zeros(LoopCount)  #空气密度*定压比热
        # ras = ras0*ones(LoopCount,1) #地表到冠层的空气动力学阻力，s/m
        # raa = np.zeros(LoopCount) #冠层到参考高度（2m的空气动力学阻力，s/m
        # rss = np.zeros(LoopCount) #土壤表面阻力，s/m
        # rac = np.zeros(LoopCount) #冠层边界阻力，s/m#rsc = np.zeros(LoopCount) #冠层气孔阻力，s/m
        #rsc = np.zeros(LoopCount) #
        # ETo = np.zeros(LoopCount) #SW模型计算蒸散发量，mm/h
        # E = np.zeros(LoopCount) #SW模型计算蒸发量，mm/h
        # T = np.zeros(LoopCount) #考虑水分胁迫系数的SW模型计算蒸腾量，mm/h
        Ks = np.zeros(self.LoopCount)  # 水分胁迫系数
        # SD = np.zeros(LoopCount)          #太阳倾斜角，°

        # for t == 1
        # ... status variables
        SurfaceVolume = self.d1_0 * self.phi1  # 表面积水量，mm
        SoilVolume = self.xita2_0 * self.D2  # 土壤层初始蓄水量，mm
        StorageVolume = self.d3_0 * self.phi3  # 淹没层初始蓄水量，mm

        # 计算胁迫因子
        # 水分胁迫系数赋值
        if self.xita2_0 >= self.xitacb:
            Ks[0] = 1
        else:
            Ks[0] = (self.xita2_0-self.xitaWP)/(self.xitacb-self.xitaWP)

        # 溢流层表面蒸发速率，mm/hr，PM模型
        es2[0] = 0.6108*np.exp(17.27*self.Tair[0] /
                               (self.Tair[0]+237.3))  # 饱和水汽压，kpa
        ea2[0] = self.RH[0]/100*es2[0]  # 实际水汽压，kpa
        # Slope of saturation vapour pressure curve，kPa/℃
        delta[0] = 4098*es2[0]/(self.Tair[0]+237.3)**2
        Rn[0] = (1-self.albedo)*self.Rsolar[0]  # 净太阳辐射，W/m2，不考虑长波辐射的损失
        if self.d1_0 == 0:
            e1[0] = 0
        else:
            e1[0] = (0.408*delta[0]*0.8*Rn[0]+self.y[0]*37.5/(self.Tair[0]+273) *
                     self.Uwind[0]*(es2[0]-ea2[0]))/(delta[0]+self.y[0]*(1+0.34*self.Uwind[0]))

        # 考虑水分胁迫的基质层蒸散，mm/h
        e2[0] = Ks[0]*(0.408*delta[0]*0.8*Rn[0]+self.y[0]*37.5/(self.Tair[0]+273)
                       * self.Uwind[0]*(es2[0]-ea2[0]))/(delta[0]+self.y[0]*(1+0.34*self.Uwind[0]))

        # 积水时砾石层水分蒸发速率，mm/hr
        if self.d3_0 > 0:
            e3[0] = self.C1*(1-self.xita2_0/self.phi2)*self.e0 * \
                np.exp(17.62*self.gravelT[0]/(24.3+self.gravelT[0]))
        else:
            e3[0] = 0

        # 溢流层水量，mm/hr
        ia[0] = self.i0[0] + self.d1_0*self.phi1/self.Tstep
        # 土壤表面入渗速率，mm/hr
        if ia[0] == 0:
            f1[0] = 0
        elif ia[0] <= self.Ksat:
            f1[0] = ia[0]
        else:
            f1[0] = self.Ksat*(1+(self.phi2-self.xita2_0) *
                               (self.d1_0+self.psi2)/self.F_0)

        if f1[0] > ia[0]:
            f1[0] = ia[0]

        # 溢流层溢流速率，mm/hr
        if self.d1_0 > self.D1:
            q1[0] = max((self.d1_0 - self.D1)/self.Tstep, 0)
        else:
            q1[0] = 0

        # 土壤层水分渗出速率，mm/hr
        if self.xita2_0 > self.xitaFC:
            f2[0] = self.Ksat * np.exp(-self.HCO*(self.phi2-self.xita2_0))
        else:
            f2[0] = 0

        # 砾石层穿孔管出流速率，mm/hr
        if self.d3_0 < self.D3D:
            h3[0] = 0
        elif self.d3_0 > self.D3D and self.d3_0 < self.D3:
            h3[0] = self.d3_0 - self.D3D
        elif self.xita2_0 > self.xitaFC and self.xita2_0 < self.phi2:
            h3[0] = (self.D3-self.D3D)+(self.xita2_0-self.xitaFC) / \
                (self.phi2-self.xitaFC)*self.D2
        else:
            h3[0] = (self.D3-self.D3D)+self.D2+self.d1_0

        q3[0] = self.C3D*(h3[0])**self.eta3D

        # ... flux limit and water balance
        # 新增：保证当溢流层水深低于最小可溢流深度时，溢流停止
        q1[0] = min(q1[0], (self.d1_0-self.D1)*self.phi1/self.Tstep+self.i0[0])
        q1[0] = max(q1[0], 0)
        # 保证砾石层出流不会出现在砾石层水位低于排水高度之后
        q3[0] = min(q3[0], (self.d3_0-self.D3D) *
                    self.phi3/self.Tstep+f2[0]-e3[0])
        q3[0] = max(q3[0], 0)
        # 保证土壤层出渗速率不会超过砾石层排水流量
        f2[0] = min(f2[0], (self.D3-self.d3_0) *
                    self.phi3/self.Tstep+q3[0]+e3[0])
        f2[0] = max(f2[0], 0)
        # 保证土壤层出渗不会导致土壤层含水量低于田间持水量
        f2[0] = min(f2[0], (self.xita2_0-self.xitaFC)
                    * self.D2/self.Tstep+f1[0]-e2[0])
        f2[0] = max(f2[0], 0)
        # 使得土壤层饱和时，土壤层入渗速率受到底部渗出流量的影响
        f1[0] = min(f1[0], (self.phi2-self.xita2_0)
                    * self.D2/self.Tstep+f2[0]+e2[0])
        f1[0] = max(f1[0], 0)
        f1[0] = min(f1[0], self.d1_0*self.phi1 /
                    self.Tstep+(self.i0[0]-e1[0]-q1[0]))
        f1[0] = max(f1[0], 0)

        if self.xita2_0 == self.phi2 and self.d3_0 == self.D3:
            if f2[0] > q3[0]:
                f2[0] = q3[0]
            else:
                q3[0] = max(f2[0], 0)

            f1[0] = min(f1[0], f2[0])

        # 土壤层累积入渗量，mm
        F1[0] = self.F_0 + f1[0]*self.Tstep
        if f1[0] == 0 and ia[0] == 0:
            F1[0] = 0

        # ... update water balance,按1分钟更新
        d3[0] = self.d3_0 + (f2[0]+q1[0]-e3[0]-q3[0]) / \
            self.phi3*self.Tstep  # 砾石层水深，mm
        xita2[0] = self.xita2_0 + \
            (f1[0]-e2[0]-f2[0]+e3[0])/self.D2*self.Tstep  # 土壤层含水量
        if xita2[0] > self.phi2:
            xita2[0] = self.phi2

        d1[0] = self.d1_0 + (self.i0[0]-e1[0]-f1[0]-q1[0]) / \
            self.phi1*self.Tstep  # 溢流层水深，mm
        # t == 1

        for t in range(1, self.LoopCount):
            # ... status variables
            SurfaceVolume = d1[t-1] * self.phi1
            SoilVolume = xita2[t-1] * self.D2
            StorageVolume = d3[t-1] * self.phi3

            # 设置胁迫因子
            # 水分胁迫系数赋值
            if xita2[t-1] >= self.xitacb:
                Ks[t] = 1
            elif xita2[t-1] < self.xitacb and xita2[t-1] >= self.xitaWP:
                Ks[t] = (xita2[t-1]-self.xitaWP)/(self.xitacb-self.xitaWP)
            else:
                xita2[t-1] = self.xitaWP
                Ks[t] = 0

            # 溢流层表面蒸发速率，mm/hr
            Rn[t] = (1-self.albedo)*self.Rsolar[t]  # 净太阳辐射，W/m2，不考虑长波辐射的损失
            es2[t] = 0.6108*np.exp(17.27*self.Tair[t] /
                                   (self.Tair[t]+237.3))  # 饱和水汽压，kPa
            ea2[t] = self.RH[t]/100*es2[t]  # 实际水汽压，kPa
            D[t] = es2[t]-ea2[t]  # 饱和水汽压差，kpa
            # Slope of saturation vapour pressure curve，kPa/℃
            delta[t] = 4098*es2[t]/(self.Tair[t]+237.3)**2

            if d1[t-1] > 0:
                e1[t] = (0.408*delta[t]*0.8*Rn[t]+self.y[t]*37.5/(self.Tair[t]+273) *
                         self.Uwind[t]*(es2[t]-ea2[t]))/(delta[t]+self.y[t]*(1+0.34*self.Uwind[t]))
            else:
                e1[t] = 0

            e2[t] = Ks[t]*(0.408*delta[t]*0.8*Rn[t]+self.y[t]*37.5/(self.Tair[t]+273)
                           * self.Uwind[t]*(es2[t]-ea2[t]))/(delta[t]+self.y[t]*(1+0.34*self.Uwind[t]))

            # 砾石层水分蒸发速率，mm/hr
            if d3[t-1] > 0:
                e3[t] = self.C1*(1-xita2[t-1]/self.phi2)*self.e0 * \
                    np.exp(17.62*self.gravelT[t]/(24.3+self.gravelT[t]))
            else:
                e3[t] = 0

            # 溢流层水量，mm/hr
            ia[t] = self.i0[t] + d1[t]*self.phi1/self.Tstep
            # 土壤表面入渗速率，mm/hr
            if ia[t] == 0:
                f1[t] = 0
            elif ia[t] <= self.Ksat:
                f1[t] = ia[t]
            else:
                f1[t] = self.Ksat*(1+(self.phi2-xita2[t-1])
                                   * (d1[t-1]+self.psi2)/F1[t-1])

            if f1[t] > ia[t]:
                f1[t] = ia[t]

            # 溢流层溢流速率，mm/hr
            q1[t] = max((d1[t-1] - self.D1)/self.Tstep, 0)

            # 土壤层水分渗出速率，mm/hr
            if xita2[t-1] > self.xitaFC:
                f2[t] = self.Ksat * np.exp(-self.HCO*(self.phi2-xita2[t-1]))
            else:
                f2[t] = 0

           # 砾石层穿孔管出流速率，mm/hr
            if d3[t-1] < self.D3D:
                h3[t] = 0
            elif d3[t-1] > self.D3D and d3[t-1] < self.D3:
                h3[t] = d3[t-1] - self.D3D
            else:
                if xita2[t-1] > self.xitaFC:
                    if xita2[t-1] < self.phi2:
                        h3[t] = (self.D3-self.D3D)+(xita2[t-1] -
                                                    self.xitaFC)/(self.phi2-self.xitaFC)*self.D2
                    else:  # if soilTheta[t-1] == soilVoidFrace
                        h3[t] = (self.D3-self.D3D)+self.D2+d1[t-1]

            q3[t] = self.C3D*(h3[t])**self.eta3D

            # ... flux limit and water balance
            # 新增：保证当溢流层水深低于最小可溢流深度时，溢流停止
            q1[t] = min(q1[t], (d1[t-1]-self.D1) *
                        self.phi1/self.Tstep+self.i0[t])
            q1[t] = max(q1[t], 0)
            # 保证砾石层出流不会出现在砾石层水位低于排水高度之后
            q3[t] = min(q3[t], (d3[t-1]-self.D3D) *
                        self.phi3/self.Tstep+f2[t]-e3[t])
            q3[t] = max(q3[t], 0)
            # 保证土壤层出渗速率不会超过砾石层排水流量
            f2[t] = min(f2[t], (self.D3-d3[t-1]) *
                        self.phi3/self.Tstep+q3[t]+e3[t])
            f2[t] = max(f2[t], 0)
            # 保证土壤层出渗不会导致土壤层含水量低于田间持水量
            f2[t] = min(f2[t], (xita2[t-1]-self.xitaFC)
                        * self.D2/self.Tstep+f1[t]-e2[t])
            f2[t] = max(f2[t], 0)
            # 使得土壤层饱和时，土壤层入渗速率受到底部渗出流量的影响
            f1[t] = min(f1[t], (self.phi2-xita2[t-1]) *
                        self.D2/self.Tstep+f2[t]+e2[t])
            f1[t] = max(f1[t], 0)
            f1[t] = min(f1[t], self.d1_0*self.phi1 /
                        self.Tstep+(self.i0[t]-e1[t]-q1[t]))
            f1[t] = max(f1[t], 0)

            if xita2[t-1] == self.phi2 and d3[t-1] == self.D3:
                if f2[t] > q3[t]:
                    f2[t] = q3[t]
                else:
                    q3[t] = max(f2[t], 0)

                f1[t] = min(f1[t], f2[t])

            # 土壤层累积入渗量，mm
            F1[t] = F1[t-1] + f1[t]*self.Tstep
            if f1[t] == 0 and ia[t] == 0:
                F1[t] = 0

            # ... update water balance
            d3[t] = d3[t-1] + (f2[t]+q1[t]-e3[t]-q3[t]) / \
                self.phi3*self.Tstep  # 砾石层水深，mm
            if d3[t] < 0:
                d3[t] = 0

            xita2[t] = xita2[t-1] + \
                (f1[t]-e2[t]-f2[t]+e3[t])/self.D2*self.Tstep  # 土壤层含水量
            if xita2[t] > self.phi2:
                xita2[t] = self.phi2

            d1[t] = d1[t-1] + (self.i0[t]-e1[t]-f1[t]-q1[t]) / \
                self.phi1*self.Tstep  # 溢流层水深，mm
            if d1[t] < 0:
                d1[t] = 0

        return q3

    def outflow_NSE(self, q3):
        # 获取实测数据
        self.get_observed_data
        # 计算实测出流的NSE
        self.q3sim = np.zeros(len(self.q3obs))
        Aq3 = np.zeros(len(self.q3obs))
        Bq3 = np.zeros(len(self.q3obs))
        for t in range(len(self.q3obs)):
            self.q3sim[t] = q3[int(self.Qnumberobs[t])-1]
            Aq3[t] = (self.q3obs[t]-self.q3sim[t])**2
            Bq3[t] = (self.q3obs[t]-np.mean(self.q3obs))**2

        NSE_q3 = 1-np.sum(Aq3)/np.sum(Bq3)

        return NSE_q3

    def green_roof_sim(self, main):
        # 设置仿真时间
        self.start_dt_str = main.start_dt_str
        self.end_dt_str = main.end_dt_str
        self.Tstep = main.time_step
        # 检查相关设置是否正确
        if not check_weather_file(main):
            return
        # 天气文件赋值
        # TODO：是否需要支持雨型生成
        self.weather_file_path = main.weather_file_path
        self.get_weather_data
        if not check_datetime_setting(main, self.LoopCount, self.start_dt_str, self.end_dt_str, self.Tstep):
            return
        # 仿真，并返回结果
        q3 = self.sim
        # 结果可视化
        self.show_single_sponge_sim_curve(
            q3, obs=None, NSE=None, main=main)

        self.result = {"降雨强度(mm/min)": self.i0, "出流量(mm/min)": q3}

        QMessageBox.information(main, '运行完毕', '仿真已完成！')
        main.green_roof_single_sim_flag = True

    def green_roof_sim_and_val(self, main):
        # TODO：仿真结果很离谱，需要调试
        # 设置仿真时间
        self.start_dt_str = main.start_dt_str
        self.end_dt_str = main.end_dt_str
        self.Tstep = main.time_step
        # 检查相关设置是否正确
        if (not check_weather_file(main)) or \
                (not check_observed_file(main)):
            return
        # 天气文件赋值
        # TODO：是否需要支持雨型生成
        self.observed_file_path = main.observed_file_path
        self.weather_file_path = main.weather_file_path
        if not check_datetime_setting(main, self.LoopCount, self.start_dt_str, self.end_dt_str, self.Tstep):
            return
        # 仿真，并返回结果
        q3 = self.sim
        NSE = self.outflow_NSE(q3)
        q3obs = self.q3obs
        q3sim = self.q3sim
        # 结果可视化
        self.show_single_sponge_sim_curve(q3sim, q3obs, NSE, main)

        QMessageBox.information(main, '运行完毕', '仿真已完成！')

    def show_single_sponge_sim_curve(self, q3, obs, NSE, main):
        width, height = main.green_roof_sim_curve.width(), main.green_roof_sim_curve.height()
        F = fig_single_sponge_sim_curve(
            q3, obs, "绿色屋顶", self.start_dt_str, self.end_dt_str, width, height)  # 结果可视化

        main.scene = QGraphicsScene()  # 创建一个场景
        main.scene.addWidget(F)  # 将图形元素添加到场景中
        main.green_roof_sim_curve.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.green_roof_sim_curve.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.green_roof_sim_curve.setScene(main.scene)  # 将创建添加到图形视图显示窗口
