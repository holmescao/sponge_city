from utils.algo.general_functions import (save_dict_to_yaml, check_datetime,
                                          save_sim_results,
                                          save_sim_params,
                                          check_datetime_setting,
                                          check_observed_file,
                                          check_weather_file)
from utils.algo.figure_function import fig_single_sponge_sim_curve
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene
from PyQt5.QtCore import Qt
import numpy as np
import math


class SinglePermeablePavement:
    def __init__(self,
                 observed_file_path="",
                 weather_file_path="") -> None:
        """参数初始化"""
        # 一些初始参数（四场雨的率定结果
        # 表面层参数
        # 用于Green-Ampt公式的参数（表面层）
        self.Ks1 = 0.42712880401611325  # 表面层饱和导水率(mm/min)淘宝说可达2mm/s
        self.phi1 = 0.16501304931640626  # 表面层孔隙率（淘宝说0.15-0.30）
        self.theta_1 = 0.029326210403442382  # 表面层初始含水量
        self.S1 = 53.03145765228272  # 表面层湿润锋吸力
        self.Res1 = 17.45003372192383  # 恢复系数
        # 表面层底部渗出参数
        self.theta_FC1 = 0.0301
        self.HCO1 = 0.016635312271118165

        # 找平层参数
        # 用于Green-Ampt公式的参数（找平层，透水混凝土是5-10mm的瓜米石,属于细砾）
        self.Ks2 = 0.4001  # 找平层饱和导水率（参考取值6-60?)
        self.phi2 = 0.19784970951080325  # 找平层孔隙率（参考取值：0.25-0.38）
        self.theta_2 = 0.02593806667327881  # 找平层初始含水量
        self.S2 = 262.8870211469651         # 找平层湿润锋吸力
        self.Res2 = 0.0001  # 恢复系数
        # 找平层底部渗出参数
        self.theta_FC2 = 0.03150794734954834
        self.HCO2 = 0.00010095348358154297

        # 砾石层参数
        # （砾石层，<3cm砾石）
        self.phi3 = 0.3336394226074219  # 砾石层孔隙率（参考取值：0.24-0.36）
        # 孔口出流公式的参数
        self.C = 0.05047444458007813  # 孔流系数
        self.eta = 1.1155852115631104  # 孔流指数

        # 三场0.1年降雨率定的最好结果
        # #用于Green-Ampt公式的参数（表面层）
        # self.Ks1 = 0.3462890625	## 表面层饱和导水率(mm/min)淘宝说可达2mm/s
        # self.phi1 = 0.15555419921875# 表面层孔隙率（淘宝说0.15-0.30）
        # theta_1 = 	0.02259368896484375# 表面层初始含水量
        # self.S1 = 	96.502685546875# 表面层湿润锋吸力
        # self.Res1 = 	7.7388763427734375#恢复系数
        # #表面层底部渗出参数
        # self.theta_FC1 = 	0.023220825195312503
        # self.HCO1 = 	0.555694580078125
        #
        # #找平层参数
        # #用于Green-Ampt公式的参数（找平层，透水混凝土是5-10mm的瓜米石,属于细砾）
        # self.Ks2 = 	0.650543212890625      ## 找平层饱和导水率（参考取值6-60?)
        # self.phi2 = 	0.333404541015625        ## 找平层孔隙率（参考取值：0.25-0.38）
        # self.theta_2 = 	0.08013000488281251   # 找平层初始含水量
        # self.S2 = 	91.998291015625                 # 找平层湿润锋吸力
        # self.Res2 = 	32.489013671875     #恢复系数
        # #找平层底部渗出参数
        # self.theta_FC2 = 	0.048382568359375
        # self.HCO2 = 	0.5552663803100586
        #
        # #砾石层参数
        # #（砾石层，<3cm砾石）
        # self.phi3 = 	0.3656007766723633        ## 砾石层孔隙率（参考取值：0.24-0.36）
        # #孔口出流公式的参数
        # self.C = 	0.02142333984375            ## 孔流系数
        # self.eta = 	1.599365234375	          ## 孔流指数

        # 高度参数,单位为mm
        # TODO：这些需要做为用户输入参数吗
        self.L1 = 100            # 表面层高度                 目前是渗透混凝土
        self.L2 = 20             # 找平层高度                 对应的是瓜米石（5-10 mm）
        self.L3 = 200            # 砾石层高度
        self.L4 = 20            # 蓄水层高度

        # #蒸散发参数(“暂时删除，之后再添加用公式计算”）
        # e1 = 0          # 表面层蒸散发
        # e2 = 0          # 找平层蒸散发
        # e3 = 0          # 去掉蓄水层的砾石层蒸散发
        # e4 = 0          # 蓄水层的蒸散发

        # 均匀降雨
        q_in = 0.332        # 降雨速率，目前是0.1年一遇（0.332 mm/min)，历时60min
        # self.Tstep = 1          # 时间步长为 1 min

        # #计算 t = 1 时各参数
        # x= symbols('x')
        # tp1 = solve(((self.phi1 - q_in * x / self.L1) * self.S1)/(q_in * (q_in / self.Ks1-1))- x,x)
        # print(tp1)

        # t = [0, self.Tstep]  # 时间序列

        # TODO：这些需要做为用户输入参数吗
        # 表面层的渗入和渗出
        # 设置的初始参数都默认为第0分钟，降雨为1-60共60min
        self.theta1 = [self.theta_1]          # 表面层含水量变化
        self.F1 = [0]                    # 表面层累积下渗量
        self.f1 = [0]                    # 表面层下渗速率
        self.f2 = [0]                    # 表面层渗出速率
        self.ia = [0]                    # 实际入流速率
        self.d1 = [0]                    # 表面层蓄水深度

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
        # 一些初始参数（四场雨的率定结果
        # 表面层参数
        # 用于Green-Ampt公式的参数（表面层）
        self.Ks1 = params.Ks1.value()  # 表面层饱和导水率(mm/min)淘宝说可达2mm/s
        self.phi1 = params.phi1.value()  # 表面层孔隙率（淘宝说0.15-0.30）
        self.theta_1 = params.theta_1.value()  # 表面层初始含水量
        self.S1 = params.S1.value()  # 表面层湿润锋吸力
        self.Res1 = params.Res1.value()  # 恢复系数
        # 表面层底部渗出参数
        self.theta_FC1 = params.theta_FC1.value()
        self.HCO1 = params.HCO1.value()

        # 找平层参数
        # 用于Green-Ampt公式的参数（找平层，透水混凝土是5-10mm的瓜米石,属于细砾）
        self.Ks2 = params.Ks2.value()  # 找平层饱和导水率（参考取值6-60?)
        self.phi2 = params.phi2.value()  # 找平层孔隙率（参考取值：0.25-0.38）
        self.theta_2 = params.theta_2.value()  # 找平层初始含水量
        self.S2 = params.S2.value()         # 找平层湿润锋吸力
        self.Res2 = params.Res2.value()  # 恢复系数
        # 找平层底部渗出参数
        self.theta_FC2 = params.theta_FC2.value()
        self.HCO2 = params.HCO2.value()

        # 砾石层参数
        # （砾石层，<3cm砾石）
        self.phi3 = params.phi3.value()  # 砾石层孔隙率（参考取值：0.24-0.36）
        # 孔口出流公式的参数
        self.C = params.C.value()  # 孔流系数
        self.eta = params.eta.value()  # 孔流指数

    @property
    def pack_params(self):
        permeable_pavement_params_dict = {
            "砾石层": {
                "砾石层孔隙率": self.phi3,
                "孔流系数": self.C,
                "孔流指数": self.eta,
            },
            "找平层": {
                "饱和导水率": self.Ks2,
                "孔隙率": self.phi2,
                "初始含水量": self.theta_2,
                "湿润锋吸力": self.S2,
                "恢复系数": self.Res2,
                "底部渗出参数FC2": self.theta_FC2,
                "底部渗出参数HCO2": self.HCO2,
            },
            "表层": {
                "饱和导水率": self.Ks1,
                "孔隙率": self.phi1,
                "初始含水量": self.theta_1,
                "湿润锋吸力": self.S1,
                "恢复系数": self.Res1,
                "底部渗出参数FC2": self.theta_FC1,
                "底部渗出参数HCO2": self.HCO1,
            }
        }

        return permeable_pavement_params_dict

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
        self.i0 = data[:]  # 降雨量，mm/min
        # self.Rsolar = data[:, 1]/3600*10**6  # 太阳辐射，MJ/(m2 h)转换成W/m2
        # self.Tair = data[:, 2]  # 气温，℃
        # self.gravelT = data[:, 2]  # 蓄水层水文，假定与气温相同，℃
        # self.RH = data[:, 3]  # 空气湿度，#
        # self.Uwind = data[:, 4]  # 风速，m/s
        # P = InputData8(:,6)  #大气压，kPa
        # 将大气压kpa转换为Psychrometric constant，kPa/℃
        # self.y = 0.665*(10 ** (-3))*data[:, 5]
        # Ra_solar = data(:,8) #地外太阳辐射，W/m2 # 20211106

        # 设置循环长度
        self.LoopCount = len(data)

    @property
    def sim(self):
        self.get_weather_data

        self.ia = [0]
        rain = list(self.i0)  # 降雨量，mm/min
        self.ia += rain
        self.LoopCount = len(self.ia)

        """参数赋值"""
        ia = self.ia
        Ks1 = self.Ks1
        phi1 = self.phi1
        theta_1 = self.theta_1
        S1 = self.S1
        Res1 = self.Res1
        theta_FC1 = self.theta_FC1
        HCO1 = self.HCO1

        # 用于Green-Ampt公式的参数（找平层，透水混凝土是5-10mm的瓜米石,属于细砾）
        Ks2 = self.Ks2
        phi2 = self.phi2
        theta_2 = self.theta_2
        S2 = self.S2
        Res2 = self.Res2
        # 找平层底部渗出参数
        theta_FC2 = self.theta_FC2
        HCO2 = self.HCO2

        # 砾石层参数
        # （砾石层，<3cm砾石）
        phi3 = self.phi3
        # 孔口出流公式的参数
        C = self.C
        eta = self.eta

        # 高度参数,单位为mm
        L1 = self.L1
        L2 = self.L2
        L3 = self.L3
        L4 = self.L4

        theta1 = self.theta1
        F1 = self.F1
        f1 = self.f1
        f2 = self.f2
        ia = self.ia
        d1 = self.d1
        Tstep = self.Tstep * 60
        # 表面层下渗速率
        if ia[1] == 0:
            f1.append(0)
        elif ia[1] <= Ks1 or F1[0] == 0:
            f1.append(ia[1])
        else:
            Fs1 = Ks1 * S1 * (phi1-theta1[0])/(ia[1] - Ks1)
            if F1[0] + ia[1] * Tstep < Fs1:
                f1.append(ia[1])
            else:
                f1.append(
                    Ks1 * (1 + ((phi1 - theta1[0]) * (d1[0] + S1) / F1[0])))
        # 表面层入渗速率受到表面现有水量的影响
        if f1[1] > ia[1]:
            f1[1] = ia[1]
        # 表面层渗出速率
        if theta1[0] > theta_FC1:
            f2.append(Ks1 * np.e ** (-HCO1 * (phi1 - theta1[0])))
            if f1[1] == 0:
                delta_theta1 = math.sqrt(Ks1)/Res1 * (phi1 - theta1[0]) * Tstep
                if theta1[0] - delta_theta1 >= theta_FC1:
                    f2[1] = L1 * delta_theta1 / Tstep
                else:
                    f2[1] = L1 * (theta1[0] - theta_FC1)/Tstep
        else:
            f2.append(0)
        if f2[1] > f1[1] and f1[1] != 0:
            f2[1] = f1[1]
        # 表面层饱和时，入渗速率受到底部渗出流量的限制
        f1[1] = min(f1[1], (phi1-theta1[0]) * L1 / Tstep + f2[1])
        f1[1] = max(f1[1], 0)
        # 保证表面层出渗后不会导致表面层含水量低于田间持水量
        f2[1] = min(f2[1], (theta1[0] - theta_FC1) * L1 / Tstep + f1[1])
        f2[1] = max(f2[1], 0)

        # 找平层的渗入和渗出
        theta2 = [theta_2]    # 找平层含水量变化
        F2 = [0]            # 找平层累积下渗量
        infil2 = [0]        # 找平层下渗速率
        f3 = [0]            # 找平层渗出速率
        # 找平层下渗速率
        if f2[1] == 0:
            infil2.append(0)
        elif f2[1] <= Ks2 or F2[0] == 0:
            infil2.append(f2[1])
        else:
            Fs2 = Ks2 * S2 * (phi2 - theta2[0]) / (f2[1] - Ks2)
            if F2[0] + f2[1] * Tstep < Fs2:
                infil2.append(f2[1])
            else:
                infil2.append(Ks2 * (1 + ((phi2 - theta2[0]) * S2) / F2[0]))
        if infil2[1] > f2[1]:
            infil2[1] = f2[1]
        f2[1] = infil2[1]
        # 找平层渗出速率
        if theta2[0] > theta_FC2:
            f3.append(Ks2 * np.e ** (-HCO2 * (phi2 - theta2[0])))
            if f2[1] == 0:
                delta_theta2 = math.sqrt(Ks2)/Res2 * (phi2 - theta2[0]) * Tstep
                if theta2[0] - delta_theta2 >= theta_FC2:
                    f3[1] = L2 * delta_theta2 / Tstep
                else:
                    f3[1] = L2 * (theta2[0] - theta_FC2) / Tstep
        else:
            f3.append(0)

        # 保证找平层饱和时，找平层入渗速率受到底部渗出流量的影响
        f2[1] = min(f2[1], (phi2 - theta2[0]) * L2 / Tstep + f3[1])
        f2[1] = max(f2[1], 0)
        # 保证找平层出渗后不会导致找平层含水量低于田间持水量
        f3[1] = min(f3[1], (theta2[0] - theta_FC2) * L2 / Tstep + f2[1])
        f3[1] = max(f3[1], 0)

        # 砾石层的渗入和渗出
        q_out = [0]             # 出水管速率
        d3 = [19.5]               # 蓄水总深度
        theta3 = [d3[0]/L3*phi3]    # 砾石层含水量
        h = [0]                 # 溢出高度
        Q_out = [0]             # 流出流量 mL/min

        if d3[0] <= L4:
            h.append(0)
        elif d3[0] > L4 and d3[0] < L3:
            h.append(d3[0] - L4)
        else:
            if theta2[0] < phi2 and theta2[0] >= theta_FC2:
                h.append(L3-L4 + (theta2[0]-theta_FC2)/(phi2-theta_FC2)*L2)
            else:
                if theta1[0] < phi1 and theta1[0] >= theta_FC1:
                    h.append(L3 - L4 + L2 +
                             (theta1[0] - theta_FC1) / (phi1 - theta_FC1) * L1)
                else:
                    h.append(L3 - L4 + L2 + L1 + d1[0])

        q_out.append(C * h[0] ** eta)
        # 保证砾石层出流不会出现在砾石层水位低于排水高度后
        q_out[1] = min(q_out[1], (d3[0] - L4) * phi3/Tstep + f3[1])
        q_out[1] = max(q_out[1], 0)
        # 砾石层饱和时，砾石层入渗速率收到底部渗出流量的影响
        f3[1] = min(f3[1], (phi3 - theta3[0]) * L3 / Tstep + q_out[1])
        f3[1] = max(f3[1], 0)
        # 保证找平层出身不会超过砾石层排水水量
        f3[1] = min(f3[1], (L3-d3[0])*phi3/Tstep + q_out[1])
        f3[1] = max(f3[1], 0)
        if theta2[0] == phi2 and d3[0] == L3:
            if f3[1] > q_out[1]:
                f3[1] = q_out[1]
            else:
                q_out[1] = max(f3[1], 0)
            f2[1] = min(f3[1], f2[1])
            if theta1[0] == phi1:
                f1[1] = min(f1[1], f2[1])

        Q_out.append(q_out[1] * 360)

        # 参数计算
        d1.append((ia[1] - f1[1])*Tstep)
        d3.append(d3[0] + (f3[1]-q_out[1])/phi3 * Tstep)
        theta3.append(min(phi3, theta3[0] + (f3[1]-q_out[1])/L3 * Tstep))
        if f1[1] == 0 and f2[1] != 0:
            delta_theta1 = math.sqrt(Ks1) / Res1 * (phi1 - theta1[0]) * Tstep
            if theta1[0] - delta_theta1 >= theta_FC1:
                theta1.append(theta1[0] - delta_theta1)
                F1.append(max(0, F1[0] - L1*delta_theta1))
            else:
                theta1.append(theta_FC1)
                F1.append(max(0, F1[0] - L1 * (theta1[0]-theta_FC1)))
        else:
            F1.append(F1[0] + f1[1] * Tstep)
            theta1.append(min(phi1, theta1[0] + (f1[1] - f2[1]) / L1 * Tstep))

        if f2[1] == 0 and f3[1] != 0:
            delta_theta2 = math.sqrt(Ks2)/Res2 * (phi2 - theta2[0]) * Tstep
            if theta2[0] - delta_theta2 >= theta_FC2:
                theta2.append(theta2[0] - delta_theta2)
                F2.append(max(0, F2[0] - L2*delta_theta2))
            else:
                theta2.append(theta_FC2)
                F2.append(max(0, F2[0] - L2 * (theta2[0] - theta_FC2)))
        else:
            F2.append(F2[0] + f2[1] * Tstep)
            theta2.append(min(phi2, theta2[0] + (f2[1] - f3[1]) / L2 * Tstep))

        # #######
        a = Q_out[1]
        # #######
        Qy = [0, 0]
        for i in range(2, self.LoopCount):
            # 表面层的渗入和渗出
            # 表面层下渗速率
            if ia[i] == 0:
                f1.append(0)
            elif ia[i] <= Ks1 or F1[i-1] == 0:
                f1.append(ia[i])
            else:
                Fs1 = Ks1 * S1 * (phi1 - theta1[0]) / (ia[1] - Ks1)
                if F1[i-1] + ia[i] * Tstep < Fs1:
                    f1.append(ia[i])
                else:
                    f1.append(
                        Ks1 * (1 + ((phi1 - theta1[i-1]) * (d1[i-1]+S1)) / F1[i-1]))
            # 表面层入渗速率受到表面现有水量的影响
            if f1[i] > ia[i]:
                f1[i] = ia[i]
            # 表面层渗出速率
            if theta1[i-1] > theta_FC1:
                f2.append(Ks1 * np.e ** (-HCO1 * (phi1 - theta1[i - 1])))
                if f1[i] == 0:
                    delta_theta1 = math.sqrt(Ks1) / Res1 * \
                        (theta1[i-1] - theta1[0]) * Tstep
                    #delta_theta1 = math.sqrt(Ks1) / Res1 * (phi1 - theta1[0]) * Tstep
                    if theta1[i-1] - delta_theta1 >= theta_FC1:
                        f2[i] = L1 * delta_theta1 / Tstep
                    else:
                        f2[i] = L1 * (theta1[i-1] - theta_FC1) / Tstep
            else:
                f2.append(0)
            if f2[i] > f1[i] and f1[i] != 0:
                f2[i] = f1[i]
            # 表面层饱和时，入渗速率受到底部渗出流量的限制
            f1[i] = min(f1[i], (phi1 - theta1[i - 1]) * L1 / Tstep + f2[i])
            f1[i] = max(f1[i], 0)
            # 保证表面层出渗后不会导致表面层含水量低于田间持水量
            f2[i] = min(f2[i], (theta1[i-1] - theta_FC1) * L1 / Tstep + f1[i])
            f2[i] = max(f2[i], 0)

            # 找平层的渗入和渗出
            # 找平层下渗速率
            if f2[i] == 0:
                infil2.append(0)
            elif f2[i] <= Ks2 or F2[i-1] == 0:
                infil2.append(f2[i])
            else:
                Fs2 = Ks2 * S2 * (phi2 - theta2[0]) / (f2[1] - Ks2)
                if F2[i-1] + f2[i] * Tstep < Fs2:
                    infil2.append(f2[i])
                else:
                    infil2.append(
                        Ks2 * (1 + ((phi2 - theta2[i - 1]) * S2) / F2[i-1]))
            if infil2[i] > f2[i]:
                infil2[i] = f2[i]
            f2[i] = infil2[i]
            # 找平层渗出速率
            if theta2[i-1] > theta_FC2:
                f3.append(Ks2 * np.e ** (-HCO2 * (phi2 - theta2[i - 1])))
                if f2[i] == L1 * (theta1[i - 1] - theta_FC1) / Tstep and f2[i] < f3[i-1]:
                    delta_theta2 = math.sqrt(Ks2) / Res2 * \
                        (theta2[i - 1] - theta2[0]) * Tstep
                    if theta2[i-1] - delta_theta2 >= theta_FC2:
                        f3[i] = f2[i] + L2 * delta_theta2 / Tstep
                    else:
                        f3[i] = f2[i] + L2 * \
                            (theta2[i - 1] - theta_FC2) / Tstep
                elif f2[i] == 0:
                    delta_theta2 = math.sqrt(Ks2) / Res2 * \
                        (theta2[i-1] - theta2[0]) * Tstep
                    #delta_theta2 = math.sqrt(Ks2) / Res2 * (phi2 - theta2[0]) * Tstep
                    if theta2[i-1] - delta_theta2 >= theta_FC2:
                        f3[i] = L2 * delta_theta2 / Tstep
                    else:
                        f3[i] = L2 * (theta2[i - 1] - theta_FC2) / Tstep

            else:
                f3.append(0)
            # if t[i] == 94:
            #     print(f3[i])
            if f3[i] > f2[i] and f2[i] != 0:
                if f2[i] == L1 * (theta1[i - 1] - theta_FC1) / Tstep and f2[i] < f3[i-1]:
                    f3[i] = max(0, f3[i])
                else:
                    f3[i] = f2[i]

            # 保证找平层饱和时，找平层入渗速率受到底部渗出流量的影响
            f2[i] = min(f2[i], (phi2 - theta2[i - 1]) * L2 / Tstep + f3[i])
            f2[i] = max(f2[i], 0)
            # 保证找平层出渗后不会导致找平层含水量低于田间持水量
            f3[i] = min(f3[i], (theta2[i-1] - theta_FC2) * L2 / Tstep + f2[i])
            f3[i] = max(f3[i], 0)

            # 砾石层的渗入和渗出
            if d3[i-1] <= L4:
                h.append(0)
            elif d3[i-1] > L4 and d3[i-1] < L3:
                h.append(d3[i-1] - L4)
            else:
                if theta2[i-1] < phi2 and theta2[i-1] >= theta_FC2:
                    h.append(L3 - L4 + (theta2[i-1] -
                                        theta_FC2) / (phi2 - theta_FC2) * L2)
                else:
                    if theta1[i-1] < phi1 and theta1[i-1] >= theta_FC1:
                        h.append(L3 - L4 + L2 +
                                 (theta1[i-1] - theta_FC1) / (phi1 - theta_FC1) * L1)
                    else:
                        h.append(L3 - L4 + L2 + L1 + d1[i-1])
            q_out.append(C * h[i-1] ** eta)
            if f2[i] == 0:
                if q_out[i] < f3[i]:
                    q_out[i] = f3[i]
                elif q_out[i] > q_out[i-1]:
                    q_out[i] = q_out[i-1]

            # 保证砾石层出流不会出现在砾石层水位低于排水高度后
            q_out[i] = min(q_out[i], (d3[i-1]-L4) * phi3 / Tstep + f3[i])
            q_out[i] = max(q_out[i], 0)
            # 砾石层饱和时，砾石层入渗速率受到底部渗出流量的影响
            f3[i] = min(f3[i], (phi3 - theta3[i - 1]) * L3 / Tstep + q_out[i])
            f3[i] = max(f3[i], 0)
            # 保证找平层出身不会超过砾石层排水水量
            f3[i] = min(f3[i], (L3 - d3[i-1]) * phi3 / Tstep + q_out[i])
            f3[i] = max(f3[i], 0)

            if theta2[i - 1] == phi2 and d3[i-1] == L3:
                if f3[i] > q_out[i]:
                    f3[i] = q_out[i]
                else:
                    q_out[i] = max(f3[i], 0)
                f2[i] = min(f3[i], f2[i])
                if theta1[i - 1] == phi1:
                    f1[i] = min(f2[i], f1[i])
            Q_out.append(q_out[i] * 360)
            a = max(a, Q_out[i])

            # 其他参数随时间的变化
            # 参数计算
            d1.append((ia[i] - f1[i]) * Tstep)
            d3.append(d3[i - 1] + (f3[i] - q_out[i])/phi3 * Tstep)
            theta3.append(
                min(phi3, theta3[i - 1] + (f3[i] - q_out[i]) / L3 * Tstep))
            if f1[i] == 0 and f2[i] != 0:
                delta_theta1 = math.sqrt(Ks1) / Res1 * \
                    (theta1[i-1] - theta1[0]) * Tstep
                #delta_theta1 = math.sqrt(Ks1) / Res1 * (phi1 - theta1[0]) * Tstep
                if theta1[i-1] - delta_theta1 >= theta_FC1:
                    theta1.append(theta1[i-1] - delta_theta1)
                    F1.append(max(0, F1[i-1] - L1 * delta_theta1))
                else:
                    theta1.append(theta_FC1)
                    F1.append(max(0, F1[i-1] - L1 * (theta1[i-1] - theta_FC1)))
            else:
                F1.append(F1[i - 1] + f1[i] * Tstep)
                theta1.append(
                    min(phi1, theta1[i - 1] + (f1[i] - f2[i]) / L1 * Tstep))

            if f2[i] == 0 and f3[i] != 0:
                delta_theta2 = math.sqrt(Ks2) / Res2 * \
                    (theta2[i - 1] - theta2[0]) * Tstep
                # delta_theta2 = math.sqrt(Ks2) / Res2 * (phi2 - theta2[0]) * Tstep
                if theta2[i-1] - delta_theta2 >= theta_FC2:
                    theta2.append(theta2[i-1] - delta_theta2)
                    F2.append(max(0, F2[i-1] - L2 * delta_theta2))
                else:
                    theta2.append(theta_FC2)
                    F2.append(max(0, F2[i-1] - L2 * (theta2[i-1]-theta_FC2)))
            else:
                F2.append(F2[i - 1] + f2[i] * Tstep)
                theta2.append(
                    min(phi2, theta2[i - 1] + (f2[i] - f3[i]) / L2 * Tstep))

        return Q_out[1:]

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

    def permeable_pavement_sim(self, main):
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
        self.show_single_sponge_sim_curve(q3, obs=None, NSE=None, main=main)

        self.result = {"降雨强度(mm/min)": self.ia, "出流量(mm/min)": q3}

        QMessageBox.information(main, '运行完毕', '仿真已完成！')
        main.permeable_pavement_single_sim_flag = True

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
            q3, obs, "渗透铺装", self.start_dt_str, self.end_dt_str, width, height)  # 结果可视化

        main.scene = QGraphicsScene()  # 创建一个场景
        main.scene.addWidget(F)  # 将图形元素添加到场景中
        main.green_roof_sim_curve.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.green_roof_sim_curve.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        main.green_roof_sim_curve.setScene(main.scene)  # 将创建添加到图形视图显示窗口
