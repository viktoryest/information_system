import glob
import json
import os.path
from PySide6 import QtMultimedia
from PySide6.QtCore import QUrl
from PySide6.QtGui import QFont, QFontDatabase, Qt, QColor
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from functools import partial
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QWidget, QScrollBar

from current_artist_elements import create_current_artist_photo, create_current_artist_title, \
    create_current_artist_description, create_paintings_button
from current_embroiderer_elements import create_current_embroiderer_photo, create_current_embroiderer_title, \
    create_current_embroiderer_description
from current_master_elements import create_current_master_button, create_name_button, create_current_master_title, \
    create_current_master_description, create_left_arrow, create_right_arrow
from embroiderers_masters_buttons import create_embroidery_masters_buttons
from embroidery_widget_elements import create_embroiderers_button, create_embroidery_title, create_embroidery_main_text
from jewelry_masters_buttons import create_jewelry_masters_buttons
from left_menu_buttons import create_masters_button, create_video_photo_button, create_embroidery_button, \
    create_painting_button
from painting_master_buttons import create_painting_masters_buttons
from photo_elements import create_left_arrow_button, create_right_arrow_button, create_photo_title, \
    create_left_arrow_button_full, create_right_arrow_button_full, create_photo_previews
from common_elements import create_back_button
from jewelry_widget_elements import create_jewelry_pass, create_jewelry_content, create_jewelry_title_1, \
    create_jewelry_main_text_1, create_jewelry_title_2, create_jewelry_main_text_2
from main_hall_buttons import create_jewelry, create_embroidery, create_painting
from video_elements import create_video_title, create_video_preview, create_play_button


class Ui_MyMainWindow(object):
    play_video_state = False
    embroidery_play_video_state = False
    embroidery_play_buttons = []
    current_photo_index = 0
    clicked_photo_index = 0
    indicators = []
    photo_widgets = []
    photo_preview_buttons = []
    embroidery_preview_buttons = []
    photo_preview = None
    jewelry_data = None
    embroidery_data = None
    jewelry_master_buttons = []
    embroidery_master_buttons = []
    painting_master_buttons = []
    current_master_index = 0
    current_embroiderer_index = 0
    current_artist_index = 0
    painting_index = 0
    with open("texts/painting/artists.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        artists_data = data
    paintings_folder = os.path.abspath(os.path.join
                                        (f"{artists_data['persons'][current_artist_index]['paintings_path']}",
                                            "*"))
    paintings_path = sorted(glob.glob(paintings_folder))

    paintings_widgets = []

    dirname = os.path.dirname(__file__)

    jewelry_photo_common = os.path.join(dirname, 'images/jewelry/photo_common')
    jewelry_photo_common_path = os.path.join(jewelry_photo_common, '*')

    jewelry_photo_masters = os.path.join(dirname, 'images/jewelry/photo_masters')
    jewelry_photo_masters_path = os.path.join(jewelry_photo_masters, '*')

    masters_paths = sorted(glob.glob(jewelry_photo_masters_path))
    photo_paths = sorted(glob.glob(jewelry_photo_common_path))
    files_amount = len(glob.glob(jewelry_photo_common_path))

    embroidery_photo_common = os.path.join(dirname, 'images/embroidery/photo_common')
    embroidery_photo_common_path = os.path.join(embroidery_photo_common, '*')

    embroiderers_photos = os.path.join(dirname, 'images/embroidery/embroiderers_photos')
    embroiderers_photo_path = os.path.join(embroiderers_photos, '*')

    embroiderers_paths = sorted(glob.glob(embroiderers_photo_path))
    embroidery_photo_paths = sorted(glob.glob(embroidery_photo_common_path))
    embroidery_files_amount = len(glob.glob(embroidery_photo_common_path))

    embroidery_photo_widgets = []
    embroidery_current_photo_index = 0
    embroidery_clicked_photo_index = 0

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
        self.embroidery = create_embroidery(self.main_hall, self.show_embroidery_widget)
        self.painting = create_painting(self.main_hall, self.show_painting_widget)

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
        self.font_20_bold = QFont(fontName, 20, QFont.Bold)
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
        self.back_button_jewelry_content = create_back_button(self.jewelry_content, self.show_main_hall)

        # set widget for video and photo content
        self.video_photo_widget = QtWidgets.QWidget(parent=self.jewelry_widget)
        self.video_photo_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.video_photo_widget.setStyleSheet("background: transparent; border: 0;")
        self.video_photo_widget.setObjectName("video_photo_widget")
        self.video_photo_widget.hide()

        # set back button for video and photo content
        self.back_button_video_photo = create_back_button(self.video_photo_widget, self.back_to_jewelry)

        # set photo title
        self.photo_title = create_photo_title(self.video_photo_widget)
        # set arrow buttons for photo
        self.photo_left_button = create_left_arrow_button(self.video_photo_widget, self.show_previous_photo)
        self.photo_right_button = create_right_arrow_button(self.video_photo_widget, self.show_next_photo)

        # set video title
        self.video_title = create_video_title(self.video_photo_widget)
        # set video preview
        self.video_preview = create_video_preview(self.video_photo_widget, 1014, 285, 361, 307,
                                                  'images/jewelry/play_preview.png')
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
                                                                     self.jewelry_master_buttons,
                                                                     self.change_clicked_master)[0]
        self.jewelry_data = create_jewelry_masters_buttons(self.masters_buttons_widget, self.font_18,
                                                           self.jewelry_master_buttons,
                                                           self.change_clicked_master)[1]

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

        self.left_arrow = create_left_arrow(self.current_master, self.show_previous_master)
        self.right_arrow = create_right_arrow(self.current_master, self.show_next_master)

        self.embroidery_widget = QtWidgets.QWidget(parent=self.main_hall)
        self.embroidery_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.embroidery_widget.setStyleSheet("background-image: url(:/embroidery/embroidery_bg.png); border: 0;")
        self.embroidery_widget.setObjectName("embroidery_widget")
        self.embroidery_widget.hide()

        self.embroiderers = QtWidgets.QWidget(parent=self.embroidery_widget)
        self.embroiderers.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.embroiderers.setStyleSheet("background-image: transparent; border: 0;")
        self.embroiderers.setObjectName("embroiderers")
        self.embroiderers.hide()

        self.embroidery_content = QtWidgets.QWidget(parent=self.embroidery_widget)
        self.embroidery_content.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.embroidery_content.setStyleSheet("background-image: transparent; border: 0; "
                                              "qproperty-textInteractionFlags: NoTextInteraction;")
        self.embroidery_content.setObjectName("embroiderers")
        self.embroidery_content.hide()

        self.embroidery_history = QtWidgets.QTextBrowser(self.embroidery_content)
        self.embroidery_history.setGeometry(QtCore.QRect(600, 200, 1200, 700))

        self.embroidery_history.setStyleSheet("QTextEdit {background: transparent; border: 0;} QScrollBar {width: 0;}")
        self.embroidery_history.setTextColor(QColor(73, 64, 69))
        self.embroidery_history.setFont(self.font_18)
        self.embroidery_history.setFontPointSize(18)
        self.embroidery_history.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.embroidery_history.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.embroidery_history.setLineWidth(0)
        self.embroidery_history.setObjectName("embroidery_history")

        with open("texts/embroidery/embroidery_history.html", "r", encoding="utf-8") as file:
            html_text = file.read()
            html_with_color = f'<font color="#494045">{html_text}</font>'
            self.embroidery_history.setHtml(html_with_color)

        self.embroidery_buttons_widget = QtWidgets.QWidget(parent=self.embroiderers)
        self.embroidery_buttons_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.embroidery_buttons_widget.setStyleSheet("background: transparent; border: 0;")
        self.embroidery_buttons_widget.setObjectName("embroidery_buttons_widget")
        self.embroidery_buttons_widget.hide()

        # embroidery masters buttons
        self.embroidery_master_buttons = create_embroidery_masters_buttons(self.embroidery_buttons_widget, self.font_18,
                                                                           self.embroidery_master_buttons,
                                                                           self.change_clicked_embroiderer)[0]
        self.embroidery_data = create_embroidery_masters_buttons(self.embroidery_buttons_widget, self.font_18,
                                                                 self.embroidery_master_buttons,
                                                                 self.change_clicked_embroiderer)[1]

        # embroiderers back button
        self.back_button_embroiderers = create_back_button(self.embroidery_buttons_widget, self.back_to_embroidery)

        # current embroiderer
        self.current_embroiderer = QtWidgets.QWidget(parent=self.embroiderers)
        self.current_embroiderer.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.current_embroiderer.setStyleSheet("background: transparent; border: 0;")
        self.current_embroiderer.setObjectName("current_embroiderer")
        self.current_embroiderer.hide()

        self.current_embroiderer_back_button = create_back_button(self.current_embroiderer, self.back_to_embroiderers)

        self.left_arrow = create_left_arrow(self.current_embroiderer, self.show_previous_embroiderer)
        self.right_arrow = create_right_arrow(self.current_embroiderer, self.show_next_embroiderer)

        self.emb_line = QtWidgets.QLabel(parent=self.current_embroiderer)
        self.emb_line.setGeometry(QtCore.QRect(1300, 292, 564, 2))
        self.emb_line.setStyleSheet("background-image: url(:/jewelry/line.png); border: 0;")
        self.emb_line.setObjectName("emb_line")

        self.embroidery_video_photo = QtWidgets.QWidget(parent=self.embroidery_widget)
        self.embroidery_video_photo.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.embroidery_video_photo.setStyleSheet("background: transparent; border: 0;")
        self.embroidery_video_photo.setObjectName("embroidery_video_photo")
        self.embroidery_video_photo.hide()

        self.embroidery_photo_title = create_photo_title(self.embroidery_video_photo)
        self.photo_left_button = create_left_arrow_button(self.embroidery_video_photo,
                                                          self.embroidery_show_previous_photo)
        self.photo_right_button = create_right_arrow_button(self.embroidery_video_photo,
                                                            self.embroidery_show_next_photo)
        self.embroidery_video_title = create_video_title(self.embroidery_video_photo)

        self.embroidery_video_photo_back_button = create_back_button(self.embroidery_video_photo,
                                                                     self.back_to_embroidery)

        self.embroidery_player = QMediaPlayer()
        self.embroidery_videoWidget = QVideoWidget(parent=self.embroidery_video_photo)
        self.embroidery_player.setVideoOutput(self.embroidery_videoWidget)
        self.embroidery_player.videoOutput().setFixedSize(1920, 1080)
        self.embroidery_player.videoOutput().move(0, 0)
        self.embroidery_player.videoOutput().hide()
        self.embroidery_player.setAudioOutput(QtMultimedia.QAudioOutput(self.embroidery_videoWidget))
        for i in range(1, 4):
            self.embroidery_video_preview = create_video_preview(self.embroidery_video_photo, 290 + i * 361, 285,
                                                                 361, 307,
                                                                 f'images/embroidery/video_previews/preview_{i}.png')
            self.embroidery_play_button = create_play_button(self.embroidery_video_photo,
                                                             partial(self.embroidery_play_video, i))
            self.embroidery_play_button.setGeometry(QtCore.QRect(290 + i * 361, 285, 361, 307))
            self.embroidery_play_buttons.append(self.embroidery_play_button)

        for i in range(4):
            canvas = create_photo_previews(i, self.embroidery_files_amount, self.embroidery_video_photo,
                                           self.embroidery_photo_common_path)[1]
            self.embroidery_photo_preview = \
                create_photo_previews(i, self.embroidery_files_amount, self.embroidery_video_photo,
                                      self.embroidery_photo_common_path)[0]
            self.embroidery_photo_preview.setPixmap(canvas)
            self.embroidery_photo_preview.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.embroidery_photo_preview.setText("")
            self.embroidery_photo_preview.setObjectName("embroidery_photo_preview")
            self.embroidery_photo_widgets.append(self.embroidery_photo_preview)

            # set button for photo preview
            self.embroidery_photo_preview_button = QtWidgets.QPushButton(parent=self.embroidery_video_photo)
            self.embroidery_photo_preview_button.setGeometry(QtCore.QRect(630 + i * 290, 705, 264, 211))
            self.embroidery_photo_preview_button.setStyleSheet("background-image: transparent; border: 0;")
            self.embroidery_photo_preview_button.setText("")
            self.embroidery_photo_preview_button.setObjectName("photo_preview_button")
            self.embroidery_photo_preview_button.clicked.connect(partial(self.embroidery_change_clicked, i))
            self.embroidery_preview_buttons.append(self.embroidery_photo_preview_button)

        # photo gallery widget
        self.embroidery_photo_gallery = QtWidgets.QWidget(parent=self.embroidery_widget)
        self.embroidery_photo_gallery.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.embroidery_photo_gallery.setStyleSheet("background: transparent; border: 0;")
        self.embroidery_photo_gallery.setObjectName("embroidery_photo_gallery")
        self.embroidery_photo_gallery.hide()

        self.back_button_gallery = create_back_button(self.embroidery_photo_gallery,
                                                      self.back_to_embroidery_video_photo)

        self.embroidery_photo_viewer = QtWidgets.QLabel(parent=self.embroidery_photo_gallery)

        self.gallery_left_arrow = create_left_arrow_button_full(self.embroidery_photo_gallery,
                                                                self.embroidery_show_previous_photo)
        self.gallery_right_arrow = create_right_arrow_button_full(self.embroidery_photo_gallery,
                                                                  self.embroidery_show_next_photo)

        self.painting_widget = QtWidgets.QWidget(parent=self.main_hall)
        self.painting_widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.painting_widget.setStyleSheet("background: url(:painting/painting_bg.png);; border: 0;")
        self.painting_widget.setObjectName("painting_widget")
        self.painting_widget.hide()

        self.buttons_on_painting = QtWidgets.QWidget(parent=self.painting_widget)
        self.buttons_on_painting.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.buttons_on_painting.setStyleSheet("background: transparent; border: 0;")
        self.buttons_on_painting.setObjectName("buttons_on_painting")
        self.buttons_on_painting.hide()

        self.painting_buttons_back = create_back_button(self.buttons_on_painting, self.show_main_hall)

        self.painting_master_buttons = create_painting_masters_buttons(self.buttons_on_painting, self.font_18,
                                                                       self.painting_master_buttons,
                                                                       self.change_clicked_artist)[0]
        self.artists_data = create_painting_masters_buttons(self.buttons_on_painting, self.font_18,
                                                            self.painting_master_buttons,
                                                            self.change_clicked_artist)[1]

        self.current_artist = QtWidgets.QWidget(parent=self.painting_widget)
        self.current_artist.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.current_artist.setStyleSheet("background: transparent; border: 0;")
        self.current_artist.setObjectName("current_artist")
        self.current_artist.hide()

        self.current_artist_back_button = create_back_button(self.current_artist, self.show_painting_widget)
        self.current_artist_back_button.setGeometry(QtCore.QRect(1100, 975, 175, 73))

        self.left_arrow = create_left_arrow(self.current_artist, self.show_previous_artist)
        self.right_arrow = create_right_arrow(self.current_artist, self.show_next_artist)

        self.artist_line = QtWidgets.QLabel(parent=self.current_artist)
        self.artist_line.setGeometry(QtCore.QRect(1300, 292, 564, 2))
        self.artist_line.setStyleSheet("background-image: url(:/jewelry/line.png); border: 0;")
        self.artist_line.setObjectName("artist_line")

        self.paintings_gallery = QtWidgets.QWidget(parent=self.painting_widget)
        self.paintings_gallery.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.paintings_gallery.setStyleSheet("background: transparent; border: 0;")
        self.paintings_gallery.setObjectName("paintings_gallery")
        self.paintings_gallery.hide()

        self.painting_left_arrow = create_left_arrow_button_full(self.paintings_gallery,
                                                                 self.show_previous_painting)
        self.painting_right_arrow = create_right_arrow_button_full(self.paintings_gallery,
                                                                   self.show_next_painting)

        self.paintings_gallery_back = create_back_button(self.paintings_gallery, self.show_current_artist)

        self.jewelry_button_on_painting = create_jewelry_pass(self.painting_widget, self.show_jewelry_widget)
        self.jewelry_button_on_painting.setStyleSheet("background-image: url(:/left_menu/jewelry_menu_inactive.png); "
                                                      "border: 0; background-repeat: no-repeat;")
        self.jewelry_button_on_painting.setGeometry(QtCore.QRect(0, 285, 491, 307))

        self.embroidery_button_on_painting = create_embroidery_button(self.painting_widget, self.show_embroidery_content)
        self.embroidery_button_on_painting.setGeometry(QtCore.QRect(0, 440, 491, 150))
        self.painting_on_painting = create_painting_button(self.painting_widget, None)
        self.painting_on_painting.setStyleSheet("background-image: url(:/left_menu/painting_inactive.png); "
                                                "background-repeat: no-repeat;")
        self.painting_on_painting.setGeometry(QtCore.QRect(0, 620, 491, 150))

        # buttons for left menu
        self.masters_button = create_masters_button(self.jewelry_widget, self.masters_pressed)
        self.video_photo_button = create_video_photo_button(self.jewelry_widget, self.video_photo_pressed)
        self.embroidery_button = create_embroidery_button(self.jewelry_widget, self.embroidery_pressed)
        self.painting_button = create_painting_button(self.jewelry_widget, self.show_painting_widget)

        self.jewelry_button_on_embroidery = create_jewelry_pass(self.embroidery_widget, self.show_jewelry_widget)
        self.jewelry_button_on_embroidery.setStyleSheet("background-image: url(:/left_menu/jewelry_menu_inactive.png);"
                                                        " border: 0;")
        self.jewelry_button_on_embroidery.setGeometry(QtCore.QRect(0, 285, 491, 161))

        self.embroidery_button_on_embroidery = create_embroidery_button(self.embroidery_widget,
                                                                        self.show_embroidery_content)
        self.embroidery_button_on_embroidery.setStyleSheet("background-image: "
                                                           "url(:/left_menu/embroidery_menu_active.png); border: 0;")
        self.embroidery_button_on_embroidery.setGeometry(QtCore.QRect(0, 445, 465, 121))
        self.embroiderers_button = create_embroiderers_button(self.embroidery_widget, self.show_embroiderers_buttons)
        self.embroidery_video_photo_button = create_video_photo_button(self.embroidery_widget,
                                                                       self.show_embroidery_video_photo)
        self.embroidery_video_photo_button.setStyleSheet("background-image: url(:/jewelry/video_photo.png); border: 0;"
                                                         "background-repeat: no-repeat;")
        self.embroidery_video_photo_button.setGeometry(QtCore.QRect(40, 645, 452, 130))
        self.embroidery_painting_button = create_painting_button(self.embroidery_widget, self.show_painting_widget)
        self.embroidery_content_back_button = create_back_button(self.embroidery_content, self.show_main_hall)

        MyMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MyMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MyMainWindow)

    def show_main_hall(self):
        self.main_hall.show()
        self.jewelry_widget.hide()
        self.embroidery_widget.hide()
        self.painting_widget.hide()

    def show_jewelry_widget(self):
        self.masters_button.setStyleSheet("background-image: url(:/jewelry/masters.png); border: 0;")
        self.video_photo_button.setStyleSheet("background-image: url(:/jewelry/video_photo.png);"
                                              "background-repeat: no-repeat; border: 0;")
        self.video_photo_button.setGeometry(QtCore.QRect(40, 485, 452, 121))
        self.jewelry_widget.show()
        self.embroidery_widget.hide()
        self.painting_widget.hide()
        self.jewelry_content.show()

    def show_embroidery_widget(self):
        self.embroidery_widget.show()
        self.embroidery_content.show()
        self.painting_widget.hide()

    def show_painting_widget(self):
        self.painting_widget.show()
        self.embroidery_widget.hide()
        self.jewelry_widget.hide()
        self.buttons_on_painting.show()
        self.current_artist.hide()
        self.paintings_gallery.hide()

    def show_embroiderers_buttons(self):
        self.embroiderers_button.setStyleSheet("background-image: url(:/left_menu/embroiderers_active.png); "
                                               "background-repeat: no-repeat; border: 0;")
        self.embroiderers_button.setGeometry(QtCore.QRect(60, 554, 402, 115))
        self.embroidery_video_photo_button.setStyleSheet("background-image: url(:/jewelry/video_photo.png); "
                                                         "border: 0; background-repeat: no-repeat;")
        self.embroidery_video_photo_button.setGeometry(QtCore.QRect(37, 645, 452, 130))
        self.embroidery_content.hide()
        self.embroidery_buttons_widget.show()
        self.embroiderers.show()
        self.current_embroiderer.hide()
        self.embroidery_video_photo.hide()

    def back_to_embroiderers(self):
        self.embroidery_buttons_widget.show()
        self.embroidery_content.hide()
        self.current_embroiderer.hide()

    def show_embroidery_video_photo(self):
        self.embroidery_video_photo_button.setStyleSheet("background-image: url(:/jewelry/video_photo_pressed.png); "
                                                         "border: 0; background-repeat: no-repeat;")
        self.embroidery_video_photo_button.setGeometry(QtCore.QRect(63, 670, 452, 130))
        self.embroiderers_button.setStyleSheet("background-image: url(:/left_menu/embroiderers.png);"
                                               "border: 0; background-repeat: no-repeat;")
        self.embroiderers_button.setGeometry(QtCore.QRect(40, 554, 452, 121))
        self.embroidery_widget.show()
        self.embroidery_video_photo.show()
        self.embroidery_widget.show()
        self.embroidery_buttons_widget.hide()
        self.current_embroiderer.hide()
        self.embroidery_content.hide()
        self.embroidery_photo_gallery.hide()
        self.jewelry_content.hide()

    def show_embroidery_content(self):
        self.embroidery_video_photo_button.setStyleSheet("background-image: url(:/jewelry/video_photo.png); "
                                                         "border: 0; background-repeat: no-repeat;")
        self.embroidery_video_photo_button.setGeometry(QtCore.QRect(37, 645, 452, 130))
        self.embroiderers_button.setStyleSheet("background-image: url(:/left_menu/embroiderers.png);"
                                               "border: 0; background-repeat: no-repeat;")
        self.embroiderers_button.setGeometry(QtCore.QRect(40, 554, 452, 121))
        self.embroidery_content.show()
        self.embroidery_buttons_widget.hide()
        self.embroidery_video_photo.hide()
        self.current_embroiderer.hide()
        self.embroidery_photo_gallery.hide()
        self.jewelry_content.hide()

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

    def embroidery_play_video(self, index):
        self.embroidery_play_video_state = True
        self.embroidery_play_button.hide()
        self.embroidery_video_preview.hide()
        self.embroidery_player.setSource(QUrl.fromLocalFile(f"video/embroidery/video_{index}.mp4"))
        for button in self.embroidery_preview_buttons:
            button.hide()
        for button in self.embroidery_play_buttons:
            button.hide()
        self.embroidery_videoWidget.show()
        self.embroidery_player.videoOutput().show()
        self.embroidery_player.play()

    def stop_video(self):
        self.play_video_state = False
        self.player.stop()
        self.player.videoOutput().hide()
        self.video_preview.show()
        self.play_button.show()

    def embroidery_stop_video(self):
        self.embroidery_play_video_state = False
        self.embroidery_player.stop()
        self.embroidery_player.videoOutput().hide()
        for button in self.embroidery_preview_buttons:
            button.show()
        for button in self.embroidery_play_buttons:
            button.show()

        self.embroidery_video_preview.show()

        self.embroidery_play_button.show()

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

    def embroidery_open_gallery(self):
        self.embroidery_video_photo.hide()
        if hasattr(self, 'embroidery_photo_viewer'):
            self.embroidery_photo_viewer.hide()
        self.embroidery_photo_viewer = QtWidgets.QLabel(parent=self.embroidery_photo_gallery)
        photo_amount = len(self.embroidery_photo_paths)
        half_photo_amount = photo_amount // 2
        offset = 1180 - half_photo_amount * 32
        embroidery_clicked_photo_index = self.embroidery_current_photo_index + self.embroidery_clicked_photo_index
        if embroidery_clicked_photo_index >= len(self.embroidery_photo_paths):
            embroidery_clicked_photo_index = embroidery_clicked_photo_index - len(self.embroidery_photo_paths)
        if embroidery_clicked_photo_index < 0:
            embroidery_clicked_photo_index = embroidery_clicked_photo_index + len(self.embroidery_photo_paths)

        if 10 >= photo_amount > 0:
            for i in range(photo_amount):
                indicator = QtWidgets.QLabel(parent=self.embroidery_photo_gallery)
                indicator.setGeometry(QtCore.QRect(offset + i * 32, 830, 30, 29))
                indicator.setStyleSheet("background-image: url(:/jewelry/indicator.png); border: 0; "
                                        "background-repeat: no-repeat")
                indicator.setText("")
                indicator.setObjectName("indicator")
                self.indicators.append(indicator)

            self.indicators[embroidery_clicked_photo_index].setStyleSheet(
                "background-image: url(:/jewelry/indicator_active.png); border: 0;")

        gallery_pixmap = QtGui.QPixmap(self.embroidery_photo_paths[embroidery_clicked_photo_index])
        self.embroidery_photo_viewer.setStyleSheet("border: 0;")
        self.embroidery_photo_viewer.setGeometry(QtCore.QRect(731, 283, 923, 627))

        max_width = 923
        max_height = 627
        scaled_pixmap = gallery_pixmap.scaled(max_width, max_height, QtCore.Qt.KeepAspectRatio,
                                              QtCore.Qt.SmoothTransformation)

        self.embroidery_photo_viewer.setAlignment(QtCore.Qt.AlignCenter)
        self.embroidery_photo_viewer.setText("")
        self.embroidery_photo_viewer.setPixmap(scaled_pixmap)
        self.embroidery_photo_viewer.setObjectName("embroidery_photo_viewer")

        self.embroidery_photo_viewer.show()
        self.embroidery_photo_gallery.show()

    def change_cliked(self, clicked_index):
        self.clicked_photo_index = clicked_index
        self.open_gallery()

    def embroidery_change_clicked(self, clicked_index):
        self.embroidery_clicked_photo_index = clicked_index
        self.embroidery_open_gallery()

    def back_to_embroidery_video_photo(self):
        self.embroidery_video_photo.show()
        self.embroidery_photo_gallery.hide()
        self.embroidery_photo_viewer.hide()

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

    def embroidery_pressed(self):
        self.jewelry_widget.hide()
        self.masters_widget.hide()
        self.video_photo_widget.hide()
        self.masters_widget.hide()
        self.jewelry_content.hide()
        self.embroidery_video_photo.hide()
        self.embroidery_widget.show()
        self.embroidery_content.show()
        self.embroidery_photo_gallery.hide()
        self.painting_widget.hide()


    def back_to_jewelry(self):
        self.masters_widget.hide()
        self.video_photo_widget.hide()
        self.jewelry_content.show()
        self.jewelry_widget.show()
        self.video_photo_button.setGeometry(QtCore.QRect(40, 485, 452, 121))
        self.video_photo_button.setStyleSheet("background-image: url(:/jewelry/video_photo.png); border: 0;")
        self.masters_button.setGeometry(QtCore.QRect(40, 392, 452, 121))
        self.masters_button.setStyleSheet("background-image: url(:/jewelry/masters.png); border: 0;")

    def back_to_masters(self):
        self.current_master.hide()
        self.masters_buttons_widget.show()

    def back_to_embroidery(self):
        self.embroidery_content.show()
        self.embroidery_widget.show()
        self.embroidery_buttons_widget.hide()
        self.current_embroiderer.hide()
        self.embroidery_video_photo.hide()

    def change_clicked_master(self, master_index):
        self.current_master_index = master_index
        self.show_current_master(self.current_master_index)

    def change_clicked_embroiderer(self, embroiderer_index):
        self.current_embroiderer_index = embroiderer_index
        self.show_current_embroiderer(self.current_embroiderer_index)

    def show_images(self, photo_paths):
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

    def embroidery_show_images(self, embroidery_photo_paths):
        if self.embroidery_photo_gallery.isVisible():
            self.embroidery_photo_paths = embroidery_photo_paths
            self.video_photo_pressed()
            self.embroidery_open_gallery()

        if len(embroidery_photo_paths) < 4:
            return
        elif self.embroidery_current_photo_index >= len(embroidery_photo_paths):
            self.embroidery_current_photo_index = 0
        elif self.embroidery_current_photo_index < 0:
            self.embroidery_current_photo_index = len(embroidery_photo_paths) - 1

        for i in range(4):
            photo_index = self.embroidery_current_photo_index + i
            if photo_index >= len(embroidery_photo_paths):
                photo_index = photo_index - len(embroidery_photo_paths)

            pixmap = QtGui.QPixmap(embroidery_photo_paths[photo_index])

            preview_width = self.embroidery_photo_widgets[i].width()
            preview_height = self.embroidery_photo_widgets[i].height()

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

            self.embroidery_photo_widgets[i].setPixmap(canvas)

    def show_next_photo(self):
        self.current_photo_index += 1
        self.indicators.clear()
        if len(self.photo_paths) < 4:
            return
        elif self.current_photo_index >= len(self.photo_paths):
            self.current_photo_index = 0
        elif self.current_photo_index < 0:
            self.current_photo_index = len(self.photo_paths) - 1
        self.show_images(sorted(glob.glob(self.jewelry_photo_common_path)))

    def embroidery_show_next_photo(self):
        self.embroidery_current_photo_index += 1
        self.indicators.clear()
        if len(self.embroidery_photo_paths) < 4:
            return
        elif self.embroidery_current_photo_index >= len(self.embroidery_photo_paths):
            self.embroidery_current_photo_index = 0
        elif self.embroidery_current_photo_index < 0:
            self.embroidery_current_photo_index = len(self.embroidery_photo_paths) - 1
        self.embroidery_show_images(sorted(glob.glob(self.embroidery_photo_common_path)))

    def show_previous_photo(self):
        self.current_photo_index -= 1
        if len(self.photo_paths) < 4:
            return
        elif self.current_photo_index >= len(self.photo_paths):
            self.current_photo_index = 0
        elif self.current_photo_index < 0:
            self.current_photo_index = len(self.photo_paths) - 1
        self.indicators.clear()
        self.show_images(sorted(glob.glob(self.jewelry_photo_common_path)))

    def embroidery_show_previous_photo(self):
        self.embroidery_current_photo_index -= 1
        if len(self.embroidery_photo_paths) < 4:
            return
        elif self.embroidery_current_photo_index >= len(self.embroidery_photo_paths):
            self.embroidery_current_photo_index = 0
        elif self.embroidery_current_photo_index < 0:
            self.embroidery_current_photo_index = len(self.embroidery_photo_paths) - 1
        self.indicators.clear()
        self.embroidery_show_images(sorted(glob.glob(self.embroidery_photo_common_path)))

    def show_next_master(self):
        if self.current_master_index < len(self.jewelry_data['persons']) - 1:
            self.current_master_index += 1
        else:
            self.current_master_index = 0
        self.show_current_master(self.current_master_index)

    def show_previous_master(self):
        if self.current_master_index > 0:
            self.current_master_index -= 1
        else:
            self.current_master_index = len(self.jewelry_data['persons']) - 1
        self.show_current_master(self.current_master_index)

    def show_next_embroiderer(self):
        if self.current_embroiderer_index < len(self.embroidery_data['persons']) - 1:
            self.current_embroiderer_index += 1
        else:
            self.current_embroiderer_index = 0
        self.show_current_embroiderer(self.current_embroiderer_index)

    def show_previous_embroiderer(self):
        if self.current_embroiderer_index > 0:
            self.current_embroiderer_index -= 1
        else:
            self.current_embroiderer_index = len(self.embroidery_data['persons']) - 1
        self.show_current_embroiderer(self.current_embroiderer_index)

    def show_current_master(self, index):
        self.masters_buttons_widget.hide()

        if hasattr(self, 'master_photo_label'):
            full_path = os.path.abspath(f"{self.jewelry_data['persons'][index]['image']}")
            pixmap = QtGui.QPixmap(full_path)
            pixmap = pixmap.scaledToWidth(413)
            pixmap = pixmap.scaledToHeight(517)
            self.master_photo_label.setPixmap(pixmap)
        else:
            self.master_photo_label = create_current_master_button(self.current_master, index, self.jewelry_data)

        if hasattr(self, 'person_name_button'):
            self.person_name_button.setText(self.jewelry_data['persons'][index]['full_name'])
        else:
            self.person_name_button = create_name_button(self.current_master, index, self.jewelry_data, self.font_24)

        if hasattr(self, 'master_title'):
            self.master_title.setText(self.jewelry_data['persons'][index]['title'])
            self.master_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        else:
            self.master_title = create_current_master_title(self.current_master, index, self.jewelry_data, self.font_20)

        if hasattr(self, 'master_description'):
            self.master_description.setText(self.jewelry_data['persons'][index]['description'])
            self.master_description.setAlignment(Qt.AlignmentFlag.AlignJustify)
        else:
            self.master_description = create_current_master_description(self.current_master, index, self.jewelry_data,
                                                                        self.font_16)

        self.current_master.show()

    def show_current_embroiderer(self, index):
        self.embroidery_buttons_widget.hide()
        self.embroidery_content.hide()

        if hasattr(self, 'embroiderer_photo_label'):
            full_path = os.path.abspath(f"{self.embroidery_data['persons'][index]['image']}")
            pixmap = QtGui.QPixmap(full_path)
            pixmap = pixmap.scaledToWidth(413)
            pixmap = pixmap.scaledToHeight(517)
            self.embroiderer_photo_label.setPixmap(pixmap)
        else:
            self.embroiderer_photo_label = create_current_embroiderer_photo(self.current_embroiderer, index,
                                                                            self.embroidery_data)

        if hasattr(self, 'person_name_button'):
            self.person_name_button.setText(self.embroidery_data['persons'][index]['full_name'])
        else:
            self.person_name_button = create_name_button(self.current_embroiderer, index, self.embroidery_data,
                                                         self.font_24)

        if hasattr(self, 'embroiderer_title'):
            self.embroiderer_title.setText(self.embroidery_data['persons'][index]['title'])
            self.embroiderer_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        else:
            self.embroiderer_title = create_current_embroiderer_title(self.current_embroiderer, index,
                                                                      self.embroidery_data, self.font_20)

        if hasattr(self, 'embroiderer_description'):
            self.embroiderer_description.setText(self.embroidery_data['persons'][index]['description'])
            self.embroiderer_description.setAlignment(Qt.AlignmentFlag.AlignJustify)
        else:
            self.embroiderer_description = create_current_embroiderer_description(self.current_embroiderer, index,
                                                                                  self.embroidery_data, self.font_16)

        self.current_embroiderer.show()

    def change_clicked_artist(self, artist_index):
        self.current_artist_index = artist_index
        self.show_current_artist(self.current_artist_index)

    def show_current_artist(self, index):
        index = self.current_artist_index

        self.paintings_gallery.hide()
        self.buttons_on_painting.hide()
        no_photo = self.artists_data['persons'][index]['image'] == 'No photo'

        if hasattr(self, 'artist_photo_label'):
            full_path = os.path.abspath(f"{self.artists_data['persons'][index]['image']}")
            pixmap = QtGui.QPixmap(full_path)
            pixmap = pixmap.scaledToWidth(413)
            pixmap = pixmap.scaledToHeight(517)
            self.artist_photo_label.setPixmap(pixmap)
        else:
            self.artist_photo_label = create_current_artist_photo(self.current_artist, index,
                                                                  self.artists_data)

        if hasattr(self, 'artist_name_button'):
            self.artist_name_button.setText(self.artists_data['persons'][index]['full_name'])
        else:
            self.artist_name_button = create_name_button(self.current_artist, index, self.artists_data,
                                                         self.font_24)

        if hasattr(self, 'artist_title'):
            if no_photo:
                self.artist_title.setGeometry(580, 380, 1220, 36)
                self.artist_title.setText(self.artists_data['persons'][index]['title'])
                self.artist_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            else:
                self.artist_title.setGeometry(1109, 393, 684, 36)
                self.artist_title.setText(self.artists_data['persons'][index]['title'])
                self.artist_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        else:
            if no_photo:
                self.artist_title = create_current_artist_title(self.current_artist, index,
                                                                self.artists_data, self.font_20_bold,
                                                                580, 380, 1220, 36)
            else:
                self.artist_title = create_current_artist_title(self.current_artist, index,
                                                                self.artists_data, self.font_20_bold,
                                                                1109, 393, 684, 36)

        if hasattr(self, 'artist_description'):
            if no_photo:
                self.artist_description.setGeometry(580, 440, 1220, 350)
            else:
                self.artist_description.setGeometry(1109, 440, 684, 350)
            self.artist_description.setText(self.artists_data['persons'][index]['description'])
            self.artist_description.setAlignment(Qt.AlignmentFlag.AlignJustify)
        else:
            if no_photo:
                self.artist_description = create_current_artist_description(self.current_artist, index,
                                                                            self.artists_data, self.font_16,
                                                                            580, 440, 1220, 350)
            else:
                self.artist_description = create_current_artist_description(self.current_artist, index,
                                                                            self.artists_data, self.font_16,
                                                                            1109, 440, 684, 350)
        if hasattr(self, 'paintings_button'):
            if no_photo:
                self.paintings_button.setGeometry(990, 800, 402, 106)
            else:
                self.paintings_button.setGeometry(1250, 800, 402, 106)
        else:
            if no_photo:
                self.paintings_button = create_paintings_button(self.current_artist, self.show_paintings_gallery,
                                                                990, 800, 402, 106)
            else:
                self.paintings_button = create_paintings_button(self.current_artist, self.show_paintings_gallery,
                                                                1250, 800, 402, 106)

        self.current_artist.show()

    def show_paintings_gallery(self):
        self.current_artist.hide()
        if not self.paintings_gallery.isVisible():
            self.painting_index = 0

        paintings_folder = os.path.abspath(os.path.join
                                        (f"{self.artists_data['persons'][self.current_artist_index]['paintings_path']}",
                                            "*"))
        paintings_path = sorted(glob.glob(paintings_folder))

        if hasattr(self, 'painting_viewer'):
            gallery_pixmap = QtGui.QPixmap(paintings_path[self.painting_index])
            self.painting_viewer.setPixmap(gallery_pixmap)
            self.painting_viewer.setStyleSheet("border: 0;")

            max_width = 923
            max_height = 627
            scaled_pixmap = gallery_pixmap.scaled(max_width, max_height, QtCore.Qt.KeepAspectRatio,
                                                  QtCore.Qt.SmoothTransformation)
            self.painting_viewer.setPixmap(scaled_pixmap)
            x_offset = (923 - scaled_pixmap.width()) / 2
            y_offset = (627 - scaled_pixmap.height()) / 2

            self.painting_viewer.setObjectName("painting_viewer")
            self.painting_viewer.setGeometry(QtCore.QRect(731 + x_offset, 283 + y_offset, 923, 627))
            self.paintings_widgets.append(self.painting_viewer)
        else:
            self.painting_viewer = QtWidgets.QLabel(parent=self.paintings_gallery)
            gallery_pixmap = QtGui.QPixmap(paintings_path[self.painting_index])
            self.painting_viewer.setStyleSheet("border: 0;")

            max_width = 923
            max_height = 627
            scaled_pixmap = gallery_pixmap.scaled(max_width, max_height, QtCore.Qt.KeepAspectRatio,
                                                  QtCore.Qt.SmoothTransformation)
            self.painting_viewer.setPixmap(scaled_pixmap)
            x_offset = (923 - scaled_pixmap.width()) / 2
            y_offset = (627 - scaled_pixmap.height()) / 2

            self.painting_viewer.setObjectName("painting_viewer")
            self.painting_viewer.setGeometry(QtCore.QRect(731 + x_offset, 283 + y_offset, 923, 627))
            self.paintings_widgets.append(self.painting_viewer)

        if hasattr(self, "painting_title"):
            print('hasattr')
            self.painting_title.setStyleSheet("background: transparent; border: 0; "
                                              "qproperty-textInteractionFlags: NoTextInteraction;")
            self.painting_title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.painting_title.setGeometry(QtCore.QRect(700, 200, 1000, 36))
            self.painting_title.setText(paintings_path[self.painting_index].split('\\')[-1].split('.')[0])
            self.painting_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            self.painting_title.setTextColor(QColor(73, 64, 69))
            self.painting_title.setFont(self.font_20)
            self.painting_title.setObjectName("painting_title")

        else:
            print('no attr')
            self.painting_title = QtWidgets.QTextEdit(self.paintings_gallery)
            self.painting_title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.painting_title.setGeometry(QtCore.QRect(700, 200, 1000, 36))
            self.painting_title.setText(paintings_path[self.painting_index].split('\\')[-1].split('.')[0])
            self.painting_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            self.painting_title.setTextColor(QColor(73, 64, 69))
            self.painting_title.setFont(self.font_20)
            self.painting_title.setObjectName("painting_title")
            self.painting_title.setStyleSheet("background: transparent; border: 0; "
                                              "qproperty-textInteractionFlags: NoTextInteraction;")

        self.painting_left_arrow = create_left_arrow_button_full(self.paintings_gallery, self.show_previous_painting)
        self.painting_right_arrow = create_right_arrow_button_full(self.paintings_gallery, self.show_next_painting)




            # photo_amount = len(paintings_path)
            # half_photo_amount = photo_amount // 2
            # offset = 1420 - half_photo_amount * 32
            # if 10 >= photo_amount > 0:
            #     for i in range(photo_amount):
            #         indicator = QtWidgets.QLabel(parent=self.paintings_gallery)
            #         indicator.setGeometry(QtCore.QRect(offset + i * 32, 830, 30, 29))
            #         indicator.setStyleSheet("background-image: url(:/jewelry/indicator.png); border: 0; "
            #                                 "background-repeat: no-repeat")
            #         indicator.setText("")
            #         indicator.setObjectName("indicator")
            #         self.indicators.append(indicator)
            #
            # self.indicators[self.painting_index].setStyleSheet(
            #     "background-image: url(:/jewelry/indicator_active.png); border: 0;")

        self.paintings_gallery.show()

    def show_previous_artist(self):
        if self.current_artist_index > 0:
            self.current_artist_index -= 1
        else:
            self.current_artist_index = len(self.artists_data['persons']) - 1
        self.show_current_artist(self.current_artist_index)

    def show_next_artist(self):
        if self.current_artist_index < len(self.artists_data['persons']) - 1:
            self.current_artist_index += 1
        else:
            self.current_artist_index = 0
        self.show_current_artist(self.current_artist_index)

    def show_previous_painting(self):
        paintings_folder = os.path.abspath(os.path.join
                                           (f"{self.artists_data['persons'][self.current_artist_index]['paintings_path']}",
                                            "*"))
        paintings_path = sorted(glob.glob(paintings_folder))
        current_folder_length = len(paintings_path)
        if self.painting_index < 0:
            self.painting_index = current_folder_length - 1
        else:
            self.painting_index -= 1
        self.show_paintings_gallery()

    def show_next_painting(self):
        paintings_folder = os.path.abspath(os.path.join
                                           (f"{self.artists_data['persons'][self.current_artist_index]['paintings_path']}",
                                            "*"))
        paintings_path = sorted(glob.glob(paintings_folder))
        current_folder_length = len(paintings_path)

        if self.painting_index >= current_folder_length - 1:
            self.painting_index = 0
        else:
            self.painting_index += 1
        self.show_paintings_gallery()


    def retranslateUi(self, MyMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MyMainWindow.setWindowTitle(_translate("MyMainWindow", "Мстёрский музей"))
