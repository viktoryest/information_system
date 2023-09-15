from PySide6 import QtWidgets, QtCore


def create_back_button(parent, clicked):
    back_button = QtWidgets.QPushButton(parent=parent)
    back_button.setGeometry(QtCore.QRect(1100, 975, 175, 73))
    back_button.setStyleSheet("background-image: url(:/images/back.png); border: 0;")
    back_button.setText("")
    back_button.setObjectName("back_button")
    back_button.clicked.connect(clicked)
    return back_button


def create_line(parent):
    line = QtWidgets.QLabel(parent=parent)
    line.setGeometry(QtCore.QRect(1300, 292, 564, 2))
    line.setStyleSheet("background-image: url(:/jewelry/line.png); border: 0;")
    line.setObjectName("line")