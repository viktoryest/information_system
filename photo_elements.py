from PySide6 import QtWidgets, QtCore


def create_photo_title(parent):
    photo_title = QtWidgets.QLabel(parent=parent)
    photo_title.setGeometry(QtCore.QRect(1007, 600, 370, 43))
    photo_title.setStyleSheet("background-image: url(:/jewelry/photo_title.png); border: 0;")
    photo_title.setText("")
    photo_title.setObjectName("photo_title")
    return photo_title
    
    
def create_left_arrow_button(parent, clicked):
    photo_left_button = QtWidgets.QPushButton(parent=parent)
    photo_left_button.setGeometry(QtCore.QRect(585, 765, 25, 64))
    photo_left_button.setStyleSheet("background-image: url(:/images/photo_left_button.png); border: 0;")
    photo_left_button.setText("")
    photo_left_button.setObjectName("photo_left_button")
    photo_left_button.clicked.connect(clicked)
    return photo_left_button


def create_right_arrow_button(parent, clicked):
    photo_right_button = QtWidgets.QPushButton(parent=parent)
    photo_right_button.setGeometry(QtCore.QRect(1790, 765, 25, 64))
    photo_right_button.setStyleSheet("background-image: url(:/images/photo_right_button.png); border: 0;")
    photo_right_button.setText("")
    photo_right_button.setObjectName("photo_right_button")
    photo_right_button.clicked.connect(clicked)
    return photo_right_button


def create_left_arrow_button_full(parent, clicked):
    gallery_left_arrow = QtWidgets.QPushButton(parent=parent)
    gallery_left_arrow.setGeometry(QtCore.QRect(593, 605, 25, 64))
    gallery_left_arrow.setStyleSheet("background-image: url(:/images/photo_left_button.png); border: 0;")
    gallery_left_arrow.setText("")
    gallery_left_arrow.setObjectName("gallery_left_arrow")
    gallery_left_arrow.clicked.connect(clicked)
    return gallery_left_arrow


def create_right_arrow_button_full(parent, clicked):
    gallery_left_arrow = QtWidgets.QPushButton(parent=parent)
    gallery_left_arrow.setGeometry(QtCore.QRect(1770, 605, 25, 64))
    gallery_left_arrow.setStyleSheet("background-image: url(:/images/photo_right_button.png); border: 0;")
    gallery_left_arrow.setText("")
    gallery_left_arrow.setObjectName("gallery_left_arrow")
    gallery_left_arrow.clicked.connect(clicked)
    return gallery_left_arrow





