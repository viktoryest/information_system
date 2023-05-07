import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from info_sys import Ui_MyMainWindow
import images


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MyMainWindow()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

