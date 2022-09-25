from utils.algo.figure_function import fig_rain_generate
from utils.algo.rain_generate import rain_generate
from utils.ui.rain_generate import Ui_RainGenerate  # 导入面源斑块选择界面
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QDialog
from PyQt5.QtCore import Qt


class RainGenerate(QDialog, Ui_RainGenerate):
    def __init__(self, parent=None):
        super(RainGenerate, self).__init__(parent)
        self.setupUi(self)             # 创建界面

    def open_rain_generate_dialog(self, main):
        self.reject = False

        # 临时保存当前选项值
        peak = self.doubleSpinBox_peak.value()
        return_period = self.spinBox_return_period.value()
        duration = self.spinBox_duration.value()
        params_dict = self.Temp_assign_rain_generate_params(
            peak, return_period, duration)

        # 生成雨型
        rain = rain_generate(peak, return_period, duration)
        # 画图
        self.show_rain_generate(rain, main)
        # 监测参数更新
        self.doubleSpinBox_peak.valueChanged.connect(
            lambda: self.Dynamic_update_rain_generate_params(main))
        self.spinBox_return_period.valueChanged.connect(
            lambda: self.Dynamic_update_rain_generate_params(main))
        self.spinBox_duration.valueChanged.connect(
            lambda: self.Dynamic_update_rain_generate_params(main))

        # 退出
        # self.accepted.connect(
        #     lambda: self.reset_rain_generate_params(params_dict))
        self.rejected.connect(
            lambda: self.reset_rain_generate_params(params_dict))

        # 打开、保持窗口
        self.show()

    def Temp_assign_rain_generate_params(self, peak, return_period, duration):
        return {"peak": peak, "return_period": return_period, "duration": duration}

    def Dynamic_update_rain_generate_params(self, main):
        # 生成新雨型
        peak = self.doubleSpinBox_peak.value()
        return_period = self.spinBox_return_period.value()
        duration = self.spinBox_duration.value()
        rain = rain_generate(peak, return_period, duration)
        # 画图
        self.show_rain_generate(rain, main)

    def show_rain_generate(self, rain, main):
        F_rain = fig_rain_generate(rain,
                                   width=self.graphicsView_rain_generate.width(),
                                   height=self.graphicsView_rain_generate.height())
        # 将图形元素添加到场景中
        main.scene_rain_generate = QGraphicsScene()
        main.scene_rain_generate.addWidget(F_rain)
        self.graphicsView_rain_generate.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.graphicsView_rain_generate.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.graphicsView_rain_generate.setScene(
            main.scene_rain_generate)  # 将创建添加到图形视图显示窗口

    def reset_rain_generate_params(self, params_dict):
        self.reject = True
        self.doubleSpinBox_peak.setValue(
            params_dict["peak"])
        self.spinBox_return_period.setValue(
            params_dict["return_period"])
        self.spinBox_duration.setValue(
            params_dict["duration"])
