import os
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from OpenProgram_ui import Ui_MainWindow


class OpenPrograms(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = sqlite3.connect('Open-Program.sqlite3')
        self.cursor = self.database.cursor()
        for i in self.cursor.execute('select name from openprogram').fetchall():
            self.listOfApps.addItem(*i)
        self.addButton.clicked.connect(self.add)
        self.openPath.clicked.connect(self.open)
        self.removeButton.clicked.connect(self.remove)
        self.listOfApps.clicked.connect(self.get)

    def open(self):
        os.startfile(self.inputPath.text())

    def add(self):
        self.listOfApps.addItem(self.inputName.text())
        try:
            self.cursor.execute(f"insert into openprogram values({len(self.listOfApps)}, '{self.inputName.text()}', "
                                f"'{self.inputPath.text()}')")
            self.database.commit()
        except Exception:
            self.cursor.execute("create table openprogram (id, name, path)")
            self.cursor.execute(f"insert into openprogram values (1, {self.inputName.text()}, {self.inputPath.text()})")
            self.database.commit()

    def get(self):
        self.inputName.setText(self.listOfApps.currentItem().text())
        self.inputPath.setText(*self.cursor.execute(f'''select path from openprogram 
                                      where name = "{self.listOfApps.currentItem().text()}"''').fetchall()[0])

    def remove(self):
        self.listOfApps.removeItemWidget()


app = QApplication(sys.argv)
ex = OpenPrograms()
ex.show()
sys.exit(app.exec_())
