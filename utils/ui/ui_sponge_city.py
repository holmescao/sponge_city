# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sponge_city.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLayout,
    QListView, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QTabWidget, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.action_openfile = QAction(MainWindow)
        self.action_openfile.setObjectName(u"action_openfile")
        self.action_sim_green_roof = QAction(MainWindow)
        self.action_sim_green_roof.setObjectName(u"action_sim_green_roof")
        self.action_open_observed_file = QAction(MainWindow)
        self.action_open_observed_file.setObjectName(u"action_open_observed_file")
        self.action_open_weather_file = QAction(MainWindow)
        self.action_open_weather_file.setObjectName(u"action_open_weather_file")
        self.action_sim_and_val_green_roof = QAction(MainWindow)
        self.action_sim_and_val_green_roof.setObjectName(u"action_sim_and_val_green_roof")
        self.actionDates = QAction(MainWindow)
        self.actionDates.setObjectName(u"actionDates")
        self.action_Block = QAction(MainWindow)
        self.action_Block.setObjectName(u"action_Block")
        self.action_block_rainfall_file = QAction(MainWindow)
        self.action_block_rainfall_file.setObjectName(u"action_block_rainfall_file")
        self.action_sim_block = QAction(MainWindow)
        self.action_sim_block.setObjectName(u"action_sim_block")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(994, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout_2.addWidget(self.listView)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget_single_sponge_res = QTabWidget(self.centralwidget)
        self.tabWidget_single_sponge_res.setObjectName(u"tabWidget_single_sponge_res")
        self.tab_single_block = QWidget()
        self.tab_single_block.setObjectName(u"tab_single_block")
        self.green_roof_sim_curve = QGraphicsView(self.tab_single_block)
        self.green_roof_sim_curve.setObjectName(u"green_roof_sim_curve")
        self.green_roof_sim_curve.setGeometry(QRect(90, 80, 1021, 581))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.green_roof_sim_curve.sizePolicy().hasHeightForWidth())
        self.green_roof_sim_curve.setSizePolicy(sizePolicy2)
        self.tabWidget_single_sponge_res.addTab(self.tab_single_block, "")
        self.tab_block = QWidget()
        self.tab_block.setObjectName(u"tab_block")
        self.verticalLayout = QVBoxLayout(self.tab_block)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_block_res = QTabWidget(self.tab_block)
        self.tabWidget_block_res.setObjectName(u"tabWidget_block_res")
        self.tab_block_rainfall = QWidget()
        self.tab_block_rainfall.setObjectName(u"tab_block_rainfall")
        self.widget = QWidget(self.tab_block_rainfall)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 60, 1211, 391))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.block_rainfall_sim_res_rainfall = QGraphicsView(self.widget)
        self.block_rainfall_sim_res_rainfall.setObjectName(u"block_rainfall_sim_res_rainfall")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.block_rainfall_sim_res_rainfall.sizePolicy().hasHeightForWidth())
        self.block_rainfall_sim_res_rainfall.setSizePolicy(sizePolicy3)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        self.block_rainfall_sim_res_rainfall.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        self.block_rainfall_sim_res_rainfall.setForegroundBrush(brush1)

        self.horizontalLayout.addWidget(self.block_rainfall_sim_res_rainfall)

        self.block_rainfall_sim_res_pollution = QGraphicsView(self.widget)
        self.block_rainfall_sim_res_pollution.setObjectName(u"block_rainfall_sim_res_pollution")
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.NoBrush)
        self.block_rainfall_sim_res_pollution.setBackgroundBrush(brush2)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.NoBrush)
        self.block_rainfall_sim_res_pollution.setForegroundBrush(brush3)

        self.horizontalLayout.addWidget(self.block_rainfall_sim_res_pollution)

        self.block_rainfall_sim_res_runoff = QGraphicsView(self.widget)
        self.block_rainfall_sim_res_runoff.setObjectName(u"block_rainfall_sim_res_runoff")
        sizePolicy3.setHeightForWidth(self.block_rainfall_sim_res_runoff.sizePolicy().hasHeightForWidth())
        self.block_rainfall_sim_res_runoff.setSizePolicy(sizePolicy3)
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.NoBrush)
        self.block_rainfall_sim_res_runoff.setBackgroundBrush(brush4)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.NoBrush)
        self.block_rainfall_sim_res_runoff.setForegroundBrush(brush5)

        self.horizontalLayout.addWidget(self.block_rainfall_sim_res_runoff)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.tabWidget_block_res.addTab(self.tab_block_rainfall, "")
        self.tab_block_month = QWidget()
        self.tab_block_month.setObjectName(u"tab_block_month")
        self.tabWidget_block_res.addTab(self.tab_block_month, "")
        self.tab_block_year = QWidget()
        self.tab_block_year.setObjectName(u"tab_block_year")
        self.tabWidget_block_res.addTab(self.tab_block_year, "")

        self.verticalLayout.addWidget(self.tabWidget_block_res)

        self.tabWidget_single_sponge_res.addTab(self.tab_block, "")

        self.verticalLayout_2.addWidget(self.tabWidget_single_sponge_res)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 2)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 8)
        self.horizontalLayout_2.setStretch(3, 1)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_5 = QMenu(self.menu)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_block_file_load = QMenu(self.menu)
        self.menu_block_file_load.setObjectName(u"menu_block_file_load")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menusimulate = QMenu(self.menu_3)
        self.menusimulate.setObjectName(u"menusimulate")
        self.menusimulate_validate = QMenu(self.menu_3)
        self.menusimulate_validate.setObjectName(u"menusimulate_validate")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy1.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy1)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.menu_block_file_load.menuAction())
        self.menu_5.addAction(self.action_open_observed_file)
        self.menu_5.addAction(self.action_open_weather_file)
        self.menu_block_file_load.addAction(self.action_block_rainfall_file)
        self.menu_2.addAction(self.actionDates)
        self.menu_2.addAction(self.action_Block)
        self.menu_3.addAction(self.menusimulate.menuAction())
        self.menu_3.addAction(self.menusimulate_validate.menuAction())
        self.menusimulate.addAction(self.action_sim_green_roof)
        self.menusimulate.addAction(self.action_sim_block)
        self.menusimulate_validate.addAction(self.action_sim_and_val_green_roof)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget_single_sponge_res.setCurrentIndex(1)
        self.tabWidget_block_res.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sponge City", None))
        self.action_openfile.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_sim_green_roof.setText(QCoreApplication.translate("MainWindow", u"\u7eff\u8272\u5c4b\u9876", None))
        self.action_open_observed_file.setText(QCoreApplication.translate("MainWindow", u"\u89c2\u6d4b\u6587\u4ef6", None))
        self.action_open_weather_file.setText(QCoreApplication.translate("MainWindow", u"\u6c14\u8c61\u6587\u4ef6", None))
        self.action_sim_and_val_green_roof.setText(QCoreApplication.translate("MainWindow", u"\u7eff\u8272\u5c4b\u9876", None))
        self.actionDates.setText(QCoreApplication.translate("MainWindow", u"\u4eff\u771f\u65e5\u671f", None))
        self.action_Block.setText(QCoreApplication.translate("MainWindow", u"\u9762\u6e90\u6591\u5757", None))
        self.action_block_rainfall_file.setText(QCoreApplication.translate("MainWindow", u"\u964d\u96e8\u65f6\u5e8f\u6587\u4ef6", None))
        self.action_sim_block.setText(QCoreApplication.translate("MainWindow", u"\u9762\u6e90\u6591\u5757", None))
        self.tabWidget_single_sponge_res.setTabText(self.tabWidget_single_sponge_res.indexOf(self.tab_single_block), QCoreApplication.translate("MainWindow", u"\u6d77\u7ef5\u5355\u4f53", None))
        self.tabWidget_block_res.setTabText(self.tabWidget_block_res.indexOf(self.tab_block_rainfall), QCoreApplication.translate("MainWindow", u"\u573a\u6b21\u964d\u96e8", None))
        self.tabWidget_block_res.setTabText(self.tabWidget_block_res.indexOf(self.tab_block_month), QCoreApplication.translate("MainWindow", u"\u6708\u5ea6", None))
        self.tabWidget_block_res.setTabText(self.tabWidget_block_res.indexOf(self.tab_block_year), QCoreApplication.translate("MainWindow", u"\u5e74\u5ea6", None))
        self.tabWidget_single_sponge_res.setTabText(self.tabWidget_single_sponge_res.indexOf(self.tab_block), QCoreApplication.translate("MainWindow", u"\u9762\u6e90\u6591\u5757", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u7eff\u8272\u5c4b\u9876", None))
        self.menu_block_file_load.setTitle(QCoreApplication.translate("MainWindow", u"\u9762\u6e90\u6591\u5757", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.menusimulate.setTitle(QCoreApplication.translate("MainWindow", u"\u4eff\u771f", None))
        self.menusimulate_validate.setTitle(QCoreApplication.translate("MainWindow", u"\u4eff\u771f\u548c\u9a8c\u8bc1", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

