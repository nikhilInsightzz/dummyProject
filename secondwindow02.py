# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondwindow12.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(794, 484)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1881, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(500, 340, 891, 661))
        self.tableView.setObjectName("tableView")
        self.matchconfigtitle = QtWidgets.QTextBrowser(self.centralwidget)
        self.matchconfigtitle.setGeometry(QtCore.QRect(510, 180, 891, 91))
        self.matchconfigtitle.setObjectName("matchconfigtitle")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(780, 440, 241, 211))
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(5, 0, item)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(884, 460, 101, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(884, 490, 101, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(884, 580, 101, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(884, 550, 101, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(884, 520, 101, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(884, 610, 101, 31))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(820, 660, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Nimbus Roman [UKWN]")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setObjectName("save")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("SecondWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; color:#3465a4;\">SET CONFIGURATION</span></p></body></html>"))
        self.matchconfigtitle.setHtml(_translate("SecondWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600; color:#729fcf;\">Match Config</span></p></body></html>"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("SecondWindow", "Location"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("SecondWindow", "Values"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        item = self.table.item(0, 0)
        item.setText(_translate("SecondWindow", "1"))
        item = self.table.item(1, 0)
        item.setText(_translate("SecondWindow", "2"))
        item = self.table.item(2, 0)
        item.setText(_translate("SecondWindow", "3"))
        item = self.table.item(3, 0)
        item.setText(_translate("SecondWindow", "4"))
        item = self.table.item(4, 0)
        item.setText(_translate("SecondWindow", "5"))
        item = self.table.item(5, 0)
        item.setText(_translate("SecondWindow", "6"))
        self.table.setSortingEnabled(__sortingEnabled)
        self.comboBox.setItemText(0, _translate("SecondWindow", "Red"))
        self.comboBox.setItemText(1, _translate("SecondWindow", "White"))
        self.comboBox_2.setItemText(0, _translate("SecondWindow", "Red"))
        self.comboBox_2.setItemText(1, _translate("SecondWindow", "White"))
        self.comboBox_3.setItemText(0, _translate("SecondWindow", "Red"))
        self.comboBox_3.setItemText(1, _translate("SecondWindow", "White"))
        self.comboBox_4.setItemText(0, _translate("SecondWindow", "Red"))
        self.comboBox_4.setItemText(1, _translate("SecondWindow", "White"))
        self.comboBox_5.setItemText(0, _translate("SecondWindow", "Red"))
        self.comboBox_5.setItemText(1, _translate("SecondWindow", "White"))
        self.comboBox_6.setItemText(0, _translate("SecondWindow", "Red"))
        self.comboBox_6.setItemText(1, _translate("SecondWindow", "White"))
        self.save.setText(_translate("SecondWindow", "SAVE"))