#####透水混凝土
#=
import math
import xlrd
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

#一些初始参数（四场雨的率定结果
#表面层参数
#用于Green-Ampt公式的参数（表面层）
Ks1 =       0.42712880401611325	## 表面层饱和导水率(mm/min)淘宝说可达2mm/s
phi1 = 		0.16501304931640626	# 表面层孔隙率（淘宝说0.15-0.30）
theta_1 =	0.029326210403442382	# 表面层初始含水量
S1 = 	    53.03145765228272	# 表面层湿润锋吸力
Res1 = 	    17.45003372192383	#恢复系数
#表面层底部渗出参数
theta_FC1 = 0.0301
HCO1 = 		0.016635312271118165

#找平层参数
#用于Green-Ampt公式的参数（找平层，透水混凝土是5-10mm的瓜米石,属于细砾）
Ks2 = 		0.4001		## 找平层饱和导水率（参考取值6-60?)
phi2 = 		0.19784970951080325	## 找平层孔隙率（参考取值：0.25-0.38）
theta_2 = 	0.02593806667327881	# 找平层初始含水量
S2 = 		262.8870211469651									# 找平层湿润锋吸力
Res2 = 		0.0001							#恢复系数
#找平层底部渗出参数
theta_FC2 = 0.03150794734954834
HCO2 = 		0.00010095348358154297

#砾石层参数
#（砾石层，<3cm砾石）
phi3 = 		0.3336394226074219	## 砾石层孔隙率（参考取值：0.24-0.36）
#孔口出流公式的参数
C = 		0.05047444458007813			## 孔流系数
eta = 		1.1155852115631104			  ## 孔流指数

#三场0.1年降雨率定的最好结果
# #用于Green-Ampt公式的参数（表面层）
# Ks1 = 0.3462890625	## 表面层饱和导水率(mm/min)淘宝说可达2mm/s
# phi1 = 0.15555419921875# 表面层孔隙率（淘宝说0.15-0.30）
# theta_1 = 	0.02259368896484375# 表面层初始含水量
# S1 = 	96.502685546875# 表面层湿润锋吸力
# Res1 = 	7.7388763427734375#恢复系数
# #表面层底部渗出参数
# theta_FC1 = 	0.023220825195312503
# HCO1 = 	0.555694580078125
#
# #找平层参数
# #用于Green-Ampt公式的参数（找平层，透水混凝土是5-10mm的瓜米石,属于细砾）
# Ks2 = 	0.650543212890625      ## 找平层饱和导水率（参考取值6-60?)
# phi2 = 	0.333404541015625        ## 找平层孔隙率（参考取值：0.25-0.38）
# theta_2 = 	0.08013000488281251   # 找平层初始含水量
# S2 = 	91.998291015625                 # 找平层湿润锋吸力
# Res2 = 	32.489013671875     #恢复系数
# #找平层底部渗出参数
# theta_FC2 = 	0.048382568359375
# HCO2 = 	0.5552663803100586
#
# #砾石层参数
# #（砾石层，<3cm砾石）
# phi3 = 	0.3656007766723633        ## 砾石层孔隙率（参考取值：0.24-0.36）
# #孔口出流公式的参数
# C = 	0.02142333984375            ## 孔流系数
# eta = 	1.599365234375	          ## 孔流指数

#高度参数,单位为mm
L1 = 100            # 表面层高度                 目前是渗透混凝土
L2 = 20             # 找平层高度                 对应的是瓜米石（5-10 mm）
L3 = 200            # 砾石层高度
L4 = 20             # 蓄水层高度

# #蒸散发参数(“暂时删除，之后再添加用公式计算”）
# e1 = 0          # 表面层蒸散发
# e2 = 0          # 找平层蒸散发
# e3 = 0          # 去掉蓄水层的砾石层蒸散发
# e4 = 0          # 蓄水层的蒸散发

#均匀降雨
q_in = 0.332        # 降雨速率，目前是0.1年一遇（0.332 mm/min)，历时60min
Tstep = 1          # 时间步长为 1 min

# #计算 t = 1 时各参数
# x= symbols('x')
# tp1 = solve(((phi1 - q_in * x / L1) * S1)/(q_in * (q_in / Ks1-1))- x,x)
# print(tp1)

t = [0 , Tstep]         #时间序列

#表面层的渗入和渗出
#设置的初始参数都默认为第0分钟，降雨为1-60共60min
theta1 = [theta_1]          # 表面层含水量变化
F1 = [0]                    # 表面层累积下渗量
f1 = [0]                    # 表面层下渗速率
f2 = [0]                    # 表面层渗出速率
ia = [0]                    # 实际入流速率
d1 = [0]                    # 表面层蓄水深度
#可用降雨速率
ia.append(q_in + d1[0]*Tstep)
#表面层下渗速率
if ia[1] == 0 :
    f1.append(0)
elif  ia[1] <= Ks1  or F1[0] == 0:
    f1.append(ia[1])
else :
    Fs1 = Ks1 * S1 * (phi1-theta1[0])/(ia[1] - Ks1)
    if F1[0] +ia[1] * Tstep < Fs1 :
        f1.append(ia[1])
    else :
        f1.append(Ks1 * (1 + ((phi1 - theta1[0]) * (d1[0] + S1) / F1[0])))
#表面层入渗速率受到表面现有水量的影响
if f1[1] > ia[1] :
    f1[1] = ia[1]
#表面层渗出速率
if theta1[0] > theta_FC1:
    f2.append(Ks1 * np.e ** (-HCO1 * (phi1 - theta1[0])))
    if f1[1] == 0 :
        delta_theta1 = math.sqrt(Ks1)/Res1 * (phi1 - theta1[0]) *Tstep
        if theta1[0] - delta_theta1 >= theta_FC1 :
            f2[1] = L1 * delta_theta1 / Tstep
        else :
            f2[1] = L1 * (theta1[0] -theta_FC1)/Tstep
else :
    f2.append(0)
if f2[1] > f1[1] and f1[1] != 0:
        f2[1] = f1[1]
#表面层饱和时，入渗速率受到底部渗出流量的限制
f1[1] = min (f1[1], (phi1-theta1[0]) * L1 / Tstep + f2[1])
f1[1] = max(f1[1],0)
#保证表面层出渗后不会导致表面层含水量低于田间持水量
f2[1] = min (f2[1] , (theta1[0] - theta_FC1) * L1 / Tstep + f1[1])
f2[1] = max (f2[1] , 0)

#找平层的渗入和渗出
theta2 = [theta_2]    # 找平层含水量变化
F2 = [0]            # 找平层累积下渗量
infil2 = [0]        # 找平层下渗速率
f3 = [0]            # 找平层渗出速率
#找平层下渗速率
if  f2[1] == 0 :
    infil2.append(0)
elif f2[1] <= Ks2 or F2[0] == 0 :
    infil2.append(f2[1])
else :
    Fs2 = Ks2 * S2 * (phi2 - theta2[0]) / (f2[1] - Ks2)
    if F2[0] + f2[1] *Tstep < Fs2 :
        infil2.append(f2[1])
    else:
        infil2.append(Ks2 * (1 + ((phi2 - theta2[0]) * S2) / F2[0]))
if infil2[1] > f2[1] :
    infil2[1] = f2[1]
f2[1] = infil2[1]
#找平层渗出速率
if theta2[0] > theta_FC2:
    f3.append(Ks2 * np.e ** (-HCO2 * (phi2 - theta2[0])))
    if f2[1] == 0 :
        delta_theta2 = math.sqrt(Ks2)/Res2 * (phi2 - theta2[0]) *Tstep
        if theta2[0] - delta_theta2 >= theta_FC2 :
            f3[1] = L2 * delta_theta2 / Tstep
        else :
            f3[1] = L2 * (theta2[0] - theta_FC2) / Tstep
else:
    f3.append(0)

#保证找平层饱和时，找平层入渗速率受到底部渗出流量的影响
f2[1] = min (f2[1] , (phi2 - theta2[0]) * L2 /Tstep + f3[1] )
f2[1] = max (f2[1] , 0)
#保证找平层出渗后不会导致找平层含水量低于田间持水量
f3[1] = min(f3[1],(theta2[0] - theta_FC2) * L2 / Tstep + f2[1])
f3[1] = max(f3[1],0)

#砾石层的渗入和渗出
q_out = [0]             # 出水管速率
d3 = [19.5]               # 蓄水总深度
theta3= [d3[0]/L3*phi3]    # 砾石层含水量
h = [0]                 # 溢出高度
Q_out = [0]             # 流出流量 mL/min

if d3[0] <= L4 :
    h.append(0)
elif d3[0] > L4 and d3[0] < L3 :
    h.append(d3[0] - L4)
else :
    if theta2[0] < phi2 and theta2[0] >= theta_FC2 :
        h.append(L3-L4 + (theta2[0]-theta_FC2)/(phi2-theta_FC2)*L2)
    else:
        if theta1[0] < phi1 and theta1[0] >= theta_FC1:
            h.append(L3 - L4 + L2 + (theta1[0] - theta_FC1) / (phi1 - theta_FC1) * L1)
        else :
            h.append(L3 - L4 + L2 + L1 +d1[0])

q_out.append(C * h[0] ** eta)
#保证砾石层出流不会出现在砾石层水位低于排水高度后
q_out[1] = min (q_out[1], (d3[0] - L4 ) *phi3/Tstep + f3[1])
q_out[1] = max (q_out[1],0)
#砾石层饱和时，砾石层入渗速率收到底部渗出流量的影响
f3[1] = min (f3[1] , (phi3 - theta3[0]) * L3 /Tstep + q_out[1] )
f3[1] = max (f3[1] , 0)
#保证找平层出身不会超过砾石层排水水量
f3[1] = min(f3[1] ,(L3-d3[0])*phi3/Tstep + q_out[1])
f3[1] = max(f3[1] , 0)
if theta2[0] == phi2 and d3[0] == L3:
    if f3[1] > q_out[1] :
        f3[1] =q_out[1]
    else :
        q_out[1] =max(f3[1] , 0)
    f2[1] = min (f3[1] , f2[1])
    if theta1[0] == phi1 :
        f1[1] = min (f1[1] , f2[1])

Q_out.append(q_out[1] * 360)


#参数计算
d1.append((ia[1] - f1[1])*Tstep)
d3.append(d3[0] + (f3[1]-q_out[1])/phi3 * Tstep)
theta3.append(min(phi3, theta3[0] + (f3[1]-q_out[1])/L3 * Tstep))
if f1[1] == 0 and f2[1] != 0:
    delta_theta1 = math.sqrt(Ks1) / Res1 * (phi1 - theta1[0]) * Tstep
    if theta1[0] - delta_theta1 >= theta_FC1:
        theta1.append(theta1[0] - delta_theta1)
        F1.append (max(0,F1[0] - L1*delta_theta1))
    else:
        theta1.append(theta_FC1)
        F1.append(max(0, F1[0] - L1 * (theta1[0]-theta_FC1)))
else:
    F1.append(F1[0] + f1[1] * Tstep)
    theta1.append(min(phi1, theta1[0] + (f1[1] - f2[1]) / L1 * Tstep))

if f2[1] == 0 and f3[1] != 0:
    delta_theta2 = math.sqrt(Ks2)/Res2 * (phi2 - theta2[0]) *Tstep
    if theta2[0] -delta_theta2 >= theta_FC2 :
        theta2.append(theta2[0] - delta_theta2)
        F2.append (max(0,F2[0] - L2*delta_theta2))
    else:
        theta2.append(theta_FC2)
        F2.append(max(0, F2[0] - L2 * (theta2[0] - theta_FC2)))
else:
    F2.append(F2[0] + f2[1] * Tstep)
    theta2.append(min(phi2, theta2[0] + (f2[1] - f3[1]) / L2 * Tstep))

f = open("result_pc0512.txt", "w")
print("t\tia\tf1\tf2\tf3\tF1\tF2\t theta1\t theta2\t theta3\td1\td3\tq_out\tQ_out",file=f)
print(t[1], ia[1], f1[1], f2[1],  f3[1],
      F1[1],F2[1],
      theta1[1],theta2[1],theta3[1],
      d1[1], d3[1], q_out[1], Q_out[1],sep = '\t',file=f)
#######
a = Q_out[1]
#######
Qy = [0,0]
for i in range(2,int(181/Tstep)):
    t.append(t[i-1] + Tstep)         #时间序列
    #可用降雨速率
    if i <= 60/Tstep :
        ia.append(q_in + d1[i-1] / Tstep)
    else :
        ia.append(d1[i-1]/ Tstep)
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
            f1.append(Ks1 * (1 + ((phi1 - theta1[i-1]) * (d1[i-1]+S1)) / F1[i-1]))
    # 表面层入渗速率受到表面现有水量的影响
    if f1[i] > ia[i]:
        f1[i] = ia[i]
    # 表面层渗出速率
    if theta1[i-1] > theta_FC1 :
        f2.append(Ks1 * np.e ** (-HCO1 * (phi1 - theta1[i - 1])))
        if f1[i] == 0 :
            delta_theta1 = math.sqrt(Ks1) / Res1 * (theta1[i-1] - theta1[0]) * Tstep
            #delta_theta1 = math.sqrt(Ks1) / Res1 * (phi1 - theta1[0]) * Tstep
            if theta1[i-1] -delta_theta1 >= theta_FC1 :
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
    elif f2[i] <= Ks2 or F2[i-1] == 0 :
        infil2.append(f2[i])
    else:
        Fs2 = Ks2 * S2 * (phi2 - theta2[0]) / (f2[1] - Ks2)
        if F2[i-1] + f2[i] * Tstep < Fs2:
            infil2.append(f2[i])
        else:
            infil2.append(Ks2 * (1 + ((phi2 - theta2[i - 1]) * S2) / F2[i-1]))
    if infil2[i] > f2[i] :
        infil2[i] = f2[i]
    f2[i] = infil2[i]
    # 找平层渗出速率
    if theta2[i-1] > theta_FC2:
        f3.append(Ks2 * np.e ** (-HCO2 * (phi2 - theta2[i - 1])))
        if f2[i] == L1 * (theta1[i - 1] - theta_FC1) / Tstep and f2[i] < f3[i-1]:
            delta_theta2 = math.sqrt(Ks2) / Res2 * (theta2[i - 1] - theta2[0]) * Tstep
            if theta2[i-1] - delta_theta2 >= theta_FC2 :
                f3[i] = f2[i] + L2 * delta_theta2 / Tstep
            else :
                f3[i] = f2[i] + L2 * (theta2[i - 1] - theta_FC2) / Tstep
        elif  f2[i] == 0 :
            delta_theta2 = math.sqrt(Ks2) / Res2 * (theta2[i-1] - theta2[0]) * Tstep
            #delta_theta2 = math.sqrt(Ks2) / Res2 * (phi2 - theta2[0]) * Tstep
            if theta2[i-1] - delta_theta2 >= theta_FC2 :
                f3[i] = L2 * delta_theta2 / Tstep
            else :
                f3[i] = L2 * (theta2[i - 1] - theta_FC2) / Tstep


    else:
        f3.append(0)
    if t[i] == 94 :
        print(f3[i])
    if f3[i] > f2[i] and f2[i] != 0:
        if f2[i] == L1 * (theta1[i - 1] - theta_FC1) / Tstep and f2[i] < f3[i-1]:
            f3[i] = max(0, f3[i])
        else :
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
    elif d3[i-1] > L4 and d3[i-1] < L3 :
        h.append(d3[i-1] - L4)
    else:
        if theta2[i-1] < phi2 and theta2[i-1] >= theta_FC2:
            h.append(L3 - L4 + (theta2[i-1] - theta_FC2) / (phi2 - theta_FC2) * L2)
        else:
            if theta1[i-1] < phi1 and theta1[i-1] >= theta_FC1:
                h.append(L3 - L4 + L2 + (theta1[i-1] - theta_FC1) / (phi1 - theta_FC1) * L1)
            else:
                h.append(L3 - L4 + L2 + L1 + d1[i-1])
    q_out.append(C * h[i-1] ** eta)
    if f2[i] == 0 :
        if q_out[i] < f3[i] :
            q_out[i] = f3[i]
        elif q_out[i] > q_out[i-1] :
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
    d1.append( (ia[i] - f1[i]) * Tstep)
    d3.append(d3[i - 1] + (f3[i] - q_out[i] )/phi3 * Tstep)
    theta3.append(min(phi3, theta3[i - 1] + (f3[i] - q_out[i] ) / L3 * Tstep))
    if f1[i] == 0 and f2[i] != 0:
        delta_theta1 = math.sqrt(Ks1) / Res1 * (theta1[i-1] - theta1[0]) * Tstep
        #delta_theta1 = math.sqrt(Ks1) / Res1 * (phi1 - theta1[0]) * Tstep
        if theta1[i-1] - delta_theta1 >= theta_FC1:
            theta1.append(theta1[i-1] - delta_theta1)
            F1.append(max(0,F1[i-1] - L1 * delta_theta1))
        else :
            theta1.append(theta_FC1)
            F1.append(max(0, F1[i-1] - L1 * (theta1[i-1] - theta_FC1)))
    else:
        F1.append(F1[i - 1] + f1[i] * Tstep)
        theta1.append(min(phi1, theta1[i - 1] + (f1[i] - f2[i] ) / L1 * Tstep))

    if f2[i] == 0 and f3[i] != 0:
        delta_theta2 = math.sqrt(Ks2) / Res2 * (theta2[i - 1] - theta2[0]) * Tstep
        # delta_theta2 = math.sqrt(Ks2) / Res2 * (phi2 - theta2[0]) * Tstep
        if theta2[i-1] - delta_theta2 >= theta_FC2 :
            theta2.append(theta2[i-1] - delta_theta2)
            F2.append(max(0,F2[i-1] - L2 * delta_theta2))
        else :
            theta2.append(theta_FC2)
            F2.append(max(0, F2[i-1]- L2 * (theta2[i-1]-theta_FC2)))
    else:
        F2.append(F2[i - 1] + f2[i] * Tstep)
        theta2.append(min(phi2, theta2[i - 1] + (f2[i] - f3[i]) / L2 * Tstep))
    print(t[i], ia[i],f1[i], f2[i], f3[i],
          F1[i], F2[i],
          theta1[i], theta2[i], theta3[i],
          d1[i], d3[i], q_out[i], Q_out[i], sep='\t', file=f)
f.close()
######
#峰值
print(a)
#####


#更新画图库
params={
    'axes.labelsize':'10',       #轴上字的大小
    'xtick.labelsize':'12',      #横坐标图例尺寸
    'ytick.labelsize':'12',      #纵坐标图例尺寸
    'lines.linewidth':'2',       #线宽
    'legend.fontsize':'12',      #图例大小
    'font.family':'FangSong',    #字体
    'figure.figsize':'8,6'       #图表大小
}
pylab.rcParams.update(params)
plt.rcParams['axes.unicode_minus']=False


#导入数据文件
data0 = xlrd.open_workbook('pc_hydrodata.xlsx')
# 导入实测流量数据
table0 = data0.sheets()[0]  # 根据索引顺序索引sheet表,从0开始
row0 = table0.nrows  # 获取该sheet表中的行数
col0 = table0.ncols  # 获取该sheet表中的列数
#读取三场实测流量数据并计算平均流量
T1=[]
Qr1=[]
T2=[]
Qr2=[]
T3=[]
Qr3=[]
sum_Qr1 = 0
sum_Qr2 = 0
sum_Qr3 = 0
num = 0
for row0_index in range(1, row0):
    T1.append(table0.cell(row0_index, 0).value)
    Qr1.append(table0.cell(row0_index, 1).value)
    sum_Qr1 = sum_Qr1 + Qr1[row0_index - 1]
    T2.append(table0.cell(row0_index, 2).value)
    Qr2.append(table0.cell(row0_index, 3).value)
    sum_Qr2 = sum_Qr2 + Qr2[row0_index - 1]
    T3.append(table0.cell(row0_index, 4).value)
    Qr3.append(table0.cell(row0_index, 5).value)
    sum_Qr3 = sum_Qr3 + Qr3[row0_index - 1]
    num = num + 1
average_Qr1 = sum_Qr1 / num
average_Qr2 = sum_Qr2 / num
average_Qr3 = sum_Qr3 / num

#NSE计算
Qm1 = []
Qm2 = []
Qm3 = []
#获得实测出流值对应的模拟出流值
for r in range(0 , row0 - 1 ) :            #实测值的循环
    for m in range(0 , int(181/Tstep)):        #模拟值的循环
        if T1[r] == t[m] :
            Qm1.append(Q_out[m])
        if T2[r] == t[m] :
            Qm2.append(Q_out[m])
        if T3[r] == t[m] :
            Qm3.append(Q_out[m])

a1 = 0
b1 = 0
a2 = 0
b2 = 0
a3 = 0
b3 = 0
for i in range(num) :
    a1 = a1 + math.pow(Qr1[i]-Qm1[i], 2)
    b1 = b1 + math.pow(Qr1[i] - average_Qr1, 2)
    a2 = a2 + math.pow(Qr2[i]-Qm2[i], 2)
    b2 = b2 + math.pow(Qr2[i] - average_Qr2, 2)
    a3 = a3 + math.pow(Qr3[i]-Qm3[i], 2)
    b3 = b3 + math.pow(Qr3[i] - average_Qr3, 2)
NSE1 = 1 - a1/b1
NSE2 = 1 - a2/b2
NSE3 = 1 - a3/b3
print(NSE1)
print(NSE2)
print(NSE3)

#绘制点线图
figure = plt.plot(t,Q_out,'o-',label='模拟值',markersize=4)
figure1 = plt.plot(T1, Qr1,'bv--', label = '20220427', markersize=5 )
figure2 = plt.plot(T2, Qr2,'gv--', label = '20220430', markersize=5 )
figure3 = plt.plot(T3, Qr3,'rv--', label = '20220503', markersize=5 )

plt.legend(loc = 'upper right')
plt.title("渗透混凝土水量模型模拟")
plt.xlabel('Time(min)')
plt.ylabel('Flow Rate(mL/min)')
plt.show()
