import os

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


def create_current_artist_photo(parent, index, artists_data):
    artist_photo_label = QtWidgets.QLabel(parent=parent)
    artist_photo_label.setGeometry(QtCore.QRect(633, 400, 413, 517))
    full_path = os.path.abspath(f"{artists_data['persons'][index]['image']}")
    pixmap = QtGui.QPixmap(full_path)
    pixmap = pixmap.scaledToWidth(413)
    pixmap = pixmap.scaledToHeight(517)
    artist_photo_label.setPixmap(pixmap)
    artist_photo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    artist_photo_label.setStyleSheet("background: transparent; border: 0;")
    artist_photo_label.setObjectName("artist_photo_label")
    return artist_photo_label


def create_current_artist_title(parent, index, artists_data, font_20):
    artist_title = QtWidgets.QTextEdit(parent=parent)
    artist_title.setGeometry(QtCore.QRect(1109, 393, 684, 36))
    artist_title.setStyleSheet("background: transparent; qproperty-textInteractionFlags: NoTextInteraction;")
    artist_title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    artist_title.setTextColor(QColor(68, 59, 64))
    artist_title.setFont(font_20)
    artist_title.setText(artists_data['persons'][index]['title'])
    artist_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    artist_title.setObjectName("artist_title")
    artist_title.setReadOnly(True)
    return artist_title


def create_current_artist_description(parent, index, artists_data, font_16):
    artist_description = QtWidgets.QTextEdit(parent=parent)
    artist_description.setGeometry(QtCore.QRect(1109, 440, 684, 477))
    artist_description.setStyleSheet("background: transparent; qproperty-textInteractionFlags: NoTextInteraction;")
    artist_description.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    artist_description.setTextColor(QColor(68, 59, 64))
    artist_description.setFont(font_16)
    artist_description.setText(artists_data['persons'][index]['description'])
    artist_description.setAlignment(Qt.AlignmentFlag.AlignJustify)
    artist_description.setObjectName("artist_description")
    artist_description.setReadOnly(True)
    return artist_description
