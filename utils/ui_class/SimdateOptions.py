from utils.ui.sim_dates import Ui_SimDates # 导入时间选择界面
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox,QGraphicsScene,QDialog
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt


class SimdateOptions(QDialog, Ui_SimDates):
    def __init__(self, parent=None):
        super(SimdateOptions, self).__init__(parent)
        self.setupUi(self)             # 创建界面