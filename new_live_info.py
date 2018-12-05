# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_live.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import new_change
import new_extend
import sys,time,re
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
        self.pushButton.setGeometry(QtCore.QRect(130, 320, 70, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFocus()
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(215, 320, 70, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 320, 70, 30))
        self.pushButton_3.setObjectName("pushButton_2")
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

        # 设置续住按钮信号
        self.pushButton.clicked.connect(self.extend)
        # 设置换房按钮信号
        self.pushButton_2.clicked.connect(self.change)
        # 设置退房按钮信号
        self.pushButton_3.clicked.connect(self.checkout)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "房态"))
        self.pushButton.setText(_translate("Form", "续住"))
        self.pushButton_2.setText(_translate("Form", "换房"))
        self.pushButton_3.setText(_translate("Form", "退房"))
        self.label.setText(_translate("Form", "入住信息:"))

        # 显示预订信息
        self.show_live_info()

    def show_live_info(self):
        self.textEdit.clear()
        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()
        try:
            sql_select = "select * from check_in_info where room_num = '%s'"%self.room_num
            cursor.execute(sql_select)
            data = cursor.fetchone()
            if not data:
                QMessageBox.information(self, '提示信息', '没有入住信息', QMessageBox.Ok)
                return
            come_time = data[-2].strftime('%Y-%m-%d %H:%M:%S')
            self.textEdit.setPlainText("姓名:%s\n手机号:%s\n身份证号:%s\n房间号:%s     押金:%s\n房价:%s     会员价:%s\n入住人数:%s\n入住时间:%s\n房间到期:%s\n"\
            %(data[1],data[2],data[3],data[5],data[6],data[7],data[8],data[9],come_time,data[11]))
        except Exception as e:
            print("查询失败",e)
        cursor.close()
        db.close()


    def extend(self):
        extend_window = QDialog()
        ui = new_extend.Ui_Dialog()
        ui.setupUi(extend_window,self.room_num)
        extend_window.show()
        self.Form.close()
        extend_window.exec_()

    def change(self):
        change_window = QDialog()
        ui = new_change.Ui_Dialog()
        ui.setupUi(change_window,self.room_num)
        change_window.show()
        self.Form.close()
        change_window.exec_()

    def checkout(self):
        data = self.textEdit.toPlainText()
        if not data:
            return
        deposit = re.findall('押金:\d+',data)
        if not deposit:
            print("未匹配到内容")
            return
        back_cash = deposit[0][3:]
        reply = QMessageBox.question(self, '退房确认',
            "房号:%s\n押金:%s\n\n确认退房?"%(self.room_num,back_cash), QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                db = pymysql.connect(host = config.HOST, user = config.USER,\
                            password = config.PASSWORD, database = "hotelDB",\
                            charset = "utf8")        
                cursor = db.cursor()
                sql_update = "update room_info set 房间状态='空闲' where 房间号='%s'"%self.room_num
                cursor.execute(sql_update)
                sql_update = "update check_in_info set end_date = '%s' where room_num = '%s'"%\
                            (time.ctime(), self.room_num)
                cursor.execute(sql_update)
                sql_insert = "insert into live_history(name, gender, ID_num,room_num,\
                        deposit, price, phone_num, people_count, start_date, end_date)\
                        select name, gender, ID_num, room_num, deposit, price, phone_num,\
                        people_count, start_date, end_date from check_in_info where\
                        room_num = '%s'"%self.room_num
                cursor.execute(sql_insert)
                sql_delete = "delete from check_in_info where room_num = '%s'"%self.room_num
                cursor.execute(sql_delete)
                db.commit()
                print("退房成功")
                QMessageBox.information(self, '提示信息', '%s退房成功'%self.room_num, QMessageBox.Ok)
            except Exception as e:
                db.rollback()
                print("退房失败",e)
                QMessageBox.information(self, '提示信息', '退房失败', QMessageBox.Ok)
            cursor.close()
            db.close()
            self.textEdit.setPlainText('')
            self.Form.close()
        else:
            return
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
