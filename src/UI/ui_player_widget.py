# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player_widget.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(441, 104)
        Form.setStyleSheet("\"")
        self.playback_slider = QtWidgets.QSlider(Form)
        self.playback_slider.setGeometry(QtCore.QRect(90, 51, 261, 20))
        self.playback_slider.setOrientation(QtCore.Qt.Horizontal)
        self.playback_slider.setObjectName("playback_slider")
        self.song_name_lbl = QtWidgets.QLabel(Form)
        self.song_name_lbl.setGeometry(QtCore.QRect(90, 10, 261, 21))
        self.song_name_lbl.setObjectName("song_name_lbl")
        self.play_button = QtWidgets.QPushButton(Form)
        self.play_button.setGeometry(QtCore.QRect(20, 50, 61, 23))
        self.play_button.setObjectName("play_button")
        self.volume_knob = QtWidgets.QDial(Form)
        self.volume_knob.setGeometry(QtCore.QRect(360, 40, 41, 41))
        self.volume_knob.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        self.volume_knob.setObjectName("volume_knob")
        self.song_time_lbl = QtWidgets.QLabel(Form)
        self.song_time_lbl.setGeometry(QtCore.QRect(350, 10, 71, 21))
        self.song_time_lbl.setObjectName("song_time_lbl")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.song_name_lbl.setText(_translate("Form", "song_name_here"))
        self.play_button.setText(_translate("Form", "Play"))
        self.song_time_lbl.setText(_translate("Form", "00:00/00:00"))

