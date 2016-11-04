from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()
        url = QLineEdit()
        save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")

        url.setPlaceholderText('URL')
        save_location.setPlaceholderText('File save location')

        progress.setValue()
        layout.addWidget(url)
        layout.addWidget(save_location)
        layout.addWidget(progress)
        layout.addWidget(download)


        self.setLayout(layout)

        self.setWindowTitle('pyDownloader')
        self.setFocus() #set focus on entire app




app = QApplication(sys.argv)
dialog = Downloader()

dialog.show()
app.exec_()