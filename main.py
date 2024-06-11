from PyQt5.QtWidgets import *
import sys
from localization import local

current_lang = "en"
ua = local("localization/ua.json")
en = local("localization/en_login.json")

App = QApplication(sys.argv)

login = QWidget()
login.setStyleSheet("""background-image: url("data/background.jpg"); background-repeat: no-repeat; background-position: center; color: #FFFFFF; border: 0px; font-size: 35px;""")
login.setFixedSize(440, 700)

loginMainLine = QVBoxLayout()
label_line = QHBoxLayout()
login_line = QHBoxLayout()
password_line = QHBoxLayout()
sing_in_line = QHBoxLayout()
sing_up_line = QHBoxLayout()
chek_line = QHBoxLayout()

login_label = QLabel(en.get("login"))
login_label.setStyleSheet("""font-size: 45px; background:rgba(0, 0, 0, 0);""")

login_input = QLineEdit()
password_input = QLineEdit()
for widget in [login_input, password_input]: widget.setStyleSheet("""color: #FFFFFF; border-radius: 10px; border-style: outset; background: #222222; width: 340; height: 45; font-size: 25px; padding: 10px;""")
login_input.setPlaceholderText(en.get("ent-login"))
password_input.setPlaceholderText(en.get("ent-password"))
sing_in = QPushButton(en.get("sing-in"))
sing_up = QPushButton(en.get("sing-up"))
for widget in [sing_in, sing_up]: widget.setStyleSheet("""QPushButton {color: #FFFFFF; border-radius: 10px; border-style: outset; background: #222222; width: 340; height: 45; font-size: 25; padding: 5px;} QPushButton:hover {background: #191919} QPushButton:pressed {border-style: inset; background: #151515}""")
ua_localization = QCheckBox(en.get("ua-localization"))
ua_localization.setStyleSheet("""font-size: 16px; background:rgba(0, 0, 0, 0);""")

spliter = QSplitter()
spliter.setStyleSheet("""background:rgba(0, 0, 0, 0);""")

chek_line.addWidget(spliter)
chek_line.addWidget(ua_localization)
chek_line.addWidget(spliter)

label_line.addWidget(spliter)
label_line.addWidget(login_label)
label_line.addWidget(spliter)

login_line.addWidget(spliter)
login_line.addWidget(login_input)
login_line.addWidget(spliter)

password_line.addWidget(spliter)
password_line.addWidget(password_input)
password_line.addWidget(spliter)

sing_in_line.addWidget(spliter)
sing_in_line.addWidget(sing_in)
sing_in_line.addWidget(spliter)

sing_up_line.addWidget(spliter)
sing_up_line.addWidget(sing_up)
sing_up_line.addWidget(spliter)

loginMainLine.addLayout(chek_line)
loginMainLine.addWidget(spliter)
loginMainLine.addWidget(spliter)
loginMainLine.addWidget(spliter)
loginMainLine.addLayout(label_line)
loginMainLine.addWidget(spliter)
loginMainLine.addWidget(spliter)
loginMainLine.addWidget(spliter)
loginMainLine.addWidget(spliter)
loginMainLine.addWidget(spliter)
loginMainLine.addLayout(login_line)
loginMainLine.addLayout(password_line)
loginMainLine.addLayout(sing_in_line)
loginMainLine.addLayout(sing_up_line)
loginMainLine.addWidget(spliter)

login.setLayout(loginMainLine)


#------------------------------------


game = QWidget()
game.setFixedSize(440, 700)


def localization():
    global current_lang
    if current_lang == "en":
        current_lang = "ua"
        login_label.setText(ua.get("login"))
        login_input.setPlaceholderText(ua.get("ent-login"))
        password_input.setPlaceholderText(ua.get("ent-password"))
        sing_in.setText(ua.get("sing-in"))
        sing_up.setText(ua.get("sing-up"))
        ua_localization.setText(ua.get("ua-localization"))
    else:
        current_lang = "en"
        login_label.setText(en.get("login"))
        login_input.setPlaceholderText(en.get("ent-login"))
        password_input.setPlaceholderText(en.get("ent-password"))
        sing_in.setText(en.get("sing-in"))
        sing_up.setText(en.get("sing-up"))
        ua_localization.setText(en.get("ua-localization"))

def logining(login_, password):
    login.close()
    game.show()

ua_localization.clicked.connect(localization)

sing_in.clicked.connect(lambda: logining("zufel", "password"))

login.show()
App.exec()
