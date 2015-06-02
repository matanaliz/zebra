#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from login_dialog import LoginDialog
from song_widget import SongWidget
from UI.ui_main_widget import Ui_MainWidget
from vk_api import VkApi
from vk_audio import VkAudio


class ZebraApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        api = VkApi()
        if api.isLogedIn():
            audio = VkAudio.parse(api.audio_get(api.current_user_id, api.audio_get_count(api.current_user_id)))

            for song in audio:
                btn = QPushButton()
                btn.setText(song.artist + song.title)
                btn.clicked.connect(lambda: self.ui.player_widget_content.prepare_playback())
                self.ui.songs_widget_content.add_widget_item(btn)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    login = LoginDialog()
    if not login.exec_():
        sys.exit(-1)

    ex = ZebraApplication()
    sys.exit(app.exec_())
