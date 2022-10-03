#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget, QApplication, QListWidget, QPushButton, QAbstractItemView, QVBoxLayout, \
    QHBoxLayout

"""
Напишите программу, состоящую из двух списков Listbox. В первом будет,
например, перечень товаров, заданный программно. Второй изначально пуст, пусть это
будет перечень покупок. При клике на одну кнопку товар должен переходить из одного
списка в другой. При клике на вторую кнопку – возвращаться (человек передумал покупать).
Предусмотрите возможность множественного выбора элементов списка и их перемещения
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task1")
        self.setGeometry(370, 300, 370, 300)
        self.lst1 = QListWidget()
        self.lst1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lst2 = QListWidget()
        self.lst2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lst1.addItems(products)
        self.btn1 = QPushButton("Добавить >>")
        self.btn2 = QPushButton("<< Удалить")
        self.btn1.clicked.connect(self.addItem)
        self.btn2.clicked.connect(self.removeItem)

    def align(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.lst1)
        hbox.addLayout(vbox)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        hbox.addWidget(self.lst2)
        self.setLayout(hbox)

    def addItem(self):
        listItems = self.lst1.selectedItems()
        for item in listItems:
            self.lst1.takeItem(self.lst1.row(item))
            self.lst2.addItem(item)

    def removeItem(self):
        listItems = self.lst2.selectedItems()
        for item in listItems:
            self.lst2.takeItem(self.lst2.row(item))
            self.lst1.addItem(item)


if __name__ == "__main__":
    products = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple']
    app = QApplication(sys.argv)
    window = MainWindow()
    window.align()
    window.show()
    sys.exit(app.exec_())