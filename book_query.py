# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_query.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog
import sys,re
import time
import pymysql
import config


class Ui_Form(QDialog, QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(277, 28, 400, 30))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(249, 100, 89, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(349, 96, 200, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(152, 150, 500, 350))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(301, 530, 200, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 530, 80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(573, 530, 80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #设置查询信号
        self.pushButton_2.clicked.connect(self.book_query)

        #设置查询所有预定的信号
        self.pushButton.clicked.connect(self.book_queryall)

        #设置取消按钮信号
        self.pushButton_3.clicked.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "预定查询"))
        self.label.setText(_translate("Form", "预定信息查询系统"))
        self.label_2.setText(_translate("Form", "手机号"))
        self.pushButton.setText(_translate("Form", "查询所有预定信息"))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.pushButton_3.setText(_translate("Form", "取消"))


    def book_query(self):
        self.textEdit.clear()
        tel = self.lineEdit.text()
        lst = re.findall('^1[0-9]{10}',tel)
        if not tel:
            QMessageBox.information(self, '提示信息', '请输入手机号', QMessageBox.Ok)
            return
        if not lst:
            QMessageBox.information(self, '提示信息', '手机号输入有误', QMessageBox.Ok)
            return
        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()
        try:
            sql_select = "select * from book_info where phone_num = '%s'"%tel
            cursor.execute(sql_select)
            data = cursor.fetchone()
            if not data:
                QMessageBox.information(self, '提示信息', '没有该号码的预定信息', QMessageBox.Ok)
                return
            newtime = data[4].strftime('%Y-%m-%d %H:%M:%S')
            self.textEdit.setPlainText("姓名:%s\n手机号:%s\n房间号:%s\n预定时间:%s\n预计离店时间:%s\n"\
            	%(data[1],data[2],data[3],newtime,data[5]))
        except Exception as e:
            print("查询失败",e)
        cursor.close()
        db.close()


    def book_queryall(self):
        self.textEdit.clear()
        str = ""
        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()
        try:
            sql_select = "select * from book_info"
            cursor.execute(sql_select)
            data = cursor.fetchall()
            if not data:
                QMessageBox.information(self, '提示信息', '没有预定信息', QMessageBox.Ok)
                return
            for dataone in data:
                newtime = dataone[4].strftime('%Y-%m-%d %H:%M:%S')
                str += "姓名:%s\n手机号:%s\n房间号:%s\n预定时间:%s\n预计离店时间:%s\n*******************\n"\
                %(dataone[1],dataone[2],dataone[3],newtime,dataone[5])
            self.textEdit.setPlainText(str)
        except Exception as e:
            print("查询失败",e)
        cursor.close()
        db.close()

    # def closeEvent(self, event):
    #     """
    #     重写closeEvent方法，实现dialog窗体关闭时执行一些代码
    #     :param event: close()触发的事件
    #     :return: None
    #     """
    #     reply = QtWidgets.QMessageBox.question(self,
    #                 '本程序',
    #                 "是否要退出程序？",
    #                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
    #                 QtWidgets.QMessageBox.No)
    #     if reply == QtWidgets.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())