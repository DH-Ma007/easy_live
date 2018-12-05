# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change.ui'
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

class Ui_Dialog(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("QWidget{background-image:url('image/sand.jpg')};")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(165, 70, 146, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(165, 142, 146, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 68, 80, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 80, 30))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 220, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 220, 80, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label.setStyleSheet("QWidget{background:transparent};")
        self.label_2.setStyleSheet("QWidget{background:transparent};")

        # 房间号正则限制
        reg = QRegExp("^\d+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.lineEdit.setValidator(pValidator)
        self.lineEdit_2.setValidator(pValidator)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #绑定更换房间槽函数
        self.pushButton.clicked.connect(self.change)
        #绑定更换房间槽函数
        self.pushButton_2.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "换房"))
        self.label.setText(_translate("Dialog", "当前房间号"))
        self.label_2.setText(_translate("Dialog", "更换房间号"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))

    def change(self):
        current_room_num = self.lineEdit.text()
        new_room_num = self.lineEdit_2.text()

        if not current_room_num:
            QMessageBox.information(self, '提示', '请输入当前房间号', QMessageBox.Ok)
            return
        if not new_room_num:
            QMessageBox.information(self, '提示', '请输入新的房间号', QMessageBox.Ok)
            return
        try:
            db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
            cursor = db.cursor()
            sql_select = "select * from check_in_info where room_num = '%s'"%current_room_num
            cursor.execute(sql_select)
            data = cursor.fetchall()
            if not data:
                print("没有此房间入住信息")
                QMessageBox.information(self, '提交失败', '没有此房间入住信息', QMessageBox.Ok)
                return

            sql_select = "select * from room_info where 房间号='%s'"%new_room_num
            cursor.execute(sql_select)
            data = cursor.fetchone()
            if not data:
                QMessageBox.information(self, '更换失败', '房间%s不存在'%new_room_num, QMessageBox.Ok)
                return
            elif data[5] == '已预定':
                QMessageBox.information(self, '更换失败', '房间%s已经被预定'%new_room_num, QMessageBox.Ok)
                return
            elif data[5] == '入住':
                QMessageBox.information(self, '更换失败', '房间%s已经有客'%new_room_num, QMessageBox.Ok)
                return
            sql_update = "update check_in_info set room_num = '%s'\
                        where room_num = '%s'"%(new_room_num, current_room_num)
            cursor.execute(sql_update)

            sql_update = "update room_info set 房间状态='入住' where 房间号='%s'"%new_room_num
            cursor.execute(sql_update)

            sql_update = "update room_info set 房间状态='空闲' where 房间号='%s'"%current_room_num
            cursor.execute(sql_update)

            sql_select = "select 押金,价格,会员价 from room_info where 房间号='%s'"%new_room_num
            cursor.execute(sql_select)
            deposit, price, vip_price = cursor.fetchone()

            sql_update = "update check_in_info set deposit='%d',price='%d',vip_price='%d'\
                            where room_num='%s'"%(deposit, price, vip_price,new_room_num)
            cursor.execute(sql_update)
            db.commit()

        except Exception as e:
            db.rollback()
            QMessageBox.information(self, '出错', '房间更换失败', QMessageBox.Ok)
            print("房号修改失败",e)

        cursor.close()
        db.close()

        QMessageBox.information(self, '提交完成', '房间更换成功\n已换至%s'%new_room_num, QMessageBox.Ok)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit.setFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Dialog()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())