import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QFont


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title= "Simple Account Registration"
        self.x=200
        self.y=300
        self.width=350
        self.height=350
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.setStyleSheet("Background-color: #8B8878")

        self.textboxlbl = QLabel("Registration Form ", self)
        self.textboxlbl.move(115,10)
        self.textboxlbl.setFont(QFont("Times New Roman", 15))

        labels = ["First name:", "Last name:", "Username:", "Password:", "Email Address:", "Contact Number:"]
        self.textboxes = []

        y = 40
        for label_text in labels:
            lbl = QLabel(label_text, self)
            lbl.move(10, y)
            lbl.setFont(QFont("Times New Roman", 11))

            textbox = QLineEdit(self)
            textbox.move(120, y)
            textbox.resize(200, 20)
            textbox.setFont(QFont("Times New Roman", 11))

            self.textboxes.append(textbox)
            y +=30

        self.button = QPushButton("Clear", self)
        self.button.move(75, 220)
        self.button.clicked.connect(self.clear)

        self.button1 = QPushButton("Submit", self)
        self.button1.move(200, 220)
        self.button1.clicked.connect(self.submit)


        self.show()

    def clear(self):
        for textbox in self.textboxes:
            textbox.clear()

    def submit(self):
        details = "\n".join(
            [f"{label.text()} {textbox.text()}" for label, textbox in zip(self.findChildren(QLabel)[1:], self.textboxes)]
        )
        QMessageBox.information(self, "Registration Details", f"Submitted Information:\n\n{details}")

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())