import pandas as pd
import os
import yaml
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene


def open_observed_file(main):
    main.observed_file_path, filetype = QFileDialog.getOpenFileName(main,
                                                                    u"选取观测文件",
                                                                    "./",
                                                                    "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔

    if ".txt" not in main.observed_file_path:
        QMessageBox.critical(
            main,
            '错误',
            "数据文件格式必须为'*.txt'！")


def open_weather_file(main):
    main.weather_file_path, filetype = QFileDialog.getOpenFileName(main,
                                                                   u"选取气象文件",
                                                                   "./",
                                                                   "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
    if ".txt" not in main.weather_file_path:
        QMessageBox.critical(
            main,
            '错误',
            "数据文件格式必须为'*.txt'！")


def check_weather_file(main):
    # 判断是否选择了路径，若无，则要弹窗
    if not hasattr(main, 'weather_file_path'):
        QMessageBox.critical(
            main,
            '错误',
            '执行 仿真 前，请先选择数据文件，气象是必选的）！')
        return False
    else:
        return True


def check_observed_file(main):
    # 判断是否选择了路径，若无，则要弹窗
    if not hasattr(main, 'observed_file_path'):
        QMessageBox.critical(
            main,
            '错误',
            '执行 仿真+验证 前，请先选择数据文件，观测是必选的）！')
        return False
    else:
        return True


def check_datetime_setting(main, LoopCount, start_dt_str, end_dt_str, Tstep):
    # 检查仿真时间是否正确
    if not check_datetime(LoopCount,
                          start_dt_str=start_dt_str,
                          end_dt_str=end_dt_str,
                          time_step=Tstep):
        QMessageBox.critical(
            main,
            '错误',
            '仿真日期长度与真实数据长度不匹配！请检查仿真日期参数或真实数据文件')
        return False
    else:
        return True


def save_dict_to_yaml(dict_value: dict, save_path: str):
    """dict保存为yaml"""
    with open(save_path, 'w', encoding='utf-8') as file:
        file.write(yaml.dump(dict_value, allow_unicode=True,
                   default_flow_style=False))


def read_yaml_to_dict(yaml_path: str, ):
    with open(yaml_path) as file:
        dict_value = yaml.load(file.read(), Loader=yaml.FullLoader)
        return dict_value


def check_datetime(data_num, start_dt_str, end_dt_str, time_step):
    start_dt = datetime.datetime.strptime(start_dt_str, "%Y-%m-%d %H:%M")
    end_dt = datetime.datetime.strptime(end_dt_str, "%Y-%m-%d %H:%M")

    # 计算日期之间的点数
    time_delta = end_dt - start_dt
    total_min = time_delta.days * 24 * 60 + time_delta.seconds // 60
    step_per_min = 1/time_step/60
    time_num = int(total_min * step_per_min) + 1

    return True if data_num == time_num else False


def save_single_sponge_sim_results(model_name, data, start_date, end_date, freq='1min'):
    # 路径设置
    # cur_path = os.path.split(os.path.realpath(__file__))[0]
    timestamp = str(datetime.datetime.now()).split(
        ".")[0].replace(" ", "T").replace("-", "").replace(":", "")
    # save_dir = os.path.join(cur_path,"results", "single_sponge",timestamp)
    save_dir = os.path.join("results", "single_sponge", timestamp)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    # 仿真结果数据整合成df
    dates = pd.date_range(start=start_date, end=end_date, freq=freq)
    date_list = [x.strftime("%Y-%m-%d %H:%M") for x in dates]
    sim_results = pd.DataFrame(data={"仿真时间(min)": date_list,
                                     "出流量 (mm/hr)": data})
    # 执行保存

    save_path = os.path.join(save_dir, "result_%s_sim.xlsx" % (model_name))
    sim_results.to_excel(save_path, index=False)

    return save_dir, timestamp


def save_single_sponge_sim_params(model_name, params_dict, start_date, end_date, timestamp, freq='1min'):
    # 路径设置
    save_dir = os.path.join("results", "single_sponge", timestamp)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    def merge_two_dicts(x, y):
        """Given two dicts, merge them into a new dict as a shallow copy."""
        x.update(y)
        return x

    other_cfg = {
        "基本信息":
            {
                "本次实验的时间戳": timestamp,
                "仿真海绵单体模型": model_name,
                "仿真起始日期+时间": start_date,
                "仿真结束日期+时间": end_date,
                "时间步长": freq,
            }
    }
    params_dict = merge_two_dicts(other_cfg, {"用户输入参数": params_dict})

    save_path = os.path.join(
        save_dir, "result_%s_params.yaml" % (model_name))
    save_dict_to_yaml(params_dict, save_path)
