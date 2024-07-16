import datetime
from PyQt5.QtWidgets import *
from localization import Local, current_lang
from loger import logger, logger_read
import sys
import json
from data import user_data_dump, user_data_load, data_dump, data_load

ua, en = Local("localization/ua.json"), Local("localization/en.json")
status = [False, "debug-line"]


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
info_line = QHBoxLayout()
label_line = QHBoxLayout()
login_line = QHBoxLayout()
password_line = QHBoxLayout()
sing_in_line = QHBoxLayout()
sing_up_line = QHBoxLayout()
localization_line = QHBoxLayout()

info = QLineEdit()
info.setPlaceholderText(getcurlenglocal("debug-line"))
info.setReadOnly(True)
login_label = QLabel(getcurlenglocal("login"))
login_input = QLineEdit()
password_input = QLineEdit()
login_input.setPlaceholderText(getcurlenglocal("ent-login"))
password_input.setPlaceholderText(getcurlenglocal("ent-password"))
sing_in = QPushButton(getcurlenglocal("sing-in"))
sing_up = QPushButton(getcurlenglocal("sing-up"))
ualocalization = QCheckBox(getcurlenglocal("ua-localization"))


def centerwidget(widget, line):
    line.addWidget(QSplitter())
    line.addWidget(widget)
    line.addWidget(QSplitter())


centerwidget(ualocalization, localization_line)
centerwidget(info, info_line)
centerwidget(login_label, label_line)
centerwidget(login_input, login_line)
centerwidget(password_input, password_line)
centerwidget(sing_in, sing_in_line)
centerwidget(sing_up, sing_up_line)

loginMainLine.addLayout(localization_line)
for i in range(4): loginMainLine.addWidget(QSplitter())
loginMainLine.addLayout(label_line)
for i in range(5): loginMainLine.addWidget(QSplitter())
loginMainLine.addLayout(info_line)
loginMainLine.addLayout(login_line)
loginMainLine.addLayout(password_line)
loginMainLine.addLayout(sing_in_line)
loginMainLine.addLayout(sing_up_line)
loginMainLine.addWidget(QSplitter())


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

balance = QLabel()
main_btn = QPushButton()
energy_balance = QLabel()
energy_limit = QLabel()
energy_progres = QProgressBar()

game_line.addWidget(menu)
balance_line = QHBoxLayout()
centerwidget(balance, balance_line)
game_line.addWidget(QSplitter())
game_line.addLayout(balance_line)
game_line.addWidget(QSplitter())
game_line.addWidget(main_btn)
energy_line = QHBoxLayout()
energy_data = QVBoxLayout()
energy_data.addWidget(energy_balance)
energy_data.addWidget(energy_limit)
energy_line.addLayout(energy_data)
energy_line.addWidget(energy_progres)
game_line.addLayout(energy_line)
game.setLayout(game_line)

# game-my statistic
game_statistic = QWidget()
game_statistic.setStyleSheet(open("Styles/game_statistic.qss").read())
game_statistic.setFixedSize(440, 700)

# shop-promo-history
shop_promo_history = QWidget()
shop_promo_history.setStyleSheet(open("Styles/promo/game_history.qss").read())
shop_promo_history.setFixedSize(440, 700)

# shop-promo-enter
shop_promo_enter = QWidget()
shop_promo_enter.setStyleSheet(open("Styles/promo/game_enter.qss").read())
shop_promo_enter.setFixedSize(440, 700)

# shop-promo-create
shop_promo_create = QWidget()
shop_promo_create.setStyleSheet(open("Styles/promo/game_create.qss").read())
shop_promo_create.setFixedSize(440, 700)

# shop-boosts
shop_boosts = QWidget()
shop_boosts.setStyleSheet(open("Styles/game_boosts.qss").read())
shop_boosts.setFixedSize(440, 700)

# shop-pumping
shop_pumping = QWidget()
shop_pumping.setStyleSheet(open("Styles/game_pumping.qss").read())
shop_pumping.setFixedSize(440, 700)

# func


def localization():
    global current_lang
    current_lang = "ua" if current_lang == "en" else "en"
    logger.info("localization lang set to {}".format(current_lang))
    info.setPlaceholderText(getcurlenglocal("debug-line"))
    login_label.setText(getcurlenglocal("login"))
    login_input.setPlaceholderText(getcurlenglocal("ent-login"))
    password_input.setPlaceholderText(getcurlenglocal("ent-password"))
    sing_in.setText(getcurlenglocal("sing-in"))
    sing_up.setText(getcurlenglocal("sing-up"))
    ualocalization.setText(getcurlenglocal("ua-localization"))
    info.setText(getcurlenglocal(status[1], current_lang)) if info.text() != "" else info.setPlaceholderText(getcurlenglocal(status[1], current_lang))


def menu_func(q):
    match q.text():
        case "My statistic":
            go_statistic()
        case "Quit game":
            quit_game_func()
        case "Go menu":
            go_login()
        case "Accept":
            del_account_accept()
        case "Reject":
            del_account_reject()
        case "History":
            promo_history_func()
        case "Enter":
            promo_enter_func()
        case "Create":
            promo_create_func()
        case "Boosts":
            boosts_open()
        case "Pumping":
            pumping_opne()
        case "Моя статистика":
            go_statistic()
        case "Вийти з гри":
            quit_game_func()
        case "Вийти в меню входу":
            go_login()
        case "Прийняти":
            del_account_accept()
        case "Відмінити":
            del_account_reject()
        case "Історія":
            promo_history_func()
        case "Ввести":
            promo_enter_func()
        case "Створити":
            promo_create_func()
        case "Бусти":
            boosts_open()
        case "Прокачка":
            pumping_opne()
        case _:
            print("crt error")


def singin(status):
    user = user_data_load("data/game.json", status[1])
    if status[0]:
        print(user["login"], user["password"])
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
        balance.setText(str(user["cur balance"]))
        energy_balance.setText(str(user["energy"]))
        energy_limit.setText(f"""/{user["energy limit"]}""")
        progres = 100/(user["energy limit"]/user["energy"])
        energy_progres.setValue(int(progres))

        game.show()
        login.close()
    else:
        info.setText(getcurlenglocal(status[1], current_lang))


def singup(status):
    status_code, status_text = status[0], status[1]
    if status_code:
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
    else:
        info.setText(getcurlenglocal(status_text, current_lang))


def cehksingin(user_login, user_password):
    global status
    logger.info("try to sing in as {}:{}".format(user_login, user_password))
    status = [False, getcurlenglocal("None error", "en")]
    log = ["None", "crt"]
    with open("data/game.json") as file:
        data = json.loads(file.read())
        logger.info("data dump sucefulled")
    if user_login == "":
        log = ["No input login", "err"]
        status = [False, getcurlenglocal("please input login", "en")]
        logger_read(log)
        singin(status)
        return
    else:
        if user_password == "":
            log = ["No input password", "err"]
            status = [False, getcurlenglocal("please input password", "en")]
            logger_read(log)
            singin(status)
            return
        else:
            for user in data["users"]:
                if user_login == user["login"]:
                    if user_password == user["password"]:
                        logger.info(f"sing in sucefulled as {user_login}")
                        status = [True, user["_id"]]
                        singin(status)
                        return
                    else:
                        log = ["invalid password", "err"]
                        status = [False, getcurlenglocal("wrong password", "en")]
                        logger_read(log)
                        singin(status)
                        return
                else:
                    log = ["invalid login", "err"]
                    status = [False, getcurlenglocal("unknown login", "en")]
            logger_read(log)
            singin(status)
            return


def cheksingup(user_login, user_password):
    global status
    logger.info("try to sing up as {}:{}".format(user_login, user_password))
    status = [False, getcurlenglocal("None error", "en")]
    with open("data/game.json", "r") as file:
        data = json.load(file)
        logger.info("data dump sucefulled")
    if user_login == "":
        log = ["No input login", "err"]
        status = [False, getcurlenglocal("please input login", "en")]
        logger_read(log)
        singup(status)
        return
    else:
        if user_password == "":
            log = ["No input password", "err"]
            status = [False, getcurlenglocal("please input password", "en")]
            logger_read(log)
            singup(status)
            return
        else:
            for user in data["users"]:
                if user_login == user["login"]:
                    logger.info(f"login already used")
                    status = [False, getcurlenglocal("login already used", "en")]
                    singup(status)
                    return
                else:
                    log = [f"sing up procesing {user_login}:{user_password} possible _id - {len(data["users"])+1}", "info"]
                    status = [True, len(data["users"])+1]
                    user = {
                        "_id": len(data["users"])+1,
                        "login": user_login,
                        "password": user_password,
                        "cur balance": 500,
                        "on tap": 1,
                        "energy": 500,
                        "energy limit": 1000,
                        "regiset date": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                        "taps": 500,
                        "all balance": 500
                    }
                    user_data_dump("data/game.json", user)
                    logger_read(log)
                    singup(status)
                    return


def go_statistic():
    game.close()
    game_statistic.show()


def quit_game_func():
    App.exit()


def go_login():
    game.close()
    login.show()


def del_account_accept():
    pass


def del_account_reject():
    pass


def promo_history_func():
    game.close()
    shop_promo_history.show()


def promo_enter_func():
    game.close()
    shop_promo_enter.show()


def promo_create_func():
    game.close()
    shop_promo_create.show()


def pumping_opne():
    game.close()
    shop_pumping.show()


def boosts_open():
    game.close()
    shop_boosts.show()


def main_func():
    user = user_data_load("data/game.json", status[1])
    if user["energy"] >= 1:
        user["cur balance"] += user["on tap"]
        user["energy"] -= user["on tap"]
        user["taps"] += 1
        user["all balance"] += user["on tap"]
        user_data_dump("data/game.json", user)
        energy_balance.setText(str(user["energy"]))
        balance.setText(str(user["cur balance"]))
        progres = 100 / (user["energy limit"] / user["energy"])
        energy_progres.setValue(int(progres))
    else:
        pass

ualocalization.clicked.connect(localization)
sing_in.clicked.connect(lambda: cehksingin("zufel", "password"))
sing_up.clicked.connect(lambda: cheksingup(login_input.text(), password_input.text()))
main_btn.clicked.connect(lambda: main_func())

gamemenu.triggered[QAction].connect(menu_func)
shopmenu.triggered[QAction].connect(menu_func)

login.show()
App.exec()
