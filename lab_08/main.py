import sys

from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QColorDialog, QMessageBox, QGraphicsScene, QWidget, QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor, QPen, QPixmap, QBrush, QImage, QPainter, QTransform
from PyQt5.QtCore import QRect, QCoreApplication, QEventLoop, QPointF, QTimerEvent
from math import sqrt


from mainwindow_ui import *


class myList(QtWidgets.QListWidget):
    def __init__(self, a, win):
        super().__init__(a)
        self.itemClicked.connect(self.listwidgetclicked)

    def listwidgetclicked(self, item):
        if item.text() != "Ребра отсекателя":
            win.set_parallel(item)
        else:
            win.redraw_all()

    

class myScene(QtWidgets.QGraphicsScene):
    def __init__(self, a, b, c, d, win):
        super().__init__(a, b, c, d)
        self.close_dot = None
        self.vert = False
        self.horiz = False
        self.last_clip = None
        self.last_line = None
        self.centre = False

    def clear(self):
        super().clear()
        self.close_dot = None
        self.vert = False
        self.horiz = False
        self.last_clip = None
        self.last_line = None
        self.centre = False

    def mousePressEvent(self, e):
        if e.button() == 1: #ЛКМ
            if self.centre:
                self.add_parallel(round(e.scenePos().x()), round(e.scenePos().y()), win.pen)
            else:
                self.add_point(round(e.scenePos().x()), round(e.scenePos().y()), win.pen)
        elif e.button() == 2: #ПКМ
            if win.closed:
                win.scene.clear()
                win.redraw_lines()
                win.closed = False
                win.clip = []
                win.listWidget.clear()
                win.listWidget.addItem("Ребра отсекателя")
            self.add_point(round(e.scenePos().x()), round(e.scenePos().y()), win.pen, mode = "clip")
                


    def keyPressEvent(self, e):
        # 16777248 shift горизонт
        # 16777249 ctrl вертик
        if not e.isAutoRepeat():
            if e.key() == 16777248:
                self.horiz = True
            elif e.key() == 16777249:
                self.vert = True

    def keyReleaseEvent(self, e):
        # 16777248 shift горизонт
        # 16777249 ctrl вертик
        if not e.isAutoRepeat():
            if e.key() == 16777248:
                self.horiz = False
            elif e.key() == 16777249:
                self.vert = False

    def add_parallel(self, x, y, pen):
        l = win.length
        t = win.t
        if t == None:
            self.addLine(x, y - l/2, x, y + l/2)
            return
        if t == 0:
            self.addLine(x - l/2, y, x + l/2, y)
            return
        xlen = win.length / sqrt(t**2 + 1)
        x1 = x - xlen /2 
        x2 = x + xlen /2 
        y1 = t * (x1 - x) + y
        y2 = t * (x2 - x) + y
        pen.setColor(win.color_line)
        # self.addLine(x1, y1, x2, y2, pen)
        self.centre = False
        self.add_point(x1, y1, pen)
        self.add_point(x2, y2, pen)
        win.item.setSelected(0)
        win.redraw_all()
        # win.redraw_edges()

    def add_point(self, x, y, pen, mode = "line"):
        x, y = round(x), round(y)
        if mode == "line":
            if self.last_line == None:
                self.last_line = [round(x), round(y)]
            else:
                if self.horiz and self.vert:
                    return
                elif self.horiz and not self.vert:
                    x = self.last_line[0]
                elif not self.horiz and self.vert:
                    y = self.last_line[1]
                pen.setColor(win.color_line)
                win.lines.append([[self.last_line[0], self.last_line[1]], [x, y]])
                self.addLine(self.last_line[0], self.last_line[1], x, y, pen)
                self.last_line = None

        elif mode == "clip":
            if self.close_dot == None:
                self.close_dot = [round(x), round(y)]
            else:
                if self.horiz and self.vert:
                    return
                elif self.horiz and not self.vert:
                    x = self.last_clip[0]
                elif not self.horiz and self.vert:
                    y = self.last_clip[1]
                pen.setColor(win.color_edge)
                win.clip.append([[self.last_clip[0], self.last_clip[1]], [x, y]])
                self.addLine(self.last_clip[0], self.last_clip[1], x, y, pen)
                first = "({:d}, {:d})".format(self.last_clip[0], self.last_clip[1])
                last = "({:d}, {:d})".format(x, y)
                win.listWidget.addItem("{:<25s} {:<25s}".format(first, last))
            self.last_clip = [x, y]
        
        

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.t = None
        self.closed = False
        self.chosen = False
        self.length = None

        self.color_clipped = QColor() 
        self.color_line = QColor() 
        self.color_edge = QColor()

        self.color_edge_def()
        self.color_clipped_def()
        self.color_line_def()

        self.pen = QPen(self.color_edge)

        self.lines = []
        self.clip = []
        self.last_dot = None
        self.rcontent = self.graphicsView.contentsRect()
        self.scene = myScene(0, 0, self.rcontent.width(), self.rcontent.height(), self)
        self.graphicsView.setScene(self.scene)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle("Ошибка ввода")

        font = QtGui.QFont()
        font.setPointSize(11)
        tmp = self.listWidget.geometry()
        self.listWidget.hide()
        self.listWidget = myList(self.centralwidget, self)
        self.listWidget.setGeometry(tmp)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItem("Ребра отсекателя")

        self.is_line = False
        self.is_clip = False
        self.cur_len = 0

        self.rect = None

        self.bind()
        self.clear()

    def close(self):
        if self.scene.close_dot == None:
            self.msg.setText("Операция невозможна: отсекатель уже замкнут или не введено еще ни одной точки")
            self.msg.show()
            return
        self.scene.add_point(self.scene.close_dot[0], self.scene.close_dot[1], self.pen, mode = "clip")
        self.scene.close_dot = None
        self.closed = True
        self.centre = self.find_centre()

    def find_centre(self):
        x0 = self.clip[0][0][0]
        x1 = self.clip[0][0][0]
        y0 =  self.clip[0][0][1]
        y1 = self.clip[0][0][1]
        for i in self.clip:
            if i[0][0] > x1:
                x1 = i[0][0]
            if i[0][0] < x0:
                x0 = i[0][0]
            if i[0][1] > y1:
                y1 = i[0][1]
            if i[0][1] < y0:
                y0 = i[0][1]
        return [(x1 + x0)/2, (y1 + y0)/2]

    def choose_color_clipped(self):
        self.color_clipped = QColorDialog.getColor()
        self.color_ind_clipped.setStyleSheet("background-color:" + self.color_clipped.name() + ";border: 1px solid black;")

    def choose_color_edge(self):
        self.color_edge = QColorDialog.getColor()
        self.color_ind_edge.setStyleSheet("background-color:" + self.color_edge.name() + ";border: 1px solid black;")

    def choose_color_line(self):
        self.color_line = QColorDialog.getColor()
        self.color_ind_line.setStyleSheet("background-color:" + self.color_line.name() + ";border: 1px solid black;")
        
    def color_clipped_def(self):
        self.color_clipped.setRgb(0, 0, 255)
        self.color_ind_clipped.setStyleSheet("background-color:" + self.color_clipped.name() + ";border: 1px solid black;")

    def color_edge_def(self):
        self.color_edge.setRgb(0, 0, 0)
        self.color_ind_edge.setStyleSheet("background-color:" + self.color_edge.name() + ";border: 1px solid black;")

    def color_line_def(self):
        self.color_line.setRgb(255, 0, 0)
        self.color_ind_line.setStyleSheet("background-color:" + self.color_line.name() + ";border: 1px solid black;")

    def redraw_lines(self):
        self.pen.setColor(self.color_line)
        for i in self.lines:
            self.scene.addLine(i[0][0], i[0][1], i[1][0], i[1][1], self.pen)

    def redraw_edges(self):
        self.pen.setColor(self.color_edge)
        for i in self.clip:
            self.scene.addLine(i[0][0], i[0][1], i[1][0], i[1][1], self.pen)
    
    def redraw_all(self):
        self.scene.clear()
        self.redraw_edges()
        self.redraw_lines()

    def clear(self):
        self.scene.clear()
        self.listWidget.clear()
        self.listWidget.addItem("Ребра отсекателя")
        self.lines = []
        self.clip = []
        self.last_dot = None
        self.t = None
        self.chosen = False
        self.length = None

    def draw_parallel(self):
        if not self.chosen:
            self.msg.setText("Не выбрано ребро, параллельно которому требуется построить отрезок")
            self.msg.show()
            return
        
        try:
            self.length = int(self.lineEdit.text().strip())
            if (self.length <= 0):
                self.msg.setText("Ошибка ввода в поле длины отрезка. Необходимо ввести ровно одно натуральное число")
                self.msg.show() 
                return
        except:
            self.msg.setText("Ошибка ввода в поле длины отрезка. Необходимо ввести ровно одно натуральное число")
            self.msg.show()
            return
        
        self.scene.centre = True
   

    def set_parallel(self, item):
        s1, s2, s3, s4= item.text().split()
        x1, y1, x2, y2 = map(int, [s1[1:-1], s2[:-1], s3[1:-1], s4[:-1]])
        if x1 == x2:
            self.t = None
        else:
            self.t = (y2 - y1) / (x2 - x1)
        self.chosen = True
        self.redraw_all()
        self.pen.setColor(QColor(255,0,255))
        self.pen.setWidth(2)
        self.scene.addLine(x1, y1, x2, y2, self.pen)
        self.pen.setWidth(1)
        self.item = item
        
    def bind(self):
        self.but_clear.clicked.connect(self.clear)
        self.but_close_2.clicked.connect(self.draw_parallel)
        self.but_close.clicked.connect(self.close)
        self.but_fill.clicked.connect(self.cut)
        self.but_color_clipped.clicked.connect(self.choose_color_clipped)
        self.but_color_edge.clicked.connect(self.choose_color_edge)
        self.but_color_line.clicked.connect(self.choose_color_line)
        self.but_color_clipped_def.clicked.connect(self.color_clipped_def)
        self.but_color_line.clicked.connect(self.color_line_def)
        self.but_color_edge_def.clicked.connect(self.color_edge_def)

    def button_lock(self, arr):
        for i in arr:
            i.setEnabled(False)
        self.vert = True
        self.horiz = True

    def button_unlock(self, arr):
        for i in arr:
            i.setEnabled(True)
        self.vert = False
        self.horiz = False


    def line_mode(self):
        if self.is_line:
            self.is_line = False
            self.button_unlock(self.lines_buttons)
        else:
            self.is_line = True
            self.button_lock(self.lines_buttons)
            self.pen.setColor(self.color_line)
    
    def clip_mode(self):
        if self.is_clip:
            self.is_clip = False
            self.button_unlock(self.clip_buttons)
        else:
            self.is_clip = True
            self.button_lock(self.clip_buttons)
            self.pen.setColor(self.color_clip)
    
    def draw_new_segment(self, point1, point2, t_beg, t_end):
        x_beg = round(point1[0] + (point2[0] - point1[0]) * t_beg)
        y_beg = round(point1[1] + (point2[1] - point1[1]) * t_beg)
        x_end = round(point1[0] + (point2[0] - point1[0]) * t_end)
        y_end = round(point1[1] + (point2[1] - point1[1]) * t_end)
        self.scene.addLine(x_beg, y_beg, x_end, y_end, pen = self.pen)

    def clipping(self):
        self.pen.setColor(self.color_fill)
        if self.rect == None:
            self.msg.setText("Не введен отсекатель!")
            self.msg.show() 
            return
        
        for line in self.lines:
            p1 = [i for i in line[0]]
            p2 = [i for i in line[1]]
            self.cut()
    
    def cut(self):
        if not self.closed:
            self.msg.setText("Отсекатель не замкнут!")
            self.msg.show() 
            return
        if not check_clip(self.clip):
            self.msg.setText("Отсекатель не выпуклый!")
            self.msg.show() 
            return
        self.pen.setColor(self.color_clipped)
        self.pen.setWidth(2)
        for i in self.lines:
            self.kb_cut(i, self.centre)
        self.pen.setWidth(1)

    def kb_cut(self, line, centre):
        point1 = line[0]
        point2 = line[1]
        t_beg = 0
        t_end = 1
        # директриса отрезка
        D = [point2[0] - point1[0], point2[1] - point1[1]]

        for edge in self.clip:
            # вычисляем внутреннюю нормаль к i-й стороне
            normal = inner_normal(edge, centre)
            # вычисляем вектор от начала отрезка до i-й вершины
            W = [point1[0] - edge[1][0], point1[1] - edge[1][1]]
            # вычисляем два скалярных произведения
            Dsm = scalar_mult(D, normal)
            Wsm = scalar_mult(W, normal)

             # если отрезок параллелен ребру отсекателя или вырожден в точку (P2==P1)
            if Dsm == 0:
                # если расположен по видимую сторону от текущей стороны - отсекать нечего
                if Wsm >= 0:
                    continue
                # а если невидим относительно текущей стороны, значит является полностью невидимым
                else:
                    return
            # иначе находим точку пересечения отрезка и текущего ребра
            else:
                t = -Wsm / Dsm

            # если точка пересечения относится к началу видимой области
            if Dsm > 0:
                # если отрезок пересекает ребро за конечной точкой отрезка - невидимый
                if t > 1:
                    return 
                # иначе обновляем нижнюю видимую точку в случае необходимости
                else:
                    t_beg = max(t_beg, t)
            # если точка пересечения относится к концу видимой области - по аналогии
            else:
                if t < 0:
                    return 
                else:
                    t_end = min(t_end, t)
        # проверка на корректность
        if t_beg <= t_end:
            self.draw_new_segment(point1, point2, t_beg, t_end)

    
#   отсекатель проверяется на выпуклость
def check_clip(clip):
    global_direction = 0
    i = 0
    n = len(clip)
    for i in range(n - 1):
        cur_direction = vect_mult_sign_z(clip[i][0], clip[i][1], clip[i + 1][1])

        if global_direction == 0:
            global_direction = cur_direction
        else:
            if global_direction != cur_direction:
                return False
    return True

# определение "знака" (знака проекции на ось z) векторного произведения
# векторов [point1, point2] и [point2, point3]
def vect_mult_sign_z(point1, point2, point3):
    x1 = point2[0] - point1[0]
    y1 = point2[1] - point1[1]
    x2 = point3[0] - point2[0]
    y2 = point3[1] - point2[1]
    z = x1 * y2 - y1 * x2
    if z > 0:
        return 1
    elif z < 0:
        return -1
    return 0

# внутренняя нормаль к стороне
def inner_normal(edge, central):
    point1, point2 = edge
    i = point2[0] - point1[0]
    j = point2[1] - point1[1]

    if j == 0:
        normal = [0, 1]
    else:
        normal = [j, -i]

    if scalar_mult_sign(normal, [central[0] - point2[0], central[1] - point2[1]]) < 0:
        normal[0] *= -1
        normal[1] *= -1
    return normal

# знак скалярного произведения векторов vec1 и vec2
def scalar_mult_sign(vec1, vec2):
    sm = scalar_mult(vec1, vec2)
    if sm > 0:
        return 1
    elif sm < 0:
        return -1
    return 0
   
   # скалярное произведение векторов vec1 и vec2
def scalar_mult(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]
       
def swap(p1, p2):
    t = [i for i in p1]
    p1[0] = p2[0]
    p1[1] = p2[1]
    p2[0] = t[0]
    p2[1] = t[1]

def is_visible(code1, code2):
    flag = 1
    for i in range(len(code1)):
        if not (code1[i] == code2[i] == 0):
            flag = 0
    return flag



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())