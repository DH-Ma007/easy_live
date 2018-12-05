# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room_book.ui'
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

#重新定义LineEdit类，并定义信号，以便主程序处理
class MyLineEdit(QtWidgets.QLineEdit):
    inp_text_signal = QtCore.pyqtSignal(str)   #定义信号
    def __init__(self, parent):
        super(MyLineEdit,self).__init__(parent)
    def keyPressEvent(self, event):       
        event.ignore()

class Ui_room_book_2(QWidget):
    def __init__(self):
        super().__init__()

    def setupUi(self, room_book_2,room_num):
        self.room_num = room_num
        self.book_window = room_book_2
        room_book_2.setObjectName("room_book_2")
        room_book_2.resize(400, 305)
        room_book_2.setStyleSheet("QWidget{background-image:url('image/sand.jpg')};")

        self.lineEdit_name = QtWidgets.QLineEdit(room_book_2)
        self.lineEdit_name.setGeometry(QtCore.QRect(130, 59, 158, 27))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.setFocus()
        self.lineEdit_tel = QtWidgets.QLineEdit(room_book_2)
        self.lineEdit_tel.setGeometry(QtCore.QRect(130, 100, 158, 27))
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.lineEdit_room = MyLineEdit(room_book_2)
        self.lineEdit_room.setGeometry(QtCore.QRect(130, 141, 158, 27))
        self.lineEdit_room.setObjectName("lineEdit_room")
        self.lineEdit_room.setText(room_num)
        self.lineEdit_day_come = MyLineEdit(room_book_2)
        self.lineEdit_day_come.setGeometry(QtCore.QRect(130, 182, 158, 27))
        self.lineEdit_day_come.setText("")
        self.lineEdit_day_come.setObjectName("lineEdit_day_come")
        self.label_tel = QtWidgets.QLabel(room_book_2)
        self.label_tel.setGeometry(QtCore.QRect(64, 101, 51, 23))
        self.label_tel.setObjectName("label_tel")
        self.label_room_num = QtWidgets.QLabel(room_book_2)
        self.label_room_num.setGeometry(QtCore.QRect(64, 143, 61, 23))
        self.label_room_num.setObjectName("label_room_num")
        self.label_name = QtWidgets.QLabel(room_book_2)
        self.label_name.setGeometry(QtCore.QRect(64, 60, 59, 23))
        self.label_name.setObjectName("label_name")
        self.label_day_come = QtWidgets.QLabel(room_book_2)
        self.label_day_come.setGeometry(QtCore.QRect(64, 184, 61, 23))
        self.label_day_come.setObjectName("label_day_come")

        self.label_name.setStyleSheet("QWidget{background:transparent};")
        self.label_tel.setStyleSheet("QWidget{background:transparent};")
        self.label_room_num.setStyleSheet("QWidget{background:transparent};")
        self.label_day_come.setStyleSheet("QWidget{background:transparent};")

        #创建日历按钮
        self.pushButton = QtWidgets.QPushButton(room_book_2)
        self.pushButton.setGeometry(QtCore.QRect(263, 184, 22, 22))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{border-image: url(image/cal.gif)};")
        self.pushButton.setToolTip('点击选择日期')

        self.pushButton_5 = QtWidgets.QPushButton(room_book_2)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 240, 90, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        # 姓名输入限制，不允许有数字和特殊字符，允许中间有一个空格
        reg1 = QRegExp('^[^(\d|\W)]+( ?[^(\d|\W)]+)*$')
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg1)
        self.lineEdit_name.setValidator(pValidator)

        # 手机号正则限制
        reg2 = QRegExp("^1[0-9]{10}$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg2)
        self.lineEdit_tel.setValidator(pValidator)

        # 房间号正则限制
        reg3 = QRegExp("^\d+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg3)
        self.lineEdit_room.setValidator(pValidator)

        #绑定预定信息录入槽函数
        self.pushButton_5.clicked.connect(self.book)

         #点击日历图标按钮调用日历显示函数
        self.pushButton.clicked.connect(self.calendar_show) 

        self.retranslateUi(room_book_2)
        QtCore.QMetaObject.connectSlotsByName(room_book_2)

    def retranslateUi(self, room_book_2):
        _translate = QtCore.QCoreApplication.translate
        room_book_2.setWindowTitle(_translate("room_book_2", "房间预定"))
        self.pushButton_5.setText(_translate("room_book_2", "确定"))
        self.lineEdit_name.setPlaceholderText(_translate("room_book_2", "请输入姓名"))
        self.lineEdit_day_come.setPlaceholderText(_translate("room_book_2", "请选择日期"))
        self.label_tel.setText(_translate("room_book_2", "手机号"))
        self.label_room_num.setText(_translate("room_book_2", "预定房号"))
        self.label_name.setText(_translate("room_book_2", "宾客姓名"))
        self.label_day_come.setText(_translate("room_book_2", "入住日期"))

    # 定义预定槽函数
    def book(self):
        name = self.lineEdit_name.text()
        phone_num = self.lineEdit_tel.text()
        room_num = self.lineEdit_room.text()
        arrival_time = self.lineEdit_day_come.text()

        if not name:
            QMessageBox.warning(self,'警告','姓名不能为空', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        if not phone_num:
            QMessageBox.warning(self,'警告','手机号不能为空', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        if len(phone_num) != 11:
            # QMessageBox.warning(self, '提示信息', '身份证号长度不匹配', QMessageBox.Ok)
            QMessageBox.warning(self,'警告','手机号输入有误', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        if not room_num:
            QMessageBox.information(self,'提示','请选择房间号', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        if not arrival_time:
            QMessageBox.information(self,'提示','请选择离店日期', \
                QMessageBox.Ok, QMessageBox.Ok)
            return  

        db = pymysql.connect(host = "localhost", user = "root",\
                        password = "123456", database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()

        sql_select = "select * from room_info where 房间号 = '%s'" % room_num
        cursor.execute(sql_select)
        data = cursor.fetchone()
        if not data:
            QMessageBox.warning(self,'警告', '没有%s这个房间'%room_num,QMessageBox.Ok)
            return
        elif data[5] == '已预定':
            QMessageBox.information(self, '预定失败', '此房间已经被预定', QMessageBox.Ok)
            return
        elif data[5] == '入住':
            QMessageBox.information(self, '预定失败', '此房间已经有客', QMessageBox.Ok)
            return
        try:
            sql_insert = "insert into book_info(name, phone_num,\
                        room_num, end_date) values('%s', '%s', '%s', '%s')"\
                        %(name, phone_num, room_num, arrival_time)
            cursor.execute(sql_insert)
            sql_update = "update room_info set 房间状态='已预定' where 房间号='%s'"%room_num
            cursor.execute(sql_update)
            db.commit()

        except Exception as e:
            db.rollback()
            print("预定信息录入失败")
        cursor.close()
        db.close()

        res = QMessageBox.information(self,\
                    '消息', '预定登记完成！\n姓名:%s\n房间号:%s\n到店时间:%s'%\
                    (name,room_num,arrival_time),QMessageBox.Ok)
        print('预定信息录入成功')
        self.book_window.close()
        # 登记成功，清除部分信息
        # if res == QMessageBox.Ok:
        #     self.lineEdit_name.setText('')
        #     self.lineEdit_tel.setText('')
        #     self.lineEdit_room.setText('')
        #     self.lineEdit_day_come.setText('')

    #定义日历窗口显示函数
    def calendar_show(self):
        calendar_window = QDialog()
        UI_cal = Ui_Dialog()
        UI_cal.setupUi(calendar_window)
        calendar_window.show()
        calendar_window.exec_()
        date = UI_cal.calendarWidget.selectedDate()
        self.lineEdit_day_come.setText(date.toString("yyyy-MM-dd"))

#定义一个日历窗体类
class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(411, 285)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 411, 281))
        self.calendarWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Dialog)
        self.calendarWidget.clicked['QDate'].connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.calendarWidget.clicked['QDate'].connect(self.send_date)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "calendar"))

    # 定义日期选择事件
    def send_date(self):
        # date = self.calendarWidget.selectedDate()      
        # self.obj.setText(date.toString("yyyy-MM-dd"))
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_room_book_2()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())