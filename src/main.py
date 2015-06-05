#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from login_dialog import LoginDialog
from track_widget import TrackWidget
from UI.ui_main_widget import Ui_MainWidget
from vk_api import VkApi
from vk_audio import VkAudio

from functools import partial

class ZebraApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        api = VkApi()
        if api.isLogedIn():
            self.track_list = VkAudio.parse(api.audio_get(api.current_user_id, api.audio_get_count(api.current_user_id)))

            for track in self.track_list:
                btn = QPushButton()
                btn.setText(track.artist + track.title)
                btn.clicked.connect(partial(self.on_track_click, track.url))
                self.ui.track_list.add_widget_item(btn)

        self.show()

    def on_track_click(self, item_id):
        if self.track_list:
            for track in self.track_list:
                if track.url == item_id:
                    self.ui.player_widget.prepare_playback(track)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    login = LoginDialog()
    if not login.exec_():
        sys.exit(-1)

    ex = ZebraApplication()
    sys.exit(app.exec_())
