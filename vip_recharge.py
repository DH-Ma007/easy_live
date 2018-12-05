# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recharge.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import pymysql
import config

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(97, 71, 89, 23))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(165, 70, 150, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(96, 140, 220, 100))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(96, 106, 89, 23))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(165, 106, 150, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 250, 60, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 250, 60, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(105, 6, 200, 40))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # 手机号正则限制
        reg1 = QRegExp("^1[0-9]{10}$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg1)
        self.lineEdit.setValidator(pValidator)
        # 充值金额正则限制
        reg2 = QRegExp("^[1-9][0-9]*$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg2)
        self.lineEdit_2.setValidator(pValidator)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 设置查询信号
        self.pushButton.clicked.connect(self.query)

        # 设置充值信号
        self.pushButton_2.clicked.connect(self.recharge)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "充值"))
        self.label.setText(_translate("Form", "手 机 号"))
        self.label_2.setText(_translate("Form", "充值金额"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "充值"))

        self.label_3.setText(_translate("Form", "会员充值系统"))

    def query(self):
        self.textEdit.clear()
        tel = self.lineEdit.text()
        if not tel:
            QMessageBox.information(self,'提示','请输入手机号',QMessageBox.Ok)
            return
        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()

        try:
            sql = "select * from vip_info where tel='%s'"%tel
            cursor.execute(sql)
            data = cursor.fetchone()
            if not data:
                QMessageBox.information(self, '提示', '没有此会员信息', QMessageBox.Ok)
                return
            self.textEdit.setPlainText("姓名:%s\n手机号:%s\n余额:%s"%(data[1],data[3],data[4]))
            print("查询成功")            
        except Exception as e:
            print("查询失败",e)
        cursor.close()
        db.close()
        return data[4]


    def recharge(self):
        YE = self.query()
        if not YE:
            return
        # self.textEdit.clear()
        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()
        tel = self.lineEdit.text()
        money = self.lineEdit_2.text()

        if not money:
            QMessageBox.information(self, '提示信息', '请输入充值金额', QMessageBox.Yes)
            return
        # try:
        YE += int(money)
        sql = "update vip_info set YE='%s' where tel='%s'"%(YE,tel)
        cursor.execute(sql)
        db.commit()
        sql = "select * from vip_info where tel='%s'"%tel
        cursor.execute(sql)
        data = cursor.fetchone()
        if not data:
            QMessageBox.information(self, '提示信息', '没有此会员信息', QMessageBox.Yes)
        print("充值成功")
        QMessageBox.information(self, '提示', '充值成功!\n姓名:%s\n手机号:%s\n余额:%s'\
            %(data[1],data[3],str(data[4])), QMessageBox.Ok)
        self.textEdit.setPlainText('')
        self.lineEdit_2.setText('')
        # except Exception as e:
        #     print("充值失败",e)
        cursor.close()
        db.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())