from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
from localization import local

ua = local("localization/ua.json")
en = local("localization/en_login.json")

App = QApplication(sys.argv)
App.setStyleSheet("""
    QWidget {
        background-image: url("data/background.jpg");
        background-repeat: no-repeat; 
        background-position: center;
        color: #FFFFFF;
        border: 0px;
        font-size: 35px;
    }
    QSplitter {
        opacity: 0;
    }
    
    QPushButton {
    color: #FFFFFF;
    border-radius: 10px;
    border-style: outset;
    background: #222222;
    width: 340;
    height: 45;
    font-size: 25;
    padding: 5px;
    }

    QPushButton:hover {
        background: #191919
    }
    
    QPushButton:pressed {
        border-style: inset;
        background: #151515
    }
    
    QLineEdit {
    color: #FFFFFF;
    border-radius: 10px;
    border-style: outset;
    background: #222222;
    width: 340;
    height: 45;
    font-size: 25px;
    padding: 10px;
    }
""")

spliter = QSplitter()

opacity_effect = QGraphicsOpacityEffect()
opacity_effect.setOpacity(0)
spliter.setGraphicsEffect(opacity_effect)

login = QWidget()
login.resize(480, 720)

login_photo_line = QHBoxLayout()
login_v_line = QVBoxLayout()
label_line = QHBoxLayout()
login_line = QHBoxLayout()
password_line = QHBoxLayout()
sing_in_line = QHBoxLayout()
sing_up_line = QHBoxLayout()
chek_line = QHBoxLayout()

login_label = QLabel(en.get("login"))
login_label.setStyleSheet("""font-size: 45px; background:rgba(0, 0, 0, 0);""")

login_photo_widget = QLabel()
login_input = QLineEdit()
password_input = QLineEdit()
login_input.setPlaceholderText(en.get("ent-login"))
password_input.setPlaceholderText(en.get("ent-password"))
sing_in = QPushButton(en.get("sing-in"))
sing_up = QPushButton(en.get("sing-up"))
dark_mode = QCheckBox(en.get("dark-mode"))
ua_localization = QCheckBox(en.get("ua-localization"))

pixmap = QPixmap("data/background.jpg")
login_photo_widget.setPixmap(pixmap)

login_photo_line.addWidget(login_photo_widget)

chek_line.addWidget(spliter)
chek_line.addWidget(ua_localization)
chek_line.addWidget(dark_mode)
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

login_v_line.addWidget(spliter)
login_v_line.addWidget(spliter)
login_v_line.addWidget(spliter)
login_v_line.addLayout(label_line)
login_v_line.addWidget(spliter)
login_v_line.addWidget(spliter)
login_v_line.addWidget(spliter)
login_v_line.addWidget(spliter)
login_v_line.addWidget(spliter)
login_v_line.addLayout(login_line)
login_v_line.addLayout(password_line)
login_v_line.addLayout(sing_in_line)
login_v_line.addLayout(sing_up_line)
login_v_line.addWidget(spliter)
login_v_line.addLayout(chek_line)

login.setLayout(login_v_line)

login.show()
App.exec()
