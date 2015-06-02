#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QWidget)
from UI.ui_song_widget import Ui_SongWidget


class SongWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_SongWidget()
        self.ui.setupUi(self)