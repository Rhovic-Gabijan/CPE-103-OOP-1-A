import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__() #initializes the main window like in the previous one
        #window = QMainwindow()
        self.title = "PyQt Button"
        self.x = 200 #or left
        self.y = 200 #or top
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        #In GUI Python, these buttons, textboxes, labels, are called widgets
        self.button = QPushButton('Click me!', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(100, 70) #button.move(x,y)

        self.button1 = QPushButton("Button 2", self)
        self.button1.setToolTip("This button does nothing..yet.")
        self.button1.move(100, 100)

        self.show()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())