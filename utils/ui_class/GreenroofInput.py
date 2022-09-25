from utils.ui.green_roof import Ui_Greenroof  # 导入绿色屋顶输入界面
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QDialog
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt


class GreenroofInput(QDialog, Ui_Greenroof):
    def __init__(self, parent=None):
        super(GreenroofInput, self).__init__(parent)
        self.setupUi(self)             # 创建界面

    def open_green_roof_Dialog(self, green_roof_Dialog, SingleGreenRoof):
        # 实例化输入界面
        # 收到确认信号后，更新参数
        self.accepted.connect(
            lambda: SingleGreenRoof.upate_params(green_roof_Dialog,))

        self.show()  # 打开窗口
