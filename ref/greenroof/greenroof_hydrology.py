import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'sans-serif'
# 设定字体为微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft Yahei']

# 绿色屋顶水文模型20220630
# 修改蓄水层最小出流深度，300改为280mm,20220710


# 输入实测出流数据,仅包括出流量不为0的数据
InputData1 = np.loadtxt('data/obsnumberoutflow20210525_0628.txt')
Qnumberobs = InputData1[:, 0]  # 实测出流流量的对应分钟序号
q3obs = InputData1[:, 1]  # 实测出流流量(仅包括不为0的数据），mm/hr
# 输入计算蒸散发所需的气象数据
InputData2 = np.loadtxt('data/meteor1min20210525_0628.txt')
i0 = InputData2[:, 0]  # 降雨量，mm/hr
Rsolar = InputData2[:, 1]/3600*10**6  # 太阳辐射，MJ/(m2 h)转换成W/m2
Tair = InputData2[:, 2]  # 气温，℃
gravelT = InputData2[:, 2]  # 蓄水层水文，假定与气温相同，℃
RH = InputData2[:, 3]  # 空气湿度，#
Uwind = InputData2[:, 4]  # 风速，m/s
# P = InputData8(:,6)  #大气压，kPa
# 将大气压kpa转换为Psychrometric constant，kPa/℃
y = 0.665*(10 ** (-3))*InputData2[:, 5]
# Ra_solar = InputData2(:,8) #地外太阳辐射，W/m2 #20211106


# 设置循环长度
LoopCount = len(InputData2)

# 设置绿色屋顶初始状态***************** initialization ******************
d1_0 = 0                   # initial depth of water stored on the surface (mm)
# soil layer initial moisture content (volume of water / total volume of soil)
xita2_0 = 0.57
d3_0 = 300    # initial depth of water in the storage layer (mm)
# initial accumulative infiltraion of surface water into the soil layer (mm),500(20200521)0500
F_0 = 0

# =========== the Design parameters ============
chang = 1000                   # 绿色屋顶长度, mm
kuan = 1000                   # 绿色屋顶宽度, mm
A = chang*kuan/10**6  # 绿色屋顶面积，m2
D1 = 30  # 溢流层深度，mm，注：论文里未注明溢流层深度
D2 = 100  # 基质层深度，mm
D3 = 300  # 蓄水层深度,mm
D3D = 280  # 蓄水层最小可出流深度,mm

# soilDensity = 1.4          # soil dry bulk density (g/cm**3)
# storageDensity = 1.8       # stone dry bulk density (g/cm**3)
# void fraction of any surface volume (i.e., the fraction of freeboard above the surface not filled with vegetation)
phi1 = 0.95

# ================ system setting ====================
Tstep = 1/60               # time step (hr),min


# 设置的常数
albedo = 0.23  # 表面反射率
e0 = 0.6113  # 0℃水的饱和蒸气压，kpa
# z00 = 0.01   #地表有效粗糙长度，m
# z = 2  #参考高度

# 已率定的水文参数,20220710
xitaFC = 0.28  # 田间持水量
xitaWP = 0.225  # 凋萎点
phi2 = 0.5  # 土壤层孔隙率
phi3 = 0.7369  # 砾石层孔隙率
C3D = 6.6077  # 孔流系数0.105,0.148,5.65
eta3D = 1  # 孔流指数，原1.865,1.93,0.9
C1 = 0.000011675  # 砾石层水分蒸发的空气动力学导率
xitacb = 0.375  # 土壤含水量大于xitacb时，植物蒸腾不受水分限制,0.28#20211223
Ksat = 178.57  # 土壤层基质流饱和导水率，mm/hr312.6044，231.72
HCO = 4.8065  # 土壤层下部水分渗出公式中的导水衰减常数34.5439
psi2 = 320.2869  # 土壤层表面水分入渗公式中的土壤层吸力水头44.1493

# 设置向量
d1 = np.zeros(LoopCount)         # depth of water stored on the surface (mm)
# soil layer moisture content (volume of water / total volume of soil)
xita2 = xitaWP*np.ones(LoopCount)
# depth of water in the storage layer (mm)
d3 = np.zeros(LoopCount)
h3 = np.zeros(LoopCount)              # suction head of the storage drain (mm)
# the effective rainfall, usually = i + q0 +d1 (mm/hr)
ia = np.zeros(LoopCount)
q1 = np.zeros(LoopCount)  # surface layer runoff or overflow rate (mm/hr)
q3 = np.zeros(LoopCount)  # storage layer underdrain outflow rate (mm/hr)
e1 = np.zeros(LoopCount)  # surface ET rate (mm/hr),PM公式
# soil layer ET rate (mm/hr),PM公式,考虑水分胁迫系数的SW模型计算蒸散发量，mm/h
e2 = np.zeros(LoopCount)
e3 = np.zeros(LoopCount)  # storage layer ET rate (mm/hr)
# infiltration rate of surface water into the soil layer (mm/hr)
f1 = np.zeros(LoopCount)
# accumulative infiltraion of surface water into the soil layer (mm)
F1 = np.zeros(LoopCount)
# percolation rate of water through the soil layer into the storage layer (mm/hr)
f2 = np.zeros(LoopCount)
es2 = np.zeros(LoopCount)  # 饱和水汽压，kPa
ea2 = np.zeros(LoopCount)  # 实际水汽压，kPa
D = np.zeros(LoopCount)  # 饱和水汽压差，kpa
delta = np.zeros(LoopCount)  # Slope of saturation vapour pressure curve，kPa/℃
# G = np.zeros(LoopCount) #土壤热通量，W/m2,白天和夜间的数值不同
Rn = np.zeros(LoopCount)  # 冠层净辐射量，W/m2,暂不考虑长波辐射的损失#
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
Ks = np.zeros(LoopCount)  # 水分胁迫系数
# SD = np.zeros(LoopCount)          #太阳倾斜角，°

# for t == 1
# ... status variables
SurfaceVolume = d1_0 * phi1  # 表面积水量，mm
SoilVolume = xita2_0 * D2  # 土壤层初始蓄水量，mm
StorageVolume = d3_0 * phi3  # 淹没层初始蓄水量，mm

# 计算胁迫因子
# 水分胁迫系数赋值
if xita2_0 >= xitacb:
    Ks[0] = 1
else:
    Ks[0] = (xita2_0-xitaWP)/(xitacb-xitaWP)


# 溢流层表面蒸发速率，mm/hr，PM模型
es2[0] = 0.6108*np.exp(17.27*Tair[0]/(Tair[0]+237.3))  # 饱和水汽压，kpa
ea2[0] = RH[0]/100*es2[0]  # 实际水汽压，kpa
# Slope of saturation vapour pressure curve，kPa/℃
delta[0] = 4098*es2[0]/(Tair[0]+237.3)**2
Rn[0] = (1-albedo)*Rsolar[0]  # 净太阳辐射，W/m2，不考虑长波辐射的损失
if d1_0 == 0:
    e1[0] = 0
else:
    e1[0] = (0.408*delta[0]*0.8*Rn[0]+y[0]*37.5/(Tair[0]+273)*Uwind[0]
             * (es2[0]-ea2[0]))/(delta[0]+y[0]*(1+0.34*Uwind[0]))

# 考虑水分胁迫的基质层蒸散，mm/h
e2[0] = Ks[0]*(0.408*delta[0]*0.8*Rn[0]+y[0]*37.5/(Tair[0]+273)
               * Uwind[0]*(es2[0]-ea2[0]))/(delta[0]+y[0]*(1+0.34*Uwind[0]))

# 积水时砾石层水分蒸发速率，mm/hr
if d3_0 > 0:
    e3[0] = C1*(1-xita2_0/phi2)*e0*np.exp(17.62*gravelT[0]/(24.3+gravelT[0]))
else:
    e3[0] = 0


# 溢流层水量，mm/hr
ia[0] = i0[0] + d1_0*phi1/Tstep
# 土壤表面入渗速率，mm/hr
if ia[0] == 0:
    f1[0] = 0
elif ia[0] <= Ksat:
    f1[0] = ia[0]
else:
    f1[0] = Ksat*(1+(phi2-xita2_0)*(d1_0+psi2)/F_0)

if f1[0] > ia[0]:
    f1[0] = ia[0]


# 溢流层溢流速率，mm/hr
if d1_0 > D1:
    q1[0] = max((d1_0 - D1)/Tstep, 0)
else:
    q1[0] = 0


# 土壤层水分渗出速率，mm/hr
if xita2_0 > xitaFC:
    f2[0] = Ksat * np.exp(-HCO*(phi2-xita2_0))
else:
    f2[0] = 0


# 砾石层穿孔管出流速率，mm/hr
if d3_0 < D3D:
    h3[0] = 0
elif d3_0 > D3D and d3_0 < D3:
    h3[0] = d3_0 - D3D
elif xita2_0 > xitaFC and xita2_0 < phi2:
    h3[0] = (D3-D3D)+(xita2_0-xitaFC)/(phi2-xitaFC)*D2
else:
    h3[0] = (D3-D3D)+D2+d1_0

q3[0] = C3D*(h3[0])**eta3D

# ... flux limit and water balance
# 新增：保证当溢流层水深低于最小可溢流深度时，溢流停止
q1[0] = min(q1[0], (d1_0-D1)*phi1/Tstep+i0[0])
q1[0] = max(q1[0], 0)
# 保证砾石层出流不会出现在砾石层水位低于排水高度之后
q3[0] = min(q3[0], (d3_0-D3D)*phi3/Tstep+f2[0]-e3[0])
q3[0] = max(q3[0], 0)
# 保证土壤层出渗速率不会超过砾石层排水流量
f2[0] = min(f2[0], (D3-d3_0)*phi3/Tstep+q3[0]+e3[0])
f2[0] = max(f2[0], 0)
# 保证土壤层出渗不会导致土壤层含水量低于田间持水量
f2[0] = min(f2[0], (xita2_0-xitaFC)*D2/Tstep+f1[0]-e2[0])
f2[0] = max(f2[0], 0)
# 使得土壤层饱和时，土壤层入渗速率受到底部渗出流量的影响
f1[0] = min(f1[0], (phi2-xita2_0)*D2/Tstep+f2[0]+e2[0])
f1[0] = max(f1[0], 0)
f1[0] = min(f1[0], d1_0*phi1/Tstep+(i0[0]-e1[0]-q1[0]))
f1[0] = max(f1[0], 0)
if xita2_0 == phi2 and d3_0 == D3:
    if f2[0] > q3[0]:
        f2[0] = q3[0]
    else:
        q3[0] = max(f2[0], 0)

    f1[0] = min(f1[0], f2[0])

# 土壤层累积入渗量，mm
F1[0] = F_0 + f1[0]*Tstep
if f1[0] == 0 and ia[0] == 0:
    F1[0] = 0


# ... update water balance,按1分钟更新
d3[0] = d3_0 + (f2[0]+q1[0]-e3[0]-q3[0])/phi3*Tstep  # 砾石层水深，mm
xita2[0] = xita2_0 + (f1[0]-e2[0]-f2[0]+e3[0])/D2*Tstep  # 土壤层含水量
if xita2[0] > phi2:
    xita2[0] = phi2

d1[0] = d1_0 + (i0[0]-e1[0]-f1[0]-q1[0])/phi1*Tstep  # 溢流层水深，mm

# t == 1

for t in range(1, LoopCount):
    # ... status variables
    SurfaceVolume = d1[t-1] * phi1
    SoilVolume = xita2[t-1] * D2
    StorageVolume = d3[t-1] * phi3

    # 设置胁迫因子
    # 水分胁迫系数赋值
    if xita2[t-1] >= xitacb:
        Ks[t] = 1
    elif xita2[t-1] < xitacb and xita2[t-1] >= xitaWP:
        Ks[t] = (xita2[t-1]-xitaWP)/(xitacb-xitaWP)
    else:
        xita2[t-1] = xitaWP
        Ks[t] = 0

    # 溢流层表面蒸发速率，mm/hr
    Rn[t] = (1-albedo)*Rsolar[t]  # 净太阳辐射，W/m2，不考虑长波辐射的损失
    es2[t] = 0.6108*np.exp(17.27*Tair[t]/(Tair[t]+237.3))  # 饱和水汽压，kPa
    ea2[t] = RH[t]/100*es2[t]  # 实际水汽压，kPa
    D[t] = es2[t]-ea2[t]  # 饱和水汽压差，kpa
    # Slope of saturation vapour pressure curve，kPa/℃
    delta[t] = 4098*es2[t]/(Tair[t]+237.3)**2

    if d1[t-1] > 0:
        e1[t] = (0.408*delta[t]*0.8*Rn[t]+y[t]*37.5/(Tair[t]+273) *
                 Uwind[t]*(es2[t]-ea2[t]))/(delta[t]+y[t]*(1+0.34*Uwind[t]))
    else:
        e1[t] = 0

    e2[t] = Ks[t]*(0.408*delta[t]*0.8*Rn[t]+y[t]*37.5/(Tair[t]+273)
                   * Uwind[t]*(es2[t]-ea2[t]))/(delta[t]+y[t]*(1+0.34*Uwind[t]))

    # 砾石层水分蒸发速率，mm/hr
    if d3[t-1] > 0:
        e3[t] = C1*(1-xita2[t-1]/phi2)*e0 * \
            np.exp(17.62*gravelT[t]/(24.3+gravelT[t]))
    else:
        e3[t] = 0

    # 溢流层水量，mm/hr
    ia[t] = i0[t] + d1[t]*phi1/Tstep
    # 土壤表面入渗速率，mm/hr
    if ia[t] == 0:
        f1[t] = 0
    elif ia[t] <= Ksat:
        f1[t] = ia[t]
    else:
        f1[t] = Ksat*(1+(phi2-xita2[t-1])*(d1[t-1]+psi2)/F1[t-1])

    if f1[t] > ia[t]:
        f1[t] = ia[t]

    # 溢流层溢流速率，mm/hr
    q1[t] = max((d1[t-1] - D1)/Tstep, 0)

    # 土壤层水分渗出速率，mm/hr
    if xita2[t-1] > xitaFC:
        f2[t] = Ksat * np.exp(-HCO*(phi2-xita2[t-1]))
    else:
        f2[t] = 0

    # 砾石层穿孔管出流速率，mm/hr
    if d3[t-1] < D3D:
        h3[t] = 0
    elif d3[t-1] > D3D and d3[t-1] < D3:
        h3[t] = d3[t-1] - D3D
    else:
        if xita2[t-1] > xitaFC:
            if xita2[t-1] < phi2:
                h3[t] = (D3-D3D)+(xita2[t-1]-xitaFC)/(phi2-xitaFC)*D2
            else:  # if soilTheta[t-1] == soilVoidFrace
                h3[t] = (D3-D3D)+D2+d1[t-1]

    q3[t] = C3D*(h3[t])**eta3D

    # ... flux limit and water balance
    # 新增：保证当溢流层水深低于最小可溢流深度时，溢流停止
    q1[t] = min(q1[t], (d1[t-1]-D1)*phi1/Tstep+i0[t])
    q1[t] = max(q1[t], 0)
    # 保证砾石层出流不会出现在砾石层水位低于排水高度之后
    q3[t] = min(q3[t], (d3[t-1]-D3D)*phi3/Tstep+f2[t]-e3[t])
    q3[t] = max(q3[t], 0)
    # 保证土壤层出渗速率不会超过砾石层排水流量
    f2[t] = min(f2[t], (D3-d3[t-1])*phi3/Tstep+q3[t]+e3[t])
    f2[t] = max(f2[t], 0)
    # 保证土壤层出渗不会导致土壤层含水量低于田间持水量
    f2[t] = min(f2[t], (xita2[t-1]-xitaFC)*D2/Tstep+f1[t]-e2[t])
    f2[t] = max(f2[t], 0)
    # 使得土壤层饱和时，土壤层入渗速率受到底部渗出流量的影响
    f1[t] = min(f1[t], (phi2-xita2[t-1])*D2/Tstep+f2[t]+e2[t])
    f1[t] = max(f1[t], 0)
    f1[t] = min(f1[t], d1_0*phi1/Tstep+(i0[t]-e1[t]-q1[t]))
    f1[t] = max(f1[t], 0)

    if xita2[t-1] == phi2 and d3[t-1] == D3:
        if f2[t] > q3[t]:
            f2[t] = q3[t]
        else:
            q3[t] = max(f2[t], 0)

        f1[t] = min(f1[t], f2[t])

    # 土壤层累积入渗量，mm
    F1[t] = F1[t-1] + f1[t]*Tstep
    if f1[t] == 0 and ia[t] == 0:
        F1[t] = 0

    # ... update water balance
    d3[t] = d3[t-1] + (f2[t]+q1[t]-e3[t]-q3[t])/phi3*Tstep  # 砾石层水深，mm
    if d3[t] < 0:
        d3[t] = 0

    xita2[t] = xita2[t-1] + (f1[t]-e2[t]-f2[t]+e3[t])/D2*Tstep  # 土壤层含水量
    if xita2[t] > phi2:
        xita2[t] = phi2

    d1[t] = d1[t-1] + (i0[t]-e1[t]-f1[t]-q1[t])/phi1*Tstep  # 溢流层水深，mm
    if d1[t] < 0:
        d1[t] = 0


# 计算实测出流的NSE
q3sim = np.zeros(len(InputData1))
Aq3 = np.zeros(len(InputData1))
Bq3 = np.zeros(len(InputData1))
for t in range(len(InputData1)):
    q3sim[t] = q3[int(Qnumberobs[t])-1]
    Aq3[t] = (q3obs[t]-q3sim[t])**2
    Bq3[t] = (q3obs[t]-np.mean(q3obs))**2

NSE_q3 = 1-np.sum(Aq3)/np.sum(Bq3)
print(NSE_q3)


def show_curve(pred, obs, NSE):
    plt.figure(figsize=(5, 5), dpi=150)
    xx_pred = range(len(pred))
    xx_obs = range(len(obs))

    plt.plot(xx_pred, pred, color='r', lw=2, linestyle="-", label="仿真值")
    plt.plot(xx_obs, pred, color='g', lw=2, linestyle="--", label="观测值")
    plt.legend()
    plt.xlabel(u"时间 (min)")
    plt.ylabel(u"出流量 (mm/hr)")
    if NSE is None:
        plt.title(u"NSE is None")
    else:
        plt.title(u"NSE=%.4f" % NSE)

    plt.grid(alpha=0.5)
    plt.show()
    plt.close()


show_curve(q3sim, q3obs, NSE_q3)
