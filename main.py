from PyQt5.QtWidgets import *
from localization import local
import sys

current_lang = "en"

ua = local("localization/ua.json")
en = local("localization/en_login.json")


def getcurlenglocal(tag, lang=None):
    if lang: return ua.get(tag) if lang == "ua" else en.get(tag)
    return ua.get(tag) if current_lang == "ua" else en.get(tag)


App = QApplication(sys.argv)

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
for i in range(4): loginMainLine.addWidget(spliter)
loginMainLine.addLayout(label_line)
for i in range(5): loginMainLine.addWidget(spliter)
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

menu = QMenuBar()
gamemenu = menu.addMenu(getcurlenglocal("game"))
shopmenu = menu.addMenu(getcurlenglocal("shop"))

statistic = QAction(getcurlenglocal("statistic"))
gamemenu.addAction(statistic)

reset = gamemenu.addMenu(getcurlenglocal("reset-data"))
reset.addAction(getcurlenglocal("accept"))
reset.addAction(getcurlenglocal("reject"))

quit_game = QAction("Quit")
gamemenu.addAction(quit_game)

game_line.addWidget(menu)

game.setLayout(game_line)

# func


def localization():
    global current_lang
    if current_lang == "en":
        current_lang = "ua"
        login_label.setText(getcurlenglocal("login", "ua"))
        login_input.setPlaceholderText(getcurlenglocal("ent-login", "ua"))
        password_input.setPlaceholderText(getcurlenglocal("ent-password", "ua"))
        sing_in.setText(getcurlenglocal("sing-in", "ua"))
        sing_up.setText(getcurlenglocal("sing-up", "ua"))
        ualocalization.setText(getcurlenglocal("ua-localization", "ua"))
    else:
        current_lang = "en"
        login_label.setText(getcurlenglocal("login"))
        login_input.setPlaceholderText(getcurlenglocal("ent-login"))
        password_input.setPlaceholderText(getcurlenglocal("ent-password"))
        sing_in.setText(getcurlenglocal("sing-in"))
        sing_up.setText(getcurlenglocal("sing-up"))
        ualocalization.setText(getcurlenglocal("ua-localization"))


def menu_func(q):
    statistic = getcurlenglocal("statistic")
    match q.text():
        case str(statistic):
            print(q.text())
        case _:
            print(q.text())


def singin(l, p):
    statistic.setText(getcurlenglocal("statistic"))
    quit_game.setText(getcurlenglocal("quit"))
    #reset.setText(getcurlenglocal("reset-data"))
    game.show()
    login.close()


def singup(l, p):
    pass


ualocalization.clicked.connect(localization)

sing_in.clicked.connect(lambda: singin("zufel", "password"))
gamemenu.triggered[QAction].connect(menu_func)


login.show()
App.exec()
