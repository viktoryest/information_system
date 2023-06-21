from PySide6.QtGui import QFontDatabase, QFont


def get_font(size, param=None):
    fontId = QFontDatabase.addApplicationFont(":/fonts/MinionPro-Regular.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
    if param:
        return QFont(fontName, size, param)
    else:
        return QFont(fontName, size)
