# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1269, 794)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(320, 0, 951, 731))
        self.graphicsView.setObjectName("graphicsView")
        self.but_clear = QtWidgets.QPushButton(self.centralwidget)
        self.but_clear.setGeometry(QtCore.QRect(20, 550, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_clear.setFont(font)
        self.but_clear.setObjectName("but_clear")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 301, 241))
        self.listWidget.setObjectName("listWidget")
        self.but_lines = QtWidgets.QPushButton(self.centralwidget)
        self.but_lines.setGeometry(QtCore.QRect(20, 340, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_lines.setFont(font)
        self.but_lines.setObjectName("but_lines")
        self.but_clip = QtWidgets.QPushButton(self.centralwidget)
        self.but_clip.setGeometry(QtCore.QRect(20, 290, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_clip.setFont(font)
        self.but_clip.setObjectName("but_clip")
        self.but_add_lines = QtWidgets.QPushButton(self.centralwidget)
        self.but_add_lines.setGeometry(QtCore.QRect(20, 390, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_add_lines.setFont(font)
        self.but_add_lines.setObjectName("but_add_lines")
        self.but_clipping = QtWidgets.QPushButton(self.centralwidget)
        self.but_clipping.setGeometry(QtCore.QRect(20, 450, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_clipping.setFont(font)
        self.but_clipping.setObjectName("but_clipping")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1269, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа #7"))
        self.but_clear.setText(_translate("MainWindow", "Очистить экран"))
        self.but_lines.setText(_translate("MainWindow", "Ввести отрезки"))
        self.but_clip.setText(_translate("MainWindow", "Ввести отсекатель"))
        self.but_add_lines.setText(_translate("MainWindow", "Добавить отрезки на\n"
"границах отсекателя"))
        self.but_clipping.setText(_translate("MainWindow", "Отсечь"))
