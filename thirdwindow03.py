# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thirdwindow103.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_thirdwindow(object):
    def setupUi(self, thirdwindow):
        thirdwindow.setObjectName("thirdwindow")
        thirdwindow.resize(1920, 1087)
        self.centralwidget = QtWidgets.QWidget(thirdwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QTextBrowser(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 1881, 91))
        self.title.setObjectName("title")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 210, 1881, 91))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 240, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 240, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(280, 238, 161, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(800, 237, 161, 41))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.fetch = QtWidgets.QPushButton(self.centralwidget)
        self.fetch.setGeometry(QtCore.QRect(1580, 226, 171, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.fetch.setFont(font)
        self.fetch.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.fetch.setObjectName("fetch")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 310, 1881, 741))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        thirdwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(thirdwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        thirdwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(thirdwindow)
        self.statusbar.setObjectName("statusbar")
        thirdwindow.setStatusBar(self.statusbar)

        self.retranslateUi(thirdwindow)
        QtCore.QMetaObject.connectSlotsByName(thirdwindow)

    def retranslateUi(self, thirdwindow):
        _translate = QtCore.QCoreApplication.translate
        thirdwindow.setWindowTitle(_translate("thirdwindow", "MainWindow"))
        self.title.setHtml(_translate("thirdwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#729fcf;\">VIEW HISTORY</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("thirdwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("thirdwindow", "Start Date"))
        self.label_2.setText(_translate("thirdwindow", "End Date"))
        self.fetch.setText(_translate("thirdwindow", "Fetch Data"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("thirdwindow", "Start date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("thirdwindow", "End date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("thirdwindow", "Fetch data"))
