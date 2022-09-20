from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import subprocess
import pyautogui as g
import time

class AutoType(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout1 = QHBoxLayout()
        self.btn_fileSelect = QPushButton("File")
        self.t_fileName = QLabel("")
        self.layout1.addWidget(self.btn_fileSelect)
        self.layout1.addWidget(self.t_fileName)
        self.btn_fileSelect.clicked.connect(self.getFilePath)

        self.btn_start = QPushButton("Start")
        self.btn_start.clicked.connect(self.startTyping)
        self.btn_stop = QPushButton("Stop")
        self.btn_stop.clicked.connect(self.stopTyping)
        self.layout1.addWidget(self.btn_start)
        self.layout1.addWidget(self.btn_stop)

        self.layout.addLayout(self.layout1)

        self.le_type = QLineEdit()

        self.layout.addWidget(self.le_type)

        self.setLayout(self.layout)

    def getFilePath(self):
        self.t_fileName.setText(QFileDialog.getOpenFileUrl()[0].fileName())

    def startTyping(self):
        self.le_type.setFocus()
        self.typer = subprocess.Popen(['python',"./autotypeCore.py", self.t_fileName.text()])

    def stopTyping(self):
        self.typer.kill()




if __name__=="__main__":
    app = QApplication()
    mainWindow = AutoType()
    mainWindow.show()
    app.exec_()
