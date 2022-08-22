# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_dates.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateTimeEdit, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_SimDates(object):
    def setupUi(self, SimDates):
        if not SimDates.objectName():
            SimDates.setObjectName(u"SimDates")
        SimDates.resize(260, 200)
        self.horizontalLayout_5 = QHBoxLayout(SimDates)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_sim_start_datetime = QLabel(SimDates)
        self.label_sim_start_datetime.setObjectName(u"label_sim_start_datetime")

        self.horizontalLayout_3.addWidget(self.label_sim_start_datetime)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_sim_end_datetime = QLabel(SimDates)
        self.label_sim_end_datetime.setObjectName(u"label_sim_end_datetime")

        self.horizontalLayout_2.addWidget(self.label_sim_end_datetime)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_sim_timestep = QLabel(SimDates)
        self.label_sim_timestep.setObjectName(u"label_sim_timestep")

        self.verticalLayout_2.addWidget(self.label_sim_timestep)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dateTime_start_edit = QDateTimeEdit(SimDates)
        self.dateTime_start_edit.setObjectName(u"dateTime_start_edit")
        self.dateTime_start_edit.setDateTime(QDateTime(QDate(2021, 5, 25), QTime(0, 1, 0)))

        self.verticalLayout.addWidget(self.dateTime_start_edit)

        self.dateTime_end_edit = QDateTimeEdit(SimDates)
        self.dateTime_end_edit.setObjectName(u"dateTime_end_edit")
        self.dateTime_end_edit.setDateTime(QDateTime(QDate(2021, 6, 29), QTime(0, 0, 0)))
        self.dateTime_end_edit.setDate(QDate(2021, 6, 29))

        self.verticalLayout.addWidget(self.dateTime_end_edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinBox_timestep = QSpinBox(SimDates)
        self.spinBox_timestep.setObjectName(u"spinBox_timestep")
        self.spinBox_timestep.setMinimum(1)

        self.horizontalLayout.addWidget(self.spinBox_timestep)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(SimDates)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.retranslateUi(SimDates)
        self.buttonBox.accepted.connect(SimDates.accept)
        self.buttonBox.rejected.connect(SimDates.reject)

        QMetaObject.connectSlotsByName(SimDates)
    # setupUi

    def retranslateUi(self, SimDates):
        SimDates.setWindowTitle(QCoreApplication.translate("SimDates", u"\u4eff\u771f\u65e5\u671f", None))
        self.label_sim_start_datetime.setText(QCoreApplication.translate("SimDates", u"\u5f00\u59cb\u65f6\u95f4", None))
        self.label_sim_end_datetime.setText(QCoreApplication.translate("SimDates", u"\u7ed3\u675f\u65f6\u95f4", None))
        self.label_sim_timestep.setText(QCoreApplication.translate("SimDates", u"\u65f6\u95f4\u6b65\u957f\uff08min\uff09", None))
        self.dateTime_start_edit.setDisplayFormat(QCoreApplication.translate("SimDates", u"yyyy/MM/dd H:mm", None))
        self.dateTime_end_edit.setDisplayFormat(QCoreApplication.translate("SimDates", u"yyyy/MM/dd H:mm", None))
    # retranslateUi

