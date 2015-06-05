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
        self.player_widget = PlayerWidget(MainWidget)
        self.player_widget.setGeometry(QtCore.QRect(230, 20, 441, 101))
        self.player_widget.setObjectName("player_widget")
        self.current_user_widget = QtWidgets.QWidget(MainWidget)
        self.current_user_widget.setGeometry(QtCore.QRect(9, 19, 211, 101))
        self.current_user_widget.setObjectName("current_user_widget")
        self.track_list = ScrollAreaWidget(MainWidget)
        self.track_list.setGeometry(QtCore.QRect(230, 130, 440, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.track_list.sizePolicy().hasHeightForWidth())
        self.track_list.setSizePolicy(sizePolicy)
        self.track_list.setMinimumSize(QtCore.QSize(440, 0))
        self.track_list.setMaximumSize(QtCore.QSize(440, 16777215))
        self.track_list.setObjectName("track_list")
        self.users_list = ScrollAreaWidget(MainWidget)
        self.users_list.setGeometry(QtCore.QRect(9, 129, 211, 641))
        self.users_list.setObjectName("users_list")

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Zebra"))

from player_widget import PlayerWidget
from scroll_area_widget import ScrollAreaWidget
