from utils.ui.block import Ui_Block # 导入面源斑块选择界面
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox,QGraphicsScene,QDialog
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Block(QDialog, Ui_Block):
    def __init__(self, parent=None):
        super(Block, self).__init__(parent)
        self.setupUi(self)             # 创建界面