# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sponge_block.ui'
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
    QGraphicsView, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_SpongeBlock(object):
    def setupUi(self, SpongeBlock):
        if not SpongeBlock.objectName():
            SpongeBlock.setObjectName(u"SpongeBlock")
        SpongeBlock.resize(1920, 1080)
        self.horizontalLayout_7 = QHBoxLayout(SpongeBlock)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_block_setting = QGroupBox(SpongeBlock)
        self.groupBox_block_setting.setObjectName(u"groupBox_block_setting")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_block_setting)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_landuse = QLabel(self.groupBox_block_setting)
        self.label_landuse.setObjectName(u"label_landuse")

        self.horizontalLayout_3.addWidget(self.label_landuse)

        self.lineEdit_landuse = QLineEdit(self.groupBox_block_setting)
        self.lineEdit_landuse.setObjectName(u"lineEdit_landuse")
        self.lineEdit_landuse.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_3.addWidget(self.lineEdit_landuse)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_underlying = QLabel(self.groupBox_block_setting)
        self.label_underlying.setObjectName(u"label_underlying")

        self.horizontalLayout_4.addWidget(self.label_underlying)

        self.lineEdit_underlying = QLineEdit(self.groupBox_block_setting)
        self.lineEdit_underlying.setObjectName(u"lineEdit_underlying")
        self.lineEdit_underlying.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.lineEdit_underlying)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_block_area = QLabel(self.groupBox_block_setting)
        self.label_block_area.setObjectName(u"label_block_area")

        self.horizontalLayout_5.addWidget(self.label_block_area)

        self.spinBox_area = QSpinBox(self.groupBox_block_setting)
        self.spinBox_area.setObjectName(u"spinBox_area")
        self.spinBox_area.setMaximum(999999)
        self.spinBox_area.setValue(10000)

        self.horizontalLayout_5.addWidget(self.spinBox_area)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalLayout_6.setStretch(0, 6)
        self.horizontalLayout_6.setStretch(1, 4)

        self.verticalLayout_2.addWidget(self.groupBox_block_setting)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.groupBox_sponge_setting = QGroupBox(SpongeBlock)
        self.groupBox_sponge_setting.setObjectName(u"groupBox_sponge_setting")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_sponge_setting)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget_sponge_setting = QTableWidget(self.groupBox_sponge_setting)
        if (self.tableWidget_sponge_setting.columnCount() < 2):
            self.tableWidget_sponge_setting.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_sponge_setting.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget_sponge_setting.rowCount() < 4):
            self.tableWidget_sponge_setting.setRowCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setItem(2, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_sponge_setting.setItem(3, 1, __qtablewidgetitem13)
        self.tableWidget_sponge_setting.setObjectName(u"tableWidget_sponge_setting")

        self.horizontalLayout.addWidget(self.tableWidget_sponge_setting)

        self.graphicsView_sponge_setting_show = QGraphicsView(self.groupBox_sponge_setting)
        self.graphicsView_sponge_setting_show.setObjectName(u"graphicsView_sponge_setting_show")
        self.graphicsView_sponge_setting_show.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.horizontalLayout.addWidget(self.graphicsView_sponge_setting_show)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox_sponge_setting)

        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 20)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.buttonBox = QDialogButtonBox(SpongeBlock)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.groupBox_block_setting.raise_()
        self.groupBox_sponge_setting.raise_()
        self.buttonBox.raise_()
        self.tableWidget_sponge_setting.raise_()
        self.graphicsView_sponge_setting_show.raise_()

        self.retranslateUi(SpongeBlock)
        self.buttonBox.accepted.connect(SpongeBlock.accept)
        self.buttonBox.rejected.connect(SpongeBlock.reject)

        QMetaObject.connectSlotsByName(SpongeBlock)
    # setupUi

    def retranslateUi(self, SpongeBlock):
        SpongeBlock.setWindowTitle(QCoreApplication.translate("SpongeBlock", u"SpongeBlock", None))
        self.groupBox_block_setting.setTitle(QCoreApplication.translate("SpongeBlock", u"\u5f53\u524d\u9762\u6e90\u6591\u5757\u8bbe\u7f6e", None))
        self.label_landuse.setText(QCoreApplication.translate("SpongeBlock", u"\u571f\u5730\u5229\u7528\u7c7b\u578b", None))
        self.lineEdit_landuse.setText(QCoreApplication.translate("SpongeBlock", u"\u8bf7\u5148\u5b9a\u4e49\u9762\u6e90\u6591\u5757", None))
        self.label_underlying.setText(QCoreApplication.translate("SpongeBlock", u"\u4e0b\u57ab\u9762\u7c7b\u578b", None))
        self.lineEdit_underlying.setText(QCoreApplication.translate("SpongeBlock", u"\u8bf7\u5148\u5b9a\u4e49\u9762\u6e90\u6591\u5757", None))
        self.label_block_area.setText(QCoreApplication.translate("SpongeBlock", u"\u5730\u5757\u9762\u79ef\uff08m\u00b2\uff09", None))
        self.groupBox_sponge_setting.setTitle(QCoreApplication.translate("SpongeBlock", u"\u6d77\u7ef5\u8bbe\u65bd\u8bbe\u7f6e", None))
        ___qtablewidgetitem = self.tableWidget_sponge_setting.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SpongeBlock", u"\u6bd4\u4f8b", None));
        ___qtablewidgetitem1 = self.tableWidget_sponge_setting.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SpongeBlock", u"\u5904\u7406\u9762\u79ef", None));
        ___qtablewidgetitem2 = self.tableWidget_sponge_setting.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SpongeBlock", u"\u7eff\u8272\u5c4b\u9876", None));
        ___qtablewidgetitem3 = self.tableWidget_sponge_setting.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SpongeBlock", u"\u751f\u7269\u6ede\u7559\u6c60", None));
        ___qtablewidgetitem4 = self.tableWidget_sponge_setting.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SpongeBlock", u"\u6e17\u900f\u94fa\u88c5", None));
        ___qtablewidgetitem5 = self.tableWidget_sponge_setting.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SpongeBlock", u"\u4e0b\u51f9\u5f0f\u7eff\u5730", None));

        __sortingEnabled = self.tableWidget_sponge_setting.isSortingEnabled()
        self.tableWidget_sponge_setting.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget_sponge_setting.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SpongeBlock", u"0", None));
        ___qtablewidgetitem7 = self.tableWidget_sponge_setting.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SpongeBlock", u"0", None));
        ___qtablewidgetitem8 = self.tableWidget_sponge_setting.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SpongeBlock", u"0", None));
        ___qtablewidgetitem9 = self.tableWidget_sponge_setting.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("SpongeBlock", u"0", None));
        ___qtablewidgetitem10 = self.tableWidget_sponge_setting.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("SpongeBlock", u"0", None));
        ___qtablewidgetitem11 = self.tableWidget_sponge_setting.item(2, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("SpongeBlock", u"0", None));
        ___qtablewidgetitem12 = self.tableWidget_sponge_setting.item(3, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("SpongeBlock", u"0", None));
        ___qtablewidgetitem13 = self.tableWidget_sponge_setting.item(3, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("SpongeBlock", u"0", None));
        self.tableWidget_sponge_setting.setSortingEnabled(__sortingEnabled)

    # retranslateUi

