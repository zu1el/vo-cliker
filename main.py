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
energy_line.addWidget(QSplitter())
energy_data.addWidget(energy_balance)
energy_data.addWidget(energy_limit)
energy_line.addLayout(energy_data)
energy_line.addWidget(QSplitter())
energy_line.addWidget(energy_progres)
energy_line.addWidget(QSplitter())
game_line.addLayout(energy_line)
game.setLayout(game_line)

# game-my statistic
game_statistic = QWidget()
game_statistic.setStyleSheet(open("Styles/game_statistic.qss").read())
game_statistic.setFixedSize(440, 700)

game_statistic_main_line = QHBoxLayout()
game_statistic_v_line = QVBoxLayout()

game_statistic_label = QLabel(getcurlenglocal("game statistic"))
game_statistic_label_line = QHBoxLayout()
game_statistic_id = QLabel(getcurlenglocal("game id"))
game_statistic_id_line = QHBoxLayout()
game_statistic_login = QLabel(getcurlenglocal("game login"))
game_statistic_login_line = QHBoxLayout()
game_statistic_cur_balance = QLabel(getcurlenglocal("game current balance"))
game_statistic_cur_balance_line = QHBoxLayout()
game_statistic_on_tap = QLabel(getcurlenglocal("game on tap"))
game_statistic_on_tap_line = QHBoxLayout()
game_statistic_cur_energy = QLabel(getcurlenglocal("game current energy"))
game_statistic_cur_energy_line = QHBoxLayout()
game_statistic_limit_energy = QLabel(getcurlenglocal("game energy limit"))
game_statistic_limit_energy_line = QHBoxLayout()
game_statistic_reg_date = QLabel(getcurlenglocal("game registr date"))
game_statistic_reg_date_line = QHBoxLayout()
game_statistic_all_taps = QLabel(getcurlenglocal("game all taps"))
game_statistic_all_taps_line = QHBoxLayout()
game_statistic_all_balance = QLabel(getcurlenglocal("game all balance"))
game_statistic_all_balance_line = QHBoxLayout()

game_statistic_v_line.addWidget(QSplitter())
game_statistic_v_line.addWidget(QSplitter())
game_statistic_v_line.addWidget(QSplitter())

centerwidget(game_statistic_label, game_statistic_label_line)
game_statistic_v_line.addLayout(game_statistic_label_line)

centerwidget(game_statistic_id, game_statistic_id_line)
game_statistic_v_line.addLayout(game_statistic_id_line)

centerwidget(game_statistic_login, game_statistic_login_line)
game_statistic_v_line.addLayout(game_statistic_login_line)

centerwidget(game_statistic_cur_balance, game_statistic_cur_balance_line)
game_statistic_v_line.addLayout(game_statistic_cur_balance_line)

centerwidget(game_statistic_all_balance, game_statistic_all_balance_line)
game_statistic_v_line.addLayout(game_statistic_all_balance_line)

centerwidget(game_statistic_on_tap, game_statistic_on_tap_line)
game_statistic_v_line.addLayout(game_statistic_on_tap_line)

centerwidget(game_statistic_all_taps, game_statistic_all_taps_line)
game_statistic_v_line.addLayout(game_statistic_all_taps_line)

centerwidget(game_statistic_cur_energy, game_statistic_cur_energy_line)
game_statistic_v_line.addLayout(game_statistic_cur_energy_line)

centerwidget(game_statistic_limit_energy, game_statistic_limit_energy_line)
game_statistic_v_line.addLayout(game_statistic_limit_energy_line)

centerwidget(game_statistic_reg_date, game_statistic_reg_date_line)
game_statistic_v_line.addLayout(game_statistic_reg_date_line)

game_statistic_main_line.addLayout(game_statistic_v_line)

game_statistic.setLayout(game_statistic_main_line)

game_statistic_v_line.addWidget(QSplitter())
game_statistic_v_line.addWidget(QSplitter())

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
        case "Boosts":
            boosts_open()
        case "Pumping":
            pumping_opne()
        case "Go login":
            go_login()
        case "Моя статистика":
            go_statistic()
        case "Вийти з гри":
            quit_game_func()
        case "Вийти в меню входу":
            go_login()
        case "Прийняти":
            del_account_accept()
        case "Бусти":
            boosts_open()
        case "Прокачка":
            pumping_opne()
        case _:
            print(q.text())


def singin(status):
    user = user_data_load("data/game.json", status[1])
    if status[0]:
        gamemenu.setTitle(getcurlenglocal("game"))
        shopmenu.setTitle(getcurlenglocal("shop"))
        statistic.setText(getcurlenglocal("statistic"))
        quit_game.setText(getcurlenglocal("quit"))
        reset.setTitle(getcurlenglocal("reset-data"))
        go_menu.setText(getcurlenglocal("go-menu"))
        reject_reset.setText(getcurlenglocal("reject"))
        accept_reset.setText(getcurlenglocal("accept"))
        boosts.setText(getcurlenglocal("boosts"))
        pumping.setText(getcurlenglocal("pumping"))
        balance.setText(str(user["cur balance"]))
        energy_balance.setText(str(user["energy"]))
        energy_limit.setText(f"""/{user["energy limit"]}""")
        try:
            progres = 100/(user["energy limit"]/user["energy"])
            energy_progres.setValue(int(progres))

        except Exception as ex:
            energy_progres.setValue(0)
        game.show()
        login.close()
    else:
        info.setText(getcurlenglocal(status[1], current_lang))


def singup(status):
    user = user_data_load("data/game.json", status[1])
    if status[0]:
        gamemenu.setTitle(getcurlenglocal("game"))
        shopmenu.setTitle(getcurlenglocal("shop"))
        statistic.setText(getcurlenglocal("statistic"))
        quit_game.setText(getcurlenglocal("quit"))
        reset.setTitle(getcurlenglocal("reset-data"))
        go_menu.setText(getcurlenglocal("go-menu"))
        reject_reset.setText(getcurlenglocal("reject"))
        accept_reset.setText(getcurlenglocal("accept"))
        boosts.setText(getcurlenglocal("boosts"))
        pumping.setText(getcurlenglocal("pumping"))
        balance.setText(str(user["cur balance"]))
        energy_balance.setText(str(user["energy"]))
        energy_limit.setText(f"""/{user["energy limit"]}""")
        try:
            progres = 100 / (user["energy limit"] / user["energy"])
            energy_progres.setValue(int(progres))

        except Exception as ex:
            energy_progres.setValue(0)
        game.show()
        login.close()
    else:
        info.setText(getcurlenglocal(status[1], current_lang))


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
    user = user_data_load("data/game.json", status[1])
    game.close()
    game_statistic.show()
    game_statistic_label.setText(getcurlenglocal("game statistic"))
    game_statistic_label.setStyleSheet("""font-size: 35px;""")
    game_statistic_id.setText(f"""{getcurlenglocal("game id")}{user["_id"]}""")
    game_statistic_reg_date.setText(f"""{getcurlenglocal("game registr date")}{str(user["regiset date"])}""")
    game_statistic_limit_energy.setText(f"""{getcurlenglocal("game energy limit")}{str(user["energy limit"])}""")
    game_statistic_cur_energy.setText(f"""{getcurlenglocal("game current energy")}{str(user["energy"])}""")
    game_statistic_all_taps.setText(f"""{getcurlenglocal("game all taps")}{str(user["taps"])}""")
    game_statistic_all_balance.setText(f"""{getcurlenglocal("game all balance")}{str(user["all balance"])}""")
    game_statistic_on_tap.setText(f"""{getcurlenglocal("game on tap")}{str(user["on tap"])}""")
    game_statistic_login.setText(f"""{getcurlenglocal("game login")}{str(user["login"])}""")
    game_statistic_cur_balance.setText(f"""{getcurlenglocal("game current balance")}{str(user["cur balance"])}""")



def quit_game_func():
    App.exit()


def go_login():
    game.close()
    login.show()


def del_account_accept():
    user = user_data_load("data/game.json", status[1])
    user["cur balance"] = 0
    user["on tap"] = 1
    user["energy"] = 500
    user["energy limit"] = 500
    user["taps"] = 0
    user["all balance"] = 0
    user_data_dump("data/game.json", user)
    balance.setText(str(user["cur balance"]))
    energy_balance.setText(str(user["energy"]))
    energy_limit.setText(f"""/{user["energy limit"]}""")
    progres = 100 / (user["energy limit"] / user["energy"])
    energy_progres.setValue(int(progres))


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
sing_in.clicked.connect(lambda: cehksingin(login_input.text(), password_input.text()))
sing_up.clicked.connect(lambda: cheksingup(login_input.text(), password_input.text()))
main_btn.clicked.connect(lambda: main_func())

gamemenu.triggered[QAction].connect(menu_func)
shopmenu.triggered[QAction].connect(menu_func)

login.show()
App.exec()
