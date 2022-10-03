#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPainter, QBrush, QPen, QPolygon
from PySide2.QtWidgets import QApplication, QWidget

# Создать изображение на холсте


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task4")
        self.setGeometry(500, 500, 500, 500)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.darkRed, 2, Qt.SolidLine))
        painter.setBrush(Qt.gray)
        painter.drawRect(129, 143, 253, 281)
        painter.setPen(QPen(Qt.darkRed, 3, Qt.SolidLine))
        painter.setBrush((QBrush(Qt.white)))
        painter.drawRect(217, 204, 70, 70)
        painter.drawLine(218, 239, 286, 240)
        painter.drawLine(250, 205, 251, 274)
        painter.setBrush((QBrush(Qt.darkMagenta)))
        points = QPolygon([
            QPoint(129, 142),
            QPoint(255, 43),
            QPoint(380, 142)
        ])
        painter.drawPolygon(points)
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
        painter.drawEllipse(415, 6, 80, 80)
        painter.drawLine(380, 25, 420, 25)
        painter.drawLine(396, 92, 419, 68)
        painter.drawLine(455, 127, 455, 88)
        self.drawGrass(painter)
        self.drawCat(painter)

    def drawGrass(self, painter):
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.darkGreen, 2, Qt.SolidLine))
        painter.setBrush(Qt.darkGreen)
        for i in range(30):
            painter.drawArc(random.randint(1, 8), 300, i * 30, 360, 0 * 100, random.randint(35, 65) * 10)

    def drawCat(self, painter):
        painter.begin(self)
        points1 = QPolygon([
            QPoint(69, 294),
            QPoint(48, 336),
            QPoint(92, 337)
        ])
        points2 = QPolygon([
            QPoint(81, 253),
            QPoint(76, 266),
            QPoint(83, 271)
        ])
        points3 = QPolygon([
            QPoint(64, 253),
            QPoint(57, 271),
            QPoint(65, 266)
        ])
        painter.setPen(QPen(Qt.yellow))
        painter.setBrush(QBrush(Qt.darkYellow))
        painter.drawPolygon(points1)
        painter.drawPolygon(points2)
        painter.drawPolygon(points3)
        painter.setPen(QPen(Qt.black))
        painter.drawLine(81, 283, 100, 287)
        painter.drawLine(80, 288, 96, 296)
        painter.drawLine(58, 284, 40, 289)
        painter.drawLine(58, 289, 41, 295)
        painter.setPen(QPen(Qt.red))
        painter.setBrush(QBrush(Qt.darkRed))
        painter.drawEllipse(55, 267, 30, 30)
        painter.drawEllipse(81, 305, 13, 13)
        painter.drawEllipse(46, 305, 13, 13)
        painter.setPen(QPen(Qt.white))
        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(62, 274, 7, 7)
        painter.drawEllipse(72, 274, 7, 7)
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(64, 277, 2, 2)
        painter.drawEllipse(75, 277, 2, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
