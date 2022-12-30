from PyQt5 import QtWidgets, uic
import sys
from mainwindow11 import Ui_MainWindow
from secondwindow12 import Ui_SecondWindow

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mainwindow11.ui', self)
        self.setconfig.clicked.connect(self.configButtonClick)

        self.show()

    def configButtonClick(self):
        print("Inside configButtonClick ")

class Ui2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2,self).__init__()
        uic.loadUi('secondwindow12.ui',self)
        self.viewhistory.clicked.connect(self.configButtonClick2)
        self.show()

    def configButton2(self):
        print("View History")



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
