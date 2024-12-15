import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QProgressBar


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QProgressBar Example")
        self.resize(400, 600)
        
        # Main widget and layout
        main_widget = QWidget(self)
        self.layuot = QVBoxLayout()  # Corrected the typo: 'layuot' to 'layuot'

        # Create the progress bar
        self.progressbar = QProgressBar(self)
        self.progressbar.setRange(0, 100)
        self.progressbar.setValue(0)
        self.progressbar.setTextVisible(True)

        # Create the button
        self.button = QPushButton("Click me", self)
        self.button.clicked.connect(self.on_clicked)

        # Timer for updating progress
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

        self.progress_value = 0  # Initial progress value

        # Add widgets to layout
        self.layuot.addWidget(self.progressbar, alignment=Qt.AlignCenter)
        self.layuot.addWidget(self.button, alignment=Qt.AlignCenter)

        # Set the layout to the main widget
        main_widget.setLayout(self.layuot)
        self.setCentralWidget(main_widget)

    def on_clicked(self):
        self.button.setDisabled(True)  # Disable the button when clicked
        self.timer.start(1000)  # Start the timer to update the progress bar

    def update_progress(self):
        self.progress_value += 25
        self.progressbar.setValue(self.progress_value)

        if self.progress_value >= 100:
            self.timer.stop()  # Stop the timer when progress reaches 100
            self.button.setEnabled(False)  # Disable the button

            # Create and add the new label
            new_label = QLabel("Program is completed")
            new_label.setAlignment(Qt.AlignCenter)  # Optionally center-align the label
            self.layuot.addWidget(new_label, alignment=Qt.AlignCenter)
            self.layuot.update()  # Update the layout to reflect the change


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
