import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

SCREEN_SIZE = [500, 500]

class DrawStar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False

    def initUI(self):
        self.setGeometry(300, 300, *SCREEN_SIZE)
        self.setWindowTitle('window')
        self.button = QPushButton(self)
        self.button.setText('показать')
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_star(qp)
            qp.end()

    def draw_star(self, qp):
        d = randint(3, 200)
        heigh, width = randint(0, 300 - d), randint(0, 300 - d)

        qp.setPen(QPen(QColor(randint(0, 255),randint(0, 255),randint(0, 255)), 4))

        qp.drawEllipse(heigh, width, d, d)

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())
