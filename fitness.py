import sys

from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        window = QtWidgets.QMainWindow()
        window.show()

        sys.exit(app.exec())


main = MainWindow()