# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'success.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
import time,sys

class Ui_Dialog(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(202, 111)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 36, 81, 21))
        self.label.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "恭喜！"))
        self.label.setText(_translate("Dialog", "登录成功！"))

