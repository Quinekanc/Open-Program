import os
import sys
import sqlite3
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog
from Open_Program_settings_ui import Ui_windowSettings
from Open_Program_ui import Ui_windowStart


class OpenProgramSettings(QMainWindow, Ui_windowSettings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = sqlite3.connect('Open-Program.sqlite3')
        self.cursor = self.database.cursor()
        self.listOfApps = []

        try:
            for element in self.cursor.execute('select name from openprogram').fetchall():
                self.listView.addItem(*element)
                self.listOfApps.append(*element)
        except Exception:
            pass

        self.addButton.clicked.connect(self.add)
        self.removeButton.clicked.connect(self.remove)
        self.dialogChoise.clicked.connect(self.dialog)
        self.listView.itemDoubleClicked.connect(self.get_double)
        self.returnButton.clicked.connect(self.return_to_start)

    def open(self):
        try:
            os.startfile(self.inputPath.text())
        except Exception:
            pass

    def dialog(self):
        try:
            file = QFileDialog.getOpenFileName(self, 'Выбрать приложение', '')[0]
            self.inputPath.setText(file)
            self.inputName.setText(file.split('/')[-1])
        except Exception:
            pass

    def add(self):
        try:
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
        except Exception:
            pass

    def get(self):
        try:
            self.inputName.setText(self.listView.currentItem().text())

            self.inputPath.setText(self.cursor.execute(f'''select path from openprogram 
                                          where name = "{self.listView.currentItem().text()}"''').fetchall()[0][0])
        except Exception:
            pass

    def get_double(self):
        try:
            self.get()
            self.open()
        except Exception:
            pass

    def remove(self):
        try:
            self.cursor.execute(f'''delete from openprogram where name = "{self.listView.currentItem().text()}"''')
            listItems = self.listView.selectedItems()
            if not listItems: return
            for item in listItems:
                self.listView.takeItem(self.listView.row(item))
            self.database.commit()
        except Exception:
            pass

    def return_to_start(self):
        try:
            ex_start.show()
            ex_start.start_func()
            ex_set.hide()
        except Exception:
            pass

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.onMainWindowResize()

    def onMainWindowResize(self):
        self.setFixedSize(math.floor(self.size().width() * 1), math.floor(self.size().height() * 1))


class OpenProgramStart(QMainWindow, Ui_windowStart):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.database = sqlite3.connect('Open-Program.sqlite3')
        self.cursor = self.database.cursor()
        self.listOfApps = []


        try:
            for element in self.cursor.execute('select name from openprogram').fetchall():
                self.listView.addItem(*element)
                self.listOfApps.append(*element)
        except Exception:
            self.cursor.execute('create table openprogram (id, name, path)')
            for element in self.cursor.execute('select name from openprogram').fetchall():
                self.listView.addItem(*element)
                self.listOfApps.append(*element)

        self.actionSettings.triggered.connect(self.return_to_settings)
        self.exitAction.triggered.connect(self.exit)
        self.listView.itemDoubleClicked.connect(self.get_double)
        self.actionDataBase.triggered.connect(self.change_db)

    def start_func(self):
        self.listView.clear()
        for element in self.cursor.execute('select name from openprogram').fetchall():
            self.listView.addItem(*element)

    def exit(self):
        try:
            ex_start.close()
        except Exception:
            pass

    def change_db(self):
        try:
            self.database.close()
            self.database = sqlite3.connect(QInputDialog.getText(self, 'Input Dialog',
                                                                 'Введите название базы данных')[0])
            self.cursor = self.database.cursor()
        except Exception:
            pass

    def return_to_settings(self):
        try:
            ex_set.show()
            ex_start.hide()
        except Exception:
            pass

    def get_double(self):
        try:
            os.startfile(self.cursor.execute(f'''select path 
            from openprogram where name = "{self.listView.currentItem().text()}"''').fetchall()[0][0])
        except Exception:
            pass

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.onMainWindowResize()

    def onMainWindowResize(self):
        self.setFixedSize(math.floor(self.size().width() * 1), math.floor(self.size().height() * 1))


app = QApplication(sys.argv)
ex_set = OpenProgramSettings()
ex_start = OpenProgramStart()
ex_start.show()
sys.exit(app.exec_())
ex_start.database.close()
ex_set.database.close()
