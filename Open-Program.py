import os
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Open_Program_settings_ui import Ui_windowSettings
from Open_Program_ui import Ui_windowStart


class OpenProgramSettings(QMainWindow, Ui_windowSettings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = sqlite3.connect('Open-Program.sqlite3')
        self.cursor = self.database.cursor()

        try:
            for element in self.cursor.execute('select name from openprogram'):
                self.listView.addItem(*element)
        except Exception:
            pass

        self.addButton.clicked.connect(self.add)
        self.removeButton.clicked.connect(self.remove)
        self.listView.itemClicked.connect(self.get)
        self.listView.itemDoubleClicked.connect(self.get_double)
        self.returnButton.clicked.connect(self.return_to_start)

    def open(self):
        os.startfile(self.inputPath.text())

    def add(self):
        if self.cursor.execute("select max(id) from openprogram").fetchall() == [(None,)]:
            self.cursor.execute(f"""
                                    insert into openprogram 
                                    values(1, '{self.inputName.text()}', '{self.inputPath.text()}')
                                """).fetchall()
        else:
            self.cursor.execute(f"""
                                    insert into openprogram 
                                    values((select max(id) from openprogram) + 1, 
                                    '{self.inputName.text()}', '{self.inputPath.text()}')
                                """).fetchall()
        self.database.commit()
        self.listView.addItem(f'{self.inputName.text()}')

    def get(self):
        self.inputName.setText(self.listView.currentItem().text())

        self.inputPath.setText(self.cursor.execute(f'''select path from openprogram 
                                      where name = "{self.listView.currentItem().text()}"''').fetchall()[0][0])

    def get_double(self):
        self.get()
        self.open()

    def remove(self):
        self.cursor.execute(f'''delete from openprogram where name = "{self.listView.currentItem().text()}"''')
        listItems = self.listView.selectedItems()
        if not listItems: return
        for item in listItems:
            self.listView.takeItem(self.listView.row(item))
        self.database.commit()

    def return_to_start(self):
        try:
            ex_start.show()
            ex_start.__init__()
            ex_set.close()
        except Exception:
            pass


class OpenProgramStart(QMainWindow, Ui_windowStart):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.database = sqlite3.connect('Open-Program.sqlite3')
        self.cursor = self.database.cursor()

        try:
            for element in self.cursor.execute('select name from openprogram'):
                self.listView.addItem(*element)
        except Exception:
            self.cursor.execute('create table openprogram (id, name, path)')
            for element in self.cursor.execute('select name from openprogram'):
                self.listView.addItem(*element)

        self.actionSettings.triggered.connect(self.return_to_settings)
        self.listView.itemDoubleClicked.connect(self.get_double)

    def start_func(self):
        for element in self.cursor.execute('select name from openprogram'):
            self.listView.addItem(*element)

    def return_to_settings(self):
        try:
            ex_start.close()
            ex_set.show()
        except Exception:
            pass

    def get_double(self):
        os.startfile(self.cursor.execute(f'''select path 
        from openprogram where name = "{self.listView.currentItem().text()}"''').fetchall()[0][0])


app = QApplication(sys.argv)
ex_set = OpenProgramSettings()
ex_start = OpenProgramStart()
ex_start.show()
sys.exit(app.exec_())
