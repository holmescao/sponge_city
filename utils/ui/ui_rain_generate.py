# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rain_generate.ui'
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
    QDoubleSpinBox, QGraphicsView, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_RainGenerate(object):
    def setupUi(self, RainGenerate):
        if not RainGenerate.objectName():
            RainGenerate.setObjectName(u"RainGenerate")
        RainGenerate.resize(1920, 1080)
        self.horizontalLayout_5 = QHBoxLayout(RainGenerate)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_rain_peak = QLabel(RainGenerate)
        self.label_rain_peak.setObjectName(u"label_rain_peak")

        self.horizontalLayout.addWidget(self.label_rain_peak)

        self.doubleSpinBox_peak = QDoubleSpinBox(RainGenerate)
        self.doubleSpinBox_peak.setObjectName(u"doubleSpinBox_peak")
        self.doubleSpinBox_peak.setMaximum(1.000000000000000)
        self.doubleSpinBox_peak.setSingleStep(0.010000000000000)
        self.doubleSpinBox_peak.setValue(0.400000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_peak)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_return_period = QLabel(RainGenerate)
        self.label_return_period.setObjectName(u"label_return_period")

        self.horizontalLayout_2.addWidget(self.label_return_period)

        self.spinBox_return_period = QSpinBox(RainGenerate)
        self.spinBox_return_period.setObjectName(u"spinBox_return_period")
        self.spinBox_return_period.setMaximum(999999)
        self.spinBox_return_period.setValue(10)

        self.horizontalLayout_2.addWidget(self.spinBox_return_period)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_rain_duration = QLabel(RainGenerate)
        self.label_rain_duration.setObjectName(u"label_rain_duration")

        self.horizontalLayout_3.addWidget(self.label_rain_duration)

        self.spinBox_duration = QSpinBox(RainGenerate)
        self.spinBox_duration.setObjectName(u"spinBox_duration")
        self.spinBox_duration.setMaximum(9999)
        self.spinBox_duration.setValue(180)

        self.horizontalLayout_3.addWidget(self.spinBox_duration)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 4)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(RainGenerate)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.graphicsView_rain_generate = QGraphicsView(RainGenerate)
        self.graphicsView_rain_generate.setObjectName(u"graphicsView_rain_generate")

        self.verticalLayout_3.addWidget(self.graphicsView_rain_generate)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 6)
        self.horizontalLayout_4.setStretch(3, 1)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.retranslateUi(RainGenerate)
        self.buttonBox.accepted.connect(RainGenerate.accept)
        self.buttonBox.rejected.connect(RainGenerate.reject)

        QMetaObject.connectSlotsByName(RainGenerate)
    # setupUi

    def retranslateUi(self, RainGenerate):
        RainGenerate.setWindowTitle(QCoreApplication.translate("RainGenerate", u"\u96e8\u578b\u751f\u6210", None))
        self.label_rain_peak.setText(QCoreApplication.translate("RainGenerate", u"\u96e8\u5cf0\u7cfb\u6570\uff080~1\uff09", None))
        self.label_return_period.setText(QCoreApplication.translate("RainGenerate", u"\u964d\u96e8\u91cd\u73b0\u671f\uff08\u5e74\uff09", None))
        self.label_rain_duration.setText(QCoreApplication.translate("RainGenerate", u"\u964d\u96e8\u5386\u65f6\uff08\u5206\u949f\uff09", None))
    # retranslateUi

