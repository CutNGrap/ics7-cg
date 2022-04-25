import sys

from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QColorDialog, QMessageBox, QGraphicsScene, QWidget
from PyQt5.QtGui import QColor, QPen, QPixmap, QBrush, QImage, QPainter
from PyQt5.QtCore import QRect, QCoreApplication, QEventLoop

from pynput import mouse 


from mainwindow_ui import *

DEL_COUNT = 1


class myScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, e):
        add_point(round(e.scenePos().x()), round(e.scenePos().y()))

    def keyPressEvent(self, e):
        global win
        # 16777248 shift горизонт
        # 16777249 ctrl вертик
        if not e.isAutoRepeat():
            if e.key() == 16777248:
                win.horiz = True
            elif e.key() == 16777249:
                win.vert = True

    def keyReleaseEvent(self, e):
        global win
        # 16777248 shift горизонт
        # 16777249 ctrl вертик
        if not e.isAutoRepeat():
            if e.key() == 16777248:
                win.horiz = False
            elif e.key() == 16777249:
                win.vert = False

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.color_bg = QColor("rgb(255, 255, 255)") 
        self.color_edge = QColor("rgb(255, 255, 255)") 
        self.color_fill = QColor("rgb(255, 255, 255)") 

        self.t_color_bg = QColor("rgb(255, 255, 255)") 
        self.t_color_edge = QColor("rgb(0, 0, 0)")
        self.color_bg_def()
        self.color_edge_def()
        self.color_fill_def()
        self.color_bg = self.t_color_bg
        self.color_edge = self.t_color_edge
        self.pen = QPen(self.color_edge)
        
        self.dots = []
        self.edges = []
        self.close_dot = None
        self.color_ind_fill.setStyleSheet("background-color:" + self.color_fill.name() + ";border: 1px solid black;")
        self.color_ind_bg.setStyleSheet("background-color:" + self.color_bg.name() + ";border: 1px solid black;")
        self.color_ind_edge.setStyleSheet("background-color:" + self.color_edge.name() + ";border: 1px solid black;")
        self.rcontent = self.graphicsView.contentsRect()
        self.scene = myScene(0, 0, self.rcontent.width(), self.rcontent.height())
        self.graphicsView.setScene(self.scene)
        self.checkBox.setChecked(True)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle("Ошибка ввода")
        self.listWidget.addItem("{:<6s} {:^6s}".format("X", "Y"))


        self.horiz = False
        self.vert = False
        self.cur_len = 0

        self.image = QImage()
        self.pix = QPixmap()

        self.buttons = [self.but_clear,self.but_close,self.but_color_bg,self.but_color_fill,self.but_color_edge,
                self.but_color_bg_def,self.but_color_fill_def,self.but_color_edge_def,self.but_add_dot,self.but_fill]

        self.bind()


    def clear(self):
        self.scene.clear()
        self.color_bg = self.t_color_bg
        self.color_edge = self.t_color_edge 
        self.color_ind_edge.setStyleSheet("background-color:" + self.color_edge.name() + ";border: 1px solid black;")
        self.listWidget.clear()
        self.listWidget.addItem("{:<6s} {:^6s}".format("X", "Y"))
        self.close_dot = None
        self.dots =[]
        self.edges=[]
        self.pen.setColor(self.color_edge)
        self.cur_len = 0

        brush = QBrush(self.color_bg)
        pen = QPen(self.color_bg)
        self.scene.addRect(0, 0, self.rcontent.width(), self.rcontent.height(), brush = brush, pen = pen)
        self.graphicsView.setScene(self.scene) 

    def button_lock(self):
        for i in self.buttons:
            i.setEnabled(False)
        self.vert = True
        self.horiz = True

    def button_unlock(self):
        for i in self.buttons:
            i.setEnabled(True)
        self.vert = False
        self.horiz = False

    def bind(self):
        self.but_clear.clicked.connect(self.clear)
        self.but_close.clicked.connect(self.close)

        self.but_color_bg.clicked.connect(self._color_bg)
        self.but_color_fill.clicked.connect(self._color_fill)
        self.but_color_edge.clicked.connect(self._color_edge)

        self.but_color_bg_def.clicked.connect(self.color_bg_def)
        self.but_color_fill_def.clicked.connect(self.color_fill_def)
        self.but_color_edge_def.clicked.connect(self.color_edge_def)

        self.but_add_dot.clicked.connect(self.init_dot_add)
        self.but_fill.clicked.connect(self.fill_by_edges)

    def init_dot_add(self):
        x,y = self.get_dot_vals()
        if x >= 0:
            add_point(x, y)

    
    def get_dot_vals(self):
        try:
            x= int(self.line_x.text().strip())
            if (x < 0):
                self.msg.setText("Ошибка ввода в поле координаты X. Необходимо ввести ровно одно целое неотрицательное число.")
                self.msg.show() 
                return -1, -1
        except:
            self.msg.setText("Ошибка ввода в поле координаты X. Необходимо ввести ровно одно целое неотрицательное число.")
            self.msg.show()
            return -1, -1

        try:
            y= int(self.line_y.text().strip())
            if (y < 0):
                self.msg.setText("Ошибка ввода в поле координаты Y. Необходимо ввести ровно одно целое неотрицательное число.")
                self.msg.show() 
                return -1, -1
        except:
            self.msg.setText("Ошибка ввода в поле координаты Y. Необходимо ввести ровно одно целое неотрицательное число.")
            self.msg.show()
            return -1, -1
        return x, y
        

    def close(self):
        if self.cur_len < 3:
            self.msg.setText("Замкнуть фигуру невозможно. Вы ввели менее трех точек для текущей фигуры")
            self.msg.show()
        else:
            self.scene.addLine(win.dots[-1][0], win.dots[-1][1], self.close_dot[0], self.close_dot[1], win.pen)
            self.edges.append([win.dots[-1][0], win.dots[-1][1], self.close_dot[0], self.close_dot[1]])
            self.close_dot = None
            self.cur_len = 0

    def color_bg_to_fill(self):
        self.color_fill = self.color_bg

    def _color_bg(self):
        self.t_color_bg = QColorDialog.getColor()
        self.color_ind_bg.setStyleSheet("background-color:" + self.t_color_bg.name() + ";border: 1px solid black;")

    def _color_edge(self):
        self.t_color_edge = QColorDialog.getColor()
        self.color_ind_edge.setStyleSheet("background-color:" + self.t_color_edge.name() + ";border: 1px solid black;")

    def _color_fill(self):
        self.color_fill = QColorDialog.getColor()
        self.color_ind_fill.setStyleSheet("background-color:" + self.color_fill.name() + ";border: 1px solid black;")
        
    def color_bg_def(self):
        self.t_color_bg.setRgb(255, 255, 255)
        self.color_ind_bg.setStyleSheet("background-color:" + self.t_color_bg.name() + ";border: 1px solid black;")

    def color_edge_def(self):
        self.t_color_edge.setRgb(0, 0, 0)
        self.color_ind_edge.setStyleSheet("background-color:" + self.t_color_edge.name() + ";border: 1px solid black;")

    def color_fill_def(self):
        self.color_fill.setRgb(255, 0, 0)
        self.color_ind_fill.setStyleSheet("background-color:" + self.color_fill.name() + ";border: 1px solid black;")

    def delay(self):
        QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 1)

        """t = QTime.currentTime().addUSecs(1)
        while QTime.currentTime() < t:
            QCoreApplication.processEvents(QEventLoop.AllEvents, 1)"""

    def fill_by_edges(self):
        if self.close_dot != None:
            self.msg.setText("Фигура не замкнута! Отмена закраски.")
            self.msg.show()
            return
        self.scene.clear()
        brush = QBrush(self.color_bg)
        pen = QPen(self.color_bg)
        self.scene.addRect(0, 0, self.rcontent.width(), self.rcontent.height(), brush = brush, pen = pen)
        self.graphicsView.setScene(self.scene) 

        global DEL_COUNT
        self.button_lock()
        scene = QGraphicsScene(0, 0, self.rcontent.width(), self.rcontent.height())
        brush = QBrush(self.color_bg)
        pen = QPen(self.color_bg)
        self.scene.addRect(0, 0, self.rcontent.width(), self.rcontent.height(), brush = brush, pen = pen)
        image = QImage(self.rcontent.width(), self.rcontent.height(), QImage.Format_ARGB32_Premultiplied)
        pix = QPixmap()
        p = QPainter()

        xm = self.find_max_x()
        delay_count = 0
        for edge in self.edges:
            p.begin(image)
            # если горизонтальное ребро - дальше
            if edge[1] == edge[3]:
                continue
            # иначе определяем границы сканирования
            if edge[1] > edge[3]:
                edge[1], edge[3] = edge[3], edge[1]

                edge[0], edge[2] = edge[2], edge[0]

            y = edge[1]
            end_y = edge[3]
            
            dx = (edge[2] - edge[0]) / (edge[3] - edge[1])
            start_x = edge[0]

            while y < end_y:
                # определяем пересечение
                x = start_x
                while x < xm:
                    col = QColor(image.pixel(int(x), int(y)))
                    if col == self.color_fill:
                        p.setPen(QPen(self.color_bg))
                    else:
                        p.setPen(QPen(self.color_fill))
                    
                    p.drawPoint(int(x), int(y))
                    x += 1

                start_x += dx
                y += 1

                self.draw_edges(image, p)
                if self.checkBox.isChecked() and delay_count == DEL_COUNT:
                    self.redraw_scene() 
                    pix.convertFromImage(image)
                    self.scene.addPixmap(pix)
                    self.delay()
                    delay_count = 0
                delay_count+=1

            if not self.checkBox.isChecked():
                pix.convertFromImage(image)
                self.scene.addPixmap(pix)
            p.end()
        p.begin(image)
        self.draw_edges(image, p)
        p.end()
        pix.convertFromImage(image)
        self.scene.addPixmap(pix)
        self.button_unlock()

    def redraw_scene(self):
        self.scene.clear()
        brush = QBrush(self.color_bg)
        pen = QPen(self.color_bg)
        self.scene.addRect(0, 0, self.rcontent.width(), self.rcontent.height(), brush = brush, pen = pen)
        self.graphicsView.setScene(self.scene)

    def draw_edges(self, image, p):
        p.setPen(QPen(self.color_edge))
        for ed in self.edges:
            p.drawLine(ed[0], ed[1], ed[2], ed[3])

    def find_max_x(self):
        xmax =  self.dots[0][0]
        for i in self.dots:
            if i[0] > xmax:
                xmax = i[0]
        return xmax

        

def add_point(x, y):
    global win
    if win.close_dot == None:
        win.close_dot = [round(x), round(y)]
    else:
        if win.horiz and win.vert:
            return
        elif win.horiz and not win.vert:
            x = win.dots[-1][0]
        elif not win.horiz and win.vert:
            y = win.dots[-1][1]
        win.edges.append([win.dots[-1][0], win.dots[-1][1], x, y])
        win.scene.addLine(win.dots[-1][0], win.dots[-1][1], x, y, win.pen)
    win.dots.append([round(x), round(y)])
    win.cur_len += 1
    win.listWidget.addItem("{:<6d} {:^6d}".format(x, y))

    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    # bar = QProgressBar()
    # bar.setProperty("value", 24)
    # bar.show()
    sys.exit(app.exec())