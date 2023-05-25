import os

from PySide6 import QtWidgets, QtCore, QtGui


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
