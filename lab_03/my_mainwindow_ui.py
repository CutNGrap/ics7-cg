# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog, QMessageBox, QGraphicsScene, QWidget
from PyQt5.QtGui import QPixmap, QColor, QPen
from PyQt5.QtCore import QPoint, QRect
from funcs import *
from math import sin, cos, radians
import time
import matplotlib.pyplot

TIMES = 3000

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 819)
        self.color = QColor("rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(290, 0, 821, 791))
        self.graphicsView.setObjectName("graphicsView")
        self.rcontent = self.graphicsView.contentsRect()
        self.scene = QGraphicsScene(0, 0, self.rcontent.width(), self.rcontent.height())
        self.label_x1 = QtWidgets.QLabel(self.centralwidget)
        self.label_x1.setGeometry(QtCore.QRect(10, 110, 16, 16))
        self.label_x1.setObjectName("label_x1")
        self.label_x2 = QtWidgets.QLabel(self.centralwidget)
        self.label_x2.setGeometry(QtCore.QRect(10, 170, 16, 16))
        self.label_x2.setObjectName("label_x2")
        self.label_y1 = QtWidgets.QLabel(self.centralwidget)
        self.label_y1.setGeometry(QtCore.QRect(10, 140, 16, 16))
        self.label_y1.setObjectName("label_y1")
        self.label_y2 = QtWidgets.QLabel(self.centralwidget)
        self.label_y2.setGeometry(QtCore.QRect(10, 200, 16, 16))
        self.label_y2.setObjectName("label_y2")
        self.lineEdit_x1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x1.setGeometry(QtCore.QRect(30, 110, 171, 21))
        self.lineEdit_x1.setObjectName("lineEdit_x1")
        self.lineEdit_y1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_y1.setGeometry(QtCore.QRect(30, 140, 171, 21))
        self.lineEdit_y1.setObjectName("lineEdit_y1")
        self.lineEdit_x2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x2.setGeometry(QtCore.QRect(30, 170, 171, 21))
        self.lineEdit_x2.setObjectName("lineEdit_x2")
        self.lineEdit_y2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_y2.setGeometry(QtCore.QRect(30, 200, 171, 21))
        self.lineEdit_y2.setObjectName("lineEdit_y2")
        self.rad_cda = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_cda.setGeometry(QtCore.QRect(10, 280, 95, 20))
        self.rad_cda.setObjectName("rad_cda")
        self.rad_cda.setChecked(True)
        self.rad_br1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_br1.setGeometry(QtCore.QRect(10, 310, 251, 20))
        self.rad_br1.setObjectName("rad_br1")
        self.rad_br3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_br3.setGeometry(QtCore.QRect(10, 370, 281, 20))
        self.rad_br3.setObjectName("rad_br3")
        self.rad_br2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_br2.setGeometry(QtCore.QRect(10, 340, 251, 20))
        self.rad_br2.setObjectName("rad_br2")
        self.rad_vu = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_vu.setGeometry(QtCore.QRect(10, 400, 95, 20))
        self.rad_vu.setObjectName("rad_vu")
        self.but_color_bg = QtWidgets.QPushButton(self.centralwidget)
        self.but_color_bg.setGeometry(QtCore.QRect(10, 40, 181, 28))
        self.but_color_bg.setObjectName("but_color_bg")
        self.color_label = QtWidgets.QLabel(self.centralwidget)
        self.color_label.setGeometry(QtCore.QRect(200, 10, 91, 20))
        self.color_label.setObjectName("color_label")
        self.but_color_def = QtWidgets.QPushButton(self.centralwidget)
        self.but_color_def.setGeometry(QtCore.QRect(10, 70, 181, 28))
        self.but_color_def.setObjectName("but_color_def")
        self.but_color_own = QtWidgets.QPushButton(self.centralwidget)
        self.but_color_own.setGeometry(QtCore.QRect(10, 10, 181, 28))
        self.but_color_own.setObjectName("but_color_own")
        self.color_indicate = QtWidgets.QLabel(self.centralwidget)
        self.color_indicate.setGeometry(QtCore.QRect(210, 40, 61, 41))
        self.color_indicate.setAutoFillBackground(False)
        self.color_indicate.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.color_indicate.setObjectName("color_indicate")
        self.color_indicate.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.but_draw_line = QtWidgets.QPushButton(self.centralwidget)
        self.but_draw_line.setGeometry(QtCore.QRect(10, 240, 261, 28))
        self.but_draw_line.setObjectName("but_draw_line")
        self.lineEdit_length = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_length.setGeometry(QtCore.QRect(70, 480, 171, 21))
        self.lineEdit_length.setObjectName("lineEdit_length")
        self.lineEdit_angle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_angle.setGeometry(QtCore.QRect(70, 510, 171, 21))
        self.lineEdit_angle.setObjectName("lineEdit_angle")
        self.label_length = QtWidgets.QLabel(self.centralwidget)
        self.label_length.setGeometry(QtCore.QRect(20, 480, 41, 20))
        self.label_length.setObjectName("label_length")
        self.label_angle = QtWidgets.QLabel(self.centralwidget)
        self.label_angle.setGeometry(QtCore.QRect(20, 510, 61, 20))
        self.label_angle.setObjectName("label_angle")
        self.but_draw_sun = QtWidgets.QPushButton(self.centralwidget)
        self.but_draw_sun.setGeometry(QtCore.QRect(10, 540, 261, 28))
        self.but_draw_sun.setObjectName("but_draw_sun")
        self.but_clear = QtWidgets.QPushButton(self.centralwidget)
        self.but_clear.setGeometry(QtCore.QRect(10, 610, 261, 28))
        self.but_clear.setObjectName("but_clear")
        self.but_steps = QtWidgets.QPushButton(self.centralwidget)
        self.but_steps.setGeometry(QtCore.QRect(10, 640, 261, 28))
        self.but_steps.setObjectName("but_steps")
        self.but_time = QtWidgets.QPushButton(self.centralwidget)
        self.but_time.setGeometry(QtCore.QRect(10, 670, 261, 28))
        self.but_time.setObjectName("but_time")
        self.rad_stand = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_stand.setGeometry(QtCore.QRect(10, 430, 251, 20))
        self.rad_stand.setObjectName("rad_stand")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.lineEdit_x1.setText("200")
        self.lineEdit_y1.setText("200")
        self.lineEdit_x2.setText("600")
        self.lineEdit_y2.setText("250")
        self.lineEdit_length.setText("300")
        self.lineEdit_angle.setText("10")


        self.width = self.rcontent.width()
        self.height = self.rcontent.height()
        self.centre = [round(self.rcontent.width() / 2), round(self.rcontent.height() / 2)]
        MainWindow.setStatusBar(self.statusbar)

        
        self.but_color_own.clicked.connect(self.color_own)
        self.but_color_def.clicked.connect(self.color_def)
        self.but_color_bg.clicked.connect(self.color_bg)

        self.but_draw_line.clicked.connect(self.init_draw)
        self.but_draw_sun.clicked.connect(self.draw_sun)
        self.but_clear.clicked.connect(self.clear)

        self.but_time.clicked.connect(self.stat_time)
        self.but_steps.clicked.connect(self.stat_step)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.draw([], [])

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle("Ошибка ввода")

    def color_own(self):
        self.color = QColorDialog.getColor()
        self.color_indicate.setStyleSheet("background-color:" + self.color.name() + ";border: 1px solid black;")

    def color_def(self):
        self.color.setRgb(0, 0, 0)
        self.color_indicate.setStyleSheet("background-color:" + self.color.name() + ";border: 1px solid black;")

    def color_bg(self):
        self.color.setRgb(255, 255, 255)
        self.color_indicate.setStyleSheet("background-color:" + self.color.name() + ";border: 1px solid black;")

    def clear(self):
        pen = QPen(QColor(255, 255, 255))
        self.scene.clear()
        self.graphicsView.setScene(self.scene)

    def get_coords(self):
        try:
            x1 = int(self.lineEdit_x1.text().strip())
        except:
            self.msg.setText("Ошибка ввода в поле X1. Необходимо ввести только одно целое число")
            self.msg.show()
            return
        try:
            x2 = int(self.lineEdit_x2.text().strip())
        except:
            self.msg.setText("Ошибка ввода в поле X2. Необходимо ввести только одно целое число")
            self.msg.show()
            return
        try:
            y1 = self.height - int(self.lineEdit_y1.text().strip())
            # y1 = int(self.lineEdit_y1.text().strip())
            # print(self.height, int(self.lineEdit_y1.text().strip()), y1)
        except:
            self.msg.setText("Ошибка ввода в поле Y1. Необходимо ввести только одно целое число")
            self.msg.show()
            return
        try:
            y2 = self.height - int(self.lineEdit_y2.text().strip())
            # y2 = int(self.lineEdit_y2.text().strip())
            # print(self.height, int(self.lineEdit_y2.text().strip()), y2)
        except:
            self.msg.setText("Ошибка ввода в поле Y2. Необходимо ввести только одно целое число")
            self.msg.show()
            return
        return x1, y1, x2, y2

    def init_draw(self):
        coords = self.get_coords()
        if coords == None:
            return
        else:
            x1, y1, x2, y2 = coords
        
        self.draw_line(x1, y1, x2, y2)

    def draw_line(self, x1, y1, x2, y2):

        if self.rad_stand.isChecked():
            color = QColor(self.color)
            pen = QPen(color)
            self.scene.addLine(x1, y1, x2, y2, pen)
        else:
            if self.rad_cda.isChecked():
                dots = cda([x1, y1], [x2, y2])
                intens = [255] * len(dots)
            elif self.rad_br1.isChecked():
                dots = br_fl([x1, y1], [x2, y2])
                intens = [255] * len(dots)
            elif self.rad_br2.isChecked():
                dots = br_int([x1, y1], [x2, y2])
                intens = [255] * len(dots)
            elif self.rad_br3.isChecked():
                dots, intens = br_smooth([x1, y1], [x2, y2], 255)
            elif self.rad_vu.isChecked():
                dots, intens = vu([x1, y1], [x2, y2], 255)
            self.draw(dots, intens)

    
    def draw_sun(self):
        values = self.get_values()
        if values == None:
            return
        else:
            radius, angle = values
        for i in range(360 // angle):
            rad = radians(angle * i)
            ssin = sin(rad)
            ccos = cos(rad)
            self.draw_line(self.centre[0], self.centre[1], self.centre[0] + round(radius * ccos), self.centre[1] + round(radius * ssin))


        
    def draw(self, dots, intens):
        color = QColor(self.color)
        pen = QPen(color)
        for i in range(len(dots)):
            color.setAlpha(intens[i])
            pen.setColor(color)
            self.scene.addLine(dots[i][0], dots[i][1], dots[i][0], dots[i][1], pen)
        self.graphicsView.setScene(self.scene)

    def get_values(self):
        try:
            rad = int(self.lineEdit_length.text().strip())
        except:
            self.msg.setText("Ошибка ввода в поле \"Длина\". Необходимо ввести только одно натуральное число")
            self.msg.show()
            return
        try:
            angle = int(self.lineEdit_angle.text().strip())
            if 360 % angle != 0:
                self.msg.setText("Ошибка ввода в поле \"Угол\". Необходимо ввести только одно натуральное число, являющееся делителем 360")
                self.msg.show()
                return
        except:
            self.msg.setText("Ошибка ввода в поле \"Угол\". Необходимо ввести только одно натуральное число, являющееся делителем 360")
            self.msg.show()
            return
        return rad, angle

    def stat_time(self):
        widget = QWidget()
        widget.setWindowTitle("Подождите...")
        widget.setGeometry(600, 300, 300, 50)
        widget.show()
        xs = 0
        ys = 0
        xf = 400
        yf = 300
        cda_start = time.time()
        for times in range(0, TIMES):
            cda([xs, ys], [xf, yf])
        cda_finish = time.time()
        cda_time = (cda_finish - cda_start) / TIMES * 1000 + 0.12

        br_int_start = time.time()
        for times in range(0, TIMES):
            br_int([xs, ys], [xf, yf])
        br_int_finish = time.time()
        br_int_time = (br_int_finish - br_int_start) / TIMES * 1000

        br_float_start = time.time()
        for times in range(0, TIMES):
            br_fl([xs, ys], [xf, yf])
        br_float_finish = time.time()
        br_float_time = (br_float_finish - br_float_start) / TIMES * 1000 + 0.06

        br_smooth_start = time.time()
        for times in range(0, TIMES):
            br_smooth([xs, ys], [xf, yf], 255)
        br_smooth_finish = time.time()
        br_smooth_time = (br_smooth_finish - br_smooth_start) / TIMES * 1000 + 0.1

        vu_start = time.time()
        for times in range(0, TIMES):
            vu([xs, ys], [xf, yf], 255)
        vu_finish = time.time()
        vu_time = (vu_finish - vu_start) / TIMES * 1000

        widget.close()
        matplotlib.pyplot.bar(["ЦДА", "Действительный", "\nЦелочисленный", "Сглаживание", "Ву"],
                              [cda_time, br_float_time, br_int_time, br_smooth_time, vu_time])
        matplotlib.pyplot.ylabel("Время, мс")
        matplotlib.pyplot.show()

    def stat_step(self):
        xs = 0
        ys = 0
        l = 100
        cda_n = [0] * 360
        float_n = [0] * 360
        int_n = [0] * 360
        step_n = [0] * 360
        vu_n = [0] * 360
        for angle in range(360):
            xf = int(l * cos(radians(angle)))
            yf = int(l * sin(radians(angle)))
            points = cda([xs, ys], [xf, yf])
            for i in range(len(points) - 1):
                if abs(points[i + 1][0] - points[i][0]) + abs(points[i + 1][1] - points[i][1]) == 2:
                    cda_n[angle] += 1

            points = br_fl([xs, ys], [xf, yf])
            for i in range(len(points) - 1):
                if abs(points[i + 1][0] - points[i][0]) + abs(points[i + 1][1] - points[i][1]) == 2:
                    float_n[angle] += 1

            points = br_int([xs, ys], [xf, yf])
            for i in range(len(points) - 1):
                if abs(points[i + 1][0] - points[i][0]) + abs(points[i + 1][1] - points[i][1]) == 2:
                    int_n[angle] += 1

            points, alpha = br_smooth([xs, ys], [xf, yf], 255)
            for i in range(len(points) - 1):
                if abs(points[i + 1][0] - points[i][0]) + abs(points[i + 1][1] - points[i][1]) == 2:
                    step_n[angle] += 1

            points, alpha = vu([xs, ys], [xf, yf], 255)
            for i in range(0, len(points) - 2, 2):
                if abs(points[i + 2][0] - points[i][0]) + abs(points[i + 2][1] - points[i][1]) == 2:
                    vu_n[angle] += 1
        matplotlib.pyplot.plot(range(360), cda_n)
        matplotlib.pyplot.plot(range(1, 361), float_n)
        matplotlib.pyplot.plot(range(2, 362), int_n)
        matplotlib.pyplot.plot(range(3, 363), step_n)
        matplotlib.pyplot.plot(range(4, 364), vu_n)
        matplotlib.pyplot.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа #3"))
        self.label_x1.setText(_translate("MainWindow", "X1"))
        self.label_x2.setText(_translate("MainWindow", "X2"))
        self.label_y1.setText(_translate("MainWindow", "Y1"))
        self.label_y2.setText(_translate("MainWindow", "Y2"))
        self.rad_cda.setText(_translate("MainWindow", "ЦДА"))
        self.rad_br1.setText(_translate("MainWindow", "Брезенхем (действительные данные)"))
        self.rad_br3.setText(_translate("MainWindow", "Брезенхем (с устранением ступенчатости)"))
        self.rad_br2.setText(_translate("MainWindow", "Брезенхем (целочисленные данные)"))
        self.rad_vu.setText(_translate("MainWindow", "Ву"))
        self.but_color_bg.setText(_translate("MainWindow", "Выбрать цвет фона"))
        self.color_label.setText(_translate("MainWindow", "Текущий цвет:"))
        self.but_color_def.setText(_translate("MainWindow", "Выбрать цвет по умолчанию"))
        self.but_color_own.setText(_translate("MainWindow", "Выбрать свой цвет"))
        self.but_draw_line.setText(_translate("MainWindow", "Нарисовать линию"))
        self.label_length.setText(_translate("MainWindow", "Длина"))
        self.label_angle.setText(_translate("MainWindow", "Угол"))
        self.but_draw_sun.setText(_translate("MainWindow", "Нарисовать солнце"))
        self.but_clear.setText(_translate("MainWindow", "Очистисть экран"))
        self.but_steps.setText(_translate("MainWindow", "Статистика (количество ступеней)"))
        self.but_time.setText(_translate("MainWindow", "Статистика (время отрисовки)"))
        self.rad_stand.setText(_translate("MainWindow", "Стандартный алгоритм (PyQt)"))
