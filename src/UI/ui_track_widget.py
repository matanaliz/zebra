# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'track_widget.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TrackWidget(object):
    def setupUi(self, TrackWidget):
        TrackWidget.setObjectName("TrackWidget")
        TrackWidget.resize(440, 20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TrackWidget.sizePolicy().hasHeightForWidth())
        TrackWidget.setSizePolicy(sizePolicy)
        TrackWidget.setMinimumSize(QtCore.QSize(0, 20))
        TrackWidget.setMaximumSize(QtCore.QSize(440, 20))
        TrackWidget.setMouseTracking(True)
        TrackWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.widget = QtWidgets.QWidget(TrackWidget)
        self.widget.setGeometry(QtCore.QRect(0, -4, 441, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_btn = QtWidgets.QPushButton(self.widget)
        self.play_btn.setObjectName("play_btn")
        self.horizontalLayout.addWidget(self.play_btn)
        self.track_name = QtWidgets.QLabel(self.widget)
        self.track_name.setObjectName("track_name")
        self.horizontalLayout.addWidget(self.track_name)
        self.track_length = QtWidgets.QLabel(self.widget)
        self.track_length.setMinimumSize(QtCore.QSize(0, 0))
        self.track_length.setMaximumSize(QtCore.QSize(16777215, 20))
        self.track_length.setObjectName("track_length")
        self.horizontalLayout.addWidget(self.track_length)

        self.retranslateUi(TrackWidget)
        QtCore.QMetaObject.connectSlotsByName(TrackWidget)

    def retranslateUi(self, TrackWidget):
        _translate = QtCore.QCoreApplication.translate
        TrackWidget.setWindowTitle(_translate("TrackWidget", "Form"))
        self.play_btn.setText(_translate("TrackWidget", "PushButton"))
        self.track_name.setText(_translate("TrackWidget", "no name"))
        self.track_length.setText(_translate("TrackWidget", "00:00/00:00"))

