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
        self.label.setGeometry(QtCore.QRect(97, 71, 92, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 150, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFocus()
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(99, 115, 220, 120))
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(135, 250, 60, 25))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 69, 25, 25))
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_2.setStyleSheet("QWidget{background:url('image/find.jpg')};")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 250, 60, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 6, 200, 40))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 设置查询信号
        self.pushButton.clicked.connect(self.cancellation)
        self.pushButton_2.clicked.connect(self.query)
        self.pushButton_3.clicked.connect(Form.close)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "销卡"))
        self.label.setText(_translate("Form", "手 机 号"))
        self.pushButton.setText(_translate("Form", "注销"))
        self.pushButton_2.setText(_translate("Form", ""))
        self.pushButton_3.setText(_translate("Form", "返回"))
        self.label_3.setText(_translate("Form", "会员注销系统"))

    def query(self):
        self.textEdit.clear()
        tel = self.lineEdit.text()
        if not tel:
            QMessageBox.information(self,'提示','请输入手机号',QMessageBox.Ok)
            return
        if len(tel) != 11:
            QMessageBox.information(self,'提示','手机号输入有误',QMessageBox.Ok)
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
            cursor.close()
            db.close()
            return data[1],data[3],data[4]
        except Exception as e:
            print("查询失败",e)
            return


    def cancellation(self):
        try:
            name,tel,money = self.query()
        except:
            return
        data = self.textEdit.toPlainText()
        if not data:
            return
        reply = QMessageBox.question(self, '销卡确认',
            "姓名:%s\n卡余额:%s\n\n确认销卡?"%(name,money), QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                db = pymysql.connect(host = config.HOST, user = config.USER,\
                            password = config.PASSWORD, database = "hotelDB",\
                            charset = "utf8")        
                cursor = db.cursor()
                sql_delete = "delete from vip_info where tel = '%s'"%tel
                cursor.execute(sql_delete)
                db.commit()
                print("销卡成功")
                QMessageBox.information(self, '提示信息', '销卡成功', QMessageBox.Ok)
            except Exception as e:
                db.rollback()
                print("销卡失败",e)
                QMessageBox.information(self, '提示信息', '销卡失败：%s'%e, QMessageBox.Ok)
            cursor.close()
            db.close()
            self.textEdit.setPlainText('')
        else:
            return

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())