import sys
from PySide6.QtGui import QKeySequence, Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from info_sys import Ui_MyMainWindow
import images


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MyMainWindow()
        self.ui.setupUi(self)
        # self.setWindowState(Qt.WindowFullScreen)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            self.setWindowState(Qt.WindowFullScreen)
        elif event.key() == Qt.Key_Escape:
            self.setWindowState(Qt.WindowNoState)
        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

