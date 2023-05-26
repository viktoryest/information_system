import os
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QColor, QPalette, Qt


def create_current_embroiderer_page(parent, index, jewelry_data):
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