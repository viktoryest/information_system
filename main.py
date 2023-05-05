import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import images

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("info_sys.ui", None)
window.show()
app.exec()
