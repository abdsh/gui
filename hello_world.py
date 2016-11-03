from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()
        self.lable = QLabel('Hello World :)')
        line_edit = QLineEdit()
        button = QPushButton("close")

        layout.addWidget(self.lable, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 2)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        # line_edit.textChanged.connect(lable.setText)
        line_edit.textChanged.connect(self.changeTextLable)


    def changeTextLable(self, text):
        self.lable.setText(text)


app = QApplication(sys.argv)
dialog = HelloWorld()

dialog.show()
app.exec_()