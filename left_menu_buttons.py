from PySide6 import QtWidgets, QtCore


def create_masters_button(parent, clicked):
    masters_button = QtWidgets.QPushButton(parent=parent)
    masters_button.setGeometry(QtCore.QRect(40, 392, 452, 121))
    masters_button.setStyleSheet("background-image: url(:/jewelry/masters.png); border: 0;")
    masters_button.setText("")
    masters_button.setObjectName("masters_button")
    masters_button.clicked.connect(clicked)
    return masters_button


def create_video_photo_button(parent, clicked):
    video_photo_button = QtWidgets.QPushButton(parent=parent)
    video_photo_button.setGeometry(QtCore.QRect(40, 485, 452, 121))
    video_photo_button.setStyleSheet("background-image: url(:/jewelry/video_photo.png); border: 0;")
    video_photo_button.setText("")
    video_photo_button.setObjectName("video_photo")
    video_photo_button.clicked.connect(clicked)
    return video_photo_button


def create_embroidery_button(parent, clicked):
    embroidery_button = QtWidgets.QPushButton(parent=parent)
    embroidery_button.setGeometry(QtCore.QRect(0, 643, 491, 160))
    embroidery_button.setStyleSheet("background-image: url(:/left_menu/embroidery_menu.png); border: 0;")
    embroidery_button.setText("")
    embroidery_button.setObjectName("embroidery_button")
    embroidery_button.clicked.connect(clicked)
    return embroidery_button


def create_painting_button(parent, clicked):
    painting_button = QtWidgets.QPushButton(parent=parent)
    painting_button.setGeometry(QtCore.QRect(0, 791, 491, 121))
    painting_button.setStyleSheet("background-image: url(:/left_menu/painting_menu.png); border: 0;")
    painting_button.setText("")
    painting_button.setObjectName("painting_button")
    painting_button.clicked.connect(clicked)
    return painting_button


