import json
from functools import partial

from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QColor, QPalette


def create_jewelry_masters_buttons(parent, font_18, show_current_master, jewelry_master_buttons, change_clicked_master):
    with open('texts/jewelry/jewelry_masters.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        jewelry_data = data
    rows = len(data['persons']) // 4
    last_row = len(data['persons']) % 4
    offset = (1330 - last_row * 310) // 2
    for i in range(rows):
        for j in range(4):
            jewelry_master_button = QtWidgets.QPushButton(parent=parent)
            jewelry_master_button.setGeometry(QtCore.QRect(589 + j * 300, 275 + i * 137, 300, 137))
            jewelry_master_button.setStyleSheet("background-image: url(:/jewelry/jewelry_masters_button.png); "
                                                "border: 0;")
            jewelry_master_button.setFont(font_18)
            palette = jewelry_master_button.palette()
            color = QColor(228, 213, 189)
            palette.setColor(QPalette.ButtonText, color)
            jewelry_master_button.setPalette(palette)
            jewelry_master_button.setText(f"{data['persons'][j]['person']}")
            jewelry_master_button.setObjectName(f"jewelry_master_button_{j}")
            jewelry_master_button.clicked.connect(partial(change_clicked_master, j))
            jewelry_master_buttons.append(jewelry_master_button)
    for i in range(last_row):
        jewelry_master_button = QtWidgets.QPushButton(parent=parent)
        jewelry_master_button.setGeometry(QtCore.QRect(570 + offset + i * 300, 275 + rows * 137, 300, 137))
        jewelry_master_button.setStyleSheet("background-image: url(:/jewelry/jewelry_masters_button.png); "
                                            "border: 0;")
        jewelry_master_button.setFont(font_18)
        palette = jewelry_master_button.palette()
        color = QColor(228, 213, 189)
        palette.setColor(QPalette.ButtonText, color)
        jewelry_master_button.setPalette(palette)
        jewelry_master_button.setText(f"{data['persons'][i + rows * 4]['person']}")
        jewelry_master_button.setObjectName(f"jewelry_master_button_{i + rows * 4}")
        jewelry_master_button.clicked.connect(partial(change_clicked_master, i + rows * 4))
        jewelry_master_buttons.append(jewelry_master_button)

    return jewelry_master_buttons, jewelry_data