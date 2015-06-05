#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QWidget)
from UI.ui_track_widget import Ui_TrackWidget


class TrackWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_TrackWidget()
        self.ui.setupUi(self)