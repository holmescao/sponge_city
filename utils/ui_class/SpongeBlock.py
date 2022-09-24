from utils.ui.sponge_block import Ui_SpongeBlock # 导入面源斑块选择界面
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox,QGraphicsScene,QDialog
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt

class SpongeBlock(QDialog, Ui_SpongeBlock):
    def __init__(self, parent=None):
        super(SpongeBlock, self).__init__(parent)
        self.setupUi(self)             # 创建界面