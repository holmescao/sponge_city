from utils.ui.block import Ui_Block  # 导入面源斑块选择界面
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QDialog
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Block(QDialog, Ui_Block):

    def __init__(self, parent=None):
        super(Block, self).__init__(parent)
        self.setupUi(self)             # 创建界面

    def open_block_dialog(self, NonPointPollution):
        # 临时保存当前选项值
        temp_block_params = NonPointPollution.Temp_assign_params(
            self)

        self.reject = False

        # 选择面源斑块类型
        self.comboBox_landuse.currentIndexChanged.connect(
            lambda: self.get_landuse_type(NonPointPollution))
        self.comboBox_underlyingsurface.currentIndexChanged.connect(
            lambda: self.get_underlyingsurface_type(NonPointPollution))

        # 更新：参数改变（真的）
        self.accepted.connect(
            lambda: NonPointPollution.update_params(self))

        # 恢复到此次打开窗口时的初始值
        self.rejected.connect(
            lambda: self.reset_block_params(NonPointPollution, temp_block_params))

        # 打开、保持窗口
        self.show()

    def get_landuse_type(self, NonPointPollution):
        # 如果是因为退出而引发的利用类型变化则跳过
        if self.reject:
            return

        # 只显示土地利用类型对应的参数值，但不更新模型的参数值
        NonPointPollution.change_landuse_params(self)

    def get_underlyingsurface_type(self, NonPointPollution):
        # 如果是因为退出而引发的利用类型变化则跳过
        if self.reject:
            return

        # 只显示下垫面类型对应的参数值，但不更新模型的参数值
        NonPointPollution.change_underlyingsurface_params(self)

    def reset_block_params(self, NonPointPollution, temp_block_params):
        self.reject = True
        NonPointPollution.reset_params(self, temp_block_params)
