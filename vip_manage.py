# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vip_manage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox,QDialog
import sys
import vip_card
import vip_recharge
import vip_query
import vip_cancell

class Ui_vip_manage_7(QWidget):
    def setupUi(self, vip_manage_7):
        vip_manage_7.setObjectName("vip_manage_7")
        vip_manage_7.resize(294, 300)
        vip_manage_7.setStyleSheet("QWidget{background-image:url('image/sand.jpg')};")
        self.pushButton_5 = QtWidgets.QPushButton(vip_manage_7)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 250, 99, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.layoutWidget = QtWidgets.QWidget(vip_manage_7)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 30, 111, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton.setStyleSheet("QWidget{background:white};")
        self.pushButton_2.setStyleSheet("QWidget{background:white};")
        self.pushButton_3.setStyleSheet("QWidget{background:white};")
        self.pushButton_4.setStyleSheet("QWidget{background:white};")

        #按钮绑定槽函数
        self.pushButton.clicked.connect(self.open_card)
        self.pushButton_2.clicked.connect(self.recharge)
        self.pushButton_3.clicked.connect(self.query)
        self.pushButton_4.clicked.connect(self.cancellation)
        self.pushButton_5.clicked.connect(vip_manage_7.close)

        self.retranslateUi(vip_manage_7)
        QtCore.QMetaObject.connectSlotsByName(vip_manage_7)

    def retranslateUi(self, vip_manage_7):
        _translate = QtCore.QCoreApplication.translate
        vip_manage_7.setWindowTitle(_translate("vip_manage_7", "会员管理"))
        self.pushButton_5.setText(_translate("vip_manage_7", "退出"))
        self.pushButton.setText(_translate("vip_manage_7", "开卡"))
        self.pushButton_2.setText(_translate("vip_manage_7", "充值"))
        self.pushButton_3.setText(_translate("vip_manage_7", "查询"))
        self.pushButton_4.setText(_translate("vip_manage_7", "销卡"))

    def open_card(self):
        open_card_window = QDialog()
        ui = vip_card.Ui_Form()
        ui.setupUi(open_card_window)
        open_card_window.show()
        open_card_window.exec_()

    def recharge(self):
        recharge_window = QDialog()
        ui = vip_recharge.Ui_Form()
        ui.setupUi(recharge_window)
        recharge_window.show()
        recharge_window.exec_()

    def query(self):
        vip_query_window = QDialog()
        ui = vip_query.Ui_Form()
        ui.setupUi(vip_query_window)
        vip_query_window.show()
        vip_query_window.exec_()

    def cancellation(self):
        vip_cancell_window = QDialog()
        ui = vip_cancell.Ui_Form()
        ui.setupUi(vip_cancell_window)
        vip_cancell_window.show()
        vip_cancell_window.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QWidget()
    ui = Ui_vip_manage_7()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())