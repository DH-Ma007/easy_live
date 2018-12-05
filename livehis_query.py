# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_query.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog
import sys
import time
import pymysql
import config

class Ui_Form(QDialog, QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(277, 28, 400, 30))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(214, 100, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(330, 96, 250, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(200, 209, 400, 300))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 520, 80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 520, 80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 140, 250, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(214, 140, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(285, 182, 300, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 定义查询信号
        self.pushButton_2.clicked.connect(self.history_query)
        self.pushButton_3.clicked.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "历史查询"))
        self.label.setText(_translate("Form", "入住历史查询系统"))
        self.label_2.setText(_translate("Form", "手 机 号"))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.pushButton_3.setText(_translate("Form", "取消"))
        self.label_3.setText(_translate("Form", "身份证号"))
        self.label_4.setText(_translate("Form", "*手机号和身份证号任意一个都可查询"))

    def history_query(self):
        self.textEdit.clear()
        str = ""
        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()
        tel = self.lineEdit.text()
        id_num = self.lineEdit_2.text()
        if not id_num and not tel:
            QMessageBox.information(self, '提示信息', '请输入手机号或身份证号', QMessageBox.Ok)
            return
        elif not id_num:
            self.textEdit.clear()
            try:
                sql_select = "select * from live_history where phone_num = '%s'"%tel
                cursor.execute(sql_select)
                dataall = cursor.fetchall()
                if not dataall:
                    QMessageBox.information(self, '提示信息', '没有历史入住信息', QMessageBox.Ok)
                    return
                for data in dataall:
                    str += "姓名:%s\n性别:%s\n手机号:%s\n身份证号:%s\n房间号:%s\n押金:%s\n房价:%s\n入住人数:%s\n入住时间:%s\n离店时间:%s\n*******************\n"\
                        %(data[1],data[4],data[2],data[3],data[5],data[6],data[7],data[8],data[9],data[10])
                self.textEdit.setPlainText(str)
            except Exception as e:
                print("查询失败",e)
        elif not tel:
            self.textEdit.clear()
            try:
                sql_select = "select * from live_history where ID_num = '%s'"%id_num
                cursor.execute(sql_select)
                dataall = cursor.fetchall()
                if not dataall:
                    QMessageBox.information(self, '提示信息', '没有历史入住信息', QMessageBox.Ok)
                    return
                for data in dataall:
                    str += "姓名:%s\n性别:%s\n手机号:%s\n身份证号:%s\n房间号:%s\n押金:%s\n房价:%s\n入住人数:%s\n入住时间:%s\n离店时间:%s\n*******************\n"\
                        %(data[1],data[4],data[2],data[3],data[5],data[6],data[7],data[8],data[9],data[10])
                self.textEdit.setPlainText(str)
            except Exception as e:
                print("查询失败",e)
        else:
            self.textEdit.clear()
            try:
                sql_select = "select * from live_history where ID_num = '%s' and phone_num = '%s'"\
                        %(id_num, tel)
                cursor.execute(sql_select)
                dataall = cursor.fetchall()
                if not dataall:
                    QMessageBox.information(self, '提示信息', '没有历史入住信息', QMessageBox.Ok)
                    return
                for data in dataall:
                    str += "姓名:%s\n性别:%s\n手机号:%s\n身份证号:%s\n房间号:%s\n押金:%s\n房价:%s\n入住人数:%s\n入住时间:%s\n离店时间:%s\n*******************\n"\
                        %(data[1],data[4],data[2],data[3],data[5],data[6],data[7],data[8],data[9],data[10])
                self.textEdit.setPlainText(str)
            except Exception as e:
                print("查询失败",e)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())