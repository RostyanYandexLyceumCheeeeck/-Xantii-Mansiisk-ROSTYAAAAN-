import sys
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QGridLayout, QMainWindow, QMessageBox, QMenu
from PyQt5.QtGui import QPainter, QColor
import random


class zheltie_okryznosti_Git(QMainWindow):
    bt: QPushButton

    def __init__(self):
        super().__init__()
        self.flag = False
        self.init_UI()

    def init_UI(self):
        uic.loadUi('untitled.ui', self)
        self.bt.clicked.connect(self.click)

    def click(self):
        self.flag = not self.flag

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            for _ in range(random.randint(0, 50)):
                x1 = random.randint(210, 800)
                y1 = random.randint(60, 800)
                peren = random.randint(0, 800 - max(x1, y1))
                x2 = x1 + peren
                y2 = y1 + peren
                self.draw_kryg(qp, x1, y1, x2, y2)
            qp.end()

    def draw_kryg(self, qp, x1, y1, x2, y2):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x1, y1, x2, y2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = zheltie_okryznosti_Git()
    ex.show()
    sys.exit(app.exec())
