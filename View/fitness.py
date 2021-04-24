# hex values for the entire app:
# #FB98AD - pinkest pink
# #1D1D1D - charcoal
# #0C0C0C - bruce lee was a god
# #F8567B - i love pink

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

# in-between menus navigation


def goToMain():
    widget.setCurrentIndex(0)  # main menu


def goToBrowse():
    widget.setCurrentIndex(1)  # browse trainings menu


def goToCreateTraining():
    widget.setCurrentIndex(2)  # create new training menu


def goToProfile():
    widget.setCurrentIndex(3)  # open profile


# def print_json():
#     clst.Calisthenics(20, 5)
#     clst.Calisthenics.encode_calisthenics(clst.Calisthenics)
#     calisthenics1_json = json.dumps(calisthenics1)
#     print(calisthenics1_json)



class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainMenu.ui", self)
        self.browse_btn.clicked.connect(goToBrowse)
        self.create_btn.clicked.connect(goToCreateTraining)
        self.profile_btn.clicked.connect(goToProfile)
        # self.create_btn.clicked.connect(print_json())


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

        def set_chosen_training(btn):
            if btn == self.bw_btn:
                if self.bw_combo.currentIndex() != 0:
                    self.chosen_training_label.setText(self.bw_combo.currentText())
                    self.chosen_type_label.setText("Body Weight")
                else:
                    self.chosen_type_label.setText("Body Weight")
                    self.chosen_training_label.setText("Pick bodyweight training type above!")
            elif btn == self.wl_btn:
                if self.wl_combo.currentIndex() != 0:
                    self.chosen_training_label.setText(self.wl_combo.currentText())
                    self.chosen_type_label.setText("Weight Lifting")
                else:
                    self.chosen_type_label.setText("Weight Lifting")
                    self.chosen_training_label.setText("Pick weight lifting training type above!")
            elif btn == self.cardio_btn:
                if self.cardio_combo.currentIndex() != 0:
                    self.chosen_training_label.setText(self.cardio_combo.currentText())
                    self.chosen_type_label.setText("Cardio")
                else:
                    self.chosen_type_label.setText("Cardio")
                    self.chosen_training_label.setText("Pick cardio training type above!")
            elif btn == self.mixed_btn:
                self.chosen_training_label.setText(self.mixed_combo.currentText())
                self.chosen_type_label.setText("Mixed")

        self.bw_btn.clicked.connect(lambda: set_chosen_training(self.bw_btn))
        self.cardio_btn.clicked.connect(lambda: set_chosen_training(self.cardio_btn))
        self.wl_btn.clicked.connect(lambda: set_chosen_training(self.wl_btn))
        self.mixed_btn.clicked.connect(lambda: set_chosen_training(self.mixed_btn))


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