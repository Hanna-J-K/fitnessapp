# hex values for the entire app:
# #FB98AD - pinkest pink
# #1D1D1D - charcoal
# #0C0C0C - bruce lee was a god
# #F8567B - i love pink

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow


# in-between menus navigation
def goToMain():
    widget.setCurrentIndex(0) # main menu

def goToBrowse():
    widget.setCurrentIndex(1) # browse trainings menu

def goToCreateTraining():
    widget.setCurrentIndex(2) # create new training menu

def goToProfile():
    widget.setCurrentIndex(3) # open profile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainMenu.ui", self)
        self.browse_btn.clicked.connect(goToBrowse)
        self.create_btn.clicked.connect(goToCreateTraining)
        self.profile_btn.clicked.connect(goToProfile)

class BrowseTrainingsWindow(QMainWindow):
    def __init__(self):
        super(BrowseTrainingsWindow, self).__init__()
        loadUi("BrowseTrainingsWindow.ui", self)
        self.main_menu_btn.clicked.connect(goToMain)
        self.new_training_btn.clicked.connect(goToCreateTraining)

class CreateNewTraining(QMainWindow):
    def __init__(self):
        super(CreateNewTraining, self).__init__()
        loadUi("CreateNewTraining.ui", self)
        self.main_menu_btn.clicked.connect(goToMain)

class Profile(QMainWindow):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi("Profile.ui", self)
        self.main_menu_btn.clicked.connect(goToMain)


# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

main_window = MainWindow()
browse_window = BrowseTrainingsWindow()
create_training_window = CreateNewTraining()
profile_window = Profile()

# add to list of widgets to switch between windows
widget.addWidget(main_window)
widget.addWidget(browse_window)
widget.addWidget(create_training_window)
widget.addWidget(profile_window)


widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()



try:
    sys.exit(app.exec_())
except:
    print("Exiting the app. Bye bye! :)")