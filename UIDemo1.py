from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QTextBrowser, QMenuBar, QStatusBar
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('mainwindow11.ui',self)

        self.button1 = self.findChild(QPushButton,'setconfig')
        self.button2 = self.findChild(QPushButton,'viewhistory')
        self.button3 = self.findChild(QPushButton,'reset')

        self.button1.clicked.connect(self.clicker1)
        self.button2.clicked.connect(self.clicker2)
        self.button3.clicked.connect(self.resetall)

        self.show()

    def clicker1(self):
        print("Clicked SetConfig")

    def clicker2(self):
        print("Clicked View History")

    def resetall(self):
        # write reset code here
        print("Reset All")
        
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
