import json

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


def create_jewelry_pass(parent, clicked):
    jewelry_pass = QtWidgets.QPushButton(parent=parent)
    jewelry_pass.setGeometry(QtCore.QRect(0, 285, 465, 110))
    jewelry_pass.setStyleSheet("background-image: url(:/left_menu/jewelry_menu.png); border: 0;")
    jewelry_pass.setText("")
    jewelry_pass.setObjectName("jewelry_pass")
    jewelry_pass.clicked.connect(clicked)


def create_jewelry_content(parent):
    jewelry_content = QtWidgets.QWidget(parent=parent)
    jewelry_content.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
    jewelry_content.setStyleSheet("background: transparent; border: 0;")
    jewelry_content.setObjectName("jewelry_content")
    return jewelry_content


def create_jewelry_title_1(parent, data, font_20):
    jewelry_title_1 = QtWidgets.QTextEdit(parent=parent)
    jewelry_title_1.setGeometry(QtCore.QRect(583, 229, 1174, 36))
    jewelry_title_1.setStyleSheet("background: transparent;")
    jewelry_title_1.setText(data['title_1'])
    jewelry_title_1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    jewelry_title_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    jewelry_title_1.setTextColor(QColor(73, 64, 69))
    jewelry_title_1.setFont(font_20)
    jewelry_title_1.setObjectName("jewelry_title_1")
    jewelry_title_1.setReadOnly(True)
    return jewelry_title_1


def create_jewelry_main_text_1(parent, data, font_16):
    jewelry_main_text_1 = QtWidgets.QTextEdit(parent=parent)
    jewelry_main_text_1.setGeometry(QtCore.QRect(588, 270, 1201, 390))
    jewelry_main_text_1.setStyleSheet("background: transparent; border: 0; line-height: 90%;")
    jewelry_main_text_1.setText(data['main_text_1'])
    jewelry_main_text_1.setAlignment(Qt.AlignmentFlag.AlignJustify | Qt.AlignmentFlag.AlignJustify)
    jewelry_main_text_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    jewelry_main_text_1.setTextColor(QColor(73, 64, 69))
    jewelry_main_text_1.setFont(font_16)
    jewelry_main_text_1.setObjectName("jewelry_main_text_1")
    jewelry_main_text_1.setReadOnly(True)
    return jewelry_main_text_1


def create_jewelry_title_2(parent, data, font_20):
    jewelry_title_2 = QtWidgets.QTextEdit(parent=parent)
    jewelry_title_2.setGeometry(QtCore.QRect(603, 686, 1174, 36))
    jewelry_title_2.setStyleSheet("background: transparent; border: 0;")
    jewelry_title_2.setText(data['title_2'])
    jewelry_title_2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    jewelry_title_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    jewelry_title_2.setTextColor(QColor(73, 64, 69))
    jewelry_title_2.setFont(font_20)
    jewelry_title_2.setObjectName("jewelry_title_2")
    jewelry_title_2.setReadOnly(True)
    return jewelry_title_2


def create_jewelry_main_text_2(parent, data, font_16):
    jewelry_main_text_2 = QtWidgets.QTextEdit(parent=parent)
    jewelry_main_text_2.setGeometry(QtCore.QRect(588, 737, 1201, 220))
    jewelry_main_text_2.setStyleSheet("background: transparent; border: 0;")
    jewelry_main_text_2.setText(data['main_text_2'])
    jewelry_main_text_2.setAlignment(Qt.AlignmentFlag.AlignJustify)
    jewelry_main_text_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    jewelry_main_text_2.setTextColor(QColor(73, 64, 69))
    jewelry_main_text_2.setFont(font_16)
    jewelry_main_text_2.setObjectName("jewelry_main_text_2")
    jewelry_main_text_2.setReadOnly(True)
    return jewelry_main_text_2
