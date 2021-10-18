import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from OpenPrograms_ui import Ui_MainWindow


class OpenPrograms(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.add)
        self.openPath.clicked.connect(self.open)
        self.listOfApps.clicked.connect(self.get)

    def open(self):
        os.startfile(self.inputPath.text())

    def add(self):
        self.listOfApps.addItem(self.inputName.text())

    def get(self):
        self.inputPath.setText(self.listOfApps.currentItem().text())


app = QApplication(sys.argv)
ex = OpenPrograms()
ex.show()
sys.exit(app.exec_())
