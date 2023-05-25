import glob
import json
import os.path
from PySide6 import QtMultimedia
from PySide6.QtCore import QUrl
from PySide6.QtGui import QFont, QFontDatabase, QColor, QPalette, Qt
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from functools import partial
from PySide6 import QtCore, QtGui, QtWidgets

from current_master_elements import create_current_master_button
from jewelry_masters_buttons import create_jewelry_masters_buttons
from left_menu_buttons import create_masters_button, create_video_photo_button, create_embroidery_button, \
    create_painting_button
from photo_elements import create_left_arrow_button, create_right_arrow_button, create_photo_title, \
    create_left_arrow_button_full, create_right_arrow_button_full, create_photo_previews
from common_elements import create_back_button
from jewelry_widget_elements import create_jewelry_pass, create_jewelry_content, create_jewelry_title_1, \
    create_jewelry_main_text_1, create_jewelry_title_2, create_jewelry_main_text_2
from main_hall_buttons import create_jewelry, create_embroidery, create_painting
from video_elements import create_video_title, create_video_preview, create_play_button


class Ui_MyMainWindow(object):
    play_video_state = False
    current_photo_index = 0
    clicked_photo_index = 0
    indicators = []
    photo_widgets = []
    photo_preview_buttons = []
    photo_preview = None
    jewelry_data = None
    jewelry_master_buttons = []

    dirname = os.path.dirname(__file__)
    jewelry_photo_common = os.path.join(dirname, 'images/jewelry/photo_common')
    jewelry_photo_common_path = os.path.join(jewelry_photo_common, '*')
    jewelry_photo_masters = os.path.join(dirname, 'images/jewelry/photo_masters')
    jewelry_photo_masters_path = os.path.join(jewelry_photo_masters, '*')
    masters_paths = sorted(glob.glob(jewelry_photo_masters_path))
    photo_paths = sorted(glob.glob(jewelry_photo_common_path))
    files_amount = len(glob.glob(jewelry_photo_common_path))

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

        # set main hall buttons
        self.jewelry = create_jewelry(self.main_hall, self.show_jewelry_widget)
        self.embroidery = create_embroidery(self.main_hall, None)
        self.painting = create_painting(self.main_hall, None)

        # set left menu widget
        self.jewelry_widget = QtWidgets.QWidget(parent=self.main_hall)
        self.jewelry_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.jewelry_widget.setStyleSheet("background-image: url(:/jewelry/jewelry_bg.png); border: 0;")
        self.jewelry_widget.setObjectName("jewelry_widget")
        self.jewelry_widget.hide()

        # set inactive button and content for jewelry
        self.jewelry_pass = create_jewelry_pass(self.jewelry_widget, None)
        self.jewelry_content = create_jewelry_content(self.jewelry_widget)

        # set fornt for jewelry content
        with open('texts/jewelry/jewelry_art.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        fontId = QFontDatabase.addApplicationFont(":/fonts/MinionPro-Regular.ttf")
        fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
        # font for title
        self.font_20 = QFont(fontName, 20)
        # font for text
        self.font_16 = QFont(fontName, 16)
        # font for buttons
        self.font_18 = QFont(fontName, 18)
        self.font_24 = QFont(fontName, 24)

        # set text for jewelry content
        self.jewelry_title_1 = create_jewelry_title_1(self.jewelry_content, data, self.font_20)
        self.jewelry_main_text_1 = create_jewelry_main_text_1(self.jewelry_content, data, self.font_16)
        self.jewelry_title_2 = create_jewelry_title_2(self.jewelry_content, data, self.font_20)
        self.jewelry_main_text_2 = create_jewelry_main_text_2(self.jewelry_content, data, self.font_16)

        # set back button
        self.back_button_jewelry_content = create_back_button(self.jewelry_content, None)
        self.back_button_jewelry_content.clicked.connect(self.show_main_hall)
        self.back_button_jewelry_content.clicked.connect(self.jewelry_widget.hide)

        # set widget for video and photo content
        self.video_photo_widget = QtWidgets.QWidget(parent=self.jewelry_widget)
        self.video_photo_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.video_photo_widget.setStyleSheet("background: transparent; border: 0;")
        self.video_photo_widget.setObjectName("video_photo_widget")
        self.video_photo_widget.hide()

        self.back_button_video_photo = create_back_button(self.video_photo_widget, self.back_to_jewelry)
        # self.back_button_video_photo.clicked.connect(self.video_photo_widget.hide)
        # self.back_button_video_photo.clicked.connect(self.jewelry_content.show)

        # set photo title
        self.photo_title = create_photo_title(self.video_photo_widget)

        # set arrow buttons for photo
        self.photo_left_button = create_left_arrow_button(self.video_photo_widget, self.show_previous_photo)
        self.photo_right_button = create_right_arrow_button(self.video_photo_widget, self.show_next_photo)

        # set video title
        self.video_title = create_video_title(self.video_photo_widget)

        # set video preview
        self.video_preview = create_video_preview(self.video_photo_widget)

        # set play button for video
        self.play_button = create_play_button(self.video_photo_widget, self.play_video)

        # video player
        self.player = QMediaPlayer()
        self.player.setSource(QUrl.fromLocalFile("video/mstera_video.mp4"))
        self.videoWidget = QVideoWidget(parent=self.video_photo_widget)
        self.player.setVideoOutput(self.videoWidget)
        self.player.videoOutput().setFixedSize(1920, 1080)
        self.player.videoOutput().move(0, 0)
        self.player.videoOutput().hide()
        self.player.setAudioOutput(QtMultimedia.QAudioOutput(self.videoWidget))

        # photo gallery widget
        self.photo_gallery_widget = QtWidgets.QWidget(parent=self.jewelry_widget)
        self.photo_gallery_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.photo_gallery_widget.setStyleSheet("background: transparent; border: 0;")
        self.photo_gallery_widget.setObjectName("video_photo_widget")
        self.photo_gallery_widget.hide()

        # set elements for photo gallery
        self.back_button_gallery = create_back_button(self.photo_gallery_widget, self.video_photo_pressed)
        self.gallery_left_arrow = create_left_arrow_button_full(self.photo_gallery_widget, self.show_previous_photo)
        self.gallery_right_button = create_right_arrow_button_full(self.photo_gallery_widget, self.show_next_photo)

        # widget for the current photo
        self.photo_viewer = QtWidgets.QLabel(parent=self.photo_gallery_widget)

        # set title for photo gallery
        self.photo_title_main = create_photo_title(self.photo_gallery_widget)

        # set previews for photos
        if self.files_amount <= 4:
            self.photo_left_button.hide()
            self.photo_right_button.hide()

        for i in range(4):
            canvas = create_photo_previews(i, self.files_amount, self.video_photo_widget,
                                           self.jewelry_photo_common_path)[1]
            self.photo_preview = create_photo_previews(i, self.files_amount, self.video_photo_widget,
                                                       self.jewelry_photo_common_path)[0]
            self.photo_preview.setPixmap(canvas)
            self.photo_preview.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.photo_preview.setText("")
            self.photo_preview.setObjectName("photo_preview")
            self.photo_widgets.append(self.photo_preview)

            # set button for photo preview
            self.photo_preview_button = QtWidgets.QPushButton(parent=self.video_photo_widget)
            self.photo_preview_button.setGeometry(QtCore.QRect(630 + i * 290, 705, 264, 211))
            self.photo_preview_button.setStyleSheet("background-image: transparent; border: 0;")
            self.photo_preview_button.setText("")
            self.photo_preview_button.setObjectName("photo_preview_button")
            self.photo_preview_button.clicked.connect(partial(self.change_cliked, i))
            self.photo_preview_buttons.append(self.photo_preview_button)

        # set widget for masters
        self.masters_widget = QtWidgets.QWidget(parent=self.jewelry_widget)
        self.masters_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.masters_widget.setStyleSheet("background: transparent; border: 0;")
        self.masters_widget.setObjectName("masters_widget")
        self.masters_widget.hide()

        self.masters_buttons_widget = QtWidgets.QWidget(parent=self.masters_widget)
        self.masters_buttons_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.masters_buttons_widget.setStyleSheet("background: transparent; border: 0;")
        self.masters_buttons_widget.setObjectName("masters_widget")
        self.masters_buttons_widget.hide()

        self.back_button_jewelry_masters = create_back_button(self.masters_buttons_widget, self.back_to_jewelry)
        self.jewelry_master_buttons = create_jewelry_masters_buttons(self.masters_buttons_widget, self.font_18,
                                                                     self.show_current_master,
                                                                     self.jewelry_master_buttons)[0]
        self.jewelry_data = create_jewelry_masters_buttons(self.masters_buttons_widget, self.font_18,
                                                           self.show_current_master, self.jewelry_master_buttons)[1]

        # set widget for master
        self.current_master = QtWidgets.QWidget(parent=self.masters_widget)
        self.current_master.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.current_master.setStyleSheet("background: transparent; border: 0;")
        self.current_master.setObjectName("masters_widget")
        self.current_master.hide()

        self.back_button_master = create_back_button(self.current_master, self.back_to_masters)

        self.line = QtWidgets.QLabel(parent=self.current_master)
        self.line.setGeometry(QtCore.QRect(1300, 292, 564, 2))
        self.line.setStyleSheet("background-image: url(:/jewelry/line.png); border: 0;")
        self.line.setObjectName("line")

        # buttons for left menu
        self.masters_button = create_masters_button(self.jewelry_widget, self.masters_pressed)
        self.video_photo_button = create_video_photo_button(self.jewelry_widget, self.video_photo_pressed)
        self.embroidery_button = create_embroidery_button(self.jewelry_widget, None)
        self.painting_button = create_painting_button(self.jewelry_widget, None)

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
        for button in self.photo_preview_buttons:
            button.hide()
        self.videoWidget.show()
        self.player.videoOutput().show()
        self.player.play()

    def stop_video(self):
        self.play_video_state = False
        self.player.stop()
        self.player.videoOutput().hide()
        for button in self.photo_preview_buttons:
            button.show()
        self.video_preview.show()
        self.play_button.show()

    def open_gallery(self):
        self.video_photo_widget.hide()
        self.photo_viewer = QtWidgets.QLabel(parent=self.photo_gallery_widget)
        photo_amount = len(self.photo_paths)
        half_photo_amount = photo_amount // 2
        offset = 1180 - half_photo_amount * 32
        if 10 >= photo_amount > 0:
            for i in range(photo_amount):
                indicator = QtWidgets.QLabel(parent=self.photo_gallery_widget)
                indicator.setGeometry(QtCore.QRect(offset + i * 32, 830, 30, 29))
                indicator.setStyleSheet("background-image: url(:/jewelry/indicator.png); border: 0; "
                                        "background-repeat: no-repeat")
                indicator.setText("")
                indicator.setObjectName("indicator")
                self.indicators.append(indicator)

        clicked_index = self.current_photo_index + self.clicked_photo_index
        if clicked_index >= len(self.photo_paths):
            clicked_index = clicked_index - len(self.photo_paths)
        if clicked_index < 0:
            clicked_index = clicked_index + len(self.photo_paths)

        self.indicators[clicked_index].setStyleSheet(
            "background-image: url(:/jewelry/indicator_active.png); border: 0;")

        gallery_pixmap = QtGui.QPixmap(self.photo_paths[clicked_index])
        self.photo_viewer.setStyleSheet("border: 0;")
        self.photo_viewer.setGeometry(QtCore.QRect(731, 283, 923, 627))

        max_width = 923
        max_height = 627
        scaled_pixmap = gallery_pixmap.scaled(max_width, max_height, QtCore.Qt.KeepAspectRatio,
                                              QtCore.Qt.SmoothTransformation)
        self.photo_viewer.setPixmap(scaled_pixmap)

        self.photo_viewer.setAlignment(QtCore.Qt.AlignCenter)
        self.photo_viewer.setText("")
        self.photo_viewer.setObjectName("photo_viewer")
        self.photo_gallery_widget.show()

    def change_cliked(self, clicked_index):
        self.clicked_photo_index = clicked_index
        self.open_gallery()

    def video_photo_pressed(self):
        self.video_photo_button.setGeometry(QtCore.QRect(64, 508, 452, 121))
        self.video_photo_button.setStyleSheet("background-image: url(:/jewelry/video_photo_pressed.png);"
                                              "background-repeat: no-repeat; border: 0;")
        self.masters_button.setGeometry(QtCore.QRect(40, 392, 452, 121))
        self.masters_button.setStyleSheet("background-image: url(:/jewelry/masters.png); border: 0;")
        self.show_video_photo()
        self.photo_viewer.hide()
        self.video_photo_widget.show()
        self.photo_gallery_widget.hide()
        self.masters_widget.hide()

    def masters_pressed(self):
        self.masters_widget.show()
        self.masters_buttons_widget.show()
        self.current_master.hide()
        self.jewelry_content.hide()
        self.video_photo_widget.hide()
        self.photo_gallery_widget.hide()
        self.video_photo_button.setGeometry(QtCore.QRect(40, 485, 452, 121))
        self.video_photo_button.setStyleSheet("background-image: url(:/jewelry/video_photo.png); border: 0;")
        self.masters_button.setGeometry(QtCore.QRect(64, 395, 452, 121))
        self.masters_button.setStyleSheet("background-image: url(:/jewelry/masters_pressed.png); "
                                          "background-repeat: no-repeat")

    def back_to_jewelry(self):
        self.masters_widget.hide()
        self.video_photo_widget.hide()
        self.jewelry_content.show()
        self.video_photo_button.setGeometry(QtCore.QRect(40, 485, 452, 121))
        self.video_photo_button.setStyleSheet("background-image: url(:/jewelry/video_photo.png); border: 0;")
        self.masters_button.setGeometry(QtCore.QRect(40, 392, 452, 121))
        self.masters_button.setStyleSheet("background-image: url(:/jewelry/masters.png); border: 0;")

    def back_to_masters(self):
        self.current_master.hide()
        self.masters_buttons_widget.show()

    def show_images(self):
        photo_paths = sorted(glob.glob(self.jewelry_photo_common_path))
        if self.photo_gallery_widget.isVisible():
            self.photo_paths = photo_paths
            self.video_photo_pressed()
            self.open_gallery()

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

            preview_width = self.photo_widgets[i].width()
            preview_height = self.photo_widgets[i].height()

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

            self.photo_widgets[i].setPixmap(canvas)

    def show_next_photo(self):
        self.current_photo_index += 1
        self.indicators.clear()
        if len(self.photo_paths) < 4:
            return
        elif self.current_photo_index >= len(self.photo_paths):
            self.current_photo_index = 0
        elif self.current_photo_index < 0:
            self.current_photo_index = len(self.photo_paths) - 1
        # new previews
        self.show_images()

    def show_previous_photo(self):
        self.current_photo_index -= 1
        if len(self.photo_paths) < 4:
            return
        elif self.current_photo_index >= len(self.photo_paths):
            self.current_photo_index = 0
        elif self.current_photo_index < 0:
            self.current_photo_index = len(self.photo_paths) - 1
        self.indicators.clear()
        self.show_images()

    def show_current_master(self, index):
        self.masters_buttons_widget.hide()

        self.master_photo_label = create_current_master_button(self.current_master, index, self.jewelry_data)

        if hasattr(self, 'person_name_button'):
            self.person_name_button.deleteLater()

        self.person_name_button = QtWidgets.QPushButton(parent=self.current_master)
        self.person_name_button.setGeometry(QtCore.QRect(633, 240, 596, 110))
        self.person_name_button.setStyleSheet("background-image: url(:/jewelry/person_button.png); border: 0; "
                                              "text-align: center; text-decoration: bold; color: #7c2832;")
        self.person_name_button.setText(self.jewelry_data['persons'][index]['full_name'])
        self.person_name_button.setFont(self.font_24)
        palette = self.person_name_button.palette()
        color = QColor(124, 40, 50)
        palette.setColor(QPalette.ButtonText, color)
        self.person_name_button.setPalette(palette)
        self.person_name_button.setObjectName("person_name_button")

        if hasattr(self, 'master_title'):
            self.master_title.deleteLater()

        self.master_title = QtWidgets.QTextEdit(parent=self.current_master)
        self.master_title.setGeometry(QtCore.QRect(1109, 393, 684, 36))
        self.master_title.setStyleSheet("background: transparent; qproperty-textInteractionFlags: NoTextInteraction;")
        self.master_title.setText(self.jewelry_data['persons'][index]['title'])
        self.master_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.master_title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.master_title.setTextColor(QColor(68, 59, 64))
        self.master_title.setFont(self.font_20)
        self.master_title.setObjectName("master_title")
        self.master_title.setReadOnly(True)

        if hasattr(self, 'master_description'):
            self.master_description.deleteLater()

        self.master_description = QtWidgets.QTextEdit(parent=self.current_master)
        self.master_description.setGeometry(QtCore.QRect(1109, 440, 684, 477))
        self.master_description.setStyleSheet("background: transparent; qproperty-textInteractionFlags: NoTextInteraction;")
        self.master_description.setText(self.jewelry_data['persons'][index]['description'])
        self.master_description.setAlignment(Qt.AlignmentFlag.AlignJustify)
        self.master_description.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.master_description.setTextColor(QColor(68, 59, 64, 1))
        self.master_description.setFont(self.font_16)
        self.master_description.setObjectName("master_description")
        self.master_description.setReadOnly(True)


        self.current_master.show()

    def retranslateUi(self, MyMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MyMainWindow.setWindowTitle(_translate("MyMainWindow", "Мстёрский музей"))
