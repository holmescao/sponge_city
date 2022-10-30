from utils.ui.export import Ui_Export  # 导入绿色屋顶输入界面
from utils.algo.general_functions import open_export_file_path, export_experiment_results
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QDialog
# from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QGraphicsScene
# from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os


class Export(QDialog, Ui_Export):
    def __init__(self, parent=None):
        super(Export, self).__init__(parent)
        self.setupUi(self)             # 创建界面

        self.root_path = os.getcwd()

    def get_experiment_type(self):
        self.expr_type = self.comboBox_expr.currentText()

    def set_save_path(self):
        self.get_experiment_type()
        # 默认保存路径
        default_save_path = os.path.join(
            self.root_path, "实验结果/%s" % self.expr_type)
        self.lineEdit_filepath.setText(default_save_path)

    def open_export_Dialog(self, main):
        """初始化"""
        self.expr_type = "海绵单体"
        # 初始化默认保存路径
        default_save_path = os.path.join(
            self.root_path, "实验结果/%s" % self.expr_type)
        self.lineEdit_filepath.setText(default_save_path)

        """更新"""
        # 选择导出的实验
        self.comboBox_expr.currentTextChanged.connect(self.set_save_path)
        # 选择路径
        self.pushButton_select_filepath.clicked.connect(
            lambda: open_export_file_path(self))

        """确认"""
        self.accepted.connect(
            lambda: export_experiment_results(main, self))

        self.show()  # 打开窗口
