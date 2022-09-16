from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.cm as cm

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


def fig_rainfall(values, width,height, start_dt_str,end_dt_str, freq):
    F1 = MyFigure(width=width, height=height, dpi=150)
    F1.resize(width,height)
    F1.axes1 = F1.fig.add_subplot(111) 

    fs = 15
    xx_pred = range(len(values))

    F1.axes1.bar(xx_pred, values, width=1,fc='b')
    # plt.show()
    # F1.axes1.plot(xx_pred,values,color='r',lw=2,linestyle="--",label="模拟值")
    xticks, xlabels = get_xticklabels(start_dt_str,end_dt_str, num=3, freq=freq,fmt="%H",tail=False)

    # F1.axes1.legend(fontsize=fs-2)
    F1.axes1.set_title(start_dt_str.replace(" ","T").split("T")[0])
    F1.axes1.set_xlabel(u"时间(h)", fontsize=fs-2)
    F1.axes1.set_ylabel(u"降雨量 (mm)", fontsize=fs-5)
    F1.axes1.set_xticks(xticks)
    F1.axes1.set_xticklabels(labels=xlabels,rotation=0)
    # F1.axes1.set_yticklabels(fontsize=fs-2)
    F1.axes1.tick_params(axis='x',labelsize=fs-3)
    F1.axes1.tick_params(axis='y',labelsize=fs)    
    F1.axes1.grid(alpha=0.5,linestyle="-.")
    # F1.show()
    
    # plt.close()

    
    return F1


def fig_runoff(values, width,height, start_dt_str,end_dt_str, freq):
    F1 = MyFigure(width=width, height=height, dpi=150)
    F1.resize(width,height)
    F1.axes1 = F1.fig.add_subplot(111) 

    fs = 15
    xx_pred = range(len(values))

    # F1.axes1.bar(xx_pred, values, width=1,fc='b')
    # plt.show()
    F1.axes1.plot(xx_pred,values,color='b',lw=1,linestyle="--",label="模拟值")
    xticks, xlabels = get_xticklabels(start_dt_str,end_dt_str, num=3, freq=freq,fmt="%H",tail=False)

    # F1.axes1.legend(fontsize=fs-2)
    F1.axes1.set_title(start_dt_str.replace(" ","T").split("T")[0])
    F1.axes1.set_xlabel(u"时间(h)", fontsize=fs-2)
    F1.axes1.set_ylabel(u"径流量 (mm/h)", fontsize=fs-5)
    F1.axes1.set_xticks(xticks)
    F1.axes1.set_xticklabels(labels=xlabels,rotation=0)
    # F1.axes1.set_yticklabels(fontsize=fs-2)
    F1.axes1.tick_params(axis='x',labelsize=fs-3)
    F1.axes1.tick_params(axis='y',labelsize=fs)    
    F1.axes1.grid(alpha=0.5,linestyle="-.")
    # F1.show()
    
    # plt.close()

    
    return F1


def fig_pollution(values, width,height, start_dt_str,end_dt_str, freq):
    F1 = MyFigure(width=width, height=height, dpi=150)
    F1.resize(width,height)
    F1.axes1 = F1.fig.add_subplot(111) 

    fs = 15
    
    num = len(values.keys())
    length = len(values[list(values.keys())[0]])
    xx_pred = range(length)
    color_list = [cm.tab10(c/num) for c in range(num)]
    all_marker_list = ["o","v","s","p","P","1", "h","D","X"]
    marker_list = all_marker_list[:num]
    color_map = dict(zip(values.keys(), color_list))
    marker_map = dict(zip(values.keys(), marker_list))
    
    for k,v in values.items():        
        F1.axes1.plot(xx_pred,v,color=color_map[k], 
                      lw=1,linestyle="-.", marker=marker_map[k],markersize=3,label=k)
        
    xticks, xlabels = get_xticklabels(start_dt_str,end_dt_str, num=3, freq=freq,fmt="%H",tail=False)

    F1.axes1.legend(fontsize=fs-8)
    F1.axes1.set_title(start_dt_str.replace(" ","T").split("T")[0])
    F1.axes1.set_xlabel(u"时间(h)", fontsize=fs-2)
    F1.axes1.set_ylabel(u"污染物 (mg/L)", fontsize=fs-5)
    F1.axes1.set_xticks(xticks)
    F1.axes1.set_xticklabels(labels=xlabels,rotation=0)
    # F1.axes1.set_yticklabels(rotation=90)
    F1.axes1.tick_params(axis='x',labelsize=fs-3)
    F1.axes1.tick_params(axis='y',labelsize=fs-3)    
    F1.axes1.grid(alpha=0.5,linestyle="-.")
    # F1.show()
    
    # plt.close()

    
    return F1



# def show_curve(pred, obs,NSE):        
#         width,height = self.green_roof_sim_curve.width(),self.green_roof_sim_curve.height()
#         F1 = MyFigure(width=width, height=height, 
#                       dpi=150)
#         F1.resize(width,height)
#         F1.axes1 = F1.fig.add_subplot(111) 
        
#         fs = 20
#         xx_pred = range(len(pred))
#         if obs is not None:
#             xx_obs = range(len(obs))

def get_xticklabels(start,end,num=6,freq='min',fmt="%Y-%m-%d %H:%M",tail=False):
    dates = pd.date_range(start=start,end=end,freq=freq)
    date_list = [x.strftime(fmt) for x in dates]

    show_dates = date_list[::len(dates)//num] 
    show_dates = show_dates + [date_list[-1]] if tail else show_dates
    
    xticks = list(range(0,len(dates),len(dates)//num))
    xticks = xticks + [len(dates)-1] if tail else xticks
        
    xlabels = [show_dates[i] for i in range(len(show_dates))]
    
    return xticks, xlabels


