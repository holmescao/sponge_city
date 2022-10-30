import pandas as pd
import os
import yaml
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene


def export_experiment_results(main, export_Dialog):
    # 判断该实验是否有仿真过
    sim_flag = False
    if export_Dialog.expr_type == "海绵单体":
        if main.green_roof_single_sim_flag:  # 绿色屋顶
            model_name = export_Dialog.expr_type+"@绿色屋顶"
            result = main.SingleGreenRoof.result
            length = len(result["降雨强度(mm/min)"])
            pack_params = main.SingleGreenRoof.pack_params
            start_date = main.SingleGreenRoof.start_dt_str

            save_process(start_date, length, result, export_Dialog,
                         main, model_name, pack_params)
            sim_flag = True
        if main.permeable_pavement_single_sim_flag:  # 渗透铺装
            model_name = export_Dialog.expr_type+"@渗透铺装"
            result = main.SinglePermeablePavement.result
            length = len(result["降雨强度(mm/min)"])
            pack_params = main.SinglePermeablePavement.pack_params
            start_date = main.SinglePermeablePavement.start_dt_str
            save_process(start_date, length, result, export_Dialog,
                         main, model_name, pack_params)
            sim_flag = True
    elif export_Dialog.expr_type == "面源斑块":
        if main.block_sim_flag:
            model_name = export_Dialog.expr_type
            result = main.NonPointPollution.result
            length = len(result["降雨强度(mm/min)"])
            pack_params = main.NonPointPollution.pack_params
            start_date = main.NonPointPollution.start_dt_str
            save_process(start_date, length, result, export_Dialog,
                         main, model_name, pack_params)
            sim_flag = True
    elif export_Dialog.expr_type == "海绵地块":
        if main.sponge_block_sim_flag:
            model_name = export_Dialog.expr_type
            result = main.NonPointControl.result
            length = len(result["降雨强度(mm/min)"])
            pack_params = main.NonPointControl.pack_params(
                main.sponge_block_Dialog, main.NonPointPollution)
            start_date = main.NonPointControl.start_dt_str
            save_process(start_date, length, result, export_Dialog,
                         main, model_name, pack_params)
            sim_flag = True
    # TODO：海绵城区
    # 判断是否进行了实验
    if not sim_flag:
        QMessageBox.critical(
            main,
            '错误',
            "未进行%s实验！" % (export_Dialog.expr_type))
        return


def save_process(start_date, length, result, export_Dialog, main, model_name, pack_params):
    # 仿真结果处理
    freq = "1min"
    dates = pd.date_range(start=start_date, periods=length, freq=freq)
    date_list = [x.strftime("%Y-%m-%d %H:%M") for x in dates]
    result["仿真时间(min)"] = date_list
    data = pd.DataFrame(result)
    # 时间放第一列
    temp = list(data.columns)
    temp2 = temp[-1:]+temp[:-2]
    data = data[temp2]

    # 设置完整保存路径
    timestamp = str(datetime.datetime.now()).split(
        ".")[0].replace(" ", "T").replace("-", "").replace(":", "")
    file_path = export_Dialog.lineEdit_filepath.text()
    full_file_path = os.path.join(file_path, timestamp)
    # 保存结果
    ADP = main.ADP+" (天)" if main.ADP != 5 else "未设置，默认污染物累积量达到最大"
    save_sim_params(full_file_path,
                    model_name=model_name,
                    params_dict=pack_params,
                    start_date=date_list[0],
                    end_date=date_list[-1],
                    ADP=ADP,
                    timestamp=timestamp,
                    freq=freq)
    save_sim_results(full_file_path,
                     model_name=model_name,
                     data=data)
    QMessageBox.information(
        export_Dialog, '保存完毕', '实验参数和结果已保存')


def open_export_file_path(main):
    cwd = os.getcwd()  # 获取当前程序文件位置
    export_file_path = QFileDialog.getExistingDirectory(
        main, "选择实验结果保存路径", cwd)  # 起始路径

    # main.export_file_path, filetype = QFileDialog.getSaveFileName(main,
    #                                                               u"选择实验结果保存路径",
    #                                                               cwd,
    #                                                               "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
    main.lineEdit_filepath.setText(export_file_path)


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


def select_weather_file(main):
    main.weather_file_path, _ = QFileDialog.getOpenFileName(main,
                                                            u"选取气象文件",
                                                            "./",
                                                            "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
    if ".txt" not in main.weather_file_path:
        QMessageBox.critical(
            main,
            '错误',
            "数据文件格式必须为'*.txt'！")


def select_district_file(main):
    main.district_file_path, _ = QFileDialog.getOpenFileName(main,
                                                             u"选取城区文件",
                                                             "./",
                                                             "All Files (*);;Text Files (*.xlsx)")  # 设置文件扩展名过滤,注意用双分号间隔
    if ".xlsx" not in main.district_file_path:
        QMessageBox.critical(
            main,
            '错误',
            "数据文件格式必须为'*.xlsx'！")


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


def check_district_file(main):
    # 判断是否选择了路径，若无，则要弹窗
    if not hasattr(main, 'district_file_path'):
        QMessageBox.critical(
            main,
            '错误',
            '执行城区仿真前，请先导入数据文件！')
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


def save_sim_results(save_dir, model_name, data):
    # 路径设置
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    # 执行保存
    save_path = os.path.join(
        save_dir, "仿真结果_%s.xlsx" % (model_name))
    data.to_excel(save_path, index=False, float_format='%.2f')


def save_sim_params(save_dir, model_name, params_dict, start_date, end_date, ADP, timestamp, freq='1min'):
    # 路径设置
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    def merge_two_dicts(x, y):
        """Given two dicts, merge them into a new dict as a shallow copy."""
        x.update(y)
        return x

    other_cfg = {
        "基本信息":
            {
                "实验时间戳": timestamp,
                "仿真模型": model_name,
                "仿真起始日期+时间": start_date,
                "仿真结束日期+时间": end_date,
                "时间步长": freq,
                "雨前干旱时间": ADP,
                # TODO：看还需要加什么信息？比如雨前干旱
            }
    }
    params_dict = merge_two_dicts(other_cfg, {"用户输入参数": params_dict})

    save_path = os.path.join(
        save_dir, "仿真参数_%s.yaml" % (model_name))
    save_dict_to_yaml(params_dict, save_path)
