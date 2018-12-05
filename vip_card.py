# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vip_card.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys,time
import pymysql
import config

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.sex1 = '男'
        self.sex2 = ''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(75, 72, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(75, 111, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(75, 150, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(75, 188, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(155, 72, 180, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(155, 110, 50, 28))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(lambda :self.btnstate(self.radioButton))
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 110, 50, 28))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(lambda :self.btnstate(self.radioButton_2))
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(155, 148, 180, 28))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(155, 191, 180, 28))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 240, 60, 25))
        font = QtGui.QFont()
        # font.setBold(True)
        font.setWeight(65)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(116, 10, 220, 50))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(22)
        font.setKerning(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        # 姓名输入限制，不允许有数字和特殊字符，允许中间有一个空格
        reg = QRegExp('^[^(\d|\W)]+( ?[^(\d|\W)]+)*$')
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.lineEdit.setValidator(pValidator)

        # 手机号正则限制
        reg1 = QRegExp("^1[0-9]{10}$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg1)
        self.lineEdit_3.setValidator(pValidator)
        # 充值金额正则限制
        reg2 = QRegExp("^[1-9][0-9]*$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg2)
        self.lineEdit_4.setValidator(pValidator)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 绑定确定按钮槽信号
        self.pushButton.clicked.connect(self.card)
 

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "开卡"))
        self.label.setText(_translate("Form", "姓  　名"))
        self.label_2.setText(_translate("Form", "性  　别"))
        self.label_3.setText(_translate("Form", "手 机 号"))
        self.label_4.setText(_translate("Form", "充值金额"))
        self.pushButton.setText(_translate("Form", "确认"))

        self.label_5.setText(_translate("Form", "会员开卡系统"))
        self.radioButton.setText(_translate("Form", "男"))
        self.radioButton_2.setText(_translate("Form", "女"))


    def btnstate(self,btn):
        if btn.text() == '男':
            if btn.isChecked() == True:
                self.sex1 = btn.text()
                # print('1',self.sex1)
            else:
                self.sex2 = btn.text()
                # print('2',self.sex2)
        if btn.text() == '女':
            if btn.isChecked() == True:
                self.sex1 = btn.text()
                # print('3',self.sex1)
            else:
                self.sex2 = btn.text()
                # print('4',self.sex2)

    def card(self):
        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()
        name = self.lineEdit.text()
        sex = self.sex1
        tel = self.lineEdit_3.text()
        money = self.lineEdit_4.text()

        sql = "select * from vip_info where tel='%s'"%tel
        cursor.execute(sql)
        data = cursor.fetchone()

        if not name:
            QMessageBox.information(self, '提示', "请输入姓名", QMessageBox.Ok)
            return
        if not tel:
            QMessageBox.information(self, '提示', "请输入手机号", QMessageBox.Ok)
            return
        if len(tel) != 11:
            QMessageBox.information(self, '提示', "手机号输入有误", QMessageBox.Ok)
            return
        if not money:
            QMessageBox.information(self, '提示', "请输入充值金额", QMessageBox.Ok)
            return
        if data:
            QMessageBox.information(self, '提示', "该号码已注册过会员", QMessageBox.Ok)
            return
        try:
            sql = "insert into vip_info(name,sex,tel,YE) values(\
                '%s','%s','%s','%s')"%(name,sex,tel,money)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            time.sleep(0.2)
            sql_select = "select id from vip_info where tel = '%s';"%tel
            cursor.execute(sql_select)
            ID = cursor.fetchone()[0]
            QMessageBox.information(self, '恭喜！', "开卡成功！\n卡号:%s\n手机号:%s\n卡余额:%s"%\
                (ID,tel,money), QMessageBox.Ok)
            self.lineEdit.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')
            self.radioButton.setChecked(True)
        except Exception as e:
            db.rollback()
            QMessageBox.information(self, '提示', "开卡失败",QMessageBox.Ok)
            print("会员开卡失败",e)
        cursor.close()
        db.close()

# 13344556677

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())