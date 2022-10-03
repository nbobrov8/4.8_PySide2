#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit

"""
Напишите программу по описанию. Размеры многострочного текстового поля определяются значениями,
введенными в однострочные текстовые поля. Изменение размера происходит при нажатии мышью на кнопку,
а также при нажатии клавиши Enter. Цвет фона экземпляра Text светлосерый (lightgrey),
когда поле не в фокусе, и белый, когда имеет фокус. Для справки: фокус перемещается по виджетам при нажатии Tab,
Ctrl+Tab, Shift+Tab, а также при клике по ним мышью (к кнопкам последнее не относится).
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        QApplication.instance().focusChanged.connect(self.on_focusChanged)
        self.setWindowTitle("Task3")
        self.setGeometry(250, 300, 250, 300)
        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit2.returnPressed.connect(self.EditSize)
        self.textbox = QTextEdit()
        self.btn1 = QPushButton("Edit")
        self.btn1.clicked.connect(self.EditSize)

    def align(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.line_edit1)
        hbox.addWidget(self.line_edit2)
        hbox.addWidget(self.btn1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.textbox)
        self.setLayout(vbox)

    def EditSize(self):
        self.textbox.resize(int(self.line_edit1.text()), int(self.line_edit2.text()))

    def on_focusChanged(self, old, new):
        if self.textbox == new:
            self.textbox.setStyleSheet(f"background-color: #fff;")
        elif self.textbox == old:
            self.textbox.setStyleSheet(f"background-color: #d3d3d3;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.align()
    window.show()
    sys.exit(app.exec_())
