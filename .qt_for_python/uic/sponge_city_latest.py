# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sponge_city_latest.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QToolBar,
    QTreeView, QVBoxLayout, QWidget)

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
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.treeView)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.horizontalLayout_30.addWidget(self.label_4)

        self.d3_0 = QDoubleSpinBox(self.tab)
        self.d3_0.setObjectName(u"d3_0")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.d3_0.sizePolicy().hasHeightForWidth())
        self.d3_0.setSizePolicy(sizePolicy4)
        self.d3_0.setMaximum(9999.000000000000000)
        self.d3_0.setValue(300.000000000000000)

        self.horizontalLayout_30.addWidget(self.d3_0)

        self.horizontalLayout_30.setStretch(0, 1)
        self.horizontalLayout_30.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.D3 = QDoubleSpinBox(self.tab)
        self.D3.setObjectName(u"D3")
        sizePolicy3.setHeightForWidth(self.D3.sizePolicy().hasHeightForWidth())
        self.D3.setSizePolicy(sizePolicy3)
        self.D3.setMaximum(99999.000000000000000)
        self.D3.setValue(300.000000000000000)

        self.horizontalLayout_7.addWidget(self.D3)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)

        self.horizontalLayout_31.addWidget(self.label_11)

        self.D3D = QDoubleSpinBox(self.tab)
        self.D3D.setObjectName(u"D3D")
        sizePolicy3.setHeightForWidth(self.D3D.sizePolicy().hasHeightForWidth())
        self.D3D.setSizePolicy(sizePolicy3)
        self.D3D.setMaximum(99999.000000000000000)
        self.D3D.setValue(280.000000000000000)

        self.horizontalLayout_31.addWidget(self.D3D)


        self.verticalLayout_8.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_19 = QLabel(self.tab)
        self.label_19.setObjectName(u"label_19")
        sizePolicy3.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy3)

        self.horizontalLayout_32.addWidget(self.label_19)

        self.phi3 = QDoubleSpinBox(self.tab)
        self.phi3.setObjectName(u"phi3")
        sizePolicy3.setHeightForWidth(self.phi3.sizePolicy().hasHeightForWidth())
        self.phi3.setSizePolicy(sizePolicy3)
        self.phi3.setDecimals(4)
        self.phi3.setMaximum(999999.000000000000000)
        self.phi3.setValue(0.736900000000000)

        self.horizontalLayout_32.addWidget(self.phi3)

        self.horizontalLayout_32.setStretch(0, 1)
        self.horizontalLayout_32.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_20 = QLabel(self.tab)
        self.label_20.setObjectName(u"label_20")
        sizePolicy3.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy3)

        self.horizontalLayout_34.addWidget(self.label_20)

        self.C3D = QDoubleSpinBox(self.tab)
        self.C3D.setObjectName(u"C3D")
        sizePolicy3.setHeightForWidth(self.C3D.sizePolicy().hasHeightForWidth())
        self.C3D.setSizePolicy(sizePolicy3)
        self.C3D.setDecimals(4)
        self.C3D.setMaximum(999999.000000000000000)
        self.C3D.setValue(6.607700000000000)

        self.horizontalLayout_34.addWidget(self.C3D)


        self.verticalLayout_8.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_21 = QLabel(self.tab)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)

        self.horizontalLayout_35.addWidget(self.label_21)

        self.eta3D = QDoubleSpinBox(self.tab)
        self.eta3D.setObjectName(u"eta3D")
        sizePolicy3.setHeightForWidth(self.eta3D.sizePolicy().hasHeightForWidth())
        self.eta3D.setSizePolicy(sizePolicy3)
        self.eta3D.setMaximum(999999.000000000000000)
        self.eta3D.setValue(1.000000000000000)

        self.horizontalLayout_35.addWidget(self.eta3D)


        self.verticalLayout_8.addLayout(self.horizontalLayout_35)


        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_36.addWidget(self.label_3)

        self.xita2_0 = QDoubleSpinBox(self.tab_2)
        self.xita2_0.setObjectName(u"xita2_0")
        sizePolicy4.setHeightForWidth(self.xita2_0.sizePolicy().hasHeightForWidth())
        self.xita2_0.setSizePolicy(sizePolicy4)
        self.xita2_0.setMaximum(1.000000000000000)
        self.xita2_0.setValue(0.570000000000000)

        self.horizontalLayout_36.addWidget(self.xita2_0)

        self.horizontalLayout_36.setStretch(0, 1)
        self.horizontalLayout_36.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)

        self.horizontalLayout_37.addWidget(self.label_9)

        self.D2 = QDoubleSpinBox(self.tab_2)
        self.D2.setObjectName(u"D2")
        sizePolicy3.setHeightForWidth(self.D2.sizePolicy().hasHeightForWidth())
        self.D2.setSizePolicy(sizePolicy3)
        self.D2.setMaximum(99999.000000000000000)
        self.D2.setValue(100.000000000000000)

        self.horizontalLayout_37.addWidget(self.D2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)

        self.horizontalLayout_38.addWidget(self.label_16)

        self.xitaFC = QDoubleSpinBox(self.tab_2)
        self.xitaFC.setObjectName(u"xitaFC")
        sizePolicy3.setHeightForWidth(self.xitaFC.sizePolicy().hasHeightForWidth())
        self.xitaFC.setSizePolicy(sizePolicy3)
        self.xitaFC.setMaximum(999999.000000000000000)
        self.xitaFC.setValue(0.280000000000000)

        self.horizontalLayout_38.addWidget(self.xitaFC)


        self.verticalLayout_9.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)

        self.horizontalLayout_39.addWidget(self.label_17)

        self.xitaWP = QDoubleSpinBox(self.tab_2)
        self.xitaWP.setObjectName(u"xitaWP")
        sizePolicy3.setHeightForWidth(self.xitaWP.sizePolicy().hasHeightForWidth())
        self.xitaWP.setSizePolicy(sizePolicy3)
        self.xitaWP.setDecimals(3)
        self.xitaWP.setMaximum(999999.000000000000000)
        self.xitaWP.setValue(0.225000000000000)

        self.horizontalLayout_39.addWidget(self.xitaWP)


        self.verticalLayout_9.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)

        self.horizontalLayout_40.addWidget(self.label_18)

        self.phi2 = QDoubleSpinBox(self.tab_2)
        self.phi2.setObjectName(u"phi2")
        sizePolicy3.setHeightForWidth(self.phi2.sizePolicy().hasHeightForWidth())
        self.phi2.setSizePolicy(sizePolicy3)
        self.phi2.setMaximum(999999.000000000000000)
        self.phi2.setValue(0.500000000000000)

        self.horizontalLayout_40.addWidget(self.phi2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_23 = QLabel(self.tab_2)
        self.label_23.setObjectName(u"label_23")
        sizePolicy3.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy3)

        self.horizontalLayout_41.addWidget(self.label_23)

        self.xitacb = QDoubleSpinBox(self.tab_2)
        self.xitacb.setObjectName(u"xitacb")
        sizePolicy3.setHeightForWidth(self.xitacb.sizePolicy().hasHeightForWidth())
        self.xitacb.setSizePolicy(sizePolicy3)
        self.xitacb.setDecimals(3)
        self.xitacb.setMaximum(999999.000000000000000)
        self.xitacb.setValue(0.375000000000000)

        self.horizontalLayout_41.addWidget(self.xitacb)


        self.verticalLayout_9.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_24 = QLabel(self.tab_2)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)

        self.horizontalLayout_42.addWidget(self.label_24)

        self.Ksat = QDoubleSpinBox(self.tab_2)
        self.Ksat.setObjectName(u"Ksat")
        sizePolicy3.setHeightForWidth(self.Ksat.sizePolicy().hasHeightForWidth())
        self.Ksat.setSizePolicy(sizePolicy3)
        self.Ksat.setMaximum(999999.000000000000000)
        self.Ksat.setValue(178.569999999999993)

        self.horizontalLayout_42.addWidget(self.Ksat)


        self.verticalLayout_9.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_25 = QLabel(self.tab_2)
        self.label_25.setObjectName(u"label_25")
        sizePolicy3.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy3)

        self.horizontalLayout_43.addWidget(self.label_25)

        self.HCO = QDoubleSpinBox(self.tab_2)
        self.HCO.setObjectName(u"HCO")
        sizePolicy3.setHeightForWidth(self.HCO.sizePolicy().hasHeightForWidth())
        self.HCO.setSizePolicy(sizePolicy3)
        self.HCO.setDecimals(4)
        self.HCO.setMaximum(999999.000000000000000)
        self.HCO.setValue(4.806500000000000)

        self.horizontalLayout_43.addWidget(self.HCO)


        self.verticalLayout_9.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_26 = QLabel(self.tab_2)
        self.label_26.setObjectName(u"label_26")
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)

        self.horizontalLayout_44.addWidget(self.label_26)

        self.psi2 = QDoubleSpinBox(self.tab_2)
        self.psi2.setObjectName(u"psi2")
        sizePolicy3.setHeightForWidth(self.psi2.sizePolicy().hasHeightForWidth())
        self.psi2.setSizePolicy(sizePolicy3)
        self.psi2.setDecimals(4)
        self.psi2.setMaximum(999999.000000000000000)
        self.psi2.setValue(320.286900000000003)

        self.horizontalLayout_44.addWidget(self.psi2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_44)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.D1 = QDoubleSpinBox(self.tab_3)
        self.D1.setObjectName(u"D1")
        sizePolicy3.setHeightForWidth(self.D1.sizePolicy().hasHeightForWidth())
        self.D1.setSizePolicy(sizePolicy3)
        self.D1.setMaximum(99999.000000000000000)
        self.D1.setValue(30.000000000000000)

        self.gridLayout.addWidget(self.D1, 0, 1, 1, 1)

        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.phi1 = QDoubleSpinBox(self.tab_3)
        self.phi1.setObjectName(u"phi1")
        sizePolicy3.setHeightForWidth(self.phi1.sizePolicy().hasHeightForWidth())
        self.phi1.setSizePolicy(sizePolicy3)
        self.phi1.setMaximum(99999.000000000000000)
        self.phi1.setValue(0.950000000000000)

        self.gridLayout.addWidget(self.phi1, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_greenroof_ok = QPushButton(self.centralwidget)
        self.pushButton_greenroof_ok.setObjectName(u"pushButton_greenroof_ok")

        self.horizontalLayout.addWidget(self.pushButton_greenroof_ok)

        self.pushButton_greenroof_cancal = QPushButton(self.centralwidget)
        self.pushButton_greenroof_cancal.setObjectName(u"pushButton_greenroof_cancal")

        self.horizontalLayout.addWidget(self.pushButton_greenroof_cancal)

        self.pushButton_greenroof_help = QPushButton(self.centralwidget)
        self.pushButton_greenroof_help.setObjectName(u"pushButton_greenroof_help")

        self.horizontalLayout.addWidget(self.pushButton_greenroof_help)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 10)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)

        self.horizontalLayout_13.addWidget(self.label_13)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.green_roof_sim_curve = QGraphicsView(self.centralwidget)
        self.green_roof_sim_curve.setObjectName(u"green_roof_sim_curve")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.green_roof_sim_curve.sizePolicy().hasHeightForWidth())
        self.green_roof_sim_curve.setSizePolicy(sizePolicy5)

        self.verticalLayout_2.addWidget(self.green_roof_sim_curve)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy5.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy5)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 3)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sponge City", None))
        self.action_openfile.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_sim_green_roof.setText(QCoreApplication.translate("MainWindow", u"\u7eff\u8272\u5c4b\u9876", None))
        self.action_open_observed_file.setText(QCoreApplication.translate("MainWindow", u"\u89c2\u6d4b\u6587\u4ef6", None))
        self.action_open_weather_file.setText(QCoreApplication.translate("MainWindow", u"\u6c14\u8c61\u6587\u4ef6", None))
        self.action_sim_and_val_green_roof.setText(QCoreApplication.translate("MainWindow", u"\u7eff\u8272\u5c4b\u9876", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u84c4\u6c34\u5c42\u6c34\u6df1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u84c4\u6c34\u5c42\u6df1\u5ea6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u84c4\u6c34\u5c42\u6700\u5c0f<br/>\u53ef\u51fa\u6d41\u6df1\u5ea6</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u783e\u77f3\u5c42\u5b54\u9699\u7387", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5b54\u6d41\u7cfb\u6570", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u5b54\u6d41\u6307\u6570", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u84c4\u6c34\u5c42", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u571f\u5c42\u542b\u6c34\u91cf", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u8d28\u5c42\u6df1\u5ea6", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u7530\u95f4\u6301\u6c34\u91cf", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u51cb\u840e\u70b9", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u5c42\u5b54\u9699\u7387", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u4e34\u754c\u542b\u6c34\u91cf", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u9971\u548c\u5bfc\u6c34\u7387", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u8870\u51cf\u5e38\u6570", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u5438\u529b\u6c34\u5934", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u5c42", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6ea2\u6d41\u5c42\u6df1\u5ea6", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u9699\u7387", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u8868\u5c42", None))
        self.pushButton_greenroof_ok.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.pushButton_greenroof_cancal.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.pushButton_greenroof_help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
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

