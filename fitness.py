# hex values for the entire app:
# #FB98AD - pinkest pink
# #1D1D1D - charcoal
# #0C0C0C - bruce lee was a god
# #F8567B - i love pink

import sys

from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        window = QtWidgets.QMainWindow()
        self.initGui(window)

        window.show()
        window.setWindowTitle("Fitness App")
        window.setGeometry(1000, 250, 600, 800)
        window.setStyleSheet("background-color: #1D1D1D")

        sys.exit(app.exec())

    def initGui(self, window):
        user_btn = QtWidgets.QPushButton("LOGIN", window)
        user_btn.setGeometry(225, 600, 100, 50)
        user_btn.setStyleSheet("background-color: #1D1D1D; color: #FB98AD; border: 5px solid #FB98AD")

main = MainWindow()