import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QListWidget,
    QMainWindow,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["one", "two", "three"])

        widget.currentItemChanged.connect(self.item_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)


    def item_changed(self, i):
        print(i.text())


    def text_changed(self, s):
        print(s)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
