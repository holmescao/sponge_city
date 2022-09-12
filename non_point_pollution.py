## 面源污染负荷估算主程序
import os
from datetime import datetime
import pandas as pd
import xlrd
import numpy as np

def get_month(begin,end):
    begin_year,end_year=begin.year,end.year
    begin_month,end_month=begin.month,end.month
    if begin_year==end_year:
        months=end_month-begin_month
    else:
        months=(end_year-begin_year)*12+end_month-begin_month
    return months + 1


""" 1. 读取Project文件"""
file_path = 'data/non_point_pollution/Project.xlsx'
io = pd.io.excel.ExcelFile(file_path)
timeseriesdata = pd.read_excel(io,sheet_name="TimeSeries").values
patchdata = pd.read_excel(io,sheet_name="Patch").values
pollutantdata = pd.read_excel(io,sheet_name="Pollutant").values
controlunitdata = pd.read_excel(io,sheet_name="ControlUnit").values
ludata = pd.read_excel(io,sheet_name="LandUse").values
usdata = pd.read_excel(io,sheet_name="UnderlyingSurface").values
io.close()

# 读取时间、降雨量、蒸发量数据
tlabel = [xlrd.xldate.xldate_as_datetime(t,0) 
          for t in timeseriesdata[:, 0]]
rain = timeseriesdata[:, 1]
evap = timeseriesdata[:, 2]

nhour = len(tlabel)
nday = int((tlabel[-1]-tlabel[0]).days) + 1
nmonth = get_month(tlabel[0],tlabel[-1])
nyear = 1

# 读取整个城区所有斑块的id数据
patchid = patchdata[:, 0]
patchstreet = patchdata[:, 1]
patchlu = patchdata[:, 2]
patchus = patchdata[:, 3]
patcharea = patchdata[:, 4]
N = len(patchid)

# 读取污染指标对应的id
pollutantid = pollutantdata[:, 0]
npl = len(pollutantid)

# 读取控制单元对应的街道和区的id
streetid = controlunitdata[:, 0]
streetdistrict = controlunitdata[:, 1]
ns = len(streetid)
nd = max(streetdistrict)

# 读取土地利用类型的id
luid = ludata[:, 0]
nlu = len(luid)

# 读取下垫面类型的id以及对应的最大初损、下渗率
usid = usdata[:, 0]
usloss = usdata[:, 2]
usinfil = usdata[:, 3]
nus = len(usid)

# 读取所有土地利用类型和下垫面类型对应的水质参数
P = {p:{"Bmax":None,
        "bt":None,
        "C1":None,
        "C2":None,
        "EMC":None,} 
     for p in range(npl)}
for p in range(npl):
    P[p]["Bmax"] = ludata[:, 2+p] ##ok<*SAGROW>
    P[p]["bt"] = ludata[:, 2+npl+p]
    P[p]["C1"] = usdata[:, 4+p]
    P[p]["C2"] = usdata[:, 4+npl+p]
    P[p]["EMC"] = usdata[:, 4+2*npl+p]


"""2. 单位面积的径流污染产生过程线模型"""
# 2.1 rainfall runoff process simulation
# 初始化
storage = np.zeros((nhour, nus))
runoff = np.zeros((nhour, nus))
storage[0,:] = usloss.T
B = np.zeros((nhour, nus*nlu*npl))
W = np.zeros((nhour, nus*nlu*npl))

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
    for p in range(npl):
        for l in range(nlu):
            for u in range(nus):
                if P[p]["EMC"][u] == 0:
                    if rain[t] == 0:
                        B[t, p*nlu*nus + l*nus + u] = min(P[p]["Bmax"][l], 
                                                                  B[t-1, p*nlu*nus + l*nus + u] + P[p]["bt"][l])
                    else:
                        W[t, p*nlu*nus + l*nus + u] = P[p]["C1"][u] * runoff[t, u]**P[p]["C2"][u] \
                            * B[t-1, p*nlu*nus + l*nus + u]
                        B[t, p*nlu*nus + l*nus + u] = max(0, B[t-1, p*nlu*nus + l*nus + u] \
                            - W[t, p*nlu*nus + l*nus + u])
                else:
                    W[t, p*nlu*nus + l*nus + u] = runoff[t, u] * P[p]["EMC"][u]


""" 3. 叠加分析"""
patchhourlyload = np.zeros((nhour, N*npl))
streethourlyload = np.zeros((nhour, ns*npl))
districthourlyload = np.zeros((nhour, nd*npl))
cityhourlyload = np.zeros((nhour, npl))
totalrunoff = 0 
totalload = np.zeros(npl)

# 遍历所有斑块，以获得不同尺度（斑块、街道、区、城市）每小时的各类污染物的负荷
for n in range(N):
    lu = patchlu[n] - 1
    us = patchus[n] -1
    totalrunoff += sum(runoff[:, us]) * patcharea[n]
    # 遍历污染指标
    for p in range(npl):
        patchhourlyload[:, n*npl+ p] = W[:,p*nlu*nus + lu*nus + us] * patcharea[n]
        streethourlyload[:, (patchstreet[n]-1)*npl+p] = \
            streethourlyload[:, (patchstreet[n]-1)*npl+p] + patchhourlyload[:, n*npl+ p]
        totalload[p] = totalload[p] + sum(patchhourlyload[:, n*npl+ p])

# 根据每小时的污染物负荷，计算出每天的负荷
patchdailyload = np.zeros((nday, N*npl))
streetdailyload = np.zeros((nday, ns*npl))
districtdailyload = np.zeros((nday, nd*npl))
citydailyload = np.zeros((nday, npl))
for d in range(nday):
    patchdailyload[d, :] = sum(patchhourlyload[d*24:(d+1)*24,:])
    streetdailyload[d, :] = sum(streethourlyload[d*24:(d+1)*24,:])

# 根据每天的污染物负荷，计算出总的负荷
streettotalload = np.zeros((ns, npl))
for s in range(ns):
    for p in range(npl):
        temp = sum(streetdailyload)
        # 计算街道年总负荷
        streettotalload[s, p] = temp[s*npl + p]
        # 计算城市日负荷
        citydailyload[:, p] = citydailyload[:, p] + streetdailyload[:, s*npl + p]


"""4. 总体验证&生成报告"""
save_root = "results/block"
report_dir = "non_point_pollution"
save_dir = os.path.join(save_root,report_dir)
if not os.path.exists(save_dir):
    os.makedirs(save_dir,exist_ok=True)
timestamp = str(datetime.now()).split(".")[0].replace(" ", "T").replace("-","").replace(":","")
save_path = os.path.join(save_dir, "result_rpua_"+timestamp+".xlsx")    

# save
totalrunoff_np = np.zeros((1,1))
totalrunoff_np[0] = totalrunoff
totalrunoff = pd.DataFrame(totalrunoff_np)
totalload = pd.DataFrame(totalload)
runoff = pd.DataFrame(runoff)
W = pd.DataFrame(W)
streettotalload = pd.DataFrame(streettotalload)
citydailyload = pd.DataFrame(citydailyload)

writer = pd.ExcelWriter(save_path)
totalrunoff.to_excel(writer,sheet_name='Sheet1',startrow=1, startcol=1, index=False,header=False)
totalload.to_excel(writer,sheet_name='Sheet1',startrow=2, startcol=1, index=False,header=False)
runoff.to_excel(writer,sheet_name='单位面积径流过程线',startrow=1, startcol=1, index=False,header=False)
W.to_excel(writer,sheet_name='单位面积负荷过程线',startrow=3, startcol=1, index=False,header=False)
streettotalload.to_excel(writer,sheet_name='街道年总负荷分布',startrow=2, startcol=1, index=False,header=False)
citydailyload.to_excel(writer,sheet_name='城市日负荷过程线',startrow=2, startcol=1, index=False,header=False)
writer.save()