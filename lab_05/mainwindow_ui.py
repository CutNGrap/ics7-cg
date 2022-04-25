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
        MainWindow.resize(1269, 948)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(320, 0, 951, 891))
        self.graphicsView.setObjectName("graphicsView")
        self.color_ind_edge = QtWidgets.QLabel(self.centralwidget)
        self.color_ind_edge.setGeometry(QtCore.QRect(10, 60, 71, 71))
        self.color_ind_edge.setAutoFillBackground(False)
        self.color_ind_edge.setText("")
        self.color_ind_edge.setAlignment(QtCore.Qt.AlignCenter)
        self.color_ind_edge.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.color_ind_edge.setObjectName("color_ind_edge")
        self.but_color_edge = QtWidgets.QPushButton(self.centralwidget)
        self.but_color_edge.setGeometry(QtCore.QRect(90, 60, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_color_edge.setFont(font)
        self.but_color_edge.setObjectName("but_color_edge")
        self.line_x = QtWidgets.QLineEdit(self.centralwidget)
        self.line_x.setGeometry(QtCore.QRect(60, 510, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_x.setFont(font)
        self.line_x.setAlignment(QtCore.Qt.AlignCenter)
        self.line_x.setObjectName("line_x")
        self.but_color_bg = QtWidgets.QPushButton(self.centralwidget)
        self.but_color_bg.setGeometry(QtCore.QRect(90, 140, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_color_bg.setFont(font)
        self.but_color_bg.setObjectName("but_color_bg")
        self.but_color_edge_def = QtWidgets.QPushButton(self.centralwidget)
        self.but_color_edge_def.setGeometry(QtCore.QRect(190, 60, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_color_edge_def.setFont(font)
        self.but_color_edge_def.setObjectName("but_color_edge_def")
        self.color_ind_bg = QtWidgets.QLabel(self.centralwidget)
        self.color_ind_bg.setGeometry(QtCore.QRect(10, 140, 71, 71))
        self.color_ind_bg.setAutoFillBackground(True)
        self.color_ind_bg.setText("")
        self.color_ind_bg.setAlignment(QtCore.Qt.AlignCenter)
        self.color_ind_bg.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.color_ind_bg.setObjectName("color_ind_bg")
        self.but_color_bg_def = QtWidgets.QPushButton(self.centralwidget)
        self.but_color_bg_def.setGeometry(QtCore.QRect(190, 140, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_color_bg_def.setFont(font)
        self.but_color_bg_def.setObjectName("but_color_bg_def")
        self.color_ind_fill = QtWidgets.QLabel(self.centralwidget)
        self.color_ind_fill.setGeometry(QtCore.QRect(10, 220, 71, 71))
        self.color_ind_fill.setAutoFillBackground(True)
        self.color_ind_fill.setText("")
        self.color_ind_fill.setAlignment(QtCore.Qt.AlignCenter)
        self.color_ind_fill.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.color_ind_fill.setObjectName("color_ind_fill")
        self.but_color_fill = QtWidgets.QPushButton(self.centralwidget)
        self.but_color_fill.setGeometry(QtCore.QRect(90, 220, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_color_fill.setFont(font)
        self.but_color_fill.setObjectName("but_color_fill")
        self.but_color_fill_def = QtWidgets.QPushButton(self.centralwidget)
        self.but_color_fill_def.setGeometry(QtCore.QRect(190, 220, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_color_fill_def.setFont(font)
        self.but_color_fill_def.setObjectName("but_color_fill_def")
        self.lab_x = QtWidgets.QLabel(self.centralwidget)
        self.lab_x.setGeometry(QtCore.QRect(10, 510, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_x.setFont(font)
        self.lab_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_x.setObjectName("lab_x")
        self.lab_y = QtWidgets.QLabel(self.centralwidget)
        self.lab_y.setGeometry(QtCore.QRect(10, 540, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_y.setFont(font)
        self.lab_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_y.setObjectName("lab_y")
        self.line_y = QtWidgets.QLineEdit(self.centralwidget)
        self.line_y.setGeometry(QtCore.QRect(60, 540, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_y.setFont(font)
        self.line_y.setAlignment(QtCore.Qt.AlignCenter)
        self.line_y.setObjectName("line_y")
        self.but_add_dot = QtWidgets.QPushButton(self.centralwidget)
        self.but_add_dot.setGeometry(QtCore.QRect(190, 510, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_add_dot.setFont(font)
        self.but_add_dot.setObjectName("but_add_dot")
        self.but_close = QtWidgets.QPushButton(self.centralwidget)
        self.but_close.setGeometry(QtCore.QRect(20, 670, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_close.setFont(font)
        self.but_close.setObjectName("but_close")
        self.lab_centre_4 = QtWidgets.QLabel(self.centralwidget)
        self.lab_centre_4.setGeometry(QtCore.QRect(10, 570, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_centre_4.setFont(font)
        self.lab_centre_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_centre_4.setObjectName("lab_centre_4")
        self.lab_centre_5 = QtWidgets.QLabel(self.centralwidget)
        self.lab_centre_5.setGeometry(QtCore.QRect(0, 620, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_centre_5.setFont(font)
        self.lab_centre_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_centre_5.setObjectName("lab_centre_5")
        self.but_fill = QtWidgets.QPushButton(self.centralwidget)
        self.but_fill.setGeometry(QtCore.QRect(20, 750, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_fill.setFont(font)
        self.but_fill.setObjectName("but_fill")
        self.but_clear = QtWidgets.QPushButton(self.centralwidget)
        self.but_clear.setGeometry(QtCore.QRect(20, 800, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.but_clear.setFont(font)
        self.but_clear.setObjectName("but_clear")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 720, 151, 20))
        self.checkBox.setObjectName("checkBox")
        self.lab_centre_6 = QtWidgets.QLabel(self.centralwidget)
        self.lab_centre_6.setGeometry(QtCore.QRect(10, 0, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_centre_6.setFont(font)
        self.lab_centre_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_centre_6.setObjectName("lab_centre_6")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 310, 271, 192))
        self.listWidget.setObjectName("listWidget")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа #5"))
        self.but_color_edge.setText(_translate("MainWindow", "Выбрать\n"
"цвет\n"
"контура"))
        self.but_color_bg.setText(_translate("MainWindow", "Выбрать\n"
"цвет\n"
"фона"))
        self.but_color_edge_def.setText(_translate("MainWindow", "По\n"
"умочанию"))
        self.but_color_bg_def.setText(_translate("MainWindow", "По\n"
"умочанию"))
        self.but_color_fill.setText(_translate("MainWindow", "Выбрать\n"
"цвет\n"
"закраски"))
        self.but_color_fill_def.setText(_translate("MainWindow", "По\n"
"умочанию"))
        self.lab_x.setText(_translate("MainWindow", "X"))
        self.lab_y.setText(_translate("MainWindow", "Y"))
        self.but_add_dot.setText(_translate("MainWindow", "Добавить\n"
"точку"))
        self.but_close.setText(_translate("MainWindow", "Замкнуть фигуру"))
        self.lab_centre_4.setText(_translate("MainWindow", "Удерживайте SHIFT, чтобы\n"
"добавить вертикальную линию"))
        self.lab_centre_5.setText(_translate("MainWindow", "Удерживайте CTRL, чтобы\n"
"добавить горизонтальную линию"))
        self.but_fill.setText(_translate("MainWindow", "Закрасить"))
        self.but_clear.setText(_translate("MainWindow", "Очистить экран"))
        self.checkBox.setText(_translate("MainWindow", "Включить задержку"))
        self.lab_centre_6.setText(_translate("MainWindow", "Изменения цвета контура и фона\n"
"вступают в силу после очистки экрана"))
