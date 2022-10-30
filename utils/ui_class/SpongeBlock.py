from utils.algo.figure_function import fig_sponge_pie
from utils.ui.sponge_block import Ui_SpongeBlock  # 导入面源斑块选择界面
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QDialog
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib.cm as cm


class SpongeBlock(QDialog, Ui_SpongeBlock):
    def __init__(self, parent=None):
        super(SpongeBlock, self).__init__(parent)
        self.setupUi(self)             # 创建界面

        self.tmp_landuse_type = "请选择"
        self.tmp_underlyingsurface_type = "请选择"

    def open_sponge_block_dialog(self, block_Dialog, main):
        self.main = main
        self.reject = False
        # %%%%%%%%%%%%%%%%这里开始%%%%%%%%%%%%%%%%
        """界面初始化"""
        landuse_type = block_Dialog.comboBox_landuse.currentText()
        underlyingsurface_type = block_Dialog.comboBox_underlyingsurface.currentText()

        if (self.tmp_landuse_type == landuse_type) and (self.tmp_underlyingsurface_type == underlyingsurface_type):
            no_change_block_type = True
        else:
            no_change_block_type = False

        self.tmp_landuse_type = landuse_type
        self.tmp_underlyingsurface_type = underlyingsurface_type

        non_def_block = "请选择"
        if (landuse_type == non_def_block) or (underlyingsurface_type == non_def_block):
            QMessageBox.critical(
                self,
                '错误',
                "请先在面源斑块窗口定义面源斑块类型")
            return

        # 显示面源斑块（土地利用类型、下垫面类型）
        self.lineEdit_landuse.setFocusPolicy(
            QtCore.Qt.ClickFocus)
        self.lineEdit_underlying.setFocusPolicy(
            QtCore.Qt.ClickFocus)
        self.lineEdit_landuse.setText(landuse_type)
        self.lineEdit_underlying.setText(
            underlyingsurface_type)
        self.lineEdit_landuse.setFocusPolicy(
            QtCore.Qt.NoFocus)
        self.lineEdit_underlying.setFocusPolicy(
            QtCore.Qt.NoFocus)

        # 临时保存当前选项值
        params_dict = self.Temp_assign_sponge_block_params
        # 设置海绵可用设施
        if not no_change_block_type:
            self.Unedit_sponge(underlyingsurface_type)

        """界面参数实时更新"""
        # 监测参数实时更新: 判断参数值是否越界、显示饼图
        self.tableWidget_sponge_setting.itemChanged.connect(
            self.Dynamic_update_sponge_block_params)
        # 面积参数更新
        self.spinBox_area.valueChanged.connect(
            self.Dynamic_update_sponge_block_area)

        # 更新：参数改变
        # self.accepted.connect()
        self.rejected.connect(
            lambda: self.reset_sponge_block_params(params_dict))

        # 打开、保持窗口
        self.show()

    def reset_sponge_block_params(self, params_dict):
        self.reject = True
        self.spinBox_area.setValue(
            params_dict["block_area"])

        temp_sponge_block_params = params_dict["sponge_params"]
        row, col = temp_sponge_block_params.shape
        for i in range(row):
            for j in range(col):
                self.tableWidget_sponge_setting.item(i, j).setText(
                    temp_sponge_block_params[i, j])

    @property
    def Temp_assign_sponge_block_params(self):
        col = 2
        temp_sponge_block_params = np.zeros(
            (self.tableWidget_sponge_setting.rowCount(), col), dtype=object)

        for i in range(self.tableWidget_sponge_setting.rowCount()):
            for j in range(col):
                temp_sponge_block_params[i, j] = self.tableWidget_sponge_setting.item(
                    i, j).text()

        return {"block_area": self.spinBox_area.value(), "sponge_params": temp_sponge_block_params}

    def Unedit_sponge(self, underlying_surface):
        # 初始化表格
        row = self.tableWidget_sponge_setting.rowCount()
        for i in range(row):
            self.tableWidget_sponge_setting = available(
                self.tableWidget_sponge_setting, i, [0])
            self.tableWidget_sponge_setting = forbidden(
                self.tableWidget_sponge_setting, i, [1])
        # TODO：土地利用类型是否也有禁用的？
        # 禁用部分设施
        if underlying_surface in "绿地, 水体":
            # 全部海绵设施均不可用
            for i in range(row):
                self.tableWidget_sponge_setting = forbidden(
                    self.tableWidget_sponge_setting, i, [0])
        elif underlying_surface in "道路, 硬地":
            # 绿色屋顶不可用
            self.tableWidget_sponge_setting = forbidden(
                self.tableWidget_sponge_setting, 0, [0])
        elif underlying_surface in "屋顶":
            # 只有绿色屋顶可用
            for i in range(1, row):
                self.tableWidget_sponge_setting = forbidden(
                    self.tableWidget_sponge_setting, i, [0])
        else:
            pass

    def Dynamic_update_sponge_block_area(self):
        if self.reject == True:
            return

        self.Dynamic_update_sponge_block_params()

    def Dynamic_update_sponge_block_params(self, item=None):
        """
        判断参数值是否越界、显示饼图
        """
        if self.reject == True or (item is not None and item.column() == 1):
            return

        block_assign, block_area, Sponge_Sum = self.cal_sponge_area

        block_assign = self.process_out_of_area(
            item, block_assign, block_area, Sponge_Sum)

        self.update_table_area(block_assign)

        block_assign[-1] = max(0, block_area-Sponge_Sum)  # 计算非海绵区域面积

        self.show_sponge_block_compose(block_assign, self.main)

    @property
    def cal_sponge_area(self):

        # 计算总面积
        block_area = self.spinBox_area.value()
        block_assign = np.zeros(5, dtype=int)
        tableWidget = self.tableWidget_sponge_setting
        row = tableWidget.rowCount()
        # 获取比例
        values = np.array([int(tableWidget.item(i, 0).text())
                           for i in range(row)])
        # 计算面积
        cover_times = 10  # 单位面积海绵处理的面积倍数
        block_assign[:4] = values * block_area // 100
        block_assign[1] *= cover_times  # 生物滞留池
        block_assign[3] *= cover_times  # 下凹式绿地

        Sponge_Sum = sum(block_assign)

        return block_assign, block_area, Sponge_Sum

    def process_out_of_area(self, item, block_assign, block_area, Sponge_Sum):
        # 对越界的处理
        cover_times = 10  # 单位面积海绵处理的面积倍数
        tableWidget = self.tableWidget_sponge_setting
        if Sponge_Sum > block_area:
            over_area = Sponge_Sum - block_area  # 4w
            if (item.row() == 1 and item.column() == 0) or (item.row() == 3 and item.column() == 0):
                origin_area = int(int(tableWidget.item(
                    item.row(), item.column()).text())*block_area*cover_times/100)
                changed_area = max(0, origin_area - over_area)
                changed_val = int(changed_area/block_area/cover_times*100)
            else:
                origin_area = int(int(tableWidget.item(
                    item.row(), item.column()).text())*block_area/100)
                changed_area = max(0, origin_area - over_area)
                changed_val = int(changed_area/block_area*100)
            # 自动调整ui界面的值
            tableWidget.item(item.row(), item.column()
                             ).setText(str(changed_val))
            # 调整面积
            block_assign[item.row()] = changed_area

        return block_assign

    def update_table_area(self, block_assign):
        # 更新ui界面的海绵面积，且列为禁动
        tableWidget = self.tableWidget_sponge_setting
        row = tableWidget.rowCount()
        for i in range(row):
            tableWidget = available(tableWidget, i, [1])
            tableWidget.item(i, 1).setText(str(block_assign[i]))
            tableWidget = forbidden(tableWidget, i, [1], zero_flag=False)

    def show_sponge_block_compose(self, block_assign, main):
        """画饼图"""
        # 获取labels
        tableWidget = self.tableWidget_sponge_setting
        row = tableWidget.rowCount()
        labels = [tableWidget.verticalHeaderItem(
            i).text() for i in range(row)]
        labels.append("非海绵区域")
        labels = np.array(labels, dtype=object)
        # 每个组成用1种颜色
        colors = np.array([cm.Set3(i/len(labels)) for i in range(len(labels))])
        # 获取显示的海绵
        zero_inds = np.where(block_assign == 0, True, False)
        block_assign = block_assign[~zero_inds]
        labels = labels[~zero_inds]
        colors = colors[~zero_inds]

        F_sponge = fig_sponge_pie(block_assign, labels, colors,
                                  width=self.graphicsView_sponge_setting_show.width(),
                                  height=self.graphicsView_sponge_setting_show.height())
        # sponge
        main.scene_sponge = QGraphicsScene()
        main.scene_sponge.addWidget(F_sponge)  # 将图形元素添加到场景中
        self.graphicsView_sponge_setting_show.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.graphicsView_sponge_setting_show.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.graphicsView_sponge_setting_show.setScene(
            main.scene_sponge)  # 将创建添加到图形视图显示窗口


def available(tableWidget, row, col_range):
    for col in col_range:
        item0 = tableWidget.item(row, col)
        item0.setFlags(QtCore.Qt.ItemFlag(63))
        item0.setBackground(QBrush(QColor(255, 255, 255)))
        # tableWidget.setItem(row, 0, item0)

    return tableWidget


def forbidden(tableWidget, row, col_range, zero_flag=True):
    """禁止对表格两列的编辑，并赋默认值

    Args:
        tableWidget (_type_): _description_
        row (_type_): _description_

    Returns:
        _type_: _description_
    """
    for col in col_range:
        item0 = tableWidget.item(row, col)
        if zero_flag:
            item0.setText("0")
        item0.setFlags(QtCore.Qt.ItemFlag(1))
        item0.setFlags(QtCore.Qt.ItemIsEditable)

    return tableWidget
