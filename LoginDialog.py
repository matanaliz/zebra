from PyQt5.QtWidgets import (QDialog)
from UI.ui_logindialog import Ui_LoginDialog


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)

        # Connect up the buttons.
        self.ui.buttonBox.accepted.connect(self.on_login)
        self.ui.buttonBox.rejected.connect(self.on_exit)

    def on_login(self):
        # verify login and password
        pass

    def on_exit(self):
        self.close()