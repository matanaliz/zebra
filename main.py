#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout)
from PlayerWidget import PlayerWidget
from LoginDialog import LoginDialog


class ZebraApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        pl = PlayerWidget()
        vbox = QVBoxLayout()
        vbox.addWidget(pl)
        self.setGeometry(300, 300, 800, 600)
        self.setLayout(vbox)
        self.setWindowTitle('Zebra Player')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    login = LoginDialog()
    if not login.exec_():
        sys.exit(-1)

    ex = ZebraApplication()
    sys.exit(app.exec_())