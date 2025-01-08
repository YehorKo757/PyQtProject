import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QMainWindow,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.setEditable(True)
        widget.addItems(["one", "two", "three"])
        widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        # Limit the number of items allowed to 10
        widget.setMaxCount(10)

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)


    def index_changed(self, i):
        print(i)


    def text_changed(self, s):
        print(s)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
