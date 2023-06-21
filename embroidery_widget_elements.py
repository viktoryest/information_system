import json
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


def create_embroiderers_button(parent, clicked):
    embroiderers_button = QtWidgets.QPushButton(parent=parent)
    embroiderers_button.setGeometry(QtCore.QRect(40, 553, 452, 121))
    embroiderers_button.setStyleSheet("background-image: url(:/left_menu/embroiderers.png); border: 0;")
    embroiderers_button.setText("")
    embroiderers_button.setObjectName("embroiderers_button")
    embroiderers_button.clicked.connect(clicked)
    return embroiderers_button


def create_embroidery_title(parent, font_20, content, y_offset):
    with open('texts/embroidery/embroidery_history.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    embroidery_title = QtWidgets.QTextEdit(parent=parent)
    embroidery_title.setGeometry(QtCore.QRect(583, y_offset, 1174, 30))
    embroidery_title.setStyleSheet("background: transparent; qproperty-textInteractionFlags: NoTextInteraction;")
    embroidery_title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    embroidery_title.setTextColor(QColor(73, 64, 69))
    embroidery_title.setFont(font_20)
    embroidery_title.setObjectName("embroidery_title")
    embroidery_title.setReadOnly(True)
    embroidery_title.setText(data[content])
    embroidery_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    return embroidery_title


def create_embroidery_main_text(parent, font_16, content, y_offset):
    with open('texts/embroidery/embroidery_history.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    embroidery_main_text = QtWidgets.QTextEdit(parent=parent)
    embroidery_main_text.setGeometry(QtCore.QRect(588, y_offset, 1201, 500))
    embroidery_main_text.setStyleSheet("background: transparent; border: 0;"
                                       "qproperty-textInteractionFlags: NoTextInteraction;")
    embroidery_main_text.setTextColor(QColor(73, 64, 69))
    embroidery_main_text.setFont(font_16)
    embroidery_main_text.setObjectName("embroidery_main_text")
    embroidery_main_text.setReadOnly(True)
    embroidery_main_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    embroidery_main_text.setText(data[content])
    embroidery_main_text.setAlignment(Qt.AlignmentFlag.AlignJustify | Qt.AlignmentFlag.AlignJustify)
    return embroidery_main_text
