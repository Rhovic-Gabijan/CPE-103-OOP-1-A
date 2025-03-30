import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__() #initializes the main window like in the previous one
        # window = QMainwindow()
        self.title= "PyQt Line Edit"
        self.x=200 #or left
        self.y=300 #or top
        self.width=300
        self.height=300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.textboxlbl = QLabel("Hello World!", self)
        self.textboxlbl.move(115,30)
        self.textboxlbl1 = QLabel("This program is written in Pycharm", self)
        self.textboxlbl1.move(75,50)

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())