# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crack.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys

import crack,threading
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.options=[]
        self.crack=crack.CrackGeetest()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(170, 80, 81, 21))
        self.emailLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.emailLabel.setTextFormat(QtCore.Qt.AutoText)
        self.emailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.emailLabel.setObjectName("emailLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(170, 140, 81, 21))
        self.passwordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.emailText = QtWidgets.QTextEdit(self.centralwidget)
        self.emailText.setGeometry(QtCore.QRect(290, 70, 171, 41))
        self.emailText.setObjectName("emailText")
        self.passwordText = QtWidgets.QTextEdit(self.centralwidget)
        self.passwordText.setGeometry(QtCore.QRect(290, 130, 171, 41))
        self.passwordText.setObjectName("passwordText")
        self.clickCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.clickCheckBox.setGeometry(QtCore.QRect(190, 210, 91, 19))
        self.clickCheckBox.setObjectName("clickCheckBox")
        self.noClickCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.noClickCheckBox.setGeometry(QtCore.QRect(370, 210, 91, 19))
        self.noClickCheckBox.setObjectName("noClickCheckBox")
        self.imageView = QtWidgets.QLabel("add a image file")
        self.imageView.setObjectName("imageview")
        self.imageView = QtWidgets.QLabel(self.centralwidget)
        self.imageView.setTextFormat(QtCore.Qt.AutoText)
        self.imageView.setGeometry(QtCore.QRect(260, 260, 200, 160))
        self.websiteLabel = QtWidgets.QLabel(self.centralwidget)
        self.websiteLabel.setGeometry(QtCore.QRect(170, 30, 81, 21))
        self.websiteLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.websiteLabel.setTextFormat(QtCore.Qt.AutoText)
        self.websiteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.websiteLabel.setObjectName("websiteLabel")
        self.websiteText = QtWidgets.QTextEdit(self.centralwidget)
        self.websiteText.setGeometry(QtCore.QRect(290, 20, 171, 41))
        self.websiteText.setObjectName("websiteText")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(530, 480, 93, 28))
        self.okButton.setObjectName("okButton")
        self.emailText.raise_()
        self.emailLabel.raise_()
        self.passwordLabel.raise_()
        self.passwordText.raise_()
        self.clickCheckBox.raise_()
        self.noClickCheckBox.raise_()
        self.imageView.raise_()
        self.websiteLabel.raise_()
        self.websiteText.raise_()
        self.okButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.okButton.clicked.connect(self.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.resize(self.image.width(), self.image.height())
    def click(self):
        website=self.websiteText.toPlainText()
        email=self.emailText.toPlainText()
        password=self.passwordText.toPlainText()
        isclick=self.clickCheckBox.isChecked()
        noclick=self.noClickCheckBox.isChecked()
        self.options.append(website)
        self.options.append(email)
        self.options.append(password)
        self.options.append( isclick)
        #self.options.append( noclick)
        self.image = QtGui.QImage("captcha1.png")
        self.imageView.setPixmap(QtGui.QPixmap.fromImage(self.image))
        try:
            t=threading.Thread(target=self.start,args=())
            t.start()
        except Exception as e:
            print(e)
        #self.crack.inital(self.options)
        #self.crack.crack()
    def start(self):
        self.crack.inital(self.options)
        print("123")
        self.crack.crack()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.emailLabel.setText(_translate("MainWindow", "邮箱"))
        self.passwordLabel.setText(_translate("MainWindow", "密码"))
        self.clickCheckBox.setText(_translate("MainWindow", "点击触发"))
        self.noClickCheckBox.setText(_translate("MainWindow", "加载触发"))
        self.websiteLabel.setText(_translate("MainWindow", "网站"))
        self.okButton.setText(_translate("MainWindow", "开始"))
        self.imageView.setText(_translate("MainWindow",'显示图片'))
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
