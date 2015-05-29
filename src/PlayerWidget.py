#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import ( QWidget, QSlider, QPushButton, QHBoxLayout)
from PyQt5.QtCore import Qt

import gi
gi.require_version('Gst', '1.0')
from gi.repository import (Gst, GObject)

from vk_api import VkApi
from vk_audio import VkAudio

class PlayerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.audio_stream_url = 'https://www.dropbox.com/s/ye1s33jaty6d9rr/fe9a35acd5e08f.mp3?dl=1'
        self.player = None

        api = VkApi()
        if (api.isLogedIn()):
            json = api.audio_get(api.current_user_id, 3)
            audios = VkAudio.parse(json)
            self.audio_stream_url = audios[0].url

        self.init_gst()
        self.init_ui()

    def init_ui(self):

        play_btn = QPushButton("Play")
        play_btn.setCheckable(True)
        play_btn.clicked[bool].connect(self.play_clicked)

        progress_slider = QSlider(Qt.Horizontal, self)
        progress_slider.sliderMoved[int].connect(self.slider_drag)

        hbox = QHBoxLayout()
        hbox.addWidget(play_btn)
        hbox.addWidget(progress_slider)
        self.setLayout(hbox)
        self.show()

    def init_gst(self):
        GObject.threads_init()
        Gst.init(None)

        self.player = Gst.ElementFactory.make("playbin", "player")
        self.player.set_property('uri', self.audio_stream_url)
        self.player.set_state(Gst.State.PAUSED)

    def play_clicked(self, pressed):
        if pressed:
            self.player.set_state(Gst.State.PLAYING)
        else:
            self.player.set_state(Gst.State.PAUSED)

    def slider_drag(self, value):
        pass

    def __on_message(self, msg):
        # TODO
        # logging
        pass
