# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_book.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import new_checkin
import book_via_room
import sys
import pymysql
import config

class Ui_Form(QWidget):
    def setupUi(self, Form, room_num):
        self.Form = Form
        self.room_num = room_num
        Form.setObjectName("Form")
        Form.resize(500, 400)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 310, 100, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFocus()
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 310, 100, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(185, 40, 150, 30))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(99, 91, 300, 200))
        self.textEdit.setObjectName("textEdit")

        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)        

        # 设置入住按钮信号
        self.pushButton.clicked.connect(self.book)

        # 设置取消预订按钮信号
        self.pushButton_2.clicked.connect(self.checkin)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "房态"))
        self.pushButton.setText(_translate("Form", "预定此房"))
        self.pushButton_2.setText(_translate("Form", "办理入住"))
        self.label.setText(_translate("Form", "空房信息"))
        self.show_room_info()

    def show_room_info(self):
        #链接数据库
        db = pymysql.connect(host=config.HOST,
                                user=config.USER,
                                password=config.PASSWORD,
                                database = "hotelDB",
                                charset = "utf8")

        cursor = db.cursor()
        try:
            sql_select = "select * from room_info where 房间号='%s'"%self.room_num
            cursor.execute(sql_select)
            data = cursor.fetchone()
            if not data:
                QMessageBox.information(self, '提示信息', '没有此房间信息', QMessageBox.Ok)
                return
            self.textEdit.setPlainText("房间号:%s\n房间类型:%s\n价格:%s\n会员价:%s\n押金:%s\n房间状态:%s\n楼层:%s"\
                %(data[1],data[0],data[3],data[4],data[2],data[5],data[6]))
        except Exception as e:
            print("查询失败",e)
        cursor.close()
        db.close()

    def checkin(self):
        checkin_window = QDialog()
        ui = new_checkin.Ui_checkin_window()
        ui.setupUi(checkin_window,self.room_num)
        checkin_window.show()
        self.Form.close()
        checkin_window.exec_()

    def book(self):
        book_window = QDialog()
        ui = book_via_room.Ui_room_book_2()
        ui.setupUi(book_window,self.room_num)
        book_window.show()
        self.Form.close()
        book_window.exec_()
        



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
