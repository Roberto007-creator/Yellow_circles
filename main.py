import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(700, 700)
        self.pixmap = QPixmap(700, 600)
        self.pixmap.fill(QColor(239, 239, 239, 180))

        self.label.setPixmap(self.pixmap)
        self.do_paint = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        qp = QPainter()
        qp.begin(self.label.pixmap())
        qp.setBrush(QColor(255, 255, 0))
        self.draw_circle(qp)
        self.label.update()

    @staticmethod
    def draw_circle(qp):
        diameter = random.randrange(10, 600)
        x = random.randrange(0, 600)
        y = random.randrange(0, 700)

        while x + diameter > 700 or y + diameter > 600:
            diameter = random.randrange(10, 600)
            x = random.randrange(0, 600)
            y = random.randrange(0, 700)

        qp.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Circles()
    window.show()
    sys.exit(app.exec())
