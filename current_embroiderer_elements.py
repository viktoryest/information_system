import os
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QColor, QPalette, Qt


def create_current_embroiderer_photo(parent, index, jewelry_data):
    embroiderer_photo_label = QtWidgets.QLabel(parent=parent)
    embroiderer_photo_label.setGeometry(QtCore.QRect(633, 400, 413, 517))
    full_path = os.path.abspath(f"{jewelry_data['persons'][index]['image']}")
    pixmap = QtGui.QPixmap(full_path)
    pixmap = pixmap.scaledToWidth(413)
    pixmap = pixmap.scaledToHeight(517)
    embroiderer_photo_label.setPixmap(pixmap)
    embroiderer_photo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    embroiderer_photo_label.setStyleSheet("background: transparent; border: 0;")
    embroiderer_photo_label.setObjectName("embroiderer_photo_label")
    return embroiderer_photo_label


def create_name_button(parent, index, embroidery_data, font_24):
    person_name_button = QtWidgets.QPushButton(parent=parent)
    person_name_button.setGeometry(QtCore.QRect(633, 240, 596, 110))
    person_name_button.setStyleSheet("background-image: url(:/jewelry/person_button.png); border: 0; "
                                          "text-align: center; text-decoration: bold; color: #7c2832;")
    person_name_button.setText(embroidery_data['persons'][index]['full_name'])
    person_name_button.setFont(font_24)
    palette = person_name_button.palette()
    color = QColor(124, 40, 50)
    palette.setColor(QPalette.ButtonText, color)
    person_name_button.setPalette(palette)
    person_name_button.setObjectName("person_name_button")
    return person_name_button


def create_current_embroiderer_title(parent, index, embroidery_data, font_20):
    embroiderer_title = QtWidgets.QTextEdit(parent=parent)
    embroiderer_title.setGeometry(QtCore.QRect(1109, 393, 684, 36))
    embroiderer_title.setStyleSheet("background: transparent; qproperty-textInteractionFlags: NoTextInteraction;")
    embroiderer_title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    embroiderer_title.setTextColor(QColor(68, 59, 64))
    embroiderer_title.setFont(font_20)
    embroiderer_title.setText(embroidery_data['persons'][index]['title'])
    embroiderer_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    embroiderer_title.setObjectName("embroiderer_title")
    embroiderer_title.setReadOnly(True)
    return embroiderer_title


def create_current_embroiderer_description(parent, index, embroidery_data, font_16):
    embroiderer_description = QtWidgets.QTextEdit(parent=parent)
    embroiderer_description.setGeometry(QtCore.QRect(1109, 440, 684, 477))
    embroiderer_description.setStyleSheet("background: transparent; qproperty-textInteractionFlags: NoTextInteraction;")
    embroiderer_description.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    embroiderer_description.setTextColor(QColor(68, 59, 64))
    embroiderer_description.setFont(font_16)
    embroiderer_description.setText(embroidery_data['persons'][index]['description'])
    embroiderer_description.setAlignment(Qt.AlignmentFlag.AlignJustify)
    embroiderer_description.setObjectName("embroiderer_description")
    embroiderer_description.setReadOnly(True)
    return embroiderer_description


def create_left_arrow(parent, clicked):
    left_arrow = QtWidgets.QPushButton(parent=parent)
    left_arrow.setGeometry(QtCore.QRect(589, 270, 21, 52))
    left_arrow.setStyleSheet("background-image: url(:/jewelry/left_arrow.png); border: 0;")
    left_arrow.setObjectName("left_arrow")
    left_arrow.clicked.connect(clicked)
    return left_arrow


def create_right_arrow(parent, clicked):
    right_arrow = QtWidgets.QPushButton(parent=parent)
    right_arrow.setGeometry(QtCore.QRect(1250, 270, 21, 52))
    right_arrow.setStyleSheet("background-image: url(:/jewelry/right_arrow.png); border: 0;")
    right_arrow.setObjectName("right_arrow")
    right_arrow.clicked.connect(clicked)
    return right_arrow
