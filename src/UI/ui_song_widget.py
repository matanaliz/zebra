# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'song_widget.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SongWidget(object):
    def setupUi(self, SongWidget):
        SongWidget.setObjectName("SongWidget")
        SongWidget.resize(440, 20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SongWidget.sizePolicy().hasHeightForWidth())
        SongWidget.setSizePolicy(sizePolicy)
        SongWidget.setMinimumSize(QtCore.QSize(0, 20))
        SongWidget.setMaximumSize(QtCore.QSize(440, 20))
        SongWidget.setMouseTracking(True)
        SongWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.widget = QtWidgets.QWidget(SongWidget)
        self.widget.setGeometry(QtCore.QRect(0, -4, 441, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.song_name = QtWidgets.QLabel(self.widget)
        self.song_name.setObjectName("song_name")
        self.horizontalLayout.addWidget(self.song_name)
        self.song_length = QtWidgets.QLabel(self.widget)
        self.song_length.setMinimumSize(QtCore.QSize(0, 0))
        self.song_length.setMaximumSize(QtCore.QSize(16777215, 20))
        self.song_length.setObjectName("song_length")
        self.horizontalLayout.addWidget(self.song_length)

        self.retranslateUi(SongWidget)
        QtCore.QMetaObject.connectSlotsByName(SongWidget)

    def retranslateUi(self, SongWidget):
        _translate = QtCore.QCoreApplication.translate
        SongWidget.setWindowTitle(_translate("SongWidget", "Form"))
        self.pushButton.setText(_translate("SongWidget", "PushButton"))
        self.song_name.setText(_translate("SongWidget", "no name"))
        self.song_length.setText(_translate("SongWidget", "00:00/00:00"))

