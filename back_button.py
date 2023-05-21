from PySide6 import QtWidgets, QtCore


def create_back_button(parent):
    back_button = QtWidgets.QPushButton(parent=parent)
    back_button.setGeometry(QtCore.QRect(1110, 975, 166, 63))
    back_button.setStyleSheet("background-image: url(:/images/back.png); border: 0;")
    back_button.setText("")
    back_button.setObjectName("back_button")
    return back_button