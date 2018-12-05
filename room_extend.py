# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room_extend.ui'
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
import config

#重新定义LineEdit类，并定义信号，以便主程序处理
class MyLineEdit(QtWidgets.QLineEdit):
    inp_text_signal = QtCore.pyqtSignal(str)   #定义信号
    def __init__(self, parent):
        super(MyLineEdit,self).__init__(parent)
    def keyPressEvent(self, event):       
        event.ignore()

class Ui_Dialog(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("QWidget{background-image:url('image/sand.jpg')};")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(97, 100, 212, 74))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = MyLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(200, 211, 65, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 211, 65, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(125, 15, 200, 40))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label.setStyleSheet("QWidget{background:transparent};")
        self.label_2.setStyleSheet("QWidget{background:transparent};")
        self.label_3.setStyleSheet("QWidget{background:transparent};")

        # 创建日历小图标
        self.cal_btn = QtWidgets.QPushButton(Dialog)
        self.cal_btn.setGeometry(QtCore.QRect(284, 145, 21, 21))
        self.cal_btn.setObjectName("cal_btn")
        self.cal_btn.setText("")
        self.cal_btn.setToolTip('点击选择日期')
        self.cal_btn.setStyleSheet("QWidget{background:transparent};")
        self.cal_btn.setStyleSheet("QPushButton{border-image: url(image/cal.gif)};")

        # 房间号正则限制
        reg = QRegExp("^\d+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.lineEdit.setValidator(pValidator)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #定义日历按钮调槽函数
        self.cal_btn.clicked.connect(self.calendar_show) 
        #定义确认按钮槽信号
        self.pushButton.clicked.connect(self.extend)
        #定义取消按钮槽信号
        self.pushButton_2.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "续住"))
        self.label.setText(_translate("Dialog", "房间号"))
        self.label_2.setText(_translate("Dialog", "离店日期"))
        self.pushButton.setText(_translate("Dialog", "确认"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.label_3.setText(_translate("Dialog", "续住管理界面"))

    def extend(self):
        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()
        room_num = self.lineEdit.text()
        end_date = self.lineEdit_2.text()
        if not room_num:
            QMessageBox.information(self, '提示', '请输入房间号', QMessageBox.Ok)
            return
        if not end_date:
            QMessageBox.information(self, '提示', '请选择离店日期', QMessageBox.Ok)
            return
        try:
            sql_select = "select * from check_in_info where room_num = %s"%room_num
            cursor.execute(sql_select)
            data = cursor.fetchone()
            if not data:
                QMessageBox.information(self, '提示', '没有此房间入住信息', QMessageBox.Ok)
                return
            # print('当前',data[-1])
            # print('续住',end_date)
            cur_year = data[-1][:4]
            cur_month = data[-1][5:7]
            cur_day = data[-1][8:]
            # print(cur_year,cur_month,cur_day)
            new_year = end_date[:4]
            new_month = end_date[5:7]
            new_day = end_date[8:]
            # print(new_year,new_month,new_day)

            if int(cur_year)>int(new_year):
                QMessageBox.warning(self, '警告', '续住日期不能早于当前日期！\n%s'%data[-1], QMessageBox.Ok)
                return
            if int(cur_month)>int(new_month):
                QMessageBox.warning(self, '警告', '续住日期不能早于当前日期！\n%s'%data[-1], QMessageBox.Ok)
                return
            if int(cur_day)>int(new_day):
                QMessageBox.warning(self, '警告', '续住日期不能早于当前日期！\n%s'%data[-1], QMessageBox.Ok)
                return
            if int(cur_day)==int(new_day):
                QMessageBox.warning(self, '警告', '续住日期不能和当前日期相同！\n%s'%data[-1], QMessageBox.Ok)
                return

            sql_update = "update check_in_info set end_date = '%s'\
                    where room_num = '%s'"%(end_date, room_num)
            cursor.execute(sql_update)
            db.commit()
            print("修改离店日期成功")
            QMessageBox.information(self, '提示', '续住成功\n延期至%s'%end_date, QMessageBox.Ok)
        except Exception as e:
            db.rollback()
            print("离店日期修改失败")
        cursor.close()
        db.close()

    #定义日历窗口显示函数
    def calendar_show(self):
        calendar_window = QDialog()
        UI_cal = Ui_Cal_Dialog()
        UI_cal.setupUi(calendar_window)
        calendar_window.show()
        calendar_window.exec_() #窗口关闭后才执行后面代码
        date = UI_cal.calendarWidget.selectedDate()
        self.lineEdit_2.setText(date.toString("yyyy-MM-dd"))

#定义一个日历窗体类
class Ui_Cal_Dialog(QWidget):
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



