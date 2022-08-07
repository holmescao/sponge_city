# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sponge_city_2022年08月07日.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGraphicsView, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QToolBar, QTreeView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 600)
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(994, 0))
        self.horizontalLayout_35 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy2)

        self.horizontalLayout_34.addWidget(self.treeView)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_11)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.F_0 = QDoubleSpinBox(self.groupBox)
        self.F_0.setObjectName(u"F_0")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.F_0.sizePolicy().hasHeightForWidth())
        self.F_0.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.F_0)

        self.d3_0 = QDoubleSpinBox(self.groupBox)
        self.d3_0.setObjectName(u"d3_0")
        sizePolicy5.setHeightForWidth(self.d3_0.sizePolicy().hasHeightForWidth())
        self.d3_0.setSizePolicy(sizePolicy5)
        self.d3_0.setMaximum(9999.000000000000000)
        self.d3_0.setValue(300.000000000000000)

        self.horizontalLayout_2.addWidget(self.d3_0)

        self.xita2_0 = QDoubleSpinBox(self.groupBox)
        self.xita2_0.setObjectName(u"xita2_0")
        sizePolicy5.setHeightForWidth(self.xita2_0.sizePolicy().hasHeightForWidth())
        self.xita2_0.setSizePolicy(sizePolicy5)
        self.xita2_0.setMaximum(1.000000000000000)
        self.xita2_0.setValue(0.570000000000000)

        self.horizontalLayout_2.addWidget(self.xita2_0)

        self.d1_0 = QDoubleSpinBox(self.groupBox)
        self.d1_0.setObjectName(u"d1_0")
        sizePolicy5.setHeightForWidth(self.d1_0.sizePolicy().hasHeightForWidth())
        self.d1_0.setSizePolicy(sizePolicy5)
        self.d1_0.setMaximum(9999.000000000000000)

        self.horizontalLayout_2.addWidget(self.d1_0)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_14.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.chang = QDoubleSpinBox(self.groupBox_2)
        self.chang.setObjectName(u"chang")
        sizePolicy4.setHeightForWidth(self.chang.sizePolicy().hasHeightForWidth())
        self.chang.setSizePolicy(sizePolicy4)
        self.chang.setMaximum(999999.000000000000000)
        self.chang.setValue(1000.000000000000000)

        self.horizontalLayout_3.addWidget(self.chang)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 3)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.kuan = QDoubleSpinBox(self.groupBox_2)
        self.kuan.setObjectName(u"kuan")
        sizePolicy4.setHeightForWidth(self.kuan.sizePolicy().hasHeightForWidth())
        self.kuan.setSizePolicy(sizePolicy4)
        self.kuan.setMaximum(99999.000000000000000)
        self.kuan.setValue(1000.000000000000000)

        self.horizontalLayout_4.addWidget(self.kuan)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 3)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_10.setStretch(0, 6)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 6)

        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.D1 = QDoubleSpinBox(self.groupBox_2)
        self.D1.setObjectName(u"D1")
        sizePolicy4.setHeightForWidth(self.D1.sizePolicy().hasHeightForWidth())
        self.D1.setSizePolicy(sizePolicy4)
        self.D1.setMaximum(99999.000000000000000)
        self.D1.setValue(30.000000000000000)

        self.horizontalLayout_5.addWidget(self.D1)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 3)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.D2 = QDoubleSpinBox(self.groupBox_2)
        self.D2.setObjectName(u"D2")
        sizePolicy4.setHeightForWidth(self.D2.sizePolicy().hasHeightForWidth())
        self.D2.setSizePolicy(sizePolicy4)
        self.D2.setMaximum(99999.000000000000000)
        self.D2.setValue(100.000000000000000)

        self.horizontalLayout_6.addWidget(self.D2)

        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 3)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11.setStretch(0, 6)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 6)

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.D3 = QDoubleSpinBox(self.groupBox_2)
        self.D3.setObjectName(u"D3")
        sizePolicy4.setHeightForWidth(self.D3.sizePolicy().hasHeightForWidth())
        self.D3.setSizePolicy(sizePolicy4)
        self.D3.setMaximum(99999.000000000000000)
        self.D3.setValue(300.000000000000000)

        self.horizontalLayout_7.addWidget(self.D3)

        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(1, 3)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.D3D = QDoubleSpinBox(self.groupBox_2)
        self.D3D.setObjectName(u"D3D")
        sizePolicy4.setHeightForWidth(self.D3D.sizePolicy().hasHeightForWidth())
        self.D3D.setSizePolicy(sizePolicy4)
        self.D3D.setMaximum(99999.000000000000000)
        self.D3D.setValue(280.000000000000000)

        self.horizontalLayout_8.addWidget(self.D3D)

        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 3)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_12.setStretch(0, 6)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 6)

        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)

        self.horizontalLayout_9.addWidget(self.label_12)

        self.phi1 = QDoubleSpinBox(self.groupBox_2)
        self.phi1.setObjectName(u"phi1")
        sizePolicy4.setHeightForWidth(self.phi1.sizePolicy().hasHeightForWidth())
        self.phi1.setSizePolicy(sizePolicy4)
        self.phi1.setMaximum(99999.000000000000000)
        self.phi1.setValue(0.950000000000000)

        self.horizontalLayout_9.addWidget(self.phi1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.horizontalLayout_9.setStretch(0, 3)
        self.horizontalLayout_9.setStretch(1, 3)
        self.horizontalLayout_9.setStretch(2, 1)
        self.horizontalLayout_9.setStretch(3, 3)
        self.horizontalLayout_9.setStretch(4, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_15.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.verticalLayout_4.setStretch(1, 2)

        self.verticalLayout_9.addLayout(self.verticalLayout_4)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_33 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)

        self.horizontalLayout_16.addWidget(self.label_14)

        self.albedo = QDoubleSpinBox(self.groupBox_3)
        self.albedo.setObjectName(u"albedo")
        sizePolicy4.setHeightForWidth(self.albedo.sizePolicy().hasHeightForWidth())
        self.albedo.setSizePolicy(sizePolicy4)
        self.albedo.setMaximum(999999.000000000000000)
        self.albedo.setValue(0.230000000000000)

        self.horizontalLayout_16.addWidget(self.albedo)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)

        self.horizontalLayout_17.addWidget(self.label_15)

        self.e0 = QDoubleSpinBox(self.groupBox_3)
        self.e0.setObjectName(u"e0")
        sizePolicy4.setHeightForWidth(self.e0.sizePolicy().hasHeightForWidth())
        self.e0.setSizePolicy(sizePolicy4)
        self.e0.setDecimals(4)
        self.e0.setMaximum(999999.000000000000000)
        self.e0.setValue(0.611300000000000)

        self.horizontalLayout_17.addWidget(self.e0)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)

        self.horizontalLayout_18.addWidget(self.label_16)

        self.xitaFC = QDoubleSpinBox(self.groupBox_3)
        self.xitaFC.setObjectName(u"xitaFC")
        sizePolicy4.setHeightForWidth(self.xitaFC.sizePolicy().hasHeightForWidth())
        self.xitaFC.setSizePolicy(sizePolicy4)
        self.xitaFC.setMaximum(999999.000000000000000)
        self.xitaFC.setValue(0.280000000000000)

        self.horizontalLayout_18.addWidget(self.xitaFC)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)

        self.horizontalLayout_19.addWidget(self.label_17)

        self.xitaWP = QDoubleSpinBox(self.groupBox_3)
        self.xitaWP.setObjectName(u"xitaWP")
        sizePolicy4.setHeightForWidth(self.xitaWP.sizePolicy().hasHeightForWidth())
        self.xitaWP.setSizePolicy(sizePolicy4)
        self.xitaWP.setDecimals(3)
        self.xitaWP.setMaximum(999999.000000000000000)
        self.xitaWP.setValue(0.225000000000000)

        self.horizontalLayout_19.addWidget(self.xitaWP)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)

        self.horizontalLayout_20.addWidget(self.label_18)

        self.phi2 = QDoubleSpinBox(self.groupBox_3)
        self.phi2.setObjectName(u"phi2")
        sizePolicy4.setHeightForWidth(self.phi2.sizePolicy().hasHeightForWidth())
        self.phi2.setSizePolicy(sizePolicy4)
        self.phi2.setMaximum(999999.000000000000000)
        self.phi2.setValue(0.500000000000000)

        self.horizontalLayout_20.addWidget(self.phi2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        sizePolicy4.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy4)

        self.horizontalLayout_21.addWidget(self.label_19)

        self.phi3 = QDoubleSpinBox(self.groupBox_3)
        self.phi3.setObjectName(u"phi3")
        sizePolicy4.setHeightForWidth(self.phi3.sizePolicy().hasHeightForWidth())
        self.phi3.setSizePolicy(sizePolicy4)
        self.phi3.setDecimals(4)
        self.phi3.setMaximum(999999.000000000000000)
        self.phi3.setValue(0.736900000000000)

        self.horizontalLayout_21.addWidget(self.phi3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_29.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")
        sizePolicy4.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy4)

        self.horizontalLayout_25.addWidget(self.label_23)

        self.xitacb = QDoubleSpinBox(self.groupBox_3)
        self.xitacb.setObjectName(u"xitacb")
        sizePolicy4.setHeightForWidth(self.xitacb.sizePolicy().hasHeightForWidth())
        self.xitacb.setSizePolicy(sizePolicy4)
        self.xitacb.setDecimals(3)
        self.xitacb.setMaximum(999999.000000000000000)
        self.xitacb.setValue(0.375000000000000)

        self.horizontalLayout_25.addWidget(self.xitacb)


        self.verticalLayout_6.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        sizePolicy4.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy4)

        self.horizontalLayout_26.addWidget(self.label_24)

        self.Ksat = QDoubleSpinBox(self.groupBox_3)
        self.Ksat.setObjectName(u"Ksat")
        sizePolicy4.setHeightForWidth(self.Ksat.sizePolicy().hasHeightForWidth())
        self.Ksat.setSizePolicy(sizePolicy4)
        self.Ksat.setMaximum(999999.000000000000000)
        self.Ksat.setValue(178.569999999999993)

        self.horizontalLayout_26.addWidget(self.Ksat)


        self.verticalLayout_6.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        sizePolicy4.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy4)

        self.horizontalLayout_27.addWidget(self.label_25)

        self.HCO = QDoubleSpinBox(self.groupBox_3)
        self.HCO.setObjectName(u"HCO")
        sizePolicy4.setHeightForWidth(self.HCO.sizePolicy().hasHeightForWidth())
        self.HCO.setSizePolicy(sizePolicy4)
        self.HCO.setDecimals(4)
        self.HCO.setMaximum(999999.000000000000000)
        self.HCO.setValue(4.806500000000000)

        self.horizontalLayout_27.addWidget(self.HCO)


        self.verticalLayout_6.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")
        sizePolicy4.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy4)

        self.horizontalLayout_28.addWidget(self.label_26)

        self.psi2 = QDoubleSpinBox(self.groupBox_3)
        self.psi2.setObjectName(u"psi2")
        sizePolicy4.setHeightForWidth(self.psi2.sizePolicy().hasHeightForWidth())
        self.psi2.setSizePolicy(sizePolicy4)
        self.psi2.setDecimals(4)
        self.psi2.setMaximum(999999.000000000000000)
        self.psi2.setValue(320.286900000000003)

        self.horizontalLayout_28.addWidget(self.psi2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")
        sizePolicy4.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy4)

        self.horizontalLayout_22.addWidget(self.label_20)

        self.C3D = QDoubleSpinBox(self.groupBox_3)
        self.C3D.setObjectName(u"C3D")
        sizePolicy4.setHeightForWidth(self.C3D.sizePolicy().hasHeightForWidth())
        self.C3D.setSizePolicy(sizePolicy4)
        self.C3D.setDecimals(4)
        self.C3D.setMaximum(999999.000000000000000)
        self.C3D.setValue(6.607700000000000)

        self.horizontalLayout_22.addWidget(self.C3D)


        self.verticalLayout_6.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        sizePolicy4.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy4)

        self.horizontalLayout_23.addWidget(self.label_21)

        self.eta3D = QDoubleSpinBox(self.groupBox_3)
        self.eta3D.setObjectName(u"eta3D")
        sizePolicy4.setHeightForWidth(self.eta3D.sizePolicy().hasHeightForWidth())
        self.eta3D.setSizePolicy(sizePolicy4)
        self.eta3D.setMaximum(999999.000000000000000)
        self.eta3D.setValue(1.000000000000000)

        self.horizontalLayout_23.addWidget(self.eta3D)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_29.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        sizePolicy4.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy4)

        self.horizontalLayout_24.addWidget(self.label_22)

        self.C1 = QDoubleSpinBox(self.groupBox_3)
        self.C1.setObjectName(u"C1")
        sizePolicy4.setHeightForWidth(self.C1.sizePolicy().hasHeightForWidth())
        self.C1.setSizePolicy(sizePolicy4)
        self.C1.setDecimals(4)
        self.C1.setMaximum(2.000000000000000)
        self.C1.setSingleStep(1.000000000000000)
        self.C1.setStepType(QAbstractSpinBox.DefaultStepType)
        self.C1.setValue(1.167500000000000)

        self.horizontalLayout_24.addWidget(self.C1)


        self.verticalLayout_7.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_33.addLayout(self.verticalLayout_7)


        self.verticalLayout_9.addWidget(self.groupBox_3)


        self.horizontalLayout_34.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_10)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)

        self.horizontalLayout_13.addWidget(self.label_13)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.green_roof_sim_curve = QGraphicsView(self.centralwidget)
        self.green_roof_sim_curve.setObjectName(u"green_roof_sim_curve")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.green_roof_sim_curve.sizePolicy().hasHeightForWidth())
        self.green_roof_sim_curve.setSizePolicy(sizePolicy6)

        self.verticalLayout_2.addWidget(self.green_roof_sim_curve)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout_34.addLayout(self.verticalLayout_2)

        self.horizontalLayout_34.setStretch(0, 3)
        self.horizontalLayout_34.setStretch(1, 1)
        self.horizontalLayout_34.setStretch(2, 15)
        self.horizontalLayout_34.setStretch(3, 1)
        self.horizontalLayout_34.setStretch(4, 8)

        self.horizontalLayout_35.addLayout(self.horizontalLayout_34)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_5 = QMenu(self.menu)
        self.menu_5.setObjectName(u"menu_5")
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
        self.menu_5.addAction(self.action_open_observed_file)
        self.menu_5.addAction(self.action_open_weather_file)
        self.menu_3.addAction(self.menusimulate.menuAction())
        self.menu_3.addAction(self.menusimulate_validate.menuAction())
        self.menusimulate.addAction(self.action_sim_green_roof)
        self.menusimulate_validate.addAction(self.action_sim_and_val_green_roof)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sponge City", None))
        self.action_openfile.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_sim_green_roof.setText(QCoreApplication.translate("MainWindow", u"\u7eff\u8272\u5c4b\u9876", None))
        self.action_open_observed_file.setText(QCoreApplication.translate("MainWindow", u"\u89c2\u6d4b\u6587\u4ef6", None))
        self.action_open_weather_file.setText(QCoreApplication.translate("MainWindow", u"\u6c14\u8c61\u6587\u4ef6", None))
        self.action_sim_and_val_green_roof.setText(QCoreApplication.translate("MainWindow", u"\u7eff\u8272\u5c4b\u9876", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u503c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u79ef\u7d2f\u6e17\u900f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u84c4\u6c34\u5c42\u6c34\u6df1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u571f\u5c42\u542b\u6c34\u91cf", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5730\u8868\u84c4\u6c34", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u53c2\u6570", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7eff\u8272\u5c4b\u9876\u957f\u5ea6", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u7eff\u8272\u5c4b\u9876\u5bbd\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6ea2\u6d41\u5c42\u6df1\u5ea6", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u8d28\u5c42\u6df1\u5ea6", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u84c4\u6c34\u5c42\u6df1\u5ea6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u84c4\u6c34\u5c42\u6700\u5c0f<br/>\u53ef\u51fa\u6d41\u6df1\u5ea6</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u9699\u7387", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e38\u6570", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u8868\u9762\u53cd\u5c04\u7387", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"0\u2103\u6c34\u7684\u9971\u548c\u84b8\u6c14\u538b", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u7530\u95f4\u6301\u6c34\u91cf", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u51cb\u840e\u70b9", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u5c42\u5b54\u9699\u7387", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u783e\u77f3\u5c42\u5b54\u9699\u7387", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u690d\u7269\u84b8\u817e\u53d7\u9650\u9608\u503c", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u5c42\u57fa\u8d28\u6d41\u9971\u548c\u5bfc\u6c34\u7387", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u6c34\u8870\u51cf\u5e38\u6570", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u5c42\u5438\u529b\u6c34\u5934", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5b54\u6d41\u7cfb\u6570", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u5b54\u6d41\u6307\u6570", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u783e\u77f3\u5c42\u6c34\u5206\u84b8\u53d1\u7684\u7a7a\u6c14\u52a8\u529b\u5b66\u5bfc\u7387\uff081e-8\uff09", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">\u51fa\u6d41\u4eff\u771f\u7ed3\u679c</span></p></body></html>", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u7eff\u8272\u5c4b\u9876", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.menusimulate.setTitle(QCoreApplication.translate("MainWindow", u"\u4eff\u771f", None))
        self.menusimulate_validate.setTitle(QCoreApplication.translate("MainWindow", u"\u4eff\u771f\u548c\u9a8c\u8bc1", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

