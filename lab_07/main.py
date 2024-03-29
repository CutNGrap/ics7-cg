import sys

from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QColorDialog, QMessageBox, QGraphicsScene, QWidget
from PyQt5.QtGui import QColor, QPen, QPixmap, QBrush, QImage, QPainter, QTransform
from PyQt5.QtCore import QRect, QCoreApplication, QEventLoop, QPointF


from mainwindow_ui import *

DEL_COUNT = 1


class myScene(QtWidgets.QGraphicsScene):
    def __init__(self, a, b, c, d, win):
        super().__init__(a, b, c, d)
        self.clip = None
        self.last_pos = None
        self.horiz = False
        self.vert = False

    def mousePressEvent(self, e):
        if win.is_line:
            self.add_point(round(e.scenePos().x()), round(e.scenePos().y()))
        elif win.is_clip and self.clip != None:
            self.removeItem(self.itemAt(self.clip, QTransform()))
            self.clip = None

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
    

    def mouseMoveEvent(self, e):
        if not win.is_clip:
            return 
        if self.clip == None:
            self.clip = e.scenePos()
            self.last_pos = e.scenePos()
        else:
            self.clear()
            win.redraw_lines()
            x1, y1 = round(self.clip.x()), round(self.clip.y())
            x2, y2 = round(e.scenePos().x()), round(e.scenePos().y())
            if x1 > x2:
                t = x1
                x1 = x2
                x2 = t
            if y1 > y2:
                t = y1
                y1 = y2
                y2 = t
            self.addRect(x1, y1, x2 - x1, y2 - y1)
            plc = QPointF(x1, y1)
            self.last_pos = plc
            win.rect = [x1, x2, y1, y2]

    def add_point(self, x, y):
        if win.last_dot == None:
            win.last_dot = [round(x), round(y)]
        else:
            if self.horiz and self.vert:
                return
            elif self.horiz and not self.vert:
                x = win.last_dot[0]
            elif not self.horiz and self.vert:
                y = win.last_dot[1]
            win.lines.append([[win.last_dot[0], win.last_dot[1]], [x, y]])
            win.scene.addLine(win.last_dot[0], win.last_dot[1], x, y, win.pen)
            first = "({:d}, {:d})".format(win.last_dot[0], win.last_dot[1])
            last = "({:d}, {:d})".format(win.last_dot[0], win.last_dot[1])
            win.listWidget.addItem("{:<25s} {:<25s}".format(first, last))
            win.last_dot = None

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.color_clip = QColor() 
        self.color_line = QColor() 
        self.color_fill = QColor()

        self.color_line.setRed(255) 
        self.color_fill.setBlue(255)

        self.pen = QPen(self.color_clip)

        self.lines = []
        self.last_dot = None
        self.rcontent = self.graphicsView.contentsRect()
        self.scene = myScene(0, 0, self.rcontent.width(), self.rcontent.height(), self)
        self.graphicsView.setScene(self.scene)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle("Ошибка ввода")
        self.listWidget.addItem("{:<25s} {:<25s}".format("Начало", "Конец"))

        self.is_line = False
        self.is_clip = False
        self.cur_len = 0

        self.rect = None

        self.clip_buttons = [self.but_clear, self.but_clipping, self.but_lines, self.but_add_lines]
        self.lines_buttons = [self.but_clear, self.but_clipping, self.but_add_lines, self.but_clip]

        self.bind()

    def redraw_lines(self):
        self.pen.setColor(self.color_line)
        for i in self.lines:
            self.scene.addLine(i[0][0], i[0][1], i[1][0], i[1][1], self.pen)

    def clear(self):
        self.scene.clear()
        self.listWidget.clear()
        self.listWidget.addItem("{:<25s} {:<25s}".format("Начало", "Конец"))
        self.lines = []
        self.last_dot = None
        
    def bind(self):
        self.but_clear.clicked.connect(self.clear)
        self.but_lines.clicked.connect(self.line_mode)
        self.but_clip.clicked.connect(self.clip_mode)
        self.but_add_lines.clicked.connect(self.add_rect_lines)
        self.but_clipping.clicked.connect(self.clipping)

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

    def add_rect_lines(self):
        if self.rect == None:
            self.msg.setText("Не введен отсекатель!")
            self.msg.show() 
            return
        
        rect = self.rect
        self.pen.setColor(self.color_line)

        vert = abs(self.rect[3] - self.rect[2]) * 0.8
        hor = abs(self.rect[1] - self.rect[0]) * 0.8

        # hor
        self.scene.add_point(rect[0] + hor, rect[2])
        self.scene.add_point(rect[1] - hor, rect[2])
        self.scene.add_point(rect[0] + hor, rect[3])
        self.scene.add_point(rect[1] - hor, rect[3])

        # vert
        self.scene.add_point(rect[0], rect[2] + vert)
        self.scene.add_point(rect[0], rect[3] - vert)
        self.scene.add_point(rect[1], rect[2] + vert)
        self.scene.add_point(rect[1], rect[3] - vert)

    def clipping(self):
        brush = QBrush(QColor(255, 255, 255))
        self.scene.addRect(self.rect[0], self.rect[2], self.rect[1] - self.rect[0], self.rect[3] - self.rect[2], brush = brush)
        self.pen.setColor(self.color_fill)
        if self.rect == None:
            self.msg.setText("Не введен отсекатель!")
            self.msg.show() 
            return
        
        for line in self.lines:
            p1 = [i for i in line[0]]
            p2 = [i for i in line[1]]
            self.sutherland_cohen(p1, p2)

    def sutherland_cohen(self, p1, p2):
        flag = 1 

        if abs(p2[0] - p1[0]) < 1e-6:
            flag = -1   # верт
        else:
            t = (p2[1] - p1[1]) / (p2[0] - p1[0])
            if abs(t) < 1e-6:
                flag = 0   # горизонтальный
        
        for i in range(4):
            code1 = get_code(p1, self.rect)
            code2 = get_code(p2, self.rect)

            if is_visible(code1, code2): #полностью видимый
                self.scene.addLine(p1[0], p1[1], p2[0], p2[1], self.pen)
                return 1
            elif code_bit_and(code1, code2) !=0 : #полностью невидимый
                return -1

            if code1[i] == code2[i]:
                continue

            if code1[i] == 0: #если первая вершина внутри
                swap(p1, p2) #поменять местами
            
            if flag != -1:
                if i < 2:
                    p1[1] = t * (self.rect[i] - p1[0]) + p1[1]
                    p1[0] = self.rect[i]
                    continue
                else:
                    p1[0] = 1/t * (self.rect[i] - p1[1]) + p1[0]

            p1[1] = self.rect[i]
            
        self.scene.addLine(p1[0], p1[1], p2[0], p2[1], self.pen)
        return 0
        
def swap(p1, p2):
    t = [i for i in p1]
    p1[0] = p2[0]
    p1[1] = p2[1]
    p2[0] = t[0]
    p2[1] = t[1]

def get_code(point, rect):
    code = [0, 0, 0, 0]
    if point[0] < rect[0]:
        code[0] = 1
    elif point[0] > rect[1]:
        code[1] = 1
    if point[1] < rect[2]:
        code[2] = 1
    elif point[1] > rect[3]:
        code[3] = 1

    return code


def code_bit_and(code1, code2):
    count = 0
    for i in range(len(code1)):
        count += code1[i] & code2[i]
    
    return count

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
    # bar = QProgressBar()
    # bar.setProperty("value", 24)
    # bar.show()
    sys.exit(app.exec())