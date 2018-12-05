# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_pwd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog,QLineEdit
from PyQt5.QtCore import Qt
import config
import pymysql
import login_register

class Ui_Form(QWidget):
    def setupUi(self, Form, hotel_form, name):
        self.hotel_form = hotel_form
        self.form = Form
        self.name = name
        Form.setObjectName("Form")
        Form.resize(411, 277)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 220, 99, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 40, 321, 151))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 63 italic 11pt \"Ubuntu\";\n"
                                "color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("font: 63 italic 11pt \"Ubuntu\";\n"
                                "color: rgb(0, 0, 127);")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("font: 63 italic 11pt \"Ubuntu\";\n"
                                "color: rgb(0, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("font: 63 italic 11pt \"Ubuntu\";\n"
                                "color: rgb(0, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit.setFocus()
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.lineEdit_3.setPlaceholderText('6-15位,不能有空格')
        self.lineEdit_4.setPlaceholderText('两次密码需保持一致')

        #设置密码框显示样式
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        #设置密码框无法复制
        self.lineEdit_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_4.setContextMenuPolicy(Qt.NoContextMenu)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.modify_pwd)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "密码管理"))
        self.pushButton.setText(_translate("Form", "确认修改"))
        self.label.setText(_translate("Form", "请输入用户名："))
        self.label_2.setText(_translate("Form", "请输入原密码："))
        self.label_3.setText(_translate("Form", "请输入新密码："))
        self.label_4.setText(_translate("Form", "请确认新密码："))

    def modify_pwd(self):
        uname = self.lineEdit.text()
        old_pwd = self.lineEdit_2.text()
        new_pwd = self.lineEdit_3.text()
        confirm_pwd = self.lineEdit_4.text()
        if not uname:
            QMessageBox.information(self, '提示信息', '用户名不能为空！', QMessageBox.Ok)
            return
        if not old_pwd:
            QMessageBox.information(self, '提示信息', '原密码不能为空！', QMessageBox.Ok)
            return
        if not new_pwd:
            QMessageBox.information(self, '提示信息', '请输入新密码！', QMessageBox.Ok)
            return
        if ' ' in new_pwd:
            QMessageBox.warning(self,'警告','密码不能包含空格', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        if len(new_pwd)<6:
            QMessageBox.warning(self,'警告','密码过短,不少于6位', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        if len(new_pwd)>15:
            QMessageBox.warning(self,'警告','密码过长,不超过15位', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        if new_pwd == old_pwd:
            QMessageBox.warning(self,'警告','新密码不能与原密码相同', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        if not confirm_pwd:
            QMessageBox.information(self, '提示信息', '请确认新密码！', QMessageBox.Ok)
            return
        if new_pwd != confirm_pwd:
            QMessageBox.information(self, '提示信息', '新密码两次输入不一致！', QMessageBox.Ok)
            return

        db = pymysql.connect(host = config.HOST, user = config.USER,\
                        password = config.PASSWORD, database = "hotelDB",\
                        charset = "utf8")
        cursor = db.cursor()

        sql = "select name from user_info where name='%s';"%uname
        cursor.execute(sql)
        result=cursor.fetchall()
        if len(result)==0:
            QMessageBox.information(self,'失败','用户名不存在!',\
                    QMessageBox.Ok)
            return

        sql = "select name,pwd from user_info where name='%s' and pwd='%s';"%(uname,old_pwd)
        cursor.execute(sql)
        result=cursor.fetchall()
        if len(result)==0:
            QMessageBox.information(self,'失败','原密码不正确!',\
                    QMessageBox.Ok)
            return
        try:
            sql_modify = "update user_info set pwd = '%s' where name='%s' and pwd='%s'"\
                        %(new_pwd,uname,old_pwd)
            cursor.execute(sql_modify)
            db.commit()
        except Exception as e:
            db.rollback()
            QMessageBox.information(self, '修改失败', '错误:%s!'%e, QMessageBox.Ok)
        finally:
            cursor.close()
            db.close()
        if uname != self.name:
            reply = QMessageBox.question(self, '成功', '密码修改成功,是否去登录验证？', \
                QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.go_login()
            else:
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
        else:
            QMessageBox.information(self, '提示', '当前账户密码已修改,请重新登录', QMessageBox.Ok)
            self.go_login()

    windowList = []
    def go_login(self):
        the_window = login_register.Main_window()
        self.windowList.append(the_window)
        the_window.show()
        self.form.close()
        self.hotel_form.hide()