import sys
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from info_sys import Ui_MyMainWindow
from PySide6.QtGui import QMouseEvent
import images, main_hall, jewelry, left_menu, fonts, embroidery, painting, video


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MyMainWindow()
        self.ui.setupUi(self)
        self.setWindowState(Qt.WindowFullScreen)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            self.setWindowState(Qt.WindowFullScreen)
        elif event.key() == Qt.Key_Escape:
            self.setWindowState(Qt.WindowNoState)
        else:
            super().keyPressEvent(event)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and self.ui.play_video_state:
            self.ui.stop_video()
        elif event.button() == Qt.LeftButton and self.ui.embroidery_play_video_state:
            self.ui.embroidery_stop_video()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

