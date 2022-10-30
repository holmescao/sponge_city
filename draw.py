import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import os
import matplotlib.cm as cm
import time

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Microsoft Yahei']  # 设定字体为微软雅黑


def show_heatmap(data, title, bar_title, ylabel, yticklabels, vmax, save_path):
    plt.figure(dpi=150)

    # 矩阵数据集，数据的index和columns分别为heatmap的y轴方向和x轴方向标签
    if "流量" in bar_title:
        cmap = plt.get_cmap('YlGnBu')
    else:
        cmap = plt.get_cmap('gist_heat_r')
        # cmap = plt.get_cmap('afmhot_r')

    ax = sns.heatmap(data,
                     cmap=cmap,
                     vmin=0,
                     vmax=vmax,
                     # annot=True,  # 默认为False，当为True时，在每个格子写入data中数据
                     # fmt=".1f",  # 设置每个格子中数据的格式，参考之前的文章，此处保留两位小数
                     # annot_kws={'size': 8, 'weight': 'normal',
                     #            'color': 'blue'},  # 设置格子中数据的大小、粗细、颜色
                     # linewidths=0.5,  # 每个格子边框宽度，默认为0
                     linecolor='black',  # 每个格子边框颜色,默认为白色
                     yticklabels=yticklabels,
                     # mask=df < 6.0,  # 热图中显示部分数据：显示数值小于6的数据
                     cbar=False,
                     )  # 使用matplotlib中的颜色盘)

    # 设置colorbar的label文本和字体大小
    cb = ax.figure.colorbar(ax.collections[0])  # 显示colorbar
    cb.ax.tick_params(labelsize=10)  # 设置colorbar刻度字体大小
    cb.set_label(bar_title)  # 设置colorbar的label

    plt.xlabel("时间(min)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()


def show_sponge_vs_non(non_sponge_data, sponge_data,
                       title, ylabel, max_val, save_path):
    plt.figure(dpi=150)

    series_len = sponge_data.shape[0]
    xx = range(series_len)
    plt.plot(xx, sponge_data, label="海绵", color="r", ls="-")
    plt.plot(xx, non_sponge_data, label="无海绵", color="b", ls="--")

    plt.xlabel("时间(min)")
    plt.ylabel(ylabel)
    plt.ylim((0, max_val*1.1))
    plt.legend()
    plt.title(title)
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()


def show_segs_curve(data, title, ylabel, max_val, save_path):
    plt.figure(dpi=150)
    # (Seg, Time)
    seg_num = data.shape[0]
    series_len = data.shape[1]

    xx = range(series_len)
    color_list = [cm.hsv(c/seg_num) for c in range(seg_num)]
    for seg in range(seg_num):
        plt.plot(xx, data[seg, :], label="河段%d" %
                 (seg+1), color=color_list[seg])

    plt.xlabel("时间(min)")
    plt.ylabel(ylabel)
    plt.ylim((0, max_val*1.1))
    plt.legend()
    plt.title(title)
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()


def draw_time_space(river_i, non_sponge_rivers, sponge_rivers, save_dir):
    """draw_river_curve 

    绘制河段曲线，一条河流（主干、支流）1张图

    Args:
        non_sponge_rivers (_type_): _description_
        sponge_rivers (_type_): _description_
    """
    mkdir(save_dir)

    """每条河的流量"""
    ylabel = "河段"
    data_type = "流量"
    bar_title = "流量(m3/min)"
    for main_branch in non_sponge_rivers[river_i]["流量"].keys():
        non_sponge_data = non_sponge_rivers[river_i]["流量"][main_branch].T
        sponge_data = sponge_rivers[river_i]["流量"][main_branch].T

        non_sponge_df = pd.DataFrame(non_sponge_data)
        sponge_df = pd.DataFrame(sponge_data)

        seg_num = non_sponge_data.shape[0]
        yticklabels = list(range(1, seg_num+1))
        max_val = max(non_sponge_data.max(), sponge_data.max())

        # 无海绵
        title = '河流%d-%s-%s（无海绵）时空图' % (river_i, main_branch, data_type)
        save_dir_ = os.path.join(save_dir, data_type)
        save_path = os.path.join(save_dir_, title+".jpg")
        mkdir(save_dir_)
        show_heatmap(non_sponge_df, title, bar_title,
                     ylabel, yticklabels,
                     vmax=max_val,
                     save_path=save_path)

        # 有海绵
        title = '河流%d-%s-%s（有海绵）时空图' % (river_i, main_branch, data_type)
        save_dir_ = os.path.join(save_dir, data_type)
        save_path = os.path.join(save_dir_, title+".jpg")
        mkdir(save_dir_)
        show_heatmap(sponge_df, title, bar_title,
                     ylabel, yticklabels,
                     vmax=max_val,
                     save_path=save_path)

    """每条河的污染物浓度"""
    for polution, polution_info in non_sponge_rivers[river_i]["浓度"].items():
        for main_branch, values in polution_info.items():  # 遍历河流分支
            data_type = polution
            non_sponge_data = non_sponge_rivers[river_i]["浓度"][polution][main_branch].T
            sponge_data = sponge_rivers[river_i]["浓度"][polution][main_branch].T

            non_sponge_df = pd.DataFrame(non_sponge_data)
            sponge_df = pd.DataFrame(sponge_data)

            seg_num = non_sponge_data.shape[0]
            yticklabels = list(range(1, seg_num+1))
            max_val = max(non_sponge_data.max(), sponge_data.max())
            bar_title = polution+"浓度 (mg/L)"
            # 无海绵
            title = '河流%d-%s-%s(无海绵)曲线图' % (river_i, main_branch, data_type)
            save_dir_ = os.path.join(save_dir, polution+"浓度")
            save_path = os.path.join(save_dir_, title+".jpg")
            mkdir(save_dir_)
            show_heatmap(non_sponge_df, title, bar_title,
                         ylabel, yticklabels,
                         vmax=max_val,
                         save_path=save_path)

            # 有海绵
            title = '河流%d-%s-%s(有海绵)曲线图' % (river_i, main_branch, data_type)
            save_dir_ = os.path.join(save_dir, polution+"浓度")
            save_path = os.path.join(save_dir_, title+".jpg")
            mkdir(save_dir_)
            show_heatmap(sponge_df, title, bar_title,
                         ylabel, yticklabels,
                         vmax=max_val,
                         save_path=save_path)


def draw_seg_curve(river_i, non_sponge_rivers, sponge_rivers, save_dir):
    """draw_seg_curve 

    时间-数值动态图
    河段对比（1条河流1张图）

    Args:
        non_sponge_rivers (_type_): _description_
        sponge_rivers (_type_): _description_
        save_dir (_type_): _description_
    """

    """流量"""
    data_type = "流量"
    for main_branch in non_sponge_rivers[river_i]["流量"].keys():
        non_sponge_data = non_sponge_rivers[river_i]["流量"][main_branch].T
        sponge_data = sponge_rivers[river_i]["流量"][main_branch].T
        ylabel = "流量(m3/min)"

        max_val = max(non_sponge_data.max(), sponge_data.max())

        # 无海绵
        title = '河流%d-%s-%s(无海绵)曲线图' % (river_i, main_branch, data_type)
        save_dir_ = os.path.join(save_dir, data_type)
        save_path = os.path.join(save_dir_, title+".jpg")
        mkdir(save_dir_)
        show_segs_curve(non_sponge_data, title, ylabel, max_val, save_path)

        # 有海绵
        title = '河流%d-%s-%s(有海绵)曲线图' % (river_i, main_branch, data_type)
        save_dir_ = os.path.join(save_dir, data_type)
        save_path = os.path.join(save_dir_, title+".jpg")
        mkdir(save_dir_)
        show_segs_curve(sponge_data, title, ylabel, max_val, save_path)

    """污染物浓度"""
    ylabel = "污染物浓度 (mg/L)"
    for polution, polution_info in non_sponge_rivers[river_i]["浓度"].items():
        for main_branch, values in polution_info.items():  # 遍历河流分支
            data_type = polution
            non_sponge_data = non_sponge_rivers[river_i]["浓度"][polution][main_branch].T
            sponge_data = sponge_rivers[river_i]["浓度"][polution][main_branch].T

            max_val = max(non_sponge_data.max(), sponge_data.max())

            # 无海绵
            title = '河流%d-%s-%s(无海绵)曲线图' % (river_i, main_branch, data_type)
            save_dir_ = os.path.join(save_dir, polution+"浓度")
            save_path = os.path.join(save_dir_, title+".jpg")
            mkdir(save_dir_)
            show_segs_curve(non_sponge_data, title, ylabel, max_val, save_path)

            # 有海绵
            title = '河流%d-%s-%s(有海绵)曲线图' % (river_i, main_branch, data_type)
            save_dir_ = os.path.join(save_dir, polution+"浓度")
            save_path = os.path.join(save_dir_, title+".jpg")
            mkdir(save_dir_)
            show_segs_curve(sponge_data, title, ylabel, max_val, save_path)


def draw_sponge_vs_non_sponge(river_i, non_sponge_rivers, sponge_rivers,
                              save_dir):
    """流量"""
    data_type = "流量"
    ylabel = "流量(m3/min)"
    for main_branch in non_sponge_rivers[river_i]["流量"].keys():
        non_sponge_data = non_sponge_rivers[river_i]["流量"][main_branch].T
        sponge_data = sponge_rivers[river_i]["流量"][main_branch].T
        max_val = max(non_sponge_data.max(), sponge_data.max())
        # 遍历河段
        for seg in range(non_sponge_data.shape[0]):
            title = '河流%d-%s-河段%s-%s 曲线图' % (river_i,
                                             main_branch, seg, data_type)

            save_dir_ = os.path.join(save_dir, data_type)
            save_path = os.path.join(save_dir_, title+".jpg")
            mkdir(save_dir_)
            show_sponge_vs_non(non_sponge_data[seg, :], sponge_data[seg, :],
                               title, ylabel, max_val, save_path)

    """污染物浓度"""
    ylabel = "污染物浓度 (mg/L)"
    for polution, polution_info in non_sponge_rivers[river_i]["浓度"].items():
        for main_branch, values in polution_info.items():
            seg_num = values.shape[1]
            for seg in range(seg_num):
                title = '河流%d-%s-河段%s-%s 曲线图' % (river_i,
                                                 main_branch, seg, polution)

                save_dir_ = os.path.join(save_dir, polution+"浓度")
                save_path = os.path.join(save_dir_, title+".jpg")
                mkdir(save_dir_)
                non_sponge_data = non_sponge_rivers[river_i]["浓度"][polution][main_branch].T
                sponge_data = sponge_rivers[river_i]["浓度"][polution][main_branch].T
                max_val = max(non_sponge_data.max(), sponge_data.max())
                show_sponge_vs_non(non_sponge_data[seg, :], sponge_data[seg, :],
                                   title, ylabel, max_val, save_path)


def mkdir(file_dir):
    if not os.path.exists(file_dir):
        os.makedirs(file_dir, exist_ok=True)


if __name__ == "__main__":
    st = time.time()
    # 加载数据
    non_sponge_rivers = np.load(
        'non_sponge_rivers.npy', allow_pickle=True).item()
    sponge_rivers = np.load(
        'sponge_rivers.npy', allow_pickle=True).item()

    """河流的动态模拟"""
    for river_i in non_sponge_rivers.keys():
        # 时间-数值动态图：河段对比
        draw_seg_curve(river_i, non_sponge_rivers, sponge_rivers,
                       save_dir="实验结果/城区/河流/时序曲线图/对比河流的所有河段")

        # 时间-数值动态图：海绵 vs. 无海绵
        draw_sponge_vs_non_sponge(river_i, non_sponge_rivers, sponge_rivers,
                                  save_dir="实验结果/城区/河流/时序曲线图/对比海绵与无海绵")

        # 时空动态分布图
        draw_time_space(river_i, non_sponge_rivers, sponge_rivers,
                        save_dir="实验结果/城区/河流/时空分布")

    """城区的动态模拟"""
    pass

    print("use time: %.2f sec." % (time.time()-st))
