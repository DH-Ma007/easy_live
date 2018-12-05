# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog
import sys
import checkin_query
import book_query
import livehis_query



class Ui_Dialog(QDialog, QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(257, 300)
        Dialog.setStyleSheet("QWidget{background-image:url('image/sand.jpg')};")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 260, 99, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 30, 141, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        # self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton.setStyleSheet("QWidget{background:white};")
        self.pushButton_2.setStyleSheet("QWidget{background:white};")
        self.pushButton_4.setStyleSheet("QWidget{background:white};")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #绑定预定查询信号
        self.pushButton.clicked.connect(self.to_book_query)

        #绑定入住查询信号
        self.pushButton_2.clicked.connect(self.to_checkin_query)

        #绑定历史查询信号
        self.pushButton_4.clicked.connect(self.to_livehis_query)

        self.pushButton_5.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "信息查询"))
        self.pushButton_5.setText(_translate("Dialog", "返回上级"))
        self.pushButton.setText(_translate("Dialog", "预定信息查询"))
        self.pushButton_2.setText(_translate("Dialog", "入住信息查询"))
        # self.pushButton_3.setText(_translate("Dialog", "所有在住信息"))
        self.pushButton_4.setText(_translate("Dialog", "入住历史查询"))

    def to_book_query(self):
        checkin_window = QDialog()
        ui = book_query.Ui_Form()
        ui.setupUi(checkin_window)
        checkin_window.show()
        checkin_window.exec_()

    def to_checkin_query(self):
        checkin_window = QDialog()
        ui = checkin_query.Ui_Form()
        ui.setupUi(checkin_window)
        checkin_window.show()
        checkin_window.exec_()

    def to_livehis_query(self):
        checkin_window = QDialog()
        ui = livehis_query.Ui_Form()
        ui.setupUi(checkin_window)
        checkin_window.show()
        checkin_window.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Dialog()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())