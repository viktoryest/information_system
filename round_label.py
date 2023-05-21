from PySide6 import QtWidgets, QtGui, QtCore


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
        if not pixmap.isNull():
            size = pixmap.size()
            scaled_size = self.size().scaled(size, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            pixmap = pixmap.scaled(scaled_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        super().setPixmap(pixmap)
        self.setScaledContents(True)
