from PySide6 import QtWidgets, QtCore


def create_embroiderers_button(parent, clicked):
    embroiderers_button = QtWidgets.QPushButton(parent=parent)
    embroiderers_button.setGeometry(QtCore.QRect(40, 553, 452, 121))
    embroiderers_button.setStyleSheet("background-image: url(:/left_menu/embroiderers.png); border: 0;")
    embroiderers_button.setText("")
    embroiderers_button.setObjectName("embroiderers_button")
    embroiderers_button.clicked.connect(clicked)
    return embroiderers_button
