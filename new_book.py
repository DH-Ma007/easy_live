# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_book.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import new_checkin
import sys
import pymysql
import config

class Ui_Form(QWidget):
    def setupUi(self, Form, room_num):
        self.Form = Form
        self.room_num = room_num
        Form.setObjectName("Form")
        Form.resize(500, 400)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(99, 91, 300, 200))
        self.textEdit.setObjectName("textEdit")
        # self.textEdit.setStyleSheet("QWidget{background:transparent};")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 310, 100, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFocus()
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 310, 100, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 40, 110, 23))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)        

        # 设置入住按钮信号
        self.pushButton.clicked.connect(self.checkin)

        # 设置取消预订按钮信号
        self.pushButton_2.clicked.connect(self.cancel_book)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "房态"))
        self.pushButton.setText(_translate("Form", "办理入住"))
        self.pushButton_2.setText(_translate("Form", "取消预订"))
        self.label.setText(_translate("Form", "预订信息:"))

        # 显示预订信息
        self.show_book_info()


    def show_book_info(self):
        self.textEdit.clear()
        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()
        try:
            sql_select = "select * from book_info where room_num = '%s'"%self.room_num
            cursor.execute(sql_select)
            data = cursor.fetchone()
            if not data:
                QMessageBox.information(self, '提示信息', '没有预定信息', QMessageBox.Yes)
                return
            newtime = data[4].strftime('%Y-%m-%d %H:%M:%S')
            self.textEdit.setPlainText("姓名:%s\n手机号:%s\n房间号:%s\n预定时间:%s\n计划入住时间:%s\n"\
                %(data[1],data[2],data[3],newtime,data[5]))
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



    def cancel_book(self):
        reply = QMessageBox.question(self, '提示信息', '确认取消预订?', QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            db = pymysql.connect(host = config.HOST, user = config.USER,\
                            password = config.PASSWORD, database = "hotelDB",\
                            charset = "utf8")
            cursor = db.cursor()
            try:
                sql_update = "update room_info set 房间状态='空闲' where 房间号='%s'"%self.room_num
                cursor.execute(sql_update)
                db.commit()
                QMessageBox.information(self, '提示信息', '预订取消成功', QMessageBox.Yes)
            except Exception as e:
                print("预订取消失败",e)
            cursor.close()
            db.close()
        else:
            pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
