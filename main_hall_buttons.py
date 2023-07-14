from PySide6 import QtWidgets, QtCore


def create_jewelry(parent, clicked):
    jewerly = QtWidgets.QPushButton(parent=parent)
    jewerly.setGeometry(QtCore.QRect(153, 310, 482, 247))
    jewerly.setStyleSheet("background-image: url(:/main_hall/jewelry.png); border: 0; background-repeat: no-repeat")
    jewerly.setText("")
    jewerly.setObjectName("jewelry")
    jewerly.clicked.connect(clicked)
    return jewerly


def create_embroidery(parent, clicked):
    embroidery = QtWidgets.QPushButton(parent=parent)
    embroidery.setGeometry(QtCore.QRect(721, 310, 482, 247))
    embroidery.setStyleSheet("background-image: url(:/main_hall/embroidery.png); border: 0; "
                             "background-repeat: no-repeat")
    embroidery.setText("")
    embroidery.setObjectName("embroidery")
    embroidery.clicked.connect(clicked)
    return embroidery


def create_painting(parent, clicked):
    painting = QtWidgets.QPushButton(parent=parent)
    painting.setGeometry(QtCore.QRect(1290, 310, 482, 247))
    painting.setStyleSheet("background-image: url(:/main_hall/painting.png); border: 0; background-repeat: no-repeat")
    painting.setText("")
    painting.setObjectName("painting")
    painting.clicked.connect(clicked)
    return painting

def create_video_page(parent, clicked):
    video_page = QtWidgets.QPushButton(parent=parent)
    video_page.setGeometry(QtCore.QRect(721, 600, 482, 190))
    video_page.setStyleSheet("background-image: url(:/main_hall/video.png); border: 0; background-repeat: no-repeat")
    video_page.setText("")
    video_page.setObjectName("video_page")
    video_page.clicked.connect(clicked)
    return video_page
