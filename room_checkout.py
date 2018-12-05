# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room_checkout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import pymysql
import time
import config

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("QWidget{background-image:url('image/sand.jpg')};")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(91, 91, 89, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(156, 93, 113, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(91, 130, 210, 100))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(142, 21, 150, 30))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 95, 27, 27))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 240, 80, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label.setStyleSheet("QWidget{background:transparent};")
        self.label_2.setStyleSheet("QWidget{background:transparent};")
        self.pushButton.setStyleSheet("QWidget{background:url('image/find.jpg')};")
        self.textEdit.setStyleSheet("QWidget{background:white};")

        # 房间号正则限制
        reg = QRegExp("^\d+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.lineEdit.setValidator(pValidator)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #绑定退房按钮信号
        self.pushButton.clicked.connect(self.query_info)
        self.pushButton_2.clicked.connect(self.checkout)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "退房"))
        self.label.setText(_translate("Form", "房间号"))
        self.label_2.setText(_translate("Form", "退房界面"))
        self.pushButton.setText(_translate("Form", ""))
        self.pushButton_2.setText(_translate("Form", "提交"))


    def query_info(self):
        self.textEdit.setPlainText('')
        room_num = self.lineEdit.text()
        if not room_num:
            QMessageBox.information(self, '提示信息', '请先输入房间号', QMessageBox.Ok)
            return

        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()

        sql_select = "select * from room_info where 房间号='%s'"%room_num
        cursor.execute(sql_select)
        data = cursor.fetchone()
        if not data:
            QMessageBox.warning(self, '查询失败', '房间号输入有误', QMessageBox.Ok)
            return

        sql_select = "select name,room_num,deposit,price,vip_price from\
                    check_in_info where room_num='%s'"%room_num
        cursor.execute(sql_select)
        data = cursor.fetchone()
        if not data:
            # self.textEdit.setPlainText("此房间没有入住信息")
            QMessageBox.information(self, '提示信息', '此房间当前无入住信息', QMessageBox.Ok)
            return
        self.textEdit.setPlainText("姓名:%s\n房间号:%s\n定金:%s"%(data[0],data[1],data[2]))

    def checkout(self):
        self.query_info()
        room_num = self.lineEdit.text()
        data = self.textEdit.toPlainText()
        if not data:
            return
        reply = QMessageBox.question(self, '退房确认',
            "房号:%s\n\n确认退房?"%room_num, QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                db = pymysql.connect(host = config.HOST, user = config.USER,\
                            password = config.PASSWORD, database = "hotelDB",\
                            charset = "utf8")        
                cursor = db.cursor()
                sql_update = "update room_info set 房间状态='空闲' where 房间号='%s'"%room_num
                cursor.execute(sql_update)
                sql_update = "update check_in_info set end_date = '%s' where room_num = '%s'"%\
                            (time.ctime(), room_num)
                cursor.execute(sql_update)
                sql_insert = "insert into live_history(name, gender, ID_num,room_num,\
                        deposit, price, phone_num, people_count, start_date, end_date)\
                        select name, gender, ID_num, room_num, deposit, price, phone_num,\
                        people_count, start_date, end_date from check_in_info where\
                        room_num = '%s'"%room_num
                cursor.execute(sql_insert)
                sql_delete = "delete from check_in_info where room_num = '%s'"%room_num
                cursor.execute(sql_delete)
                db.commit()
                print("退房成功")
                QMessageBox.information(self, '提示信息', '退房成功', QMessageBox.Ok)
            except Exception as e:
                db.rollback()
                print("退房失败",e)
                QMessageBox.information(self, '提示信息', '退房失败', QMessageBox.Ok)
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