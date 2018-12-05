# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hotel.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import login_register
import modify_password
import room_status
import room_book
import room_checkin
import room_change
import room_extend
import room_checkout
import vip_manage
import query_info


class Ui_Form(QWidget):
    def __init__(self,name):
        super().__init__()
        self.setupUi(self,name)

    #设置窗体居中显示
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #窗体界面布局
    def setupUi(self, Form, name):
        self.Form = Form
        self.name = name
        self.center()
        Form.setObjectName("Form")
        Form.resize(600, 420)

        #设置背景图
        # self.window_pale = QtGui.QPalette() 
        # self.window_pale.setBrush(self.backgroundRole(),\
        #     QtGui.QBrush(QtGui.QPixmap("image/Dubai.jpg"))) 
        # self.setPalette(self.window_pale)

        self.label = QLabel('',self)
        self.gif = QtGui.QMovie('image/Dubai.jpg')
        self.label.setScaledContents(True)
        self.label.setMovie(self.gif)
        self.gif.start()

        # self.UI.setStyleSheet("QWidget{background-image:url(image/fan.jpg)}")

        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setGeometry(320, 110, 211, 231)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_roomstatus = QPushButton(self.layoutWidget)
        self.btn_roomstatus.setObjectName("btn_roomstatus")
        self.gridLayout.addWidget(self.btn_roomstatus, 0, 0, 1, 1)
        self.btn_checkout = QPushButton(self.layoutWidget)
        self.btn_checkout.setObjectName("btn_checkout")
        self.gridLayout.addWidget(self.btn_checkout, 2, 1, 1, 1)
        self.btn_checkin = QPushButton(self.layoutWidget)
        self.btn_checkin.setObjectName("btn_checkin")
        self.gridLayout.addWidget(self.btn_checkin, 1, 0, 1, 1)
        self.btn_book = QPushButton(self.layoutWidget)
        self.btn_book.setObjectName("btn_book")
        self.gridLayout.addWidget(self.btn_book, 0, 1, 1, 1)
        self.btn_change = QPushButton(self.layoutWidget)
        self.btn_change.setObjectName("btn_change")
        self.gridLayout.addWidget(self.btn_change, 1, 1, 1, 1)
        self.btn_extend = QPushButton(self.layoutWidget)
        self.btn_extend.setObjectName("btn_extend")
        self.gridLayout.addWidget(self.btn_extend, 2, 0, 1, 1)
        self.btn_vip = QPushButton(self.layoutWidget)
        self.btn_vip.setObjectName("btn_vip")
        self.gridLayout.addWidget(self.btn_vip, 3, 0, 1, 1)
        self.btn_query = QPushButton(self.layoutWidget)
        self.btn_query.setObjectName("btn_query")
        self.gridLayout.addWidget(self.btn_query, 3, 1, 1, 1)
        self.title = QLabel(Form)
        self.title.setGeometry(30, 10, 350, 40)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setGeometry(40, 90, 230, 250)
        self.graphicsView.setStyleSheet("QGraphicsView{background-image:url(image/recept.jpg)}")
        self.graphicsView.setObjectName("graphicsView")
        self.btn_exit = QPushButton(Form)
        self.btn_exit.setGeometry(490, 380, 99, 27)
        self.btn_exit.setObjectName("btn_exit")

        self.retranslateUi(Form,name)
        QMetaObject.connectSlotsByName(Form)

        #注销按钮并设置鼠标悬停提示
        self.log_out_btn = QPushButton('注销', self)
        self.log_out_btn.setToolTip('这是注销按钮')
        #调整按钮尺寸为默认宽高
        self.log_out_btn.resize(35,25)
        #设置按钮在窗口中位置距左500距上0
        self.log_out_btn.move(500, 12)
        # log_out_btn.setStyleSheet('QPushButton{background-image:url(image/logout.jpg);}')
        self.log_out_btn.setStyleSheet('QPushButton{background-color:grey;}')

        #改密按钮并设置鼠标悬停提示
        self.modify_pwd_btn = QPushButton('改密', self)
        self.modify_pwd_btn.setToolTip('点击修改密码')
        #调整按钮尺寸为默认宽高
        self.modify_pwd_btn.resize(35,25)
        #设置按钮在窗口中位置距左500距上0
        self.modify_pwd_btn.move(540, 12)
        self.modify_pwd_btn.setStyleSheet('QPushButton{background-color:grey;}')

        #添加事件
        self.log_out_btn.clicked.connect(self.return_to_login)
        self.modify_pwd_btn.clicked.connect(self.modify_pwd)
        self.btn_roomstatus.clicked.connect(self.jump_to_roomstatus)
        self.btn_book.clicked.connect(self.jump_to_room_book)
        self.btn_checkin.clicked.connect(self.jump_to_checkin)
        self.btn_change.clicked.connect(self.jump_to_room_change)
        self.btn_extend.clicked.connect(self.jump_to_room_extend)
        self.btn_checkout.clicked.connect(self.jump_to_checkout)
        self.btn_vip.clicked.connect(self.jump_to_vip_manage)
        self.btn_query.clicked.connect(self.jump_to_info_query)
        self.btn_exit.clicked.connect(self.close)


    def retranslateUi(self, Form, name):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "欢迎,%s"%name))
        self.btn_roomstatus.setText(_translate("Form", "实时房态"))
        self.btn_checkout.setText(_translate("Form", "结算退房"))
        self.btn_checkin.setText(_translate("Form", "入住登记"))
        self.btn_book.setText(_translate("Form", "房间预订"))
        self.btn_change.setText(_translate("Form", "更换房间"))
        self.btn_extend.setText(_translate("Form", "房间续住"))
        self.btn_vip.setText(_translate("Form", "会员管理"))
        self.btn_query.setText(_translate("Form", "信息查询"))
        self.title.setText(_translate("Form", "易住酒店管理系统"))
        self.btn_exit.setText(_translate("Form", "退出系统"))

    #定义跳转至二级界面函数
    def jump_to_roomstatus(self):
        roomstatus_window = QDialog()
        ui = room_status.Ui_room()
        ui.setupUi(roomstatus_window)
        roomstatus_window.show()
        roomstatus_window.exec_()
    def jump_to_room_book(self):
        room_book_window = QDialog()
        ui = room_book.Ui_room_book_2()
        ui.setupUi(room_book_window)
        room_book_window.show()
        room_book_window.exec_()
    def jump_to_checkin(self):
        checkin_window = QDialog()
        ui = room_checkin.Ui_checkin_window()
        ui.setupUi(checkin_window)
        checkin_window.show()
        checkin_window.exec_()
    def jump_to_room_change(self):
        room_change_window = QDialog()
        ui = room_change.Ui_Dialog()
        ui.setupUi(room_change_window)
        room_change_window.show()
        room_change_window.exec_()
    def jump_to_room_extend(self):
        room_extend_window = QDialog()
        ui = room_extend.Ui_Dialog()
        ui.setupUi(room_extend_window)
        room_extend_window.show()
        room_extend_window.exec_()
    def jump_to_checkout(self):
        checkout_window = QDialog()
        ui = room_checkout.Ui_Form()
        ui.setupUi(checkout_window)
        checkout_window.show()
        checkout_window.exec_()
    def jump_to_vip_manage(self):
        vip_manage_window = QDialog()
        ui = vip_manage.Ui_vip_manage_7()
        ui.setupUi(vip_manage_window)
        vip_manage_window.show()
        vip_manage_window.exec_()
    def jump_to_info_query(self):
        query_info_window = QDialog()
        ui = query_info.Ui_Dialog()
        ui.setupUi(query_info_window)
        query_info_window.show()
        query_info_window.exec_()

    windowList = []
    def return_to_login(self):
        reply = QMessageBox.question(self, '注销确认',
            "注销本帐号并返回至登陆界面?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        the_window = login_register.Main_window()
        self.windowList.append(the_window)
        the_window.show()
        self.hide()

    def modify_pwd(self,name):
        pwd_modify_window = QDialog()
        ui = modify_password.Ui_Form()
        ui.setupUi(pwd_modify_window,self.Form,self.name)
        # self.hide()
        pwd_modify_window.show()
        pwd_modify_window.exec_()
        # self.show()

    def closeEvent(self, event):        
        reply = QMessageBox.question(self, '退出确认',
            "是否要退出系统?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            event.ignore()


if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=Ui_Form(name = '***')
    myshow.show()
    sys.exit(app.exec_())
