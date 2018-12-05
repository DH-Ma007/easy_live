# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room_show.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_room_show_1(object):
    def setupUi(self, room_show_1):
        room_show_1.setObjectName("room_show_1")
        room_show_1.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(room_show_1)
        self.pushButton.setGeometry(QtCore.QRect(287, 252, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(room_show_1)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 30, 140, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(room_show_1)
        QtCore.QMetaObject.connectSlotsByName(room_show_1)

    def retranslateUi(self, room_show_1):
        _translate = QtCore.QCoreApplication.translate
        room_show_1.setWindowTitle(_translate("room_show_1", "Dialog"))
        self.pushButton.setText(_translate("room_show_1", "返回上级"))
        self.pushButton_3.setText(_translate("room_show_1", "查看全部房间"))
        self.pushButton_4.setText(_translate("room_show_1", "按类型查看房间"))
        self.pushButton_2.setText(_translate("room_show_1", "按楼层查看房间"))

