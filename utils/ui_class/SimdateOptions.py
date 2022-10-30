from utils.ui.sim_dates import Ui_SimDates  # 导入时间选择界面
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QDialog
from PyQt5.QtCore import Qt


class SimdateOptions(QDialog, Ui_SimDates):
    def __init__(self, parent=None):
        super(SimdateOptions, self).__init__(parent)
        self.setupUi(self)             # 创建界面

    def open_sim_datetime_dialog(self, main):
        # 收到确认信号后，更新参数
        main.dateTime_start_edit = self.dateTime_start_edit
        main.dateTime_end_edit = self.dateTime_end_edit
        main.spinBox_timestep = self.spinBox_timestep
        main.spinBox_ADP = self.spinBox_ADP

        self.accepted.connect(lambda: self.update_sim_datetime(main,))
        self.show()

    def update_sim_datetime(self, main):
        # 获取更新后的时间
        # 起始时间
        main.dateTime_start_edit.setDisplayFormat("yyyy-MM-dd hh:mm")
        start_dt = main.dateTime_start_edit.dateTime()
        main.start_dt_str = start_dt.toString(
            main.dateTime_start_edit.displayFormat())
        # 结束时间
        main.dateTime_end_edit.setDisplayFormat("yyyy-MM-dd hh:mm")
        end_dt = main.dateTime_end_edit.dateTime()
        main.end_dt_str = end_dt.toString(
            main.dateTime_end_edit.displayFormat())
        # 时间步长hour
        main.time_step = main.spinBox_timestep.value() / 60
        # 雨前干旱时间day
        main.ADP = main.spinBox_ADP.value()
