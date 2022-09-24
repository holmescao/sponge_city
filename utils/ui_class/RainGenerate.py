from utils.ui.rain_generate import Ui_RainGenerate # 导入面源斑块选择界面
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox,QGraphicsScene,QDialog
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt

class RainGenerate(QDialog, Ui_RainGenerate):
    def __init__(self, parent=None):
        super(RainGenerate, self).__init__(parent)
        self.setupUi(self)             # 创建界面