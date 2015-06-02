# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_widget.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1174, 781)
        self.player_widget_content = PlayerWidget(MainWidget)
        self.player_widget_content.setGeometry(QtCore.QRect(230, 20, 441, 101))
        self.player_widget_content.setObjectName("player_widget_content")
        self.current_user_widget_content = QtWidgets.QWidget(MainWidget)
        self.current_user_widget_content.setGeometry(QtCore.QRect(9, 19, 211, 101))
        self.current_user_widget_content.setObjectName("current_user_widget_content")
        self.songs_widget_content = ScrollAreaWidget(MainWidget)
        self.songs_widget_content.setGeometry(QtCore.QRect(230, 130, 440, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songs_widget_content.sizePolicy().hasHeightForWidth())
        self.songs_widget_content.setSizePolicy(sizePolicy)
        self.songs_widget_content.setMinimumSize(QtCore.QSize(440, 0))
        self.songs_widget_content.setMaximumSize(QtCore.QSize(440, 16777215))
        self.songs_widget_content.setObjectName("songs_widget_content")
        self.widget = QtWidgets.QWidget(MainWidget)
        self.widget.setGeometry(QtCore.QRect(9, 129, 211, 641))
        self.widget.setObjectName("widget")

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Zebra"))

from scroll_area_widget import ScrollAreaWidget
from player_widget import PlayerWidget
