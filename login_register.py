
import sys,re,time
# from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton, QApplication)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pymysql import connect
import hotel
# import success
import config

# app.exec_()其实就是QApplication的方法，
# 原来这个exec_()方法的作用是“进入程序的主循环直到exit()被调用

class Main_window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def closeEvent(self, event):        
        reply = QMessageBox.question(self, '退出确认',
            "是否要退出?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #重写键盘事件   
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.pushButton2_clicked2()

    def initUI(self):
        QToolTip.setFont(QFont('仿宋', 10))

        self.setToolTip('')        

        #背景
        label = QLabel('',self)
        self.gif = QMovie('image/timg.jpg')
        label.setMovie(self.gif)
        self.gif.start()

        #标题
        biaoti = QLabel('易住酒店管理系统',self)
        biaoti.setFont(QFont('黑体', 30))
        biaoti.resize(350,200)
        biaoti.move(250,-30)
        biaoti.setStyleSheet('QLabel{color:white}')

        #登录按钮并设置鼠标悬停提示
        login = QPushButton('登录', self)
        login.setToolTip('点击登录')
        #调整按钮尺寸为默认宽高
        login.resize(login.sizeHint())
        #设置按钮在窗口中位置距左500距上0
        login.move(320, 250)
        # login.setStyleSheet('QPushButton{background:grey;}')

        # self.register = QPushButton('注册')
        #注册按钮并设置鼠标悬停提示
        register = QPushButton('注册', self)
        register.setToolTip('点击注册')
        register.resize(register.sizeHint())
        register.move(420, 250)
        # register.setStyleSheet('QPushButton{background:grey;}')

        # 设置按钮事件
        #设置注册按钮跳转
        register.clicked.connect(self.pushButton1_clicked1)
        #设置登录按钮事件
        login.clicked.connect(self.pushButton2_clicked2)

        #帐号
        name = QLabel('帐号:',self)
        name.setFont(QFont('宋体'))
        name.move(270,150)
        name.setStyleSheet('QLabel{color:white;font-weight:bold}')

        #帐号输入框
        name_text = QLineEdit(self)
        name_text.resize(180,30)
        name_text.move(320,143)
        name_text.setPlaceholderText('请输入用户名')
        name_text.setFocus()

        #密码
        passwd = QLabel('密码:',self)
        passwd.setFont(QFont('宋体'))
        passwd.move(270,200)
        passwd.setStyleSheet('QLabel{color:white;font-weight:bold}')

        #密码输入框
        passwd_text = QLineEdit(self)
        passwd_text.installEventFilter(self)
        passwd_text.resize(180,30)
        passwd_text.move(320,195)
        passwd_text.setContextMenuPolicy(Qt.NoContextMenu)
        passwd_text.setPlaceholderText('请输入密码')
        passwd_text.setEchoMode(QLineEdit.Password)


        # 设置窗口离左边的距离50 上面的距离100 宽600，高500
        self.setGeometry(350, 80, 800, 400)
        # 设置title
        self.setWindowTitle('欢迎使用易住酒店管理系统！')
        # 设置窗口无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # 窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)


        self.name_text = name_text
        self.passwd_text = passwd_text


    def pushButton1_clicked1(self):
        the_window = SecondWindow()
        self.windowList.append(the_window)
        self.hide()
        the_window.show()

    #此方法跳转会发生异常
    # def jump_to_hotel(self,name):
    #     self.hide()
    #     form1 = QDialog()
    #     ui = hotel.Ui_Form(name)
    #     form1.show()
    #     form1.exec_()
        # self.show()

    #跳转至前台界面
    def jump_to_hotel(self,name):
        the_window = hotel.Ui_Form(name)
        self.windowList.append(the_window)
        self.hide()
        the_window.show()

    windowList = []
    def pushButton2_clicked2(self):
        name = self.name_text.text()
        pwd = self.passwd_text.text()
        if not name:
            QMessageBox.warning(self,'警告','用户名不能为空',\
                QMessageBox.Ok,QMessageBox.Ok)
            return
        elif not pwd:
            QMessageBox.warning(self,'警告','密码不能为空',\
                QMessageBox.Ok,QMessageBox.Ok)
            return
        else:
            db = connect(host=config.HOST,
                         user=config.USER,
                         password=config.PASSWORD,
                         database='hotelDB',
                         charset='utf8',
                         port=3306)

            cursor = db.cursor()
            sql = "select name,pwd from user_info where name='%s' and pwd='%s';"%(name,pwd)
            cursor.execute(sql)
            result=cursor.fetchall()
            if len(result)==0:
                QMessageBox.warning(self,'请重新输入','用户名或密码错误!',\
                    QMessageBox.Ok,QMessageBox.Ok)
                return
            else:
                self.jump_to_hotel(name)



    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('易住酒店管理系统欢迎您！')
        self.setGeometry(50,100,1263,640)
        self.setWindowFlags(Qt.FramelessWindowHint)

        #背景
        label = QLabel('',self)
        self.gif = QMovie('rain.gif')
        label.setMovie(self.gif)
        self.gif.start()

        #创建一个关闭按钮
        quit = QPushButton('X',self)
        quit.clicked.connect(QCoreApplication.instance().quit)
        quit.resize(42,42)
        quit.move(0,0)
        quit.setToolTip('点击关闭')
        quit.setFlat(True)
        quit.setStyleSheet('QPushButton{background-color:white}'
                           'QPushButton{color:white}'
                           'QPushButton:hover{color:black}')


    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
        

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('注册界面')
        self.setGeometry(600,80,500,400)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        #背景
        label = QLabel('',self)
        self.gif = QMovie('image/fan.jpg')
        label.setMovie(self.gif)
        self.gif.start()

        #设置窗口布局
        #帐号输入框
        self.register_name_text = QLineEdit(self)
        self.register_name_text.resize(250, 30)
        self.register_name_text.move(20,100)
        self.register_name_text.setPlaceholderText('请输入用户名')
        self.register_name_text.setFocus()

        #帐号要求
        self.register_name_yq = QLabel('* 由字母,数字组成(5-20位)',self)
        self.register_name_yq.move(285,102)        
        self.register_name_yq.setStyleSheet('QLabel{color:white}' \
            'QLabel{font-family:"华文新魏"}')
        
        #设置账号实时验证
        self.register_name_yz1 = QLabel('*不允许有特殊字符！',self)
        self.register_name_yz1.move(25,130)
        self.register_name_yz1.setStyleSheet('QLabel{color:red;font-weight:bold}' \
                'QLabel{font-family:"楷体"}' 'QLabel{font-size:12px}')
        self.register_name_yz1.setVisible(False)

        self.register_name_yz2 = QLabel('*用户名长度不符！',self)
        self.register_name_yz2.move(25,130)        
        self.register_name_yz2.setStyleSheet('QLabel{color:red;font-weight:bold}' \
            'QLabel{font-family:"楷体"}' 'QLabel{font-size:12px}')
        self.register_name_yz2.setVisible(False)

        self.register_name_yz3 = QLabel('*用户名被占用！',self)
        self.register_name_yz3.move(25,130)        
        self.register_name_yz3.setStyleSheet('QLabel{color:red;font-weight:bold}' \
            'QLabel{font-family:"楷体"}' 'QLabel{font-size:12px}')
        self.register_name_yz3.setVisible(False)

        self.register_name_yz4 = QLabel('✔用户名可用',self)
        self.register_name_yz4.move(25,130)        
        self.register_name_yz4.setStyleSheet('QLabel{color:white}' \
            'QLabel{font-family:"楷体"}' 'QLabel{font-size:12px}')
        self.register_name_yz4.setVisible(False)

        self.register_name_yz5 = QLabel('*用户名不能为纯数字！',self)
        self.register_name_yz5.move(25,130)        
        self.register_name_yz5.setStyleSheet('QLabel{color:red;font-weight:bold}' \
            'QLabel{font-family:"楷体"}' 'QLabel{font-size:12px}')
        self.register_name_yz5.setVisible(False)

        #密码输入框
        self.register_pwd_text = QLineEdit(self)
        self.register_pwd_text.resize(250,30)
        self.register_pwd_text.move(20,170)
        #给密码框安装事件过滤器
        self.register_pwd_text.installEventFilter(self)
        #设置密码框无法复制
        self.register_pwd_text.setContextMenuPolicy(Qt.NoContextMenu)
        #设置密码框显示样式
        self.register_pwd_text.setEchoMode(QLineEdit.Password)
        self.register_pwd_text.setPlaceholderText('请输入密码')

        #提示
        self.register_pwd_yq = QLabel('* 不允许有空格,6-15位',self)
        self.register_pwd_yq.move(285,172)
        self.register_pwd_yq.setStyleSheet('QLabel{color:white}')
        
        #设置密码1实时验证
        self.register_pwd_yz1 = QLabel('*密码不允许有空格',self)
        self.register_pwd_yz1.move(25,200)
        self.register_pwd_yz1.setStyleSheet("QLabel{color:red;font-weight:bold}" \
                "QLabel{font-family:'楷体'}" "QLabel{font-size:12px}")
        self.register_pwd_yz1.setVisible(False)

        self.register_pwd_yz2 = QLabel('*密码过短',self)
        self.register_pwd_yz2.move(25,200)
        self.register_pwd_yz2.setStyleSheet("QLabel{color:red;font-weight:bold}" \
                "QLabel{font-family:'楷体'}" "QLabel{font-size:12px}")
        self.register_pwd_yz2.setVisible(False)

        self.register_pwd_yz3 = QLabel('*密码过长',self)
        self.register_pwd_yz3.move(25,200)
        self.register_pwd_yz3.setStyleSheet("QLabel{color:red;font-weight:bold}" \
                "QLabel{font-family:'楷体'}" "QLabel{font-size:12px}")
        self.register_pwd_yz3.setVisible(False)

        self.register_pwd_yz4 = QLabel('✔',self)
        self.register_pwd_yz4.move(25,200)
        self.register_pwd_yz4.setStyleSheet("QLabel{color:white}" \
                "QLabel{font-family:'楷体'}" "QLabel{font-size:12px}")
        self.register_pwd_yz4.setVisible(False)

        #密码输入框2
        self.register_pwd2_text = QLineEdit(self)
        self.register_pwd2_text.resize(250,30)
        self.register_pwd2_text.move(20,240)
        self.register_pwd2_text.setEchoMode(QLineEdit.Password)
        self.register_pwd2_text.setPlaceholderText('请确认密码')

        #密码2要求
        self.register_pwd_yq = QLabel('* 两次密码保持一致',self)
        self.register_pwd_yq.move(285,242)
        self.register_pwd_yq.setStyleSheet('QLabel{color:white}')

        #密码2即时验证结果
        self.register_pwd2_yz1 = QLabel('*两次密码不一致',self)
        self.register_pwd2_yz1.move(25,272)        
        self.register_pwd2_yz1.setStyleSheet('QLabel{color:red;font-weight:bold}' \
            'QLabel{font-family:"楷体"}' 'QLabel{font-size:12px}')
        self.register_pwd2_yz1.setVisible(False)

        #密码2即时验证结果
        self.register_pwd2_yz2 = QLabel('✔密码一致！',self)
        self.register_pwd2_yz2.move(25,272)        
        self.register_pwd2_yz2.setStyleSheet('QLabel{color:white}' \
            'QLabel{font-family:"楷体"}' 'QLabel{font-size:12px}')
        self.register_pwd2_yz2.setVisible(False)

        #注册按钮
        self.register_btn = QPushButton('注册',self)
        # self.register_btn.setAttribute()
        # self.register_btn.resize(250,30)
        # self.register_btn.move(20,310)
        self.register_btn.resize(150,35)
        self.register_btn.move(70,305)
        self.register_btn.setStyleSheet('QPushButton{background:green;}')

        #返回至登录
        self.go_login = QPushButton('登录',self)
        self.go_login.resize(40,25)
        self.go_login.move(420,10)

        #我已注册
        self.go_log = QLabel('我有账号,现在就去',self)
        self.go_log.move(288,10)
        self.go_log.setStyleSheet('QLabel{color:white}')
        # self.go_log.setStyleSheet("QLabel{background:white;}"\
        #     "QLabel{color:rgb(100,100,100,250);font-size:\
        #     15px;font-family:Roman times;}" \
        # self.go_login.setStyleSheet("QLabel:hover{color:rgb(100,100,100,120);}")


        #密码限制
        # reg = QRegExp('\S{6,15}')
        # pValidator = QRegExpValidator(self)
        # pValidator.setRegExp(reg)
        # self.register_pwd_text.setValidator(pValidator)
        # self.register_pwd2_text.setValidator(pValidator)

        #设置事件
        self.register_btn.clicked.connect(self.YanZheng)
        self.go_login.clicked.connect(self.jump_to_login)
        self.register_name_text.editingFinished.connect(self.ZHYanZheng)
        self.register_name_text.textChanged.connect(self.contentHidden)#内容改动事件
        self.register_pwd_text.textChanged.connect(self.MMYanZheng)
        self.register_pwd2_text.returnPressed.connect(self.YanZheng)
        self.register_pwd2_text.textChanged.connect(self.MMYanZheng2)


    def contentHidden(self):
        self.register_name_yz1.setVisible(False)
        self.register_name_yz2.setVisible(False)
        self.register_name_yz3.setVisible(False)
        self.register_name_yz4.setVisible(False)
        self.register_name_yz5.setVisible(False)

    def YanZheng(self):
        register_name = self.register_name_text.text() 
        register_pwd = self.register_pwd_text.text()
        register_pwd2 = self.register_pwd2_text.text()
        L = re.findall("\W+",register_name)
        if register_name == '':
            QMessageBox.warning(self,'警告','用户名不能为空', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        elif register_pwd == '':
            QMessageBox.warning(self,'警告','密码不能为空', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        elif register_pwd2 == '':
            QMessageBox.warning(self,'警告','请确认密码', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        elif L:
            QMessageBox.warning(self,'警告','用户名不允许有特殊字符', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        elif not 5<=len(register_name)<=20:
            QMessageBox.warning(self,'警告','用户名长度不符', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        elif register_name.isdigit():
            QMessageBox.warning(self,'警告','用户名不能为纯数字', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        elif ' ' in register_pwd:
            QMessageBox.warning(self,'警告','密码不能包含空格', \
                QMessageBox.Ok, QMessageBox.Ok)
            return
        elif len(register_pwd)<6:
            QMessageBox.warning(self,'警告','密码过短', \
                QMessageBox.Ok, QMessageBox.Ok)
            return

        elif len(register_pwd)>15:
            QMessageBox.warning(self,'警告','密码过长', \
                QMessageBox.Ok, QMessageBox.Ok)
            return

        elif register_pwd != register_pwd2:
            QMessageBox.warning(self,'警告','密码两次输入不一致，请重新输入',\
                 QMessageBox.Ok, QMessageBox.Ok)
            return
        else:
            db = connect(host=config.HOST,
                         user=config.USER,
                         password=config.PASSWORD,
                         database='hotelDB',
                         charset='utf8',
                         port=3306)

            cursor = db.cursor()
            sql = 'select name from user_info where name=%s;'
            cursor.execute(sql,[register_name])
            result = cursor.fetchall()
            if len(result) == 0:
                sql_insert = "insert into user_info (name,pwd) values(%s,%s);"
                cursor.execute(sql_insert,[register_name,register_pwd])
                db.commit()
                QMessageBox.about(self,'恭喜！','注册成功,点击返回登录界面')
                self.jump_to_login()
            elif result[0][0] == register_name:
                QMessageBox.warning(self,'警告','用户名被占用',QMessageBox.Ok,QMessageBox.Ok)
                return
            cursor.close()
            db.close()
            return

    def ZHYanZheng(self):
        register_name = self.register_name_text.text()
        L = re.findall("\W+",register_name)
        db = connect(host=config.HOST,
                    user=config.USER,
                    password=config.PASSWORD,
                    database='hotelDB',
                    charset='utf8',
                    port=3306)

        cursor = db.cursor()
        sql = "select name,pwd from user_info where name='%s';"%register_name
        cursor.execute(sql)
        result=cursor.fetchall()
        if L:
            self.register_name_yz1.setVisible(True)#不允许有特殊字符
            return
        elif len(register_name)==0:
            pass
        elif 0<len(register_name)<5 or len(register_name)>20:
            self.register_name_yz2.setVisible(True)#用户名长度不符
            return
        elif register_name.isdigit():
            self.register_name_yz5.setVisible(True)#用户名不能为纯数字
            return
        elif len(result)!=0:
            self.register_name_yz3.setVisible(True)#用户名已存在
            return
        else:
            self.register_name_yz4.setVisible(True)#用户名可用

    def MMYanZheng(self):
        pwd1 = self.register_pwd_text.text()
        if ' ' in pwd1:
            self.register_pwd_yz2.setVisible(False)
            self.register_pwd_yz3.setVisible(False)
            self.register_pwd_yz4.setVisible(False)
            self.register_pwd_yz1.setVisible(True)
        elif len(pwd1)==0:
            self.register_pwd_yz1.setVisible(False)
            self.register_pwd_yz3.setVisible(False)
            self.register_pwd_yz4.setVisible(False)
            self.register_pwd_yz2.setVisible(False)
        elif 0<len(pwd1)<6:
            self.register_pwd_yz1.setVisible(False)
            self.register_pwd_yz3.setVisible(False)
            self.register_pwd_yz4.setVisible(False)
            self.register_pwd_yz2.setVisible(True)
        elif len(pwd1)>15:
            self.register_pwd_yz1.setVisible(False)
            self.register_pwd_yz2.setVisible(False)
            self.register_pwd_yz4.setVisible(False)
            self.register_pwd_yz3.setVisible(True)
        else:
            self.register_pwd_yz1.setVisible(False)
            self.register_pwd_yz2.setVisible(False)
            self.register_pwd_yz3.setVisible(False)
            self.register_pwd_yz4.setVisible(True)

    def MMYanZheng2(self):
        pwd1 = self.register_pwd_text.text()
        pwd2 = self.register_pwd2_text.text()
        if pwd1 == pwd2:
            self.register_pwd2_yz1.setVisible(False)
            self.register_pwd2_yz2.setVisible(True)
        else:
            self.register_pwd2_yz2.setVisible(False)
            self.register_pwd2_yz1.setVisible(True)
    
    #重写键盘事件
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.YanZheng()

    #重写关闭事件，注册窗口关闭返回主窗口
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出',
            "放弃注册?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No) 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    windowList = []
    def jump_to_login(self):
        the_window = Main_window()
        self.windowList.append(the_window)
        self.hide()
        the_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    M = Main_window()
    M.show()
    sys.exit(app.exec_())

        
