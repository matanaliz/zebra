# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_widget.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        main_widget.setObjectName("main_widget")
        main_widget.resize(962, 781)
        self.player_widget_content = QtWidgets.QWidget(main_widget)
        self.player_widget_content.setGeometry(QtCore.QRect(230, 20, 441, 104))
        self.player_widget_content.setObjectName("player_widget_content")
        self.verticalLayoutWidget = QtWidgets.QWidget(main_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 130, 441, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.music_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.music_layout.setContentsMargins(0, 0, 0, 0)
        self.music_layout.setObjectName("music_layout")
        self.music_scroll_area = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.music_scroll_area.setWidgetResizable(True)
        self.music_scroll_area.setObjectName("music_scroll_area")
        self.music_scroll_area_widget_contents = QtWidgets.QWidget()
        self.music_scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 435, 625))
        self.music_scroll_area_widget_contents.setObjectName("music_scroll_area_widget_contents")
        self.music_scroll_area.setWidget(self.music_scroll_area_widget_contents)
        self.music_layout.addWidget(self.music_scroll_area)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(main_widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 211, 631))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.friends_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.friends_layout.setContentsMargins(0, 0, 0, 0)
        self.friends_layout.setObjectName("friends_layout")
        self.friends_scroll_area = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.friends_scroll_area.setWidgetResizable(True)
        self.friends_scroll_area.setObjectName("friends_scroll_area")
        self.friends_scroll_area_widget_contents = QtWidgets.QWidget()
        self.friends_scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 205, 625))
        self.friends_scroll_area_widget_contents.setObjectName("friends_scroll_area_widget_contents")
        self.friends_scroll_area.setWidget(self.friends_scroll_area_widget_contents)
        self.friends_layout.addWidget(self.friends_scroll_area)
        self.current_user_widget_content = QtWidgets.QWidget(main_widget)
        self.current_user_widget_content.setGeometry(QtCore.QRect(9, 19, 211, 101))
        self.current_user_widget_content.setObjectName("current_user_widget_content")

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        _translate = QtCore.QCoreApplication.translate
        main_widget.setWindowTitle(_translate("main_widget", "Zebra"))

