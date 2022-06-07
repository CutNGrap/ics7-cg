import sys

from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QColorDialog, QMessageBox, QGraphicsScene, QWidget
from PyQt5.QtGui import QColor, QPen, QPixmap, QBrush, QImage, QPainter
from PyQt5.QtCore import QRect, QCoreApplication, QEventLoop


from mainwindow_ui import *

DEL_COUNT = 1


class myScene(QtWidgets.QGraphicsScene):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
        self.flag = 0


    def mousePressEvent(self, e):
        global win
        x, y = round(e.scenePos().x()), round(e.scenePos().y())
        if win.rad_edge.isChecked():
            self.flag = 1
            add_point(x, y)
        else:
            win.seed = [x,y]
            win.fill_seed()

    def mouseReleaseEvent(self, e):
        self.flag = 0

    def mouseMoveEvent(self, e):
        if self.flag == 1:
            self.mousePressEvent(e)

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
        self.rad_edge.setChecked(True)
    
        self.last_x = None
        self.last_y = None
        self.close_dot = None

        self.horiz = False
        self.vert = False
        self.cur_len = 0

        self.image = QImage(self.rcontent.width(), self.rcontent.height(), QImage.Format_ARGB32_Premultiplied)
        self.pix = QPixmap()

        self.buttons = [self.but_clear,self.but_close,self.but_color_bg,self.but_color_fill,self.but_color_edge,
                self.but_color_bg_def,self.but_color_fill_def,self.but_color_edge_def,self.but_add_dot, self.but_close_2]

        self.bind()
        self.clear()

    def clear_img(self):
        p = QPainter()
        p.begin(self.image)
        p.setPen(QPen(self.color_edge))
        brush = QBrush(self.color_bg)
        p.fillRect(0, 0, self.rcontent.width(), self.rcontent.height(), brush)
        p.end()

        pix = QPixmap()
        pix.convertFromImage(self.image)
        self.scene.addPixmap(pix)
        
    def draw_one_pix(self):
        self.draw_line(20, 100, 22, 100)
        self.draw_line(22, 100, 22, 800)
        self.draw_line(22, 800, 20, 800)
        self.draw_line(20, 800, 20, 100)
        self.seed = (21, 400)
        self.fill_seed()

    def clear(self):
        self.scene.clear()
        self.color_bg = self.t_color_bg
        self.color_edge = self.t_color_edge 
        self.clear_img()
        self.color_ind_edge.setStyleSheet("background-color:" + self.color_edge.name() + ";border: 1px solid black;")
        self.close_dot = None
        self.last_x = None
        self.dots =[]
        self.edges=[]
        self.pen.setColor(self.color_edge)
        self.cur_len = 0
        self.seed = None

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
        self.but_close_2.clicked.connect(self.draw_one_pix)

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
        if self.close_dot==None:
            self.msg.setText("Замкнуть фигуру невозможно. Вы еще не ввели ни одной точки!")
            self.msg.show()
            return
        self.draw_line(self.close_dot[0], self.close_dot[1], self.last_x, self.last_y)
        self.close_dot = None
        self.cur_len = 0

    def draw_line(self, a, b, c, d):
        p = QPainter()
        p.begin(win.image)
        p.setPen(QPen(win.color_edge))
        p.drawLine(a, b, c, d)
        p.end()

        pix = QPixmap()
        pix.convertFromImage(win.image)
        win.scene.addPixmap(pix)

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

        """t = QTime.currentTime().addMSecs(2)
        while QTime.currentTime() < t:
            QCoreApplication.processEvents(QEventLoop.AllEvents, 1)"""

    def set_color(self, x, y, color, p):
        p.setPen(QPen(color))
        p.drawPoint(x, y)

    def fill_seed(self):
        self.scene.clear()

        global DEL_COUNT
        self.button_lock()
        pix = QPixmap()
        p = QPainter()
        p.begin(self.image)

        stack = [self.seed]
        delay_count = 0

        while stack:
            # извлекаем очередной затравочный пиксел
            point = stack.pop()
            x, y = point[0], point[1]

            # заполняем интервал вправо от затравки
            # и запоминаем крайний правый пиксел
            x_cur = x
            while self.get_color(x_cur, y) != self.color_edge and x_cur < self.rcontent.width() - 1:
                self.set_color(x_cur, y, self.color_fill, p)
                x_cur += 1
            xr = x_cur - 1

            # заполняем интервал влево от затравки 
            # и запоминаем крайний левый пиксель
            x_cur = x - 1
            while self.get_color(x_cur, y) != self.color_edge and x_cur > 0:
                self.set_color(x_cur, y, self.color_fill, p)
                x_cur -= 1
            xl = x_cur + 1
            
            # Поиск новых затравочных пикселей в интервале xl <= x <= xr на двух соседних строках y+1, y-1
            for y_ in [y + 1, y - 1]:
                x = xl
                while x <= xr:
                    
                    flag = 0 
                    # ищем (хоть один или крайний правый) затравочный пиксель
                    while ((self.get_color(x, y_) != self.color_edge) and
                           (self.get_color(x, y_) != self.color_fill) and
                           (x <= xr)) and x < self.rcontent.width() - 1 and y_ > 0 and y_ < self.rcontent.height() - 1:                                                      ###
                        flag = 1
                        x += 1

                    if flag:
                        # дошли до конца интервала
                        if ((self.get_color(x, y_) != self.color_edge) and
                           (self.get_color(x, y_) != self.color_fill) and
                           (x == xr)) and x > 0 and y_ > 0 and y_ < self.rcontent.height():
                            stack.append([x, y_])
                        # встретили границу или уже заполненную часть на интервале
                        else:
                            stack.append([x - 1, y_])

                    xn = x
                    # Поиск нового интервала в случае прерывания текущего интервала
                    while (((self.get_color(x, y_) == self.color_edge) and\
                              (self.get_color(x, y_) == self.color_fill)) and\
                              (x < xr)) and x < self.rcontent.width() - 1:
                        x += 1
                    if x == xn:
                        x += 1

            # задержка
            if self.checkBox.isChecked() and delay_count == DEL_COUNT:
                self.scene.clear()
                pix.convertFromImage(self.image)
                self.scene.addPixmap(pix)
                self.delay()
                delay_count = 0
            delay_count+=1

        p.end()
        pix.convertFromImage(self.image)
        self.scene.addPixmap(pix)
        self.button_unlock()


    def draw_dot(self, x, y):
        p = QPainter()
        p.begin(self.image)
        p.setPen(QPen(self.color_edge))
        p.drawPoint(x, y)
        p.end()

        pix = QPixmap()
        pix.convertFromImage(self.image)
        self.scene.addPixmap(pix)

    def find_max_x(self):
        xmax =  self.dots[0][0]
        for i in self.dots:
            if i[0] > xmax:
                xmax = i[0]
        return xmax

    def get_color(self, x, y):
        return QColor(self.image.pixel(x, y))

def add_point(x, y):
    global win
    if win.last_x == None:
        win.last_x = x
        win.last_y = y
    if win.close_dot == None:
        win.close_dot = [round(x), round(y)]
        win.last_x = x
        win.last_y = y
    else:
        if win.horiz and win.vert:
            return
        elif win.horiz and not win.vert:
            x = win.last_x
        elif not win.horiz and win.vert:
            y = win.last_y
        win.draw_line(win.last_x, win.last_y, x, y)
        win.last_x = x
        win.last_y = y
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    # bar = QProgressBar()
    # bar.setProperty("value", 24)
    # bar.show()
    sys.exit(app.exec())