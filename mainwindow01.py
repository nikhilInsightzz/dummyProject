# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow11.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from secondwindow12 import Ui_SecondWindow
from thirdwindow103 import Ui_thirdwindow


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openwindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_thirdwindow()
        self.ui.setupUi(self.window)
        self.window.show()    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1087)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mahindralogo = QtWidgets.QFrame(self.centralwidget)
        self.mahindralogo.setEnabled(True)
        self.mahindralogo.setGeometry(QtCore.QRect(0, -4, 211, 141))
        self.mahindralogo.setStyleSheet("image: url(:/newPrefix/mahindra-logo.jpg);")
        self.mahindralogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mahindralogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mahindralogo.setObjectName("mahindralogo")
        self.insightzzlogo = QtWidgets.QFrame(self.centralwidget)
        self.insightzzlogo.setGeometry(QtCore.QRect(1640, 0, 221, 131))
        self.insightzzlogo.setStyleSheet("image: url(:/newPrefix/Insightzzz.png);\n"
"image: url(:/newPrefix/Insightzzz.png);")
        self.insightzzlogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.insightzzlogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.insightzzlogo.setObjectName("insightzzlogo")
        self.title = QtWidgets.QTextBrowser(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(210, 0, 1431, 131))
        self.title.setObjectName("title")
        self.setconfig = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.openWindow())
        self.setconfig.setGeometry(QtCore.QRect(160, 240, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.setconfig.setFont(font)
        self.setconfig.setObjectName("setconfig")
        self.viewhistory = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.openwindow2())
        self.viewhistory.setGeometry(QtCore.QRect(720, 240, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.viewhistory.setFont(font)
        self.viewhistory.setObjectName("viewhistory")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(1260, 240, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600; color:#ad7fa8;\">DRISHTI PORTAL - DEMO PROJECT</span></p></body></html>"))
        self.setconfig.setText(_translate("MainWindow", "Set Config"))
        self.viewhistory.setText(_translate("MainWindow", "View History"))
        self.reset.setText(_translate("MainWindow", "Reset"))
# import tst_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
