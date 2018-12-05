# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog
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
    # def focusInEvent(self,e):
    #     print('focusInEvent')
    # def focusOutEvent(self,e):
    #     self.inp_text_signal.emit("移出")   #发送信号

class Ui_checkin_window(QWidget):
    def __init__(self):
        super().__init__()
        self.sex1 = '男'
        self.sex2 = ''
        self.setupUi(self)

    def setupUi(self, checkin_window):
        self.window = checkin_window
        #设置窗体
        checkin_window.setObjectName("checkin_window")
        checkin_window.resize(440, 400)
        checkin_window.setInputMethodHints(QtCore.Qt.ImhNone)
        # checkin_window.setStyleSheet("QWidget{background-color:skyblue};")
        checkin_window.setStyleSheet("QWidget{background-image:url('image/sand.jpg')};")

        #创建左侧标签
        self.label_name = QtWidgets.QLabel(checkin_window)
        self.label_name.setGeometry(QtCore.QRect(92, 40, 51, 23))
        self.label_name.setObjectName("label_name")
        self.label_name.setStyleSheet("QWidget{background:transparent};")
        self.label_sex = QtWidgets.QLabel(checkin_window)
        self.label_sex.setGeometry(QtCore.QRect(92, 72, 51, 23))
        self.label_sex.setObjectName("label_sex")
        self.label_sex.setStyleSheet("QWidget{background:transparent};")
        self.label_ID = QtWidgets.QLabel(checkin_window)
        self.label_ID.setGeometry(QtCore.QRect(92, 111, 60, 23))
        self.label_ID.setObjectName("label_ID")
        self.label_ID.setStyleSheet("QWidget{background:transparent};")
        self.label_phone = QtWidgets.QLabel(checkin_window)
        self.label_phone.setGeometry(QtCore.QRect(92, 158, 45, 23))
        self.label_phone.setObjectName("label_phone")
        self.label_phone.setStyleSheet("QWidget{background:transparent};")
        self.label_room_number = QtWidgets.QLabel(checkin_window)
        self.label_room_number.setGeometry(QtCore.QRect(92, 201, 60, 23))
        self.label_room_number.setObjectName("label_room_number")
        self.label_room_number.setStyleSheet("QWidget{background:transparent};")
        self.label_people_count = QtWidgets.QLabel(checkin_window)
        self.label_people_count.setGeometry(QtCore.QRect(92, 241, 60, 23))
        self.label_people_count.setObjectName("label_people_count")
        self.label_people_count.setStyleSheet("QWidget{background:transparent};")
        self.label_day_leave = QtWidgets.QLabel(checkin_window)
        self.label_day_leave.setGeometry(QtCore.QRect(92, 280, 60, 23))
        self.label_day_leave.setObjectName("label_day_leave")
        self.label_day_leave.setStyleSheet("QWidget{background:transparent};")
        
        # 创建姓名输入框
        self.lineEdit_name = QtWidgets.QLineEdit(checkin_window)
        self.lineEdit_name.setGeometry(QtCore.QRect(156, 40, 181, 27))
        self.lineEdit_name.setObjectName("lineEdit_name")

        # 创建性别选择按钮(男)
        self.radioButton_2 = QtWidgets.QRadioButton(checkin_window)
        self.radioButton_2.setGeometry(QtCore.QRect(161, 70, 45, 28))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet("QRadioButton{background:transparent};")

         # 创建性别选择按钮(女)
        self.radioButton = QtWidgets.QRadioButton(checkin_window)
        self.radioButton.setGeometry(QtCore.QRect(212, 70, 45, 28))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setStyleSheet("QRadioButton{background:transparent};")

         # 组合性别选择按钮以实现２选１
        self.buttonGroup = QtWidgets.QButtonGroup(checkin_window)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_2)
        self.buttonGroup.addButton(self.radioButton)

        #创建身份证号输入框,手机号输入框,房间选择框,离店时间框
        self.lineEdit_ID = QtWidgets.QLineEdit(checkin_window)
        self.lineEdit_ID.setGeometry(QtCore.QRect(157, 110, 181, 27))
        self.lineEdit_ID.setText("")
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.lineEdit_phone = QtWidgets.QLineEdit(checkin_window)
        self.lineEdit_phone.setGeometry(QtCore.QRect(157, 156, 181, 27))
        self.lineEdit_phone.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_phone.setPlaceholderText("")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.lineEdit_room = QtWidgets.QLineEdit(checkin_window)
        self.lineEdit_room.setGeometry(QtCore.QRect(157, 200, 181, 27))
        self.lineEdit_room.setObjectName("lineEdit_room")

        # 姓名输入限制，不允许有数字和特殊字符，允许中间有一个空格
        reg1 = QRegExp('^[^(\d|\W)]+( ?[^(\d|\W)]+)*$')
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg1)
        self.lineEdit_name.setValidator(pValidator)

        s ="^[1-9][0-9]{5}(19|20)[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|30|31)|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}([0-9]|x|X)$"
        # 身份证号码限制
        reg2 = QRegExp(s)
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg2)
        self.lineEdit_ID.setValidator(pValidator)

        # 手机号正则限制
        reg3 = QRegExp("^1[0-9]{10}$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg3)
        self.lineEdit_phone.setValidator(pValidator)

        # 房间号正则限制
        reg4 = QRegExp("^\d+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg4)
        self.lineEdit_room.setValidator(pValidator)

        # 创建人数选择旋钮
        self.spinBox = QtWidgets.QSpinBox(checkin_window)
        self.spinBox.setGeometry(QtCore.QRect(157, 240, 61, 27))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(1)

        #创建离店时间框
        self.lineEdit_day_leave = MyLineEdit(checkin_window)
        self.lineEdit_day_leave.setGeometry(QtCore.QRect(157, 279, 181, 27))
        self.lineEdit_day_leave.setMaxLength(50)
        self.lineEdit_day_leave.setFrame(True)
        self.lineEdit_day_leave.setObjectName("lineEdit_day_leave")

        # 创建日历小图标
        self.cal_btn = QtWidgets.QPushButton(checkin_window)
        self.cal_btn.setGeometry(QtCore.QRect(315, 282, 21, 21))
        self.cal_btn.setObjectName("cal_btn")
        self.cal_btn.setText("")
        self.cal_btn.setStyleSheet("QWidget{background:transparent};")
        # self.cal_btn.setStyleSheet("background-image: url(:/pic/image/cal.gif);")
        self.cal_btn.setStyleSheet("QPushButton{border-image: url(image/cal.gif)};")
        self.cal_btn.setToolTip('点击选择日期')

        # 设置性别选择按钮点击事件
        self.radioButton_2.toggled.connect(lambda :self.btnstate(self.radioButton_2))
        self.radioButton.toggled.connect(lambda :self.btnstate(self.radioButton))

        #　创建提交和取消按钮
        self.pushButton_2 = QtWidgets.QPushButton(checkin_window)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 341, 85, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(checkin_window)
        self.pushButton.setGeometry(QtCore.QRect(280, 341, 85, 33))
        self.pushButton.setObjectName("pushButton")

        self.cal_btn.raise_()

        # 重译Ui窗口
        self.retranslateUi(checkin_window)
        QtCore.QMetaObject.connectSlotsByName(checkin_window)

        # 提交按钮绑定入住信息验证及录入函数
        self.pushButton_2.clicked.connect(self.checkin)
        # 取消按钮调用退出提示函数
        self.pushButton.clicked.connect(self.window_close)

        #点击日历图标按钮调用日历显示函数
        self.cal_btn.clicked.connect(self.calendar_show) 
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, checkin_window):
        _translate = QtCore.QCoreApplication.translate
        checkin_window.setWindowTitle(_translate("checkin_window", "入住登记"))
        self.label_people_count.setText(_translate("checkin_window", "入住人数"))
        self.label_room_number.setText(_translate("checkin_window", "入住房号"))
        self.label_name.setText(_translate("checkin_window", "姓　名"))
        self.label_ID.setText(_translate("checkin_window", "身份证号"))
        self.label_sex.setText(_translate("checkin_window", "性　别"))
        self.label_day_leave.setText(_translate("checkin_window", "退房时间"))
        self.label_phone.setText(_translate("checkin_window", "手机号"))
        self.lineEdit_name.setPlaceholderText(_translate("checkin_window", "请输入真实姓名"))
        self.lineEdit_ID.setPlaceholderText(_translate("checkin_window", "18位身份证号"))
        self.radioButton_2.setText(_translate("checkin_window", "男"))
        self.radioButton.setText(_translate("checkin_window", "女"))
        self.pushButton_2.setText(_translate("checkin_window", "确定"))
        self.pushButton.setText(_translate("checkin_window", "取消"))

    #定义日历窗口显示函数
    def calendar_show(self):
        calendar_window = QDialog()
        UI_cal = Ui_Dialog()
        UI_cal.setupUi(calendar_window)
        calendar_window.show()
        calendar_window.exec_()
        date = UI_cal.calendarWidget.selectedDate()
        self.lineEdit_day_leave.setText(date.toString("yyyy-MM-dd"))

    #性别选择函数
    def btnstate(self,btn):
        if btn.text() == '男':
            if btn.isChecked() == True:
                self.sex1 = btn.text()
            else:
                self.sex2 = btn.text()
        if btn.text() == '女':
            if btn.isChecked() == True:
                self.sex1 = btn.text()
            else:
                self.sex2 = btn.text()
        
    #　定义提交验证函数
    def checkin(self):
        name = self.lineEdit_name.text().strip(' ')
        gender = self.sex1
        ID_num = self.lineEdit_ID.text()
        room_num = self.lineEdit_room.text()
        phone_num = self.lineEdit_phone.text()
        people_count = int(self.spinBox.value())
        end_date = self.lineEdit_day_leave.text()
        if not name:
            QMessageBox.warning(self,'警告','姓名不能为空', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        if not ID_num:
            QMessageBox.warning(self,'警告','身份证不能为空', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        if len(ID_num) != 18:
            # QMessageBox.warning(self, '提示信息', '身份证号长度不匹配', QMessageBox.Ok)
            QMessageBox.warning(self,'警告','身份证号输入有误', \
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
        if not end_date:
            QMessageBox.information(self,'提示','请选择离店日期', \
                QMessageBox.Ok, QMessageBox.Ok)
            return  
        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
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
            sql_insert = "insert into check_in_info(name, gender,\
                        ID_num,room_num, phone_num, people_count, end_date)\
                        values('%s','%s','%s','%s','%s','%d', '%s')"\
                        %(name,gender,ID_num,\
                        room_num,phone_num,people_count,end_date)
            cursor.execute(sql_insert)

            sql_update = "update room_info set 房间状态='入住' where 房间号='%s'"%room_num
            cursor.execute(sql_update)

            sql_select = "select 押金,价格,会员价 from room_info where 房间号='%s'"%room_num
            cursor.execute(sql_select)
            data = cursor.fetchone()
            if not data:
                return
            else:
                deposit, price, vip_price = data

            sql_update = "update check_in_info set deposit='%d',price='%d',vip_price='%d'\
                        where room_num='%s'"%(deposit, price, vip_price, room_num)
            cursor.execute(sql_update)
            db.commit()

            res = QMessageBox.information(self,\
                    '提示信息', '入住登记成功！\n顾客姓名:%s\n房间号:%s'%(name,room_num),\
                    QMessageBox.Ok)
            print('入住信息录入成功')
            # 登记成功，清除部分信息
            if res == QMessageBox.Ok:
                self.lineEdit_name.setText('')
                self.lineEdit_ID.setText('')
                self.lineEdit_phone.setText('')
                self.lineEdit_room.setText('')
                self.lineEdit_day_leave.setText('')
                self.spinBox.setValue(1)
                self.radioButton_2.setChecked(True)
        except Exception as e:
            db.rollback()
            print("入住信息录入失败",e)
        cursor.close()
        db.close()

    #定义取消按钮槽函数
    def window_close(self): 
        name = self.lineEdit_name.text()
        ID_num = self.lineEdit_ID.text()
        room_num = self.lineEdit_room.text()
        phone_num = self.lineEdit_phone.text()
        end_date = self.lineEdit_day_leave.text()

        content = name + ID_num + room_num + phone_num + end_date
        print(content)
        if content:
            reply = QMessageBox.question(self, '退出确认',
                "登记尚未完成，是否要退出?", QMessageBox.Yes | 
                QMessageBox.No, QMessageBox.Yes) 
            if reply == QMessageBox.Yes:                
               self.window.close()
            else:
                pass
        else:
            self.window.close()
            # sys.exit()

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


#调试函数
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # form = QWidget()
    ui = Ui_checkin_window()
    # ui.setupUi(form)
    ui.show()
    sys.exit(app.exec_())
