# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rain_generate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RainGenerate(object):
    def setupUi(self, RainGenerate):
        RainGenerate.setObjectName("RainGenerate")
        RainGenerate.resize(1920, 1080)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(RainGenerate)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_rain_peak = QtWidgets.QLabel(RainGenerate)
        self.label_rain_peak.setObjectName("label_rain_peak")
        self.horizontalLayout.addWidget(self.label_rain_peak)
        self.doubleSpinBox_peak = QtWidgets.QDoubleSpinBox(RainGenerate)
        self.doubleSpinBox_peak.setMaximum(1.0)
        self.doubleSpinBox_peak.setSingleStep(0.01)
        self.doubleSpinBox_peak.setProperty("value", 0.4)
        self.doubleSpinBox_peak.setObjectName("doubleSpinBox_peak")
        self.horizontalLayout.addWidget(self.doubleSpinBox_peak)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_return_period = QtWidgets.QLabel(RainGenerate)
        self.label_return_period.setObjectName("label_return_period")
        self.horizontalLayout_2.addWidget(self.label_return_period)
        self.spinBox_return_period = QtWidgets.QSpinBox(RainGenerate)
        self.spinBox_return_period.setMaximum(999999)
        self.spinBox_return_period.setProperty("value", 10)
        self.spinBox_return_period.setObjectName("spinBox_return_period")
        self.horizontalLayout_2.addWidget(self.spinBox_return_period)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_rain_duration = QtWidgets.QLabel(RainGenerate)
        self.label_rain_duration.setObjectName("label_rain_duration")
        self.horizontalLayout_3.addWidget(self.label_rain_duration)
        self.spinBox_duration = QtWidgets.QSpinBox(RainGenerate)
        self.spinBox_duration.setMaximum(9999)
        self.spinBox_duration.setProperty("value", 180)
        self.spinBox_duration.setObjectName("spinBox_duration")
        self.horizontalLayout_3.addWidget(self.spinBox_duration)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(RainGenerate)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.graphicsView_rain_generate = QtWidgets.QGraphicsView(RainGenerate)
        self.graphicsView_rain_generate.setObjectName("graphicsView_rain_generate")
        self.verticalLayout_3.addWidget(self.graphicsView_rain_generate)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 6)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.retranslateUi(RainGenerate)
        self.buttonBox.accepted.connect(RainGenerate.accept) # type: ignore
        self.buttonBox.rejected.connect(RainGenerate.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(RainGenerate)

    def retranslateUi(self, RainGenerate):
        _translate = QtCore.QCoreApplication.translate
        RainGenerate.setWindowTitle(_translate("RainGenerate", "雨型生成"))
        self.label_rain_peak.setText(_translate("RainGenerate", "雨峰系数（0~1）"))
        self.label_return_period.setText(_translate("RainGenerate", "降雨重现期（年）"))
        self.label_rain_duration.setText(_translate("RainGenerate", "降雨历时（分钟）"))
