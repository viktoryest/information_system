import glob

from PySide6 import QtWidgets, QtCore, QtGui

from round_label import RoundedLabel


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


def create_photo_previews(i, files_amount, parent, jewelry_photo_common_path):
    if i <= files_amount - 1:
        photo_preview = RoundedLabel(parent=parent)
        photo_preview.setGeometry(QtCore.QRect(630 + i * 290, 705, 264, 211))
        pixmap = QtGui.QPixmap(glob.glob(jewelry_photo_common_path)[i])
        photo_preview.setStyleSheet("border: 0")

        preview_width = 264
        preview_height = 211

        image_ratio = pixmap.width() / pixmap.height()

        if image_ratio > 1:
            scaled_width = int(preview_height * image_ratio)
            scaled_height = preview_height
        else:
            scaled_width = preview_width
            scaled_height = int(preview_width / image_ratio)

        scaled_pixmap = pixmap.scaled(scaled_width, scaled_height, QtCore.Qt.KeepAspectRatio,
                                      QtCore.Qt.SmoothTransformation)
        x_offset = (preview_width - scaled_width) // 2
        y_offset = (preview_height - scaled_height) // 2
        canvas = QtGui.QPixmap(preview_width, preview_height)
        canvas.fill(QtCore.Qt.transparent)

        painter = QtGui.QPainter(canvas)
        painter.drawPixmap(x_offset, y_offset, scaled_pixmap)
        painter.end()

        return photo_preview, canvas



