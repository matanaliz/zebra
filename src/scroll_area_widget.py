#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QWidget, QScrollArea, QVBoxLayout)


class ScrollAreaWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

         #Container Widget
        widget = QWidget()
        #Layout of Container Widget
        self.layout = QVBoxLayout(self)
        widget.setLayout(self.layout)

        #Scroll Area Properties
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(False)
        self.scroll.setWidget(widget)

        #Scroll Area Layer add
        scroll_layout = QVBoxLayout(self)
        scroll_layout.addWidget(self.scroll)
        self.setLayout(scroll_layout)

    def add_widget_item(self, widget_item):
        self.layout.addWidget(widget_item)
        widget_item.show()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.scroll.setWidget(widget)
