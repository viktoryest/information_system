# Form implementation generated from reading ui file 'info_sys.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import glob

from PySide6 import QtCore, QtGui, QtWidgets, QtMultimedia
import json
import os.path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QColor, QPalette, QFont, QFontDatabase, Qt
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QMessageBox
from pathlib import Path
from functools import partial


from PySide6 import QtCore, QtGui, QtWidgets

class RoundedLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.radius = 10

        # Создаем QGraphicsDropShadowEffect и задаем параметры тени
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 128))
        self.shadow.setOffset(0, 0)
        self.setGraphicsEffect(self.shadow)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), self.radius, self.radius)

        painter.setClipPath(path)
        painter.drawPixmap(self.rect(), self.pixmap())

    def setPixmap(self, pixmap):
        super().setPixmap(pixmap)
        self.setScaledContents(True)


class Ui_MyMainWindow(object):
    play_video_state = False
    current_photo_index = 0
    current_photo_gallery = 0
    dirname = os.path.dirname(__file__)
    jewelry_photo_common = os.path.join(dirname, 'images/jewelry/photo_common')
    jewelry_photo_common_path = os.path.join(jewelry_photo_common, '*')
    photo_paths = sorted(glob.glob(jewelry_photo_common_path))

    # main screen
    def setupUi(self, MyMainWindow):
        MyMainWindow.setObjectName("MyMainWindow")
        MyMainWindow.setEnabled(True)
        MyMainWindow.resize(1920, 1080)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MyMainWindow.sizePolicy().hasHeightForWidth())

        MyMainWindow.setSizePolicy(sizePolicy)
        MyMainWindow.setStyleSheet("background-image: url(:/images/background.png);")

        # set central widget
        self.centralwidget = QtWidgets.QWidget(parent=MyMainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        # set main button
        self.main_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.main_button.setGeometry(QtCore.QRect(560, 390, 859, 299))
        self.main_button.setSizePolicy(sizePolicy)
        self.main_button.setStyleSheet("background-image: url(:/images/main_button.png); border: 0;")
        self.main_button.setText("")
        self.main_button.setObjectName("main_button")
        self.main_button.clicked.connect(self.show_main_hall)

        # set main hall widget (contains 3 buttons)
        self.main_hall = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_hall.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.main_hall.setObjectName("main_hall")
        self.main_hall.hide()

        # set jewelry button
        self.jewerly = QtWidgets.QPushButton(parent=self.main_hall)
        self.jewerly.setGeometry(QtCore.QRect(153, 397, 527, 265))
        self.jewerly.setStyleSheet("background-image: url(:/main_hall/jewelry.png); border: 0;")
        self.jewerly.setText("")
        self.jewerly.setObjectName("jewelry")
        self.jewerly.clicked.connect(self.show_jewelry_widget)

        # set embroidery button
        self.embroidery = QtWidgets.QPushButton(parent=self.main_hall)
        self.embroidery.setGeometry(QtCore.QRect(721, 397, 527, 265))
        self.embroidery.setStyleSheet("background-image: url(:/main_hall/embroidery.png); border: 0;")
        self.embroidery.setText("")
        self.embroidery.setObjectName("embroidery")

        # set painting button
        self.painting = QtWidgets.QPushButton(parent=self.main_hall)
        self.painting.setGeometry(QtCore.QRect(1290, 397, 527, 265))
        self.painting.setStyleSheet("background-image: url(:/main_hall/painting.png); border: 0;")
        self.painting.setText("")
        self.painting.setObjectName("painting")

        # set left menu widget
        self.jewelry_widget = QtWidgets.QWidget(parent=self.main_hall)
        self.jewelry_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.jewelry_widget.setStyleSheet("background-image: url(:/jewelry/jewelry_bg.png); border: 0;")
        self.jewelry_widget.setObjectName("jewelry_widget")
        self.jewelry_widget.hide()

        # set inactive button for jewelry
        self.jewelry_pass = QtWidgets.QPushButton(parent=self.jewelry_widget)
        self.jewelry_pass.setGeometry(QtCore.QRect(0, 285, 465, 110))
        self.jewelry_pass.setStyleSheet("background-image: url(:/left_menu/jewelry_menu.png); border: 0;")
        self.jewelry_pass.setText("")
        self.jewelry_pass.setObjectName("jewelry_pass")

        # set widget for jewelry content
        self.jewelry_content = QtWidgets.QWidget(parent=self.jewelry_widget)
        self.jewelry_content.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.jewelry_content.setStyleSheet("background: transparent; border: 0;")
        self.jewelry_content.setObjectName("jewelry_content")

        # set fornt for jewelry content
        with open('texts/jewelry/masters.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        fontId = QFontDatabase.addApplicationFont(":/fonts/MinionPro-Regular.ttf")
        fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
        # font for title
        self.font_20 = QFont(fontName, 20)
        # font for text
        self.font_16 = QFont(fontName, 16)

        # set the 1st title for jewelry content
        self.jewelry_title_1 = QtWidgets.QTextEdit(parent=self.jewelry_content)
        self.jewelry_title_1.setGeometry(QtCore.QRect(583, 229, 1174, 36))
        self.jewelry_title_1.setStyleSheet("background: transparent;")
        self.jewelry_title_1.setText(data['title_1'])
        self.jewelry_title_1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.jewelry_title_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.jewelry_title_1.setTextColor(QColor(73, 64, 69))
        self.jewelry_title_1.setFont(self.font_20)
        self.jewelry_title_1.setObjectName("jewelry_title_1")
        self.jewelry_title_1.setReadOnly(True)

        # set the 1st text for jewelry content
        self.jewelry_main_text_1 = QtWidgets.QTextEdit(parent=self.jewelry_content)
        self.jewelry_main_text_1.setGeometry(QtCore.QRect(588, 270, 1201, 390))
        self.jewelry_main_text_1.setStyleSheet("background: transparent; border: 0; line-height: 90%;")
        self.jewelry_main_text_1.setText(data['main_text_1'])
        self.jewelry_main_text_1.setAlignment(Qt.AlignmentFlag.AlignJustify | Qt.AlignmentFlag.AlignJustify)
        self.jewelry_main_text_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.jewelry_main_text_1.setTextColor(QColor(73, 64, 69))
        self.jewelry_main_text_1.setFont(self.font_16)
        self.jewelry_main_text_1.setObjectName("jewelry_main_text_1")
        self.jewelry_main_text_1.setReadOnly(True)

        # set the 2nd title for jewelry content
        self.jewelry_title_2 = QtWidgets.QTextEdit(parent=self.jewelry_content)
        self.jewelry_title_2.setGeometry(QtCore.QRect(603, 686, 1174, 36))
        self.jewelry_title_2.setStyleSheet("background: transparent; border: 0;")
        self.jewelry_title_2.setText(data['title_2'])
        self.jewelry_title_2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.jewelry_title_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.jewelry_title_2.setTextColor(QColor(73, 64, 69))
        self.jewelry_title_2.setFont(self.font_20)
        self.jewelry_title_2.setObjectName("jewelry_title_2")
        self.jewelry_title_2.setReadOnly(True)

        # set the 2nd text for jewelry content
        self.jewelry_main_text_2 = QtWidgets.QTextEdit(parent=self.jewelry_content)
        self.jewelry_main_text_2.setGeometry(QtCore.QRect(588, 737, 1201, 220))
        self.jewelry_main_text_2.setStyleSheet("background: transparent; border: 0;")
        self.jewelry_main_text_2.setText(data['main_text_2'])
        self.jewelry_main_text_2.setAlignment(Qt.AlignmentFlag.AlignJustify)
        self.jewelry_main_text_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.jewelry_main_text_2.setTextColor(QColor(73, 64, 69))
        self.jewelry_main_text_2.setFont(self.font_16)
        self.jewelry_main_text_2.setObjectName("jewelry_main_text_2")
        self.jewelry_main_text_2.setReadOnly(True)

        # set back button
        self.back_button = QtWidgets.QPushButton(parent=self.jewelry_content)
        self.back_button.setGeometry(QtCore.QRect(1110, 975, 166, 63))
        self.back_button.setStyleSheet("background-image: url(:/images/back.png); border: 0;")
        self.back_button.setText("")
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.show_main_hall)
        self.back_button.clicked.connect(self.jewelry_widget.hide)

        # set widget for video and photo content
        self.video_photo_widget = QtWidgets.QWidget(parent=self.jewelry_widget)
        self.video_photo_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.video_photo_widget.setStyleSheet("background: transparent; border: 0;")
        self.video_photo_widget.setObjectName("video_photo_widget")
        self.video_photo_widget.hide()

        # set left arrow button for photo
        self.photo_left_button = QtWidgets.QPushButton(parent=self.video_photo_widget)
        self.photo_left_button.setGeometry(QtCore.QRect(585, 765, 25, 64))
        self.photo_left_button.setStyleSheet("background-image: url(:/images/photo_left_button.png); border: 0;")
        self.photo_left_button.setText("")
        self.photo_left_button.setObjectName("photo_left_button")
        self.photo_left_button.clicked.connect(self.show_previous_photo)

        # set right arrow button for photo
        self.photo_right_button = QtWidgets.QPushButton(parent=self.video_photo_widget)
        self.photo_right_button.setGeometry(QtCore.QRect(1790, 765, 25, 64))
        self.photo_right_button.setStyleSheet("background-image: url(:/images/photo_right_button.png); border: 0;")
        self.photo_right_button.setText("")
        self.photo_right_button.setObjectName("photo_right_button")
        self.photo_right_button.clicked.connect(self.show_next_photo)

        # set video title
        self.video_title = QtWidgets.QLabel(parent=self.video_photo_widget)
        self.video_title.setGeometry(QtCore.QRect(1007, 213, 370, 43))
        self.video_title.setStyleSheet("background-image: url(:/jewelry/video_title.png); border: 0;")
        self.video_title.setText("")
        self.video_title.setObjectName("video_title")

        # set photo title
        self.photo_title = QtWidgets.QLabel(parent=self.video_photo_widget)
        self.photo_title.setGeometry(QtCore.QRect(1007, 600, 370, 43))
        self.photo_title.setStyleSheet("background-image: url(:/jewelry/photo_title.png); border: 0;")
        self.photo_title.setText("")
        self.photo_title.setObjectName("photo_title")

        # set video preview
        self.video_preview = QtWidgets.QLabel(parent=self.video_photo_widget)
        self.video_preview.setGeometry(QtCore.QRect(1014, 285, 361, 307))
        # pixmap = QtGui.QPixmap(os.path.abspath('video/mstera_video.mp4_thumbnail.jpg'))
        pixmap = QtGui.QPixmap(os.path.abspath('images/jewelry/play_preview.png'))
        self.video_preview.setStyleSheet(f"border: 0;")
        self.video_preview.setPixmap(pixmap)
        self.video_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.video_preview.setText("")
        self.video_preview.setObjectName("video_preview")

        # set play button for video
        self.play_button = QtWidgets.QPushButton(parent=self.video_photo_widget)
        self.play_button.setGeometry(QtCore.QRect(1014, 285, 361, 307))
        self.play_button.setStyleSheet("background-image: transparent; border: 0;")
        self.play_button.setText("")
        self.play_button.setObjectName("play_button")
        self.play_button.clicked.connect(self.play_video)

        self.player = QMediaPlayer()
        self.player.setSource(QUrl.fromLocalFile("video/mstera_video.mp4"))
        self.videoWidget = QVideoWidget(parent=self.video_photo_widget)
        self.player.setVideoOutput(self.videoWidget)
        self.player.videoOutput().setFixedSize(1920, 1080)
        self.player.videoOutput().move(0, 0)
        self.player.videoOutput().hide()
        self.player.setAudioOutput(QtMultimedia.QAudioOutput(self.videoWidget))

        self.photo_gallery_widget = QtWidgets.QWidget(parent=self.jewelry_widget)
        self.photo_gallery_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.photo_gallery_widget.setStyleSheet("background: transparent; border: 0;")
        self.photo_gallery_widget.setObjectName("video_photo_widget")
        self.photo_gallery_widget.hide()

        self.photo_viewer = QtWidgets.QLabel(parent=self.photo_gallery_widget)

        self.photo_title_main = QtWidgets.QLabel(parent=self.photo_gallery_widget)
        self.photo_title_main.setGeometry(QtCore.QRect(1007, 200, 370, 43))
        self.photo_title_main.setStyleSheet("background-image: url(:/jewelry/photo_title.png); border: 0;")
        self.photo_title_main.setText("")
        self.photo_title_main.setObjectName("photo_title")

        dirname = os.path.dirname(__file__)
        jewelry_photo_common = os.path.join(dirname, 'images/jewelry/photo_common')
        jewelry_photo_common_path = os.path.join(jewelry_photo_common, '*')
        files_amount = len(glob.glob(jewelry_photo_common_path))
        self.photo_widgets = []
        for i in range(4):
            if i <= files_amount - 1:
                self.photo_preview = RoundedLabel(parent=self.video_photo_widget)
                self.photo_preview.setGeometry(QtCore.QRect(630 + i * 290, 705, 264, 211))
                self.photo_preview.setFixedSize(264, 211)
                pixmap = QtGui.QPixmap(glob.glob(jewelry_photo_common_path)[i])
                self.photo_preview.setStyleSheet("border: 0")
                self.photo_preview.setPixmap(pixmap)
                self.photo_preview.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.photo_preview.setText("")
                self.photo_preview.setObjectName("photo_preview")
                self.photo_widgets.append(self.photo_preview)

                self.photo_preview_button = QtWidgets.QPushButton(parent=self.video_photo_widget)
                self.photo_preview_button.setGeometry(QtCore.QRect(630 + i * 290, 705, 264, 211))
                self.photo_preview_button.setStyleSheet("background-image: transparent; border: 0;")
                self.photo_preview_button.setText("")
                self.photo_preview_button.setObjectName("photo_preview_button")
                self.photo_preview_button.clicked.connect(partial(self.open_gallery, i))

        # set button for masters
        self.masters = QtWidgets.QPushButton(parent=self.jewelry_widget)
        self.masters.setGeometry(QtCore.QRect(40, 392, 452, 121))
        self.masters.setStyleSheet("background-image: url(:/jewelry/masters.png); border: 0;")
        self.masters.setText("")
        self.masters.setObjectName("masters")

        # set button for video and photo
        self.video_photo = QtWidgets.QPushButton(parent=self.jewelry_widget)
        self.video_photo.setGeometry(QtCore.QRect(40, 485, 452, 121))
        self.video_photo.setStyleSheet("background-image: url(:/jewelry/video_photo.png); border: 0;")
        self.video_photo.setText("")
        self.video_photo.setObjectName("video_photo")
        self.video_photo.clicked.connect(self.video_photo_pressed)
        self.video_photo.clicked.connect(self.video_photo_widget.show)
        self.video_photo.clicked.connect(self.photo_gallery_widget.hide)

        # set button for embroidery
        self.embroidery_left = QtWidgets.QPushButton(parent=self.jewelry_widget)
        self.embroidery_left.setGeometry(QtCore.QRect(0, 643, 491, 160))
        self.embroidery_left.setStyleSheet("background-image: url(:/left_menu/embroidery_menu.png); border: 0;")
        self.embroidery_left.setText("")
        self.embroidery_left.setObjectName("embroidery_left")

        # set button for painting
        self.painting_left = QtWidgets.QPushButton(parent=self.jewelry_widget)
        self.painting_left.setGeometry(QtCore.QRect(0, 791, 491, 121))
        self.painting_left.setStyleSheet("background-image: url(:/left_menu/painting_menu.png); border: 0;")
        self.painting_left.setText("")
        self.painting_left.setObjectName("painting_left")

        MyMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MyMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MyMainWindow)

    def show_main_hall(self):
        self.main_hall.show()

    def show_jewelry_widget(self):
        self.jewelry_widget.show()

    def show_video_photo(self):
        self.play_video_state = True
        self.jewelry_content.hide()
        self.video_photo_widget.show()

    def play_video(self):
        self.video_preview.hide()
        self.play_button.hide()
        self.videoWidget.show()
        self.player.videoOutput().show()
        self.player.play()

    def stop_video(self):
        self.play_video_state = False
        self.player.stop()
        self.player.videoOutput().hide()
        self.video_preview.show()
        self.play_button.show()

    def open_gallery(self, photo_index):
        self.video_photo_widget.hide()
        self.current_photo_index = photo_index
        self.photo_viewer = QtWidgets.QLabel(parent=self.photo_gallery_widget)
        gallery_pixmap = QtGui.QPixmap(self.photo_paths[photo_index])
        self.photo_viewer.setStyleSheet("border: 0;")
        self.photo_viewer.setFixedSize(923, 627)
        self.photo_viewer.setGeometry(QtCore.QRect(731, 283, 923, 627))
        self.photo_viewer.setPixmap(gallery_pixmap)
        self.photo_viewer.setAlignment(QtCore.Qt.AlignCenter)
        self.photo_viewer.setText("")
        self.photo_viewer.setObjectName("photo_viewer")
        self.photo_gallery_widget.show()

    def video_photo_pressed(self):
        self.video_photo.setGeometry(QtCore.QRect(64, 508, 452, 121))
        self.video_photo.setStyleSheet("background-image: url(:/jewelry/video_photo_pressed.png);"
                                       "background-repeat: no-repeat; border: 0;")
        self.show_video_photo()
        # self.photo_viewer.deleteLater()
        self.photo_viewer.hide()

    def show_images(self):
        dirname = os.path.dirname(__file__)
        jewelry_photo_common = os.path.join(dirname, 'images/jewelry/photo_common')
        jewelry_photo_common_path = os.path.join(jewelry_photo_common, '*')
        photo_paths = sorted(glob.glob(jewelry_photo_common_path))
        if len(photo_paths) < 4:
            return
        elif self.current_photo_index >= len(photo_paths):
            self.current_photo_index = 0
        elif self.current_photo_index < 0:
            self.current_photo_index = len(photo_paths) - 1

        for i in range(4):
            photo_index = self.current_photo_index + i
            if photo_index >= len(photo_paths):
                photo_index = photo_index - len(photo_paths)
            pixmap = QtGui.QPixmap(photo_paths[photo_index])
            self.photo_widgets[i].setPixmap(pixmap)

    def show_next_photo(self):
        self.current_photo_index += 1
        self.show_images()

    def show_previous_photo(self):
        self.current_photo_index -= 1
        self.show_images()

    def retranslateUi(self, MyMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MyMainWindow.setWindowTitle(_translate("MyMainWindow", "Мстёрский музей"))
