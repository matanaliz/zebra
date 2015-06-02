#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt5.QtWidgets import (QDialog, QLineEdit)
from UI.ui_login_dialog import Ui_LoginDialog

from user import User
from vk_api import VkApi


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.ui.pass_edit.setEchoMode(QLineEdit.Password)
        
        # Connect up the buttons.
        self.ui.buttonBox.accepted.connect(self.on_login)
        self.ui.buttonBox.rejected.connect(self.on_exit)

    def on_login(self):
        # verify login and password
        login = self.ui.login_edit.text()
        password = self.ui.pass_edit.text()

        if len(login) == 0 or len(password) == 0:
            return
        user = User(login, password)
        api = VkApi()
        api.login(user)

    def on_exit(self):
        self.close()
