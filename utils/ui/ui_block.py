# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'block.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Block(object):
    def setupUi(self, Block):
        if not Block.objectName():
            Block.setObjectName(u"Block")
        Block.resize(450, 457)
        self.verticalLayout_29 = QVBoxLayout(Block)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.tabWidget = QTabWidget(Block)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_6 = QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.comboBox_landuse = QComboBox(self.tab)
        self.comboBox_landuse.addItem(u"\u8bf7\u9009\u62e9")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.addItem("")
        self.comboBox_landuse.setObjectName(u"comboBox_landuse")

        self.horizontalLayout_5.addWidget(self.comboBox_landuse)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 6)

        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.groupBox_Bmax = QGroupBox(self.tab)
        self.groupBox_Bmax.setObjectName(u"groupBox_Bmax")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_Bmax)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Bmax_SS = QLabel(self.groupBox_Bmax)
        self.label_Bmax_SS.setObjectName(u"label_Bmax_SS")

        self.verticalLayout.addWidget(self.label_Bmax_SS)

        self.doubleSpinBox_Bmax_SS = QDoubleSpinBox(self.groupBox_Bmax)
        self.doubleSpinBox_Bmax_SS.setObjectName(u"doubleSpinBox_Bmax_SS")

        self.verticalLayout.addWidget(self.doubleSpinBox_Bmax_SS)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_Bmax_COD = QLabel(self.groupBox_Bmax)
        self.label_Bmax_COD.setObjectName(u"label_Bmax_COD")

        self.verticalLayout_2.addWidget(self.label_Bmax_COD)

        self.doubleSpinBox_Bmax_COD = QDoubleSpinBox(self.groupBox_Bmax)
        self.doubleSpinBox_Bmax_COD.setObjectName(u"doubleSpinBox_Bmax_COD")

        self.verticalLayout_2.addWidget(self.doubleSpinBox_Bmax_COD)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_Bmax_TP = QLabel(self.groupBox_Bmax)
        self.label_Bmax_TP.setObjectName(u"label_Bmax_TP")

        self.verticalLayout_3.addWidget(self.label_Bmax_TP)

        self.doubleSpinBox_Bmax_TP = QDoubleSpinBox(self.groupBox_Bmax)
        self.doubleSpinBox_Bmax_TP.setObjectName(u"doubleSpinBox_Bmax_TP")

        self.verticalLayout_3.addWidget(self.doubleSpinBox_Bmax_TP)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_Bmax_TN = QLabel(self.groupBox_Bmax)
        self.label_Bmax_TN.setObjectName(u"label_Bmax_TN")

        self.verticalLayout_4.addWidget(self.label_Bmax_TN)

        self.doubleSpinBox_Bmax_TN = QDoubleSpinBox(self.groupBox_Bmax)
        self.doubleSpinBox_Bmax_TN.setObjectName(u"doubleSpinBox_Bmax_TN")

        self.verticalLayout_4.addWidget(self.doubleSpinBox_Bmax_TN)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_Bmax_NH3N = QLabel(self.groupBox_Bmax)
        self.label_Bmax_NH3N.setObjectName(u"label_Bmax_NH3N")

        self.verticalLayout_5.addWidget(self.label_Bmax_NH3N)

        self.doubleSpinBox_Bmax_NH3N = QDoubleSpinBox(self.groupBox_Bmax)
        self.doubleSpinBox_Bmax_NH3N.setObjectName(u"doubleSpinBox_Bmax_NH3N")

        self.verticalLayout_5.addWidget(self.doubleSpinBox_Bmax_NH3N)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_11.addWidget(self.groupBox_Bmax)

        self.groupBox_bt = QGroupBox(self.tab)
        self.groupBox_bt.setObjectName(u"groupBox_bt")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_bt)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_bt_SS = QLabel(self.groupBox_bt)
        self.label_bt_SS.setObjectName(u"label_bt_SS")

        self.verticalLayout_6.addWidget(self.label_bt_SS)

        self.doubleSpinBox_bt_SS = QDoubleSpinBox(self.groupBox_bt)
        self.doubleSpinBox_bt_SS.setObjectName(u"doubleSpinBox_bt_SS")

        self.verticalLayout_6.addWidget(self.doubleSpinBox_bt_SS)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_bt_COD = QLabel(self.groupBox_bt)
        self.label_bt_COD.setObjectName(u"label_bt_COD")

        self.verticalLayout_7.addWidget(self.label_bt_COD)

        self.doubleSpinBox_bt_COD = QDoubleSpinBox(self.groupBox_bt)
        self.doubleSpinBox_bt_COD.setObjectName(u"doubleSpinBox_bt_COD")

        self.verticalLayout_7.addWidget(self.doubleSpinBox_bt_COD)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_bt_TP = QLabel(self.groupBox_bt)
        self.label_bt_TP.setObjectName(u"label_bt_TP")

        self.verticalLayout_8.addWidget(self.label_bt_TP)

        self.doubleSpinBox_bt_TP = QDoubleSpinBox(self.groupBox_bt)
        self.doubleSpinBox_bt_TP.setObjectName(u"doubleSpinBox_bt_TP")

        self.verticalLayout_8.addWidget(self.doubleSpinBox_bt_TP)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_bt_TN = QLabel(self.groupBox_bt)
        self.label_bt_TN.setObjectName(u"label_bt_TN")

        self.verticalLayout_9.addWidget(self.label_bt_TN)

        self.doubleSpinBox_bt_TN = QDoubleSpinBox(self.groupBox_bt)
        self.doubleSpinBox_bt_TN.setObjectName(u"doubleSpinBox_bt_TN")

        self.verticalLayout_9.addWidget(self.doubleSpinBox_bt_TN)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_bt_NH3N = QLabel(self.groupBox_bt)
        self.label_bt_NH3N.setObjectName(u"label_bt_NH3N")

        self.verticalLayout_10.addWidget(self.label_bt_NH3N)

        self.doubleSpinBox_bt_NH3N = QDoubleSpinBox(self.groupBox_bt)
        self.doubleSpinBox_bt_NH3N.setObjectName(u"doubleSpinBox_bt_NH3N")

        self.verticalLayout_10.addWidget(self.doubleSpinBox_bt_NH3N)


        self.horizontalLayout_2.addLayout(self.verticalLayout_10)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_11.addWidget(self.groupBox_bt)


        self.verticalLayout_28.addLayout(self.verticalLayout_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_28)

        self.tabWidget.addTab(self.tab, "")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout_30 = QVBoxLayout(self.tab1)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.comboBox_underlyingsurface = QComboBox(self.tab1)
        self.comboBox_underlyingsurface.addItem("")
        self.comboBox_underlyingsurface.addItem("")
        self.comboBox_underlyingsurface.addItem("")
        self.comboBox_underlyingsurface.addItem("")
        self.comboBox_underlyingsurface.addItem("")
        self.comboBox_underlyingsurface.addItem("")
        self.comboBox_underlyingsurface.setObjectName(u"comboBox_underlyingsurface")

        self.horizontalLayout_9.addWidget(self.comboBox_underlyingsurface)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 5)

        self.verticalLayout_27.addLayout(self.horizontalLayout_9)

        self.groupBox_C1 = QGroupBox(self.tab1)
        self.groupBox_C1.setObjectName(u"groupBox_C1")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_C1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_C1_SS = QLabel(self.groupBox_C1)
        self.label_C1_SS.setObjectName(u"label_C1_SS")

        self.verticalLayout_12.addWidget(self.label_C1_SS)

        self.doubleSpinBox_C1_SS = QDoubleSpinBox(self.groupBox_C1)
        self.doubleSpinBox_C1_SS.setObjectName(u"doubleSpinBox_C1_SS")

        self.verticalLayout_12.addWidget(self.doubleSpinBox_C1_SS)


        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_C1_COD = QLabel(self.groupBox_C1)
        self.label_C1_COD.setObjectName(u"label_C1_COD")

        self.verticalLayout_13.addWidget(self.label_C1_COD)

        self.doubleSpinBox_C1_COD = QDoubleSpinBox(self.groupBox_C1)
        self.doubleSpinBox_C1_COD.setObjectName(u"doubleSpinBox_C1_COD")

        self.verticalLayout_13.addWidget(self.doubleSpinBox_C1_COD)


        self.horizontalLayout_7.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_C1_TP = QLabel(self.groupBox_C1)
        self.label_C1_TP.setObjectName(u"label_C1_TP")

        self.verticalLayout_14.addWidget(self.label_C1_TP)

        self.doubleSpinBox_C1_TP = QDoubleSpinBox(self.groupBox_C1)
        self.doubleSpinBox_C1_TP.setObjectName(u"doubleSpinBox_C1_TP")

        self.verticalLayout_14.addWidget(self.doubleSpinBox_C1_TP)


        self.horizontalLayout_7.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_C1_TN = QLabel(self.groupBox_C1)
        self.label_C1_TN.setObjectName(u"label_C1_TN")

        self.verticalLayout_15.addWidget(self.label_C1_TN)

        self.doubleSpinBox_C1_TN = QDoubleSpinBox(self.groupBox_C1)
        self.doubleSpinBox_C1_TN.setObjectName(u"doubleSpinBox_C1_TN")

        self.verticalLayout_15.addWidget(self.doubleSpinBox_C1_TN)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_C1_NH3N = QLabel(self.groupBox_C1)
        self.label_C1_NH3N.setObjectName(u"label_C1_NH3N")

        self.verticalLayout_16.addWidget(self.label_C1_NH3N)

        self.doubleSpinBox_C1_NH3N = QDoubleSpinBox(self.groupBox_C1)
        self.doubleSpinBox_C1_NH3N.setObjectName(u"doubleSpinBox_C1_NH3N")

        self.verticalLayout_16.addWidget(self.doubleSpinBox_C1_NH3N)


        self.horizontalLayout_7.addLayout(self.verticalLayout_16)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)


        self.verticalLayout_27.addWidget(self.groupBox_C1)

        self.groupBox_C2 = QGroupBox(self.tab1)
        self.groupBox_C2.setObjectName(u"groupBox_C2")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_C2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_C2_SS = QLabel(self.groupBox_C2)
        self.label_C2_SS.setObjectName(u"label_C2_SS")

        self.verticalLayout_17.addWidget(self.label_C2_SS)

        self.doubleSpinBox_C2_SS = QDoubleSpinBox(self.groupBox_C2)
        self.doubleSpinBox_C2_SS.setObjectName(u"doubleSpinBox_C2_SS")

        self.verticalLayout_17.addWidget(self.doubleSpinBox_C2_SS)


        self.horizontalLayout_8.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_C2_COD = QLabel(self.groupBox_C2)
        self.label_C2_COD.setObjectName(u"label_C2_COD")

        self.verticalLayout_18.addWidget(self.label_C2_COD)

        self.doubleSpinBox_C2_COD = QDoubleSpinBox(self.groupBox_C2)
        self.doubleSpinBox_C2_COD.setObjectName(u"doubleSpinBox_C2_COD")

        self.verticalLayout_18.addWidget(self.doubleSpinBox_C2_COD)


        self.horizontalLayout_8.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_C2_TP = QLabel(self.groupBox_C2)
        self.label_C2_TP.setObjectName(u"label_C2_TP")

        self.verticalLayout_19.addWidget(self.label_C2_TP)

        self.doubleSpinBox_C2_TP = QDoubleSpinBox(self.groupBox_C2)
        self.doubleSpinBox_C2_TP.setObjectName(u"doubleSpinBox_C2_TP")

        self.verticalLayout_19.addWidget(self.doubleSpinBox_C2_TP)


        self.horizontalLayout_8.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_C2_TN = QLabel(self.groupBox_C2)
        self.label_C2_TN.setObjectName(u"label_C2_TN")

        self.verticalLayout_20.addWidget(self.label_C2_TN)

        self.doubleSpinBox_C2_TN = QDoubleSpinBox(self.groupBox_C2)
        self.doubleSpinBox_C2_TN.setObjectName(u"doubleSpinBox_C2_TN")

        self.verticalLayout_20.addWidget(self.doubleSpinBox_C2_TN)


        self.horizontalLayout_8.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_C2_NH3N = QLabel(self.groupBox_C2)
        self.label_C2_NH3N.setObjectName(u"label_C2_NH3N")

        self.verticalLayout_21.addWidget(self.label_C2_NH3N)

        self.doubleSpinBox_C2_NH3N = QDoubleSpinBox(self.groupBox_C2)
        self.doubleSpinBox_C2_NH3N.setObjectName(u"doubleSpinBox_C2_NH3N")

        self.verticalLayout_21.addWidget(self.doubleSpinBox_C2_NH3N)


        self.horizontalLayout_8.addLayout(self.verticalLayout_21)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)


        self.verticalLayout_27.addWidget(self.groupBox_C2)

        self.groupBox_EMC = QGroupBox(self.tab1)
        self.groupBox_EMC.setObjectName(u"groupBox_EMC")
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_EMC)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_EMC_SS = QLabel(self.groupBox_EMC)
        self.label_EMC_SS.setObjectName(u"label_EMC_SS")

        self.verticalLayout_22.addWidget(self.label_EMC_SS)

        self.doubleSpinBox_EMC_SS = QDoubleSpinBox(self.groupBox_EMC)
        self.doubleSpinBox_EMC_SS.setObjectName(u"doubleSpinBox_EMC_SS")

        self.verticalLayout_22.addWidget(self.doubleSpinBox_EMC_SS)


        self.horizontalLayout_12.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_EMC_COD = QLabel(self.groupBox_EMC)
        self.label_EMC_COD.setObjectName(u"label_EMC_COD")

        self.verticalLayout_23.addWidget(self.label_EMC_COD)

        self.doubleSpinBox_EMC_COD = QDoubleSpinBox(self.groupBox_EMC)
        self.doubleSpinBox_EMC_COD.setObjectName(u"doubleSpinBox_EMC_COD")

        self.verticalLayout_23.addWidget(self.doubleSpinBox_EMC_COD)


        self.horizontalLayout_12.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_EMC_TP = QLabel(self.groupBox_EMC)
        self.label_EMC_TP.setObjectName(u"label_EMC_TP")

        self.verticalLayout_24.addWidget(self.label_EMC_TP)

        self.doubleSpinBox_EMC_TP = QDoubleSpinBox(self.groupBox_EMC)
        self.doubleSpinBox_EMC_TP.setObjectName(u"doubleSpinBox_EMC_TP")

        self.verticalLayout_24.addWidget(self.doubleSpinBox_EMC_TP)


        self.horizontalLayout_12.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_EMC_TN = QLabel(self.groupBox_EMC)
        self.label_EMC_TN.setObjectName(u"label_EMC_TN")

        self.verticalLayout_25.addWidget(self.label_EMC_TN)

        self.doubleSpinBox_EMC_TN = QDoubleSpinBox(self.groupBox_EMC)
        self.doubleSpinBox_EMC_TN.setObjectName(u"doubleSpinBox_EMC_TN")

        self.verticalLayout_25.addWidget(self.doubleSpinBox_EMC_TN)


        self.horizontalLayout_12.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_EMC_NH3N = QLabel(self.groupBox_EMC)
        self.label_EMC_NH3N.setObjectName(u"label_EMC_NH3N")

        self.verticalLayout_26.addWidget(self.label_EMC_NH3N)

        self.doubleSpinBox_EMC_NH3N = QDoubleSpinBox(self.groupBox_EMC)
        self.doubleSpinBox_EMC_NH3N.setObjectName(u"doubleSpinBox_EMC_NH3N")

        self.verticalLayout_26.addWidget(self.doubleSpinBox_EMC_NH3N)


        self.horizontalLayout_12.addLayout(self.verticalLayout_26)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_12)


        self.verticalLayout_27.addWidget(self.groupBox_EMC)

        self.groupBox_other = QGroupBox(self.tab1)
        self.groupBox_other.setObjectName(u"groupBox_other")
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_other)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_max_init_loss = QLabel(self.groupBox_other)
        self.label_max_init_loss.setObjectName(u"label_max_init_loss")

        self.horizontalLayout_13.addWidget(self.label_max_init_loss)

        self.doubleSpinBox_max_init_loss = QDoubleSpinBox(self.groupBox_other)
        self.doubleSpinBox_max_init_loss.setObjectName(u"doubleSpinBox_max_init_loss")

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_max_init_loss)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_infiltration_rate = QLabel(self.groupBox_other)
        self.label_infiltration_rate.setObjectName(u"label_infiltration_rate")

        self.horizontalLayout_14.addWidget(self.label_infiltration_rate)

        self.doubleSpinBox_infiltration_rate = QDoubleSpinBox(self.groupBox_other)
        self.doubleSpinBox_infiltration_rate.setObjectName(u"doubleSpinBox_infiltration_rate")

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_infiltration_rate)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)


        self.verticalLayout_27.addWidget(self.groupBox_other)


        self.verticalLayout_30.addLayout(self.verticalLayout_27)

        self.tabWidget.addTab(self.tab1, "")

        self.verticalLayout_29.addWidget(self.tabWidget)

        self.buttonBox_block = QDialogButtonBox(Block)
        self.buttonBox_block.setObjectName(u"buttonBox_block")
        self.buttonBox_block.setOrientation(Qt.Horizontal)
        self.buttonBox_block.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_29.addWidget(self.buttonBox_block)


        self.retranslateUi(Block)
        self.buttonBox_block.accepted.connect(Block.accept)
        self.buttonBox_block.rejected.connect(Block.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Block)
    # setupUi

    def retranslateUi(self, Block):
        Block.setWindowTitle(QCoreApplication.translate("Block", u"\u9762\u6e90\u6591\u5757\u7c7b\u578b\u5b9a\u4e49", None))
        self.comboBox_landuse.setItemText(1, QCoreApplication.translate("Block", u"\u5c45\u4f4f\u7528\u5730", None))
        self.comboBox_landuse.setItemText(2, QCoreApplication.translate("Block", u"\u884c\u653f\u529e\u516c\u7528\u5730", None))
        self.comboBox_landuse.setItemText(3, QCoreApplication.translate("Block", u"\u5546\u4e1a\u91d1\u878d\u7528\u5730", None))
        self.comboBox_landuse.setItemText(4, QCoreApplication.translate("Block", u"\u6587\u5316\u5a31\u4e50\u7528\u5730", None))
        self.comboBox_landuse.setItemText(5, QCoreApplication.translate("Block", u"\u4f53\u80b2\u7528\u5730", None))
        self.comboBox_landuse.setItemText(6, QCoreApplication.translate("Block", u"\u533b\u7597\u536b\u751f\u7528\u5730", None))
        self.comboBox_landuse.setItemText(7, QCoreApplication.translate("Block", u"\u6559\u80b2\u79d1\u7814\u8bbe\u8ba1\u7528\u5730", None))
        self.comboBox_landuse.setItemText(8, QCoreApplication.translate("Block", u"\u6587\u7269\u53e4\u8ff9\u7528\u5730", None))
        self.comboBox_landuse.setItemText(9, QCoreApplication.translate("Block", u"\u5176\u4ed6\u516c\u5171\u8bbe\u65bd\u7528\u5730", None))
        self.comboBox_landuse.setItemText(10, QCoreApplication.translate("Block", u"\u6df7\u5408\u7528\u5730", None))
        self.comboBox_landuse.setItemText(11, QCoreApplication.translate("Block", u"\u4e00\u7c7b\u5de5\u4e1a\u7528\u5730", None))
        self.comboBox_landuse.setItemText(12, QCoreApplication.translate("Block", u"\u4e8c\u7c7b\u5de5\u4e1a\u7528\u5730", None))
        self.comboBox_landuse.setItemText(13, QCoreApplication.translate("Block", u"\u4ed3\u50a8\uff08\u7269\u6d41\uff09\u7528\u5730", None))
        self.comboBox_landuse.setItemText(14, QCoreApplication.translate("Block", u"\u5bf9\u5916\u4ea4\u901a\u7528\u5730", None))
        self.comboBox_landuse.setItemText(15, QCoreApplication.translate("Block", u"\u5e02\u653f\u8bbe\u65bd\u7528\u5730", None))
        self.comboBox_landuse.setItemText(16, QCoreApplication.translate("Block", u"\u516c\u5171\u7eff\u5730", None))
        self.comboBox_landuse.setItemText(17, QCoreApplication.translate("Block", u"\u9632\u62a4\u7eff\u5730", None))
        self.comboBox_landuse.setItemText(18, QCoreApplication.translate("Block", u"\u98ce\u666f\u7eff\u5730", None))
        self.comboBox_landuse.setItemText(19, QCoreApplication.translate("Block", u"\u9547\u5efa\u8bbe\u7528\u5730", None))
        self.comboBox_landuse.setItemText(20, QCoreApplication.translate("Block", u"\u53d1\u5c55\u5907\u7528\u5730", None))
        self.comboBox_landuse.setItemText(21, QCoreApplication.translate("Block", u"\u6c34\u57df", None))
        self.comboBox_landuse.setItemText(22, QCoreApplication.translate("Block", u"\u6e7f\u5730", None))
        self.comboBox_landuse.setItemText(23, QCoreApplication.translate("Block", u"\u7eff\u8272\u5f00\u655e\u7a7a\u95f4", None))

        self.groupBox_Bmax.setTitle(QCoreApplication.translate("Block", u"Bmax", None))
        self.label_Bmax_SS.setText(QCoreApplication.translate("Block", u"SS", None))
        self.label_Bmax_COD.setText(QCoreApplication.translate("Block", u"COD", None))
        self.label_Bmax_TP.setText(QCoreApplication.translate("Block", u"TP", None))
        self.label_Bmax_TN.setText(QCoreApplication.translate("Block", u"TN", None))
        self.label_Bmax_NH3N.setText(QCoreApplication.translate("Block", u"NH3N", None))
        self.groupBox_bt.setTitle(QCoreApplication.translate("Block", u"bt", None))
        self.label_bt_SS.setText(QCoreApplication.translate("Block", u"SS", None))
        self.label_bt_COD.setText(QCoreApplication.translate("Block", u"COD", None))
        self.label_bt_TP.setText(QCoreApplication.translate("Block", u"TP", None))
        self.label_bt_TN.setText(QCoreApplication.translate("Block", u"TN", None))
        self.label_bt_NH3N.setText(QCoreApplication.translate("Block", u"NH3N", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Block", u"\u571f\u5730\u5229\u7528\u7c7b\u578b", None))
        self.comboBox_underlyingsurface.setItemText(0, QCoreApplication.translate("Block", u"\u8bf7\u9009\u62e9", None))
        self.comboBox_underlyingsurface.setItemText(1, QCoreApplication.translate("Block", u"\u5c4b\u9876", None))
        self.comboBox_underlyingsurface.setItemText(2, QCoreApplication.translate("Block", u"\u9053\u8def", None))
        self.comboBox_underlyingsurface.setItemText(3, QCoreApplication.translate("Block", u"\u786c\u5730", None))
        self.comboBox_underlyingsurface.setItemText(4, QCoreApplication.translate("Block", u"\u7eff\u5730", None))
        self.comboBox_underlyingsurface.setItemText(5, QCoreApplication.translate("Block", u"\u6c34\u4f53", None))

        self.groupBox_C1.setTitle(QCoreApplication.translate("Block", u"C1", None))
        self.label_C1_SS.setText(QCoreApplication.translate("Block", u"SS", None))
        self.label_C1_COD.setText(QCoreApplication.translate("Block", u"COD", None))
        self.label_C1_TP.setText(QCoreApplication.translate("Block", u"TP", None))
        self.label_C1_TN.setText(QCoreApplication.translate("Block", u"TN", None))
        self.label_C1_NH3N.setText(QCoreApplication.translate("Block", u"NH3N", None))
        self.groupBox_C2.setTitle(QCoreApplication.translate("Block", u"C2", None))
        self.label_C2_SS.setText(QCoreApplication.translate("Block", u"SS", None))
        self.label_C2_COD.setText(QCoreApplication.translate("Block", u"COD", None))
        self.label_C2_TP.setText(QCoreApplication.translate("Block", u"TP", None))
        self.label_C2_TN.setText(QCoreApplication.translate("Block", u"TN", None))
        self.label_C2_NH3N.setText(QCoreApplication.translate("Block", u"NH3N", None))
        self.groupBox_EMC.setTitle(QCoreApplication.translate("Block", u"EMC", None))
        self.label_EMC_SS.setText(QCoreApplication.translate("Block", u"SS", None))
        self.label_EMC_COD.setText(QCoreApplication.translate("Block", u"COD", None))
        self.label_EMC_TP.setText(QCoreApplication.translate("Block", u"TP", None))
        self.label_EMC_TN.setText(QCoreApplication.translate("Block", u"TN", None))
        self.label_EMC_NH3N.setText(QCoreApplication.translate("Block", u"NH3N", None))
        self.groupBox_other.setTitle(QCoreApplication.translate("Block", u"\u5176\u4ed6\u53c2\u6570", None))
        self.label_max_init_loss.setText(QCoreApplication.translate("Block", u"\u6700\u5927\u521d\u635f", None))
        self.label_infiltration_rate.setText(QCoreApplication.translate("Block", u"\u4e0b\u6e17\u7387", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("Block", u"\u4e0b\u57ab\u9762\u7c7b\u578b", None))
    # retranslateUi

