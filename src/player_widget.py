#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QWidget)
from UI.ui_player_widget import Ui_PlayerWidget

import gi
gi.require_version('Gst', '1.0')
from gi.repository import (Gst, GObject)

from vk_api import VkApi
from vk_audio import VkAudio


class PlayerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_PlayerWidget()
        self.ui.setupUi(self)

        self.ui.play_button.setCheckable(True)
        self.ui.play_button.clicked[bool].connect(self.play_toggle)
        self.ui.volume_knob.setValue(100)
        self.ui.volume_knob.valueChanged.connect(self.volume_update)

        self.track = None
        self.player = None

        api = VkApi()
        if api.isLogedIn():
            json = api.audio_get(api.current_user_id, 1)
            track_list = VkAudio.parse(json)
            self.track = track_list[0]

        self.update_ui()
        self.init_gst()

    def init_gst(self):
        GObject.threads_init()
        Gst.init(None)

        self.player = Gst.ElementFactory.make("playbin", "player")
        if self.track:
            self.player.set_property('uri', self.track.url)
        else:
            self.player.set_property('uri', 'https://www.dropbox.com/s/ye1s33jaty6d9rr/fe9a35acd5e08f.mp3?dl=1')

    def play_toggle(self, pressed):
        if pressed:
            self.player.set_state(Gst.State.PLAYING)
        else:
            self.player.set_state(Gst.State.PAUSED)

    def prepare_playback(self, track):
        self.track = track
        self.player.set_state(Gst.State.NULL)
        self.update_ui()
        self.init_gst()

    def volume_update(self, vol):
        self.player.set_property('volume', vol / 100)

    def update_ui(self):
        if self.track:
            self.ui.track_name_lbl.setText(self.track.artist + " - " + self.track.title)
            self.ui.play_button.setChecked(False)

    def slider_drag(self, value):
        pass

    def __on_message(self, msg):
        # TODO
        # logging
        pass
