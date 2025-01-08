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

        self.lwidget = QListWidget()
        self.lwidget.addItems(["one", "two", "three"])
        self.lwidget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)

        #self.lwidget.currentItemChanged.connect(self.item_changed)
        #self.lwidget.currentTextChanged.connect(self.text_changed)
        self.lwidget.selectionModel().selectionChanged.connect(self.selection_changed)

        self.setCentralWidget(self.lwidget)


    def item_changed(self, i):
        print(i.text())


    def selection_changed(self):
        # We get the currently selected items via the widget.
        print("Selected items: ", [item.text() for item in self.lwidget.selectedItems()])

    def text_changed(self, s):
        print(s)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
