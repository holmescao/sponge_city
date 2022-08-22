# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'green_roof.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Greenroof(object):
    def setupUi(self, Greenroof):
        if not Greenroof.objectName():
            Greenroof.setObjectName(u"Greenroof")
        Greenroof.resize(402, 341)
        self.horizontalLayout = QHBoxLayout(Greenroof)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Greenroof)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_4 = QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_5 = QLabel(self.tab_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_33.addWidget(self.label_5)

        self.d3_0 = QDoubleSpinBox(self.tab_4)
        self.d3_0.setObjectName(u"d3_0")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.d3_0.sizePolicy().hasHeightForWidth())
        self.d3_0.setSizePolicy(sizePolicy1)
        self.d3_0.setMaximum(9999.000000000000000)
        self.d3_0.setValue(300.000000000000000)

        self.horizontalLayout_33.addWidget(self.d3_0)

        self.horizontalLayout_33.setStretch(0, 1)
        self.horizontalLayout_33.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_14)

        self.D3 = QDoubleSpinBox(self.tab_4)
        self.D3.setObjectName(u"D3")
        sizePolicy.setHeightForWidth(self.D3.sizePolicy().hasHeightForWidth())
        self.D3.setSizePolicy(sizePolicy)
        self.D3.setMaximum(99999.000000000000000)
        self.D3.setValue(300.000000000000000)

        self.horizontalLayout_8.addWidget(self.D3)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_15 = QLabel(self.tab_4)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)

        self.horizontalLayout_45.addWidget(self.label_15)

        self.D3D = QDoubleSpinBox(self.tab_4)
        self.D3D.setObjectName(u"D3D")
        sizePolicy.setHeightForWidth(self.D3D.sizePolicy().hasHeightForWidth())
        self.D3D.setSizePolicy(sizePolicy)
        self.D3D.setMaximum(99999.000000000000000)
        self.D3D.setValue(280.000000000000000)

        self.horizontalLayout_45.addWidget(self.D3D)


        self.verticalLayout_10.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_22 = QLabel(self.tab_4)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)

        self.horizontalLayout_46.addWidget(self.label_22)

        self.phi3 = QDoubleSpinBox(self.tab_4)
        self.phi3.setObjectName(u"phi3")
        sizePolicy.setHeightForWidth(self.phi3.sizePolicy().hasHeightForWidth())
        self.phi3.setSizePolicy(sizePolicy)
        self.phi3.setDecimals(4)
        self.phi3.setMaximum(999999.000000000000000)
        self.phi3.setValue(0.736900000000000)

        self.horizontalLayout_46.addWidget(self.phi3)

        self.horizontalLayout_46.setStretch(0, 1)
        self.horizontalLayout_46.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_27 = QLabel(self.tab_4)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)

        self.horizontalLayout_47.addWidget(self.label_27)

        self.C3D = QDoubleSpinBox(self.tab_4)
        self.C3D.setObjectName(u"C3D")
        sizePolicy.setHeightForWidth(self.C3D.sizePolicy().hasHeightForWidth())
        self.C3D.setSizePolicy(sizePolicy)
        self.C3D.setDecimals(4)
        self.C3D.setMaximum(999999.000000000000000)
        self.C3D.setValue(6.607700000000000)

        self.horizontalLayout_47.addWidget(self.C3D)


        self.verticalLayout_10.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_28 = QLabel(self.tab_4)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)

        self.horizontalLayout_48.addWidget(self.label_28)

        self.eta3D = QDoubleSpinBox(self.tab_4)
        self.eta3D.setObjectName(u"eta3D")
        sizePolicy.setHeightForWidth(self.eta3D.sizePolicy().hasHeightForWidth())
        self.eta3D.setSizePolicy(sizePolicy)
        self.eta3D.setMaximum(999999.000000000000000)
        self.eta3D.setValue(1.000000000000000)

        self.horizontalLayout_48.addWidget(self.eta3D)


        self.verticalLayout_10.addLayout(self.horizontalLayout_48)


        self.verticalLayout_4.addLayout(self.verticalLayout_10)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_6 = QLabel(self.tab_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_49.addWidget(self.label_6)

        self.xita2_0 = QDoubleSpinBox(self.tab_5)
        self.xita2_0.setObjectName(u"xita2_0")
        sizePolicy1.setHeightForWidth(self.xita2_0.sizePolicy().hasHeightForWidth())
        self.xita2_0.setSizePolicy(sizePolicy1)
        self.xita2_0.setMaximum(1.000000000000000)
        self.xita2_0.setValue(0.570000000000000)

        self.horizontalLayout_49.addWidget(self.xita2_0)

        self.horizontalLayout_49.setStretch(0, 1)
        self.horizontalLayout_49.setStretch(1, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)

        self.horizontalLayout_50.addWidget(self.label_29)

        self.D2 = QDoubleSpinBox(self.tab_5)
        self.D2.setObjectName(u"D2")
        sizePolicy.setHeightForWidth(self.D2.sizePolicy().hasHeightForWidth())
        self.D2.setSizePolicy(sizePolicy)
        self.D2.setMaximum(99999.000000000000000)
        self.D2.setValue(100.000000000000000)

        self.horizontalLayout_50.addWidget(self.D2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_30 = QLabel(self.tab_5)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)

        self.horizontalLayout_51.addWidget(self.label_30)

        self.xitaFC = QDoubleSpinBox(self.tab_5)
        self.xitaFC.setObjectName(u"xitaFC")
        sizePolicy.setHeightForWidth(self.xitaFC.sizePolicy().hasHeightForWidth())
        self.xitaFC.setSizePolicy(sizePolicy)
        self.xitaFC.setMaximum(999999.000000000000000)
        self.xitaFC.setValue(0.280000000000000)

        self.horizontalLayout_51.addWidget(self.xitaFC)


        self.verticalLayout_11.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_31 = QLabel(self.tab_5)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)

        self.horizontalLayout_52.addWidget(self.label_31)

        self.xitaWP = QDoubleSpinBox(self.tab_5)
        self.xitaWP.setObjectName(u"xitaWP")
        sizePolicy.setHeightForWidth(self.xitaWP.sizePolicy().hasHeightForWidth())
        self.xitaWP.setSizePolicy(sizePolicy)
        self.xitaWP.setDecimals(3)
        self.xitaWP.setMaximum(999999.000000000000000)
        self.xitaWP.setValue(0.225000000000000)

        self.horizontalLayout_52.addWidget(self.xitaWP)


        self.verticalLayout_11.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_32 = QLabel(self.tab_5)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)

        self.horizontalLayout_53.addWidget(self.label_32)

        self.phi2 = QDoubleSpinBox(self.tab_5)
        self.phi2.setObjectName(u"phi2")
        sizePolicy.setHeightForWidth(self.phi2.sizePolicy().hasHeightForWidth())
        self.phi2.setSizePolicy(sizePolicy)
        self.phi2.setMaximum(999999.000000000000000)
        self.phi2.setValue(0.500000000000000)

        self.horizontalLayout_53.addWidget(self.phi2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_33 = QLabel(self.tab_5)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)

        self.horizontalLayout_54.addWidget(self.label_33)

        self.xitacb = QDoubleSpinBox(self.tab_5)
        self.xitacb.setObjectName(u"xitacb")
        sizePolicy.setHeightForWidth(self.xitacb.sizePolicy().hasHeightForWidth())
        self.xitacb.setSizePolicy(sizePolicy)
        self.xitacb.setDecimals(3)
        self.xitacb.setMaximum(999999.000000000000000)
        self.xitacb.setValue(0.375000000000000)

        self.horizontalLayout_54.addWidget(self.xitacb)


        self.verticalLayout_11.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_34 = QLabel(self.tab_5)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)

        self.horizontalLayout_55.addWidget(self.label_34)

        self.Ksat = QDoubleSpinBox(self.tab_5)
        self.Ksat.setObjectName(u"Ksat")
        sizePolicy.setHeightForWidth(self.Ksat.sizePolicy().hasHeightForWidth())
        self.Ksat.setSizePolicy(sizePolicy)
        self.Ksat.setMaximum(999999.000000000000000)
        self.Ksat.setValue(178.569999999999993)

        self.horizontalLayout_55.addWidget(self.Ksat)


        self.verticalLayout_11.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_35 = QLabel(self.tab_5)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)

        self.horizontalLayout_56.addWidget(self.label_35)

        self.HCO = QDoubleSpinBox(self.tab_5)
        self.HCO.setObjectName(u"HCO")
        sizePolicy.setHeightForWidth(self.HCO.sizePolicy().hasHeightForWidth())
        self.HCO.setSizePolicy(sizePolicy)
        self.HCO.setDecimals(4)
        self.HCO.setMaximum(999999.000000000000000)
        self.HCO.setValue(4.806500000000000)

        self.horizontalLayout_56.addWidget(self.HCO)


        self.verticalLayout_11.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_36 = QLabel(self.tab_5)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)

        self.horizontalLayout_57.addWidget(self.label_36)

        self.psi2 = QDoubleSpinBox(self.tab_5)
        self.psi2.setObjectName(u"psi2")
        sizePolicy.setHeightForWidth(self.psi2.sizePolicy().hasHeightForWidth())
        self.psi2.setSizePolicy(sizePolicy)
        self.psi2.setDecimals(4)
        self.psi2.setMaximum(999999.000000000000000)
        self.psi2.setValue(320.286900000000003)

        self.horizontalLayout_57.addWidget(self.psi2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_57)


        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_2 = QGridLayout(self.tab_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_37 = QLabel(self.tab_6)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_37, 0, 0, 1, 1)

        self.D1 = QDoubleSpinBox(self.tab_6)
        self.D1.setObjectName(u"D1")
        sizePolicy.setHeightForWidth(self.D1.sizePolicy().hasHeightForWidth())
        self.D1.setSizePolicy(sizePolicy)
        self.D1.setMaximum(99999.000000000000000)
        self.D1.setValue(30.000000000000000)

        self.gridLayout_2.addWidget(self.D1, 0, 1, 1, 1)

        self.label_38 = QLabel(self.tab_6)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_38, 2, 0, 1, 1)

        self.phi1 = QDoubleSpinBox(self.tab_6)
        self.phi1.setObjectName(u"phi1")
        sizePolicy.setHeightForWidth(self.phi1.sizePolicy().hasHeightForWidth())
        self.phi1.setSizePolicy(sizePolicy)
        self.phi1.setMaximum(99999.000000000000000)
        self.phi1.setValue(0.950000000000000)

        self.gridLayout_2.addWidget(self.phi1, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonBox_greenroof_ok_cancel = QDialogButtonBox(Greenroof)
        self.buttonBox_greenroof_ok_cancel.setObjectName(u"buttonBox_greenroof_ok_cancel")
        self.buttonBox_greenroof_ok_cancel.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Help|QDialogButtonBox.Ok)

        self.horizontalLayout_4.addWidget(self.buttonBox_greenroof_ok_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Greenroof)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Greenroof)
    # setupUi

    def retranslateUi(self, Greenroof):
        Greenroof.setWindowTitle(QCoreApplication.translate("Greenroof", u"\u7eff\u8272\u5c4b\u9876", None))
        self.label_5.setText(QCoreApplication.translate("Greenroof", u"\u84c4\u6c34\u5c42\u6c34\u6df1", None))
        self.label_14.setText(QCoreApplication.translate("Greenroof", u"\u84c4\u6c34\u5c42\u6df1\u5ea6", None))
        self.label_15.setText(QCoreApplication.translate("Greenroof", u"<html><head/><body><p>\u84c4\u6c34\u5c42\u6700\u5c0f<br/>\u53ef\u51fa\u6d41\u6df1\u5ea6</p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Greenroof", u"\u783e\u77f3\u5c42\u5b54\u9699\u7387", None))
        self.label_27.setText(QCoreApplication.translate("Greenroof", u"\u5b54\u6d41\u7cfb\u6570", None))
        self.label_28.setText(QCoreApplication.translate("Greenroof", u"\u5b54\u6d41\u6307\u6570", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Greenroof", u"\u84c4\u6c34\u5c42", None))
        self.label_6.setText(QCoreApplication.translate("Greenroof", u"\u571f\u5c42\u542b\u6c34\u91cf", None))
        self.label_29.setText(QCoreApplication.translate("Greenroof", u"\u57fa\u8d28\u5c42\u6df1\u5ea6", None))
        self.label_30.setText(QCoreApplication.translate("Greenroof", u"\u7530\u95f4\u6301\u6c34\u91cf", None))
        self.label_31.setText(QCoreApplication.translate("Greenroof", u"\u51cb\u840e\u70b9", None))
        self.label_32.setText(QCoreApplication.translate("Greenroof", u"\u571f\u58e4\u5c42\u5b54\u9699\u7387", None))
        self.label_33.setText(QCoreApplication.translate("Greenroof", u"\u4e34\u754c\u542b\u6c34\u91cf", None))
        self.label_34.setText(QCoreApplication.translate("Greenroof", u"\u9971\u548c\u5bfc\u6c34\u7387", None))
        self.label_35.setText(QCoreApplication.translate("Greenroof", u"\u8870\u51cf\u5e38\u6570", None))
        self.label_36.setText(QCoreApplication.translate("Greenroof", u"\u5438\u529b\u6c34\u5934", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Greenroof", u"\u571f\u58e4\u5c42", None))
        self.label_37.setText(QCoreApplication.translate("Greenroof", u"\u6ea2\u6d41\u5c42\u6df1\u5ea6", None))
        self.label_38.setText(QCoreApplication.translate("Greenroof", u"\u7a7a\u9699\u7387", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Greenroof", u"\u8868\u5c42", None))
    # retranslateUi

