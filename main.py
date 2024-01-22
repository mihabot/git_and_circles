import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Рисование окружностей')

        self.button = QPushButton('Нарисовать окружности', self)
        self.button.resize(200, 40)
        self.button.move(250, 350)
        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        for _ in range(5):
            radius = random.randint(10, 100)
            x = random.randint(0, self.width() - radius)
            y = random.randint(0, self.height() - radius)
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.setBrush(color)
            painter.drawEllipse(x, y, radius, radius)

app = QApplication(sys.argv)
window = MyWindow()
app.exec_()