import os

from PySide6 import QtWidgets, QtCore, QtGui, QtMultimedia
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget


def create_video_title(parent):
    video_title = QtWidgets.QLabel(parent=parent)
    video_title.setGeometry(QtCore.QRect(1007, 213, 370, 43))
    video_title.setStyleSheet("background-image: url(:/jewelry/video_title.png); border: 0;")
    video_title.setText("")
    video_title.setObjectName("video_title")
    return video_title


def create_video_preview(parent, xoffset, yoffset, width, height, path):
    video_preview = QtWidgets.QLabel(parent=parent)
    video_preview.setGeometry(QtCore.QRect(xoffset, yoffset, width, height))
    pixmap = QtGui.QPixmap(os.path.abspath(path))
    video_preview.setStyleSheet(f"border: 0; background: transparent;")
    video_preview.setPixmap(pixmap)
    video_preview.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    video_preview.setText("")
    video_preview.setObjectName("video_preview")
    return video_preview


def create_play_button(parent, clicked):
    play_button = QtWidgets.QPushButton(parent=parent)
    play_button.setGeometry(QtCore.QRect(1014, 285, 361, 307))
    play_button.setStyleSheet("background-image: transparent; border: 0;")
    play_button.setText("")
    play_button.setObjectName("play_button")
    play_button.clicked.connect(clicked)
    return play_button


