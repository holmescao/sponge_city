# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sponge_city_2022年08月11日 copy.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QListView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QSpacerItem, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 400)
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
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout.addWidget(self.listView)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.label_13)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.green_roof_sim_curve = QGraphicsView(self.centralwidget)
        self.green_roof_sim_curve.setObjectName(u"green_roof_sim_curve")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.green_roof_sim_curve.sizePolicy().hasHeightForWidth())
        self.green_roof_sim_curve.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.green_roof_sim_curve)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 6)
        self.horizontalLayout.setStretch(3, 4)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 994, 22))
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

