import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QSlider,
    QMainWindow,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSlider()
        # Orientation:
        # widget = QSlider(Qt.Orientation.Vertical) or
        # widget = QSlider(Qt.Orientation.Horizontal

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10, 3)

        widget.setSingleStep(3)  # Or: 0.5 for QDoubleSpinBox

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)


    def value_changed(self, i):
        print(i)


    def slider_position(self, p):
        print("position", p)


    def slider_pressed(self):
        print("Pressed!")


    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
