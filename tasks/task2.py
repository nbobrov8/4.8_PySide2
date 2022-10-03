#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit,  QVBoxLayout, QListWidget

"""
Напишите программу по следующему описанию. Нажатие Enter в однострочном текстовом поле приводит к перемещению текста из
него в список. При двойном клике по элементу-строке списка, она должна копироваться в текстовое поле.
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task2")
        self.setGeometry(190, 210, 190, 210)
        self.lst_wt = QListWidget()
        self.lst_wt.itemDoubleClicked.connect(self.replace_item)
        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.replace_text)

    def align(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.lst_wt)
        self.setLayout(vbox)

    def replace_text(self):
        self.lst_wt.addItem(self.line_edit.text())
        self.line_edit.clear()

    def replace_item(self):
        listItems = self.lst_wt.selectedItems()
        if not listItems:
            return
        for item in listItems:
            self.line_edit.setText(item.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.align()
    window.show()
    sys.exit(app.exec_())