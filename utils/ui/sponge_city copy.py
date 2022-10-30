# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sponge_city.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(994, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.listView = QtWidgets.QListView(self.centralwidget)
        # self.listView.setObjectName("listView")
        # self.horizontalLayout_2.addWidget(self.listView)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.horizontalLayout_2.addWidget(self.listView)
        haimian_listModel = QStringListModel()
        self.haimain_list = ["绿色屋顶", "渗透铺装", "下凹式绿地", "生物滞留池"]
        haimian_listModel.setStringList(self.haimain_list)
        self.listView.setModel(haimian_listModel)

        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget_single_sponge_res = QtWidgets.QTabWidget(
            self.centralwidget)
        self.tabWidget_single_sponge_res.setObjectName(
            "tabWidget_single_sponge_res")
        self.tab_single_block = QtWidgets.QWidget()
        self.tab_single_block.setObjectName("tab_single_block")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_single_block)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.green_roof_sim_curve = QtWidgets.QGraphicsView(
            self.tab_single_block)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.green_roof_sim_curve.sizePolicy().hasHeightForWidth())
        self.green_roof_sim_curve.setSizePolicy(sizePolicy)
        self.green_roof_sim_curve.setObjectName("green_roof_sim_curve")
        self.horizontalLayout_10.addWidget(self.green_roof_sim_curve)
        self.tabWidget_single_sponge_res.addTab(self.tab_single_block, "")
        self.tab_block = QtWidgets.QWidget()
        self.tab_block.setObjectName("tab_block")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_block)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_block_res = QtWidgets.QTabWidget(self.tab_block)
        self.tabWidget_block_res.setObjectName("tabWidget_block_res")
        self.tab_block_rainfall = QtWidgets.QWidget()
        self.tab_block_rainfall.setObjectName("tab_block_rainfall")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_block_rainfall)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.block_rainfall_sim_res_rainfall = QtWidgets.QGraphicsView(
            self.tab_block_rainfall)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.block_rainfall_sim_res_rainfall.sizePolicy().hasHeightForWidth())
        self.block_rainfall_sim_res_rainfall.setSizePolicy(sizePolicy)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.block_rainfall_sim_res_rainfall.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.block_rainfall_sim_res_rainfall.setForegroundBrush(brush)
        self.block_rainfall_sim_res_rainfall.setObjectName(
            "block_rainfall_sim_res_rainfall")
        self.horizontalLayout.addWidget(self.block_rainfall_sim_res_rainfall)
        self.block_rainfall_sim_res_runoff = QtWidgets.QGraphicsView(
            self.tab_block_rainfall)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.block_rainfall_sim_res_runoff.sizePolicy().hasHeightForWidth())
        self.block_rainfall_sim_res_runoff.setSizePolicy(sizePolicy)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.block_rainfall_sim_res_runoff.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.block_rainfall_sim_res_runoff.setForegroundBrush(brush)
        self.block_rainfall_sim_res_runoff.setObjectName(
            "block_rainfall_sim_res_runoff")
        self.horizontalLayout.addWidget(self.block_rainfall_sim_res_runoff)
        self.block_rainfall_sim_res_pollution = QtWidgets.QGraphicsView(
            self.tab_block_rainfall)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.block_rainfall_sim_res_pollution.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.block_rainfall_sim_res_pollution.setForegroundBrush(brush)
        self.block_rainfall_sim_res_pollution.setObjectName(
            "block_rainfall_sim_res_pollution")
        self.horizontalLayout.addWidget(self.block_rainfall_sim_res_pollution)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.tabWidget_block_res.addTab(self.tab_block_rainfall, "")
        self.tab_block_month = QtWidgets.QWidget()
        self.tab_block_month.setObjectName("tab_block_month")
        self.tabWidget_block_res.addTab(self.tab_block_month, "")
        self.tab_block_year = QtWidgets.QWidget()
        self.tab_block_year.setObjectName("tab_block_year")
        self.tabWidget_block_res.addTab(self.tab_block_year, "")
        self.verticalLayout.addWidget(self.tabWidget_block_res)
        self.tabWidget_single_sponge_res.addTab(self.tab_block, "")
        self.tab_sponge_block = QtWidgets.QWidget()
        self.tab_sponge_block.setObjectName("tab_sponge_block")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_sponge_block)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tabWidget_sponge_block_res = QtWidgets.QTabWidget(
            self.tab_sponge_block)
        self.tabWidget_sponge_block_res.setObjectName(
            "tabWidget_sponge_block_res")
        self.tab_sponge_block_rainfall = QtWidgets.QWidget()
        self.tab_sponge_block_rainfall.setObjectName(
            "tab_sponge_block_rainfall")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(
            self.tab_sponge_block_rainfall)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_sponge_block_rainfall)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 1180, 1300))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(
            self.scrollAreaWidgetContents)
        self.horizontalLayout_8.setSizeConstraint(
            QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sponge_block_rainfallrunoff_sim_res_rainfall = QtWidgets.QGraphicsView(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sponge_block_rainfallrunoff_sim_res_rainfall.sizePolicy().hasHeightForWidth())
        self.sponge_block_rainfallrunoff_sim_res_rainfall.setSizePolicy(
            sizePolicy)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_rainfallrunoff_sim_res_rainfall.setBackgroundBrush(
            brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_rainfallrunoff_sim_res_rainfall.setForegroundBrush(
            brush)
        self.sponge_block_rainfallrunoff_sim_res_rainfall.setObjectName(
            "sponge_block_rainfallrunoff_sim_res_rainfall")
        self.horizontalLayout_4.addWidget(
            self.sponge_block_rainfallrunoff_sim_res_rainfall)
        self.sponge_block_pollution_sim_res_rainfall_SS = QtWidgets.QGraphicsView(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sponge_block_pollution_sim_res_rainfall_SS.sizePolicy().hasHeightForWidth())
        self.sponge_block_pollution_sim_res_rainfall_SS.setSizePolicy(
            sizePolicy)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_pollution_sim_res_rainfall_SS.setBackgroundBrush(
            brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_pollution_sim_res_rainfall_SS.setForegroundBrush(
            brush)
        self.sponge_block_pollution_sim_res_rainfall_SS.setObjectName(
            "sponge_block_pollution_sim_res_rainfall_SS")
        self.horizontalLayout_4.addWidget(
            self.sponge_block_pollution_sim_res_rainfall_SS)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(
            QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sponge_block_pollution_sim_res_rainfall_COD = QtWidgets.QGraphicsView(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sponge_block_pollution_sim_res_rainfall_COD.sizePolicy().hasHeightForWidth())
        self.sponge_block_pollution_sim_res_rainfall_COD.setSizePolicy(
            sizePolicy)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_pollution_sim_res_rainfall_COD.setBackgroundBrush(
            brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_pollution_sim_res_rainfall_COD.setForegroundBrush(
            brush)
        self.sponge_block_pollution_sim_res_rainfall_COD.setObjectName(
            "sponge_block_pollution_sim_res_rainfall_COD")
        self.horizontalLayout_5.addWidget(
            self.sponge_block_pollution_sim_res_rainfall_COD)
        self.sponge_block_pollution_sim_res_rainfall_TP = QtWidgets.QGraphicsView(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sponge_block_pollution_sim_res_rainfall_TP.sizePolicy().hasHeightForWidth())
        self.sponge_block_pollution_sim_res_rainfall_TP.setSizePolicy(
            sizePolicy)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_pollution_sim_res_rainfall_TP.setBackgroundBrush(
            brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_pollution_sim_res_rainfall_TP.setForegroundBrush(
            brush)
        self.sponge_block_pollution_sim_res_rainfall_TP.setObjectName(
            "sponge_block_pollution_sim_res_rainfall_TP")
        self.horizontalLayout_5.addWidget(
            self.sponge_block_pollution_sim_res_rainfall_TP)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(
            QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sponge_block_pollution_sim_res_rainfall_TN = QtWidgets.QGraphicsView(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sponge_block_pollution_sim_res_rainfall_TN.sizePolicy().hasHeightForWidth())
        self.sponge_block_pollution_sim_res_rainfall_TN.setSizePolicy(
            sizePolicy)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_pollution_sim_res_rainfall_TN.setBackgroundBrush(
            brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_pollution_sim_res_rainfall_TN.setForegroundBrush(
            brush)
        self.sponge_block_pollution_sim_res_rainfall_TN.setObjectName(
            "sponge_block_pollution_sim_res_rainfall_TN")
        self.horizontalLayout_6.addWidget(
            self.sponge_block_pollution_sim_res_rainfall_TN)
        self.sponge_block_pollution_sim_res_rainfall_NH3N = QtWidgets.QGraphicsView(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sponge_block_pollution_sim_res_rainfall_NH3N.sizePolicy().hasHeightForWidth())
        self.sponge_block_pollution_sim_res_rainfall_NH3N.setSizePolicy(
            sizePolicy)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_pollution_sim_res_rainfall_NH3N.setBackgroundBrush(
            brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.sponge_block_pollution_sim_res_rainfall_NH3N.setForegroundBrush(
            brush)
        self.sponge_block_pollution_sim_res_rainfall_NH3N.setObjectName(
            "sponge_block_pollution_sim_res_rainfall_NH3N")
        self.horizontalLayout_6.addWidget(
            self.sponge_block_pollution_sim_res_rainfall_NH3N)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.addWidget(self.scrollArea)
        self.tabWidget_sponge_block_res.addTab(
            self.tab_sponge_block_rainfall, "")
        self.tab_sponge_block_month = QtWidgets.QWidget()
        self.tab_sponge_block_month.setObjectName("tab_sponge_block_month")
        self.tabWidget_sponge_block_res.addTab(self.tab_sponge_block_month, "")
        self.tab_sponge_block_year = QtWidgets.QWidget()
        self.tab_sponge_block_year.setObjectName("tab_sponge_block_year")
        self.tabWidget_sponge_block_res.addTab(self.tab_sponge_block_year, "")
        self.horizontalLayout_9.addWidget(self.tabWidget_sponge_block_res)
        self.tabWidget_single_sponge_res.addTab(self.tab_sponge_block, "")
        self.verticalLayout_2.addWidget(self.tabWidget_single_sponge_res)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 8)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menusimulate = QtWidgets.QMenu(self.menu_3)
        self.menusimulate.setObjectName("menusimulate")
        self.menu_single_sponge = QtWidgets.QMenu(self.menusimulate)
        self.menu_single_sponge.setObjectName("menu_single_sponge")
        self.menu_block = QtWidgets.QMenu(self.menusimulate)
        self.menu_block.setObjectName("menu_block")
        self.menusimulate_validate = QtWidgets.QMenu(self.menu_3)
        self.menusimulate_validate.setObjectName("menusimulate_validate")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_openfile = QtWidgets.QAction(MainWindow)
        self.action_openfile.setObjectName("action_openfile")
        self.action_sim_green_roof = QtWidgets.QAction(MainWindow)
        self.action_sim_green_roof.setObjectName("action_sim_green_roof")
        self.action_open_observed_file = QtWidgets.QAction(MainWindow)
        self.action_open_observed_file.setObjectName(
            "action_open_observed_file")
        self.action_open_weather_file = QtWidgets.QAction(MainWindow)
        self.action_open_weather_file.setObjectName("action_open_weather_file")
        self.action_sim_and_val_green_roof = QtWidgets.QAction(MainWindow)
        self.action_sim_and_val_green_roof.setObjectName(
            "action_sim_and_val_green_roof")
        self.actionDates = QtWidgets.QAction(MainWindow)
        self.actionDates.setObjectName("actionDates")
        self.action_Block = QtWidgets.QAction(MainWindow)
        self.action_Block.setObjectName("action_Block")
        self.action_block_rainfall_file = QtWidgets.QAction(MainWindow)
        self.action_block_rainfall_file.setObjectName(
            "action_block_rainfall_file")
        self.action_sim_block = QtWidgets.QAction(MainWindow)
        self.action_sim_block.setObjectName("action_sim_block")
        self.action_SpongeBlock = QtWidgets.QAction(MainWindow)
        self.action_SpongeBlock.setObjectName("action_SpongeBlock")
        self.action_sim_sponge_block = QtWidgets.QAction(MainWindow)
        self.action_sim_sponge_block.setObjectName("action_sim_sponge_block")
        self.action_rain_generate = QtWidgets.QAction(MainWindow)
        self.action_rain_generate.setObjectName("action_rain_generate")
        self.action_sim_permeablepavement = QtWidgets.QAction(MainWindow)
        self.action_sim_permeablepavement.setObjectName(
            "action_sim_permeablepavement")
        self.action_weather_file_load = QtWidgets.QAction(MainWindow)
        self.action_weather_file_load.setObjectName("action_weather_file_load")
        self.actiongreen = QtWidgets.QAction(MainWindow)
        self.actiongreen.setObjectName("actiongreen")
        self.action_expr_res_export = QtWidgets.QAction(MainWindow)
        self.action_expr_res_export.setObjectName("action_expr_res_export")
        self.menu.addSeparator()
        self.menu.addAction(self.action_weather_file_load)
        self.menu.addAction(self.action_expr_res_export)
        self.menu_2.addAction(self.actionDates)
        self.menu_2.addAction(self.action_Block)
        self.menu_2.addAction(self.action_SpongeBlock)
        self.menu_2.addAction(self.action_rain_generate)
        self.menu_single_sponge.addAction(self.action_sim_green_roof)
        self.menu_single_sponge.addAction(self.action_sim_permeablepavement)
        self.menu_block.addAction(self.action_sim_block)
        self.menu_block.addAction(self.action_sim_sponge_block)
        self.menusimulate.addAction(self.menu_single_sponge.menuAction())
        self.menusimulate.addAction(self.menu_block.menuAction())
        self.menusimulate_validate.addAction(
            self.action_sim_and_val_green_roof)
        self.menu_3.addAction(self.menusimulate.menuAction())
        self.menu_3.addAction(self.menusimulate_validate.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget_single_sponge_res.setCurrentIndex(1)
        self.tabWidget_block_res.setCurrentIndex(0)
        self.tabWidget_sponge_block_res.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sponge City"))
        self.tabWidget_single_sponge_res.setTabText(self.tabWidget_single_sponge_res.indexOf(
            self.tab_single_block), _translate("MainWindow", "海绵单体"))
        self.tabWidget_block_res.setTabText(self.tabWidget_block_res.indexOf(
            self.tab_block_rainfall), _translate("MainWindow", "场次降雨"))
        self.tabWidget_block_res.setTabText(self.tabWidget_block_res.indexOf(
            self.tab_block_month), _translate("MainWindow", "月度"))
        self.tabWidget_block_res.setTabText(self.tabWidget_block_res.indexOf(
            self.tab_block_year), _translate("MainWindow", "年度"))
        self.tabWidget_single_sponge_res.setTabText(self.tabWidget_single_sponge_res.indexOf(
            self.tab_block), _translate("MainWindow", "面源斑块"))
        self.tabWidget_sponge_block_res.setTabText(self.tabWidget_sponge_block_res.indexOf(
            self.tab_sponge_block_rainfall), _translate("MainWindow", "场次降雨"))
        self.tabWidget_sponge_block_res.setTabText(self.tabWidget_sponge_block_res.indexOf(
            self.tab_sponge_block_month), _translate("MainWindow", "月度"))
        self.tabWidget_sponge_block_res.setTabText(self.tabWidget_sponge_block_res.indexOf(
            self.tab_sponge_block_year), _translate("MainWindow", "年度"))
        self.tabWidget_single_sponge_res.setTabText(self.tabWidget_single_sponge_res.indexOf(
            self.tab_sponge_block), _translate("MainWindow", "海绵地块"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "选择"))
        self.menu_3.setTitle(_translate("MainWindow", "运行"))
        self.menusimulate.setTitle(_translate("MainWindow", "仿真"))
        self.menu_single_sponge.setTitle(_translate("MainWindow", "海绵单体"))
        self.menu_block.setTitle(_translate("MainWindow", "斑块"))
        self.menusimulate_validate.setTitle(_translate("MainWindow", "仿真和验证"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_openfile.setText(_translate("MainWindow", "打开"))
        self.action_sim_green_roof.setText(_translate("MainWindow", "绿色屋顶"))
        self.action_open_observed_file.setText(
            _translate("MainWindow", "观测文件"))
        self.action_open_weather_file.setText(_translate("MainWindow", "气象文件"))
        self.action_sim_and_val_green_roof.setText(
            _translate("MainWindow", "绿色屋顶"))
        self.actionDates.setText(_translate("MainWindow", "仿真日期"))
        self.action_Block.setText(_translate("MainWindow", "面源斑块"))
        self.action_block_rainfall_file.setText(
            _translate("MainWindow", "降雨时序文件"))
        self.action_sim_block.setText(_translate("MainWindow", "面源斑块"))
        self.action_SpongeBlock.setText(_translate("MainWindow", "海绵地块"))
        self.action_sim_sponge_block.setText(_translate("MainWindow", "海绵地块"))
        self.action_rain_generate.setText(_translate("MainWindow", "雨型生成"))
        self.action_sim_permeablepavement.setText(
            _translate("MainWindow", "渗透铺装"))
        self.action_weather_file_load.setText(
            _translate("MainWindow", "导入气象文件"))
        self.actiongreen.setText(_translate("MainWindow", "green"))
        self.action_expr_res_export.setText(_translate("MainWindow", "导出结果"))
