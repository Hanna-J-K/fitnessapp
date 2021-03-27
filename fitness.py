# hex values for the entire app:
# #FB98AD - pinkest pink
# #1D1D1D - charcoal
# #0C0C0C - bruce lee was a god
# #F8567B - i love pink

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

def goToMain():
    widget.setCurrentIndex(0)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainMenu.ui", self)
        self.browse_btn.clicked.connect(self.goToBrowse)

    def goToBrowse(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class BrowseTrainingsWindow(QMainWindow):
    def __init__(self):
        super(BrowseTrainingsWindow, self).__init__()
        loadUi("BrowseTrainingsWindow.ui", self)
        self.main_menu_btn.clicked.connect(goToMain)
    


# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
main_window = MainWindow()
browse_window = BrowseTrainingsWindow()
widget.addWidget(main_window)
widget.addWidget(browse_window)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Something went wrong. Exiting...")