from collections import OrderedDict
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.cm as cm
import numpy as np

# matplotlib.use("Qt5Agg")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Microsoft Yahei']  # 设定字体为微软雅黑


class MyFigure(FigureCanvasQTAgg):
    # 重写一个matplotlib图像绘制类
    def __init__(self, width=5, height=4, dpi=100):
        # 1、创建一个绘制窗口Figure对象
        self.fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        # 2、在父类中激活Figure窗口,同时继承父类属性
        super(MyFigure, self).__init__(self.fig)

    # 这里就是绘制图像、示例
    def plotSin(self, x, y):
        self.axes0 = self.fig.add_subplot(111)
        self.axes0.plot(x, y)


def fig_rainfall_runoff(rain, runoff, name_list, width, height, start_dt_str, freq):
    F1 = MyFigure(width=width, height=height, dpi=150)
    F1.resize(width, height)
    F1.axes1 = F1.fig.add_subplot(111)

    fs = 15
    xx_pred = range(len(rain))
    col = len(name_list)
    color_list = [cm.tab10(c/col) for c in range(col)]
    all_marker_list = ["o", "v", "s", "p", "P", "1", "h", "D", "X"]
    linestyle_list = ['--', '-']

    # rain
    ax1 = F1.axes1
    ax1.bar(xx_pred, rain, width=1, fc='b')

    # runoff
    ax2 = ax1.twinx()
    for c in range(col):
        ax2.plot(xx_pred, runoff[:, c],
                 color=color_list[c], lw=1, linestyle=linestyle_list[c],
                 #   marker=all_marker_list[c],
                 label=name_list[c])

    # F1.axes1.legend(fontsize=fs-2)
    """图形美化"""
    # 设置y轴范围
    # ax2.invert_yaxis() # 翻转坐标轴
    ax1.set_ylim((rain.max()*3, 0))
    ax2.set_ylim((0, runoff.max()*2))
    # 调整第二对坐标轴的label和tick位置
    ax1.yaxis.set_label_position("right")
    ax1.yaxis.tick_right()
    ax2.yaxis.set_label_position("left")
    ax2.yaxis.tick_left()
    # 设置坐标轴标注
    ax1.set_xlabel(u"时间(min)", fontsize=fs-2)
    ax1.set_ylabel(u"降雨强度 (mm/h)", fontsize=fs-5)
    ax2.set_ylabel(u"径流量 (mm/h)", fontsize=fs-5)
    # 设置图表标题
    ax1.set_title(start_dt_str.replace(" ", "T").split("T")[0])
    # 设置x坐标轴标签和刻度、字体
    xticks, xlabels = get_xticklabels(start_dt_str, periods=len(
        rain), num=3, freq=freq, fmt="%H:%M", tail=True)
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(labels=xlabels, rotation=0)
    ax1.tick_params(axis='x', labelsize=fs-3)
    ax1.tick_params(axis='y', labelsize=fs-3, labelcolor="b")  # 坐标轴颜色
    ax2.tick_params(axis='y', labelsize=fs-3)
    # F1.axes1.set_yticklabels(fontsize=fs-2)

    # 添加图例
    ax2.legend()
    # 添加网格
    ax1.grid(alpha=0.5, linestyle="-.")
    # ax2.grid(alpha=0.5,linestyle="-.")

    return F1


def fig_rainfall(values, width, height, start_dt_str, freq):
    F1 = MyFigure(width=width, height=height, dpi=150)
    F1.resize(width, height)
    F1.axes1 = F1.fig.add_subplot(111)

    fs = 15
    xx_pred = range(len(values))

    F1.axes1.bar(xx_pred, values, width=1, fc='b')
    # plt.show()
    # F1.axes1.plot(xx_pred,values,color='r',lw=2,linestyle="--",label="模拟值")
    xticks, xlabels = get_xticklabels(start_dt_str, periods=len(
        values), num=3, freq=freq, fmt="%H:%M", tail=True)

    # F1.axes1.legend(fontsize=fs-2)
    F1.axes1.set_title(start_dt_str.replace(" ", "T").split("T")[0])
    F1.axes1.set_xlabel(u"时间(min)", fontsize=fs-2)
    F1.axes1.set_ylabel(u"降雨量 (mm)", fontsize=fs-5)
    F1.axes1.set_xticks(xticks)
    F1.axes1.set_xticklabels(labels=xlabels, rotation=0)
    # F1.axes1.set_yticklabels(fontsize=fs-2)
    F1.axes1.tick_params(axis='x', labelsize=fs-3)
    F1.axes1.tick_params(axis='y', labelsize=fs)
    F1.axes1.grid(alpha=0.5, linestyle="-.")
    # F1.show()

    # plt.close()

    return F1


def fig_runoff(values, name_list, width, height, start_dt_str, freq):
    F1 = MyFigure(width=width, height=height, dpi=150)
    F1.resize(width, height)
    F1.axes1 = F1.fig.add_subplot(111)

    fs = 15
    xx_pred = range(values.shape[0])
    col = len(name_list)
    color_list = [cm.tab10(c/col) for c in range(col)]
    all_marker_list = ["o", "v", "s", "p", "P", "1", "h", "D", "X"]
    for c in range(col):
        F1.axes1.plot(xx_pred, values[:, c], color=color_list[c], lw=1,
                      linestyle="--", marker=all_marker_list[c], label=name_list[c]+"模拟值")

    xticks, xlabels = get_xticklabels(start_dt_str, periods=len(
        values), num=3, freq=freq, fmt="%H:%M", tail=True)

    # F1.axes1.legend(fontsize=fs-2)
    F1.axes1.set_title(start_dt_str.replace(" ", "T").split("T")[0])
    F1.axes1.set_xlabel(u"时间(min)", fontsize=fs-2)
    F1.axes1.set_ylabel(u"径流量 (mm/h)", fontsize=fs-5)
    F1.axes1.set_xticks(xticks)
    F1.axes1.set_xticklabels(labels=xlabels, rotation=0)
    # F1.axes1.set_yticklabels(fontsize=fs-2)
    F1.axes1.tick_params(axis='x', labelsize=fs-3)
    F1.axes1.tick_params(axis='y', labelsize=fs)
    F1.axes1.grid(alpha=0.5, linestyle="-.")
    # F1.show()

    # plt.close()

    return F1


def fig_vs_single_pollution(metric, vs_pollution, name_list, width, height, start_dt_str, freq):
    F1 = MyFigure(width=width, height=height, dpi=150)
    F1.resize(width, height)
    F1.axes1 = F1.fig.add_subplot(111)

    fs = 15

    col = vs_pollution.shape[1]
    length = vs_pollution.shape[0]
    xx_pred = range(length)
    color_list = [cm.tab10(c/col) for c in range(col)]
    all_marker_list = ["o", "v", "s", "p", "P", "1", "h", "D", "X"]
    linestyle_list = ['--', '-']

    for c in range(col):
        F1.axes1.plot(xx_pred, vs_pollution[:, c],
                      color=color_list[c], lw=1, linestyle=linestyle_list[c],
                      label=name_list[c])

    xticks, xlabels = get_xticklabels(
        start_dt_str, periods=length, num=3, freq=freq, fmt="%H:%M", tail=True)

    F1.axes1.legend(fontsize=fs-8)
    F1.axes1.set_title(start_dt_str.replace(
        " ", "T").split("T")[0] + "\n" + metric)
    F1.axes1.set_xlabel(u"时间(min)", fontsize=fs-2)
    F1.axes1.set_ylabel(u"污染物浓度 (mg/L)", fontsize=fs-5)
    F1.axes1.set_xticks(xticks)
    F1.axes1.set_xticklabels(labels=xlabels, rotation=0)
    F1.axes1.tick_params(axis='x', labelsize=fs-3)
    F1.axes1.tick_params(axis='y', labelsize=fs-3)
    F1.axes1.grid(alpha=0.5, linestyle="-.")

    return F1


def fig_pollution(values, width, height, start_dt_str, freq):
    F1 = MyFigure(width=width, height=height, dpi=150)
    F1.resize(width, height)
    F1.axes1 = F1.fig.add_subplot(111)

    fs = 15

    num = len(values.keys())
    length = len(values[list(values.keys())[0]])
    xx_pred = range(length)
    color_list = [cm.tab10(c/num) for c in range(num)]
    all_marker_list = ["o", "v", "s", "p", "P", "1", "h", "D", "X"]
    marker_list = all_marker_list[:num]
    color_map = dict(zip(values.keys(), color_list))
    marker_map = dict(zip(values.keys(), marker_list))

    for k, v in values.items():
        F1.axes1.plot(xx_pred, v, color=color_map[k],
                      lw=1, linestyle="-.", marker=marker_map[k], markersize=3, label=k)

    xticks, xlabels = get_xticklabels(
        start_dt_str, periods=length, num=3, freq=freq, fmt="%H:%M", tail=False)

    F1.axes1.legend(fontsize=fs-8)
    F1.axes1.set_title(start_dt_str.replace(" ", "T").split("T")[0])
    F1.axes1.set_xlabel(u"时间(min)", fontsize=fs-2)
    F1.axes1.set_ylabel(u"污染物 (mg/L)", fontsize=fs-5)
    F1.axes1.set_xticks(xticks)
    F1.axes1.set_xticklabels(labels=xlabels, rotation=0)
    F1.axes1.tick_params(axis='x', labelsize=fs-3)
    F1.axes1.tick_params(axis='y', labelsize=fs-3)
    F1.axes1.grid(alpha=0.5, linestyle="-.")

    return F1


def fig_sponge_pie(values, labels, width, height):
    F1 = MyFigure(width=width*0.8, height=height*0.8, dpi=150)
    # F1.resize(width,height)
    F1.axes1 = F1.fig.add_subplot(111)

    colors = np.array([cm.Set3(i/len(values)) for i in range(len(values))])
    # plot pie
    patches, l_text, p_text = \
        F1.axes1.pie(x=values,
                     # explode=explode,
                     labels=labels,
                     labeldistance=1.05,
                     colors=colors,
                     autopct='%.0f%%', shadow=False,
                     startangle=90, pctdistance=0.6)

    # params
    fontsize = 20
    list(map(lambda t: t.set_size(fontsize-4), l_text))
    list(map(lambda t: t.set_size(fontsize-4), p_text))

    F1.axes1.set_title(u"海绵地块组成面积比例", fontsize=fontsize)
    F1.axes1.legend(
        loc='best',
        ncol=1, fontsize=fontsize-6)
    F1.axes1.axis('equal')
    F1.resize(width, height)

    return F1


def fig_rain_generate(values, width, height):
    F1 = MyFigure(width=width, height=height, dpi=150)
    F1.resize(width, height)
    F1.axes1 = F1.fig.add_subplot(111)

    fs = 15

    ax = F1.axes1
    xx = range(values.shape[0])
    ax.plot(xx, values, color='b', lw=1, linestyle="-",
            marker='s', markersize=3, label='降雨强度')
    # ax.bar(xx, values, width=1,fc='b',label="降雨强度")

    """图片美化"""
    F1.axes1.legend(fontsize=fs-8)
    F1.axes1.set_title("芝加哥雨型生成结果")
    F1.axes1.set_xlabel(u"时间(min)", fontsize=fs-2)
    F1.axes1.set_ylabel(u"降雨强度 (mm/min)", fontsize=fs-5)
    F1.axes1.tick_params(axis='x', labelsize=fs-3)
    F1.axes1.tick_params(axis='y', labelsize=fs-3)
    F1.axes1.grid(alpha=0.5, linestyle="-.")

    return F1


def fig_single_sponge_sim_curve(pred, obs, NSE, start_dt_str, end_dt_str, width, height):

    F1 = MyFigure(width=width, height=height,
                  dpi=150)
    F1.resize(width, height)
    F1.axes1 = F1.fig.add_subplot(111)

    fs = 20
    xx_pred = range(len(pred))
    if obs is not None:
        xx_obs = range(len(obs))

    F1.axes1.plot(xx_pred, pred, color='r', lw=2,
                  linestyle="-", label="仿真值")
    if obs is not None:
        # F1.axes1.plot(xx_obs,pred,color='g',lw=2,linestyle=".",label="观测值")
        F1.axes1.plot(xx_obs, pred, "o", color='g', lw=1, label="观测值")

    if obs is not None:
        xticks, xlabels = get_xticklabels(
            start_dt_str, periods=len(pred), fmt="%Y-%m-%d %H:%M", freq='1H')
    else:
        xticks, xlabels = get_xticklabels(
            start_dt_str, periods=len(pred), fmt="%Y-%m-%d %H:%M", freq='min')

    F1.axes1.legend(fontsize=fs-2)
    F1.axes1.set_xlabel(u"时间", fontsize=fs-2)
    F1.axes1.set_ylabel(u"出流量 (mm/hr)", fontsize=fs-5)
    F1.axes1.set_xticks(xticks)
    F1.axes1.set_xticklabels(labels=xlabels, rotation=90)
    # F1.axes1.set_yticklabels(fontsize=fs-2)
    F1.axes1.tick_params(axis='x', labelsize=fs-2)
    F1.axes1.tick_params(axis='y', labelsize=fs)
    if NSE is None:
        F1.axes1.set_title(u"NSE is None", fontsize=fs)
    else:
        F1.axes1.set_title(u"NSE=%.4f" % NSE, fontsize=fs)

    F1.axes1.grid(alpha=0.5, linestyle="-.")
    # F1.axes1.set_tight_layout()

    return F1


def get_xticklabels(start, periods, num=6, freq='min', fmt="%Y-%m-%d %H:%M", tail=True):
    dates = pd.date_range(start=start, periods=periods, freq=freq)
    date_list = [x.strftime(fmt) for x in dates]

    show_dates = date_list[::len(dates)//num]
    show_dates = show_dates + [date_list[-1]] if tail else show_dates

    xticks = list(range(0, len(dates), len(dates)//num))
    xticks = xticks + [len(dates)-1] if tail else xticks

    xlabels = [show_dates[i] for i in range(len(show_dates))]

    return xticks, xlabels
