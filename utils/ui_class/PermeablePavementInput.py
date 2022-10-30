from utils.ui.permeable_pavement import Ui_PermeablePavement  # 导入绿色屋顶输入界面
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QDialog
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt


class PermeablePavementInput(QDialog, Ui_PermeablePavement):
    def __init__(self, parent=None):
        super(PermeablePavementInput, self).__init__(parent)
        self.setupUi(self)             # 创建界面

    def open_permeable_pavement_Dialog(self, permeable_pavement_Dialog, SinglePermeablePavement):
        # 实例化输入界面
        # 收到确认信号后，更新参数
        self.accepted.connect(
            lambda: SinglePermeablePavement.upate_params(permeable_pavement_Dialog,))

        self.show()  # 打开窗口
