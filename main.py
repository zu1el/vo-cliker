from PyQt5.QtWidgets import *
from localization import Local
import sys

current_lang = "en"

ua = Local("localization/ua.json")
en = Local("localization/en.json")


def getcurlenglocal(tag, lang=None):
    if lang:
        return ua.get(tag) if lang == "ua" else en.get(tag)
    return ua.get(tag) if current_lang == "ua" else en.get(tag)


App = QApplication(sys.argv)
App.setApplicationName("VO-coin")


login = QWidget()
login.setStyleSheet(open("Styles/login.qss").read())
login.setFixedSize(440, 700)

loginMainLine = QVBoxLayout()
label_line = QHBoxLayout()
login_line = QHBoxLayout()
password_line = QHBoxLayout()
sing_in_line = QHBoxLayout()
sing_up_line = QHBoxLayout()
localization_line = QHBoxLayout()

login_label = QLabel(getcurlenglocal("login"))
login_input = QLineEdit()
password_input = QLineEdit()
login_input.setPlaceholderText(getcurlenglocal("ent-login"))
password_input.setPlaceholderText(getcurlenglocal("ent-password"))
sing_in = QPushButton(getcurlenglocal("sing-in"))
sing_up = QPushButton(getcurlenglocal("sing-up"))
ualocalization = QCheckBox(getcurlenglocal("ua-localization"))

spliter = QSplitter()


def centerwidget(widget, line):
    line.addWidget(spliter)
    line.addWidget(widget)
    line.addWidget(spliter)


centerwidget(ualocalization, localization_line)
centerwidget(login_label, label_line)
centerwidget(login_input, login_line)
centerwidget(password_input, password_line)
centerwidget(sing_in, sing_in_line)
centerwidget(sing_up, sing_up_line)

loginMainLine.addLayout(localization_line)
for i in range(4):
    loginMainLine.addWidget(spliter)
loginMainLine.addLayout(label_line)
for i in range(5):
    loginMainLine.addWidget(spliter)
loginMainLine.addLayout(login_line)
loginMainLine.addLayout(password_line)
loginMainLine.addLayout(sing_in_line)
loginMainLine.addLayout(sing_up_line)
loginMainLine.addWidget(spliter)

login.setLayout(loginMainLine)


# game window


game = QWidget()
game.setStyleSheet(open("Styles/game.qss").read())
game.setFixedSize(440, 700)

game_line = QVBoxLayout()
menu_line = QHBoxLayout()

menu = QMenuBar(game)
gamemenu = menu.addMenu("")
shopmenu = menu.addMenu("")

statistic = QAction()
quit_game = QAction()
go_menu = QAction()
gamemenu.addAction(statistic)
gamemenu.addAction(quit_game)
gamemenu.addAction(go_menu)
reset = gamemenu.addMenu("")
accept_reset = reset.addAction("")
reject_reset = reset.addAction("")

boosts = QAction()
pumping = QAction()
promocode = shopmenu.addMenu("")
promo_history = promocode.addAction("")
promo_input = promocode.addAction("")
promo_create = promocode.addAction("")
shopmenu.addAction(boosts)
shopmenu.addAction(pumping)

game_line.addWidget(menu)
game.setLayout(game_line)


# func


def localization():
    global current_lang
    current_lang = "ua" if current_lang == "en" else "en"
    login_label.setText(getcurlenglocal("login"))
    login_input.setPlaceholderText(getcurlenglocal("ent-login"))
    password_input.setPlaceholderText(getcurlenglocal("ent-password"))
    sing_in.setText(getcurlenglocal("sing-in"))
    sing_up.setText(getcurlenglocal("sing-up"))
    ualocalization.setText(getcurlenglocal("ua-localization"))


def menu_func(q):
    pass


def singin(user_login, user_password):
    gamemenu.setTitle(getcurlenglocal("game"))
    shopmenu.setTitle(getcurlenglocal("shop"))
    statistic.setText(getcurlenglocal("statistic"))
    quit_game.setText(getcurlenglocal("quit"))
    reset.setTitle(getcurlenglocal("reset-data"))
    go_menu.setText(getcurlenglocal("go-menu"))
    reject_reset.setText(getcurlenglocal("reject"))
    accept_reset.setText(getcurlenglocal("accept"))
    promocode.setTitle(getcurlenglocal("promo-code"))
    promo_history.setText(getcurlenglocal("promo-history"))
    promo_input.setText(getcurlenglocal("promo-input"))
    promo_create.setText(getcurlenglocal("promo-create"))
    boosts.setText(getcurlenglocal("boosts"))
    pumping.setText(getcurlenglocal("pumping"))

    game.show()
    login.close()


def singup(user_login, user_password):
    pass


ualocalization.clicked.connect(localization)
sing_in.clicked.connect(lambda: singin(login_input.text(), password_input.text()))
gamemenu.triggered[QAction].connect(menu_func)

login.show()
App.exec()
