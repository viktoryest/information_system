import os
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QColor, QPalette, Qt


def create_current_master_button(parent, index, jewelry_data):
    master_photo_label = QtWidgets.QLabel(parent=parent)
    master_photo_label.setGeometry(QtCore.QRect(633, 400, 413, 517))
    full_path = os.path.abspath(f"{jewelry_data['persons'][index]['image']}")
    pixmap = QtGui.QPixmap(full_path)
    pixmap = pixmap.scaledToWidth(413)
    pixmap = pixmap.scaledToHeight(517)
    master_photo_label.setPixmap(pixmap)
    master_photo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    master_photo_label.setStyleSheet("background: transparent; border: 0;")
    master_photo_label.setObjectName("master_photo_label")
    return master_photo_label


def create_name_button(parent, index, jewelry_data, font_24):
    person_name_button = QtWidgets.QPushButton(parent=parent)
    person_name_button.setGeometry(QtCore.QRect(633, 240, 596, 110))
    person_name_button.setStyleSheet("background-image: url(:/jewelry/person_button.png); border: 0; "
                                          "text-align: center; text-decoration: bold; color: #7c2832;")
    person_name_button.setText(jewelry_data['persons'][index]['full_name'])
    person_name_button.setFont(font_24)
    palette = person_name_button.palette()
    color = QColor(124, 40, 50)
    palette.setColor(QPalette.ButtonText, color)
    person_name_button.setPalette(palette)
    person_name_button.setObjectName("person_name_button")
    return person_name_button


def create_current_master_title(parent, index, jewelry_data, font_20):
    master_title = QtWidgets.QTextEdit(parent=parent)
    master_title.setGeometry(QtCore.QRect(1109, 393, 684, 36))
    master_title.setStyleSheet("background: transparent; qproperty-textInteractionFlags: NoTextInteraction;")
    master_title.setText(jewelry_data['persons'][index]['title'])
    master_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    master_title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    master_title.setTextColor(QColor(68, 59, 64))
    master_title.setFont(font_20)
    master_title.setObjectName("master_title")
    master_title.setReadOnly(True)
    return master_title