# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Open_Program_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowStart(object):
    def setupUi(self, windowStart):
        windowStart.setObjectName("windowStart")
        windowStart.resize(341, 341)
        self.centralwidget = QtWidgets.QWidget(windowStart)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 10, 321, 271))
        self.listView.setObjectName("listView")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(10, 290, 321, 21))
        self.openButton.setObjectName("openButton")
        windowStart.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(windowStart)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 341, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuButton = QtWidgets.QMenu(self.menuBar)
        self.menuButton.setObjectName("menuButton")
        windowStart.setMenuBar(self.menuBar)
        self.actionSettings = QtWidgets.QAction(windowStart)
        icon = QtGui.QIcon.fromTheme("C:\\Users\\User\\PycharmProjects\\Open-Program\\icos\\cogweel.ico")
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName("actionSettings")
        self.menuButton.addAction(self.actionSettings)
        self.menuBar.addAction(self.menuButton.menuAction())

        self.retranslateUi(windowStart)
        QtCore.QMetaObject.connectSlotsByName(windowStart)

    def retranslateUi(self, windowStart):
        _translate = QtCore.QCoreApplication.translate
        windowStart.setWindowTitle(_translate("windowStart", "Open-Program"))
        self.openButton.setText(_translate("windowStart", "Открыть"))
        self.menuButton.setTitle(_translate("windowStart", "Меню"))
        self.actionSettings.setText(_translate("windowStart", "Настройки"))
