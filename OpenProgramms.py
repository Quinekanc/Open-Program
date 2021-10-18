import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from OpenProgramms_ui import Ui_MainWindow


class OpenPrograms(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.openPath.clicked.connect(self.run)

    def run(self):
        os.startfile(self.inputPath.text())

app = QApplication(sys.argv)
ex = OpenPrograms()
ex.show()
sys.exit(app.exec_())
