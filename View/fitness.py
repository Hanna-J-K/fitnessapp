# hex values for the entire app:
# #FB98AD - pinkest pink
# #1D1D1D - charcoal
# #0C0C0C - bruce lee was a god
# #F8567B - i love pink

import sys

# sys.path.insert(0, "C:\\Users\\hanka\\PycharmProjects\\fitnessapp\\FitnessApp")

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

from FitnessApp.Calisthenics import Calisthenics

from FitnessApp.Exercise import Exercise


# in-between menus navigation


def go_to_main():
    widget.setCurrentIndex(0)  # main menu


def go_to_browse():
    widget.setCurrentIndex(1)  # browse trainings menu


def go_to_create_training():
    widget.setCurrentIndex(2)  # create new training menu


def go_to_profile():
    widget.setCurrentIndex(3)  # open profile


def go_to_new_training(training):
    if training == "   CALISTHENICS":
        widget.setCurrentIndex(4)
    elif training == "   FREE WEIGHT":
        widget.setCurrentIndex(5)
    elif training == "   MACHINES":
        widget.setCurrentIndex(6)
    elif training == "   JOGGING":
        widget.setCurrentIndex(7)
    elif training == "   HIIT":
        widget.setCurrentIndex(8)
    elif training == "   YOGA":
        widget.setCurrentIndex(9)
    else:
        widget.setCurrentIndex(0)
        print(training)
        print("LALALALLA")


# def print_json():
#     clst.Calisthenics(20, 5)
#     clst.Calisthenics.encode_calisthenics(clst.Calisthenics)
#     calisthenics1_json = json.dumps(calisthenics1)
#     print(calisthenics1_json)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainMenu.ui", self)
        print(sys.path)
        self.browse_btn.clicked.connect(go_to_browse)
        self.create_btn.clicked.connect(go_to_create_training)
        self.profile_btn.clicked.connect(go_to_profile)
        # self.create_btn.clicked.connect(print_json())


class BrowseTrainingsWindow(QMainWindow):
    def __init__(self):
        super(BrowseTrainingsWindow, self).__init__()
        loadUi("BrowseTrainingsWindow.ui", self)
        self.main_menu_btn.clicked.connect(go_to_main)
        self.new_training_btn.clicked.connect(go_to_create_training)


class CreateNewTraining(QMainWindow):
    def __init__(self):
        super(CreateNewTraining, self).__init__()
        loadUi("CreateNewTraining.ui", self)
        self.main_menu_btn.clicked.connect(go_to_main)

        self.what_training = "eh"

        def set_chosen_training(btn):
            if btn == self.bw_btn:
                if self.bw_combo.currentIndex() != 0:
                    self.chosen_training_label.setText(self.bw_combo.currentText())
                    self.chosen_type_label.setText("Body Weight")
                    self.what_training = self.bw_combo.currentText()
                    print(self.what_training)
                else:
                    self.chosen_type_label.setText("Body Weight")
                    self.chosen_training_label.setText("Pick bodyweight training type above!")
            elif btn == self.wl_btn:
                if self.wl_combo.currentIndex() != 0:
                    self.chosen_training_label.setText(self.wl_combo.currentText())
                    self.chosen_type_label.setText("Weight Lifting")
                    self.what_training = self.wl_combo.currentText()
                    print(self.what_training)
                else:
                    self.chosen_type_label.setText("Weight Lifting")
                    self.chosen_training_label.setText("Pick weight lifting training type above!")
            elif btn == self.cardio_btn:
                if self.cardio_combo.currentIndex() != 0:
                    self.chosen_training_label.setText(self.cardio_combo.currentText())
                    self.chosen_type_label.setText("Cardio")
                    self.what_training = self.cardio_combo.currentText()
                    print(self.what_training)
                else:
                    self.chosen_type_label.setText("Cardio")
                    self.chosen_training_label.setText("Pick cardio training type above!")
            elif btn == self.mixed_btn:
                self.chosen_training_label.setText(self.mixed_combo.currentText())
                self.chosen_type_label.setText("Mixed")
                self.what_training = self.mixed_combo.currentText()
                print(self.what_training)

        self.bw_btn.clicked.connect(lambda: set_chosen_training(self.bw_btn))
        self.cardio_btn.clicked.connect(lambda: set_chosen_training(self.cardio_btn))
        self.wl_btn.clicked.connect(lambda: set_chosen_training(self.wl_btn))
        self.mixed_btn.clicked.connect(lambda: set_chosen_training(self.mixed_btn))

        self.next_btn.clicked.connect(lambda: go_to_new_training(self.what_training))


class Profile(QMainWindow):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi("Profile.ui", self)
        self.main_menu_btn.clicked.connect(go_to_main)


class NewCalisthenicsTraining(QMainWindow):
    def __init__(self):
        super(NewCalisthenicsTraining, self).__init__()
        loadUi("NewCalisthenicsTraining.ui", self)

        self.reps = 0
        self.sets = 0
        self.name = "eh2"

        def sets_and_reps():
            self.reps = self.rep_spin.value()
            self.sets = self.set_spin.value()
            self.name = self.training_name.text()

        self.add_btn.clicked.connect(sets_and_reps)

        self.training = Calisthenics(self.reps, self.sets, self.name)
        #
        self.create_training_btn.clicked.connect(lambda: print(self.reps))


class NewFreeWeightTraining(QMainWindow):
    def __init__(self):
        super(NewFreeWeightTraining, self).__init__()
        loadUi("NewFreeWeightTraining.ui", self)


class NewMachinesTraining(QMainWindow):
    def __init__(self):
        super(NewMachinesTraining, self).__init__()
        loadUi("NewMachinesTraining.ui", self)


class NewJoggingTraining(QMainWindow):
    def __init__(self):
        super(NewJoggingTraining, self).__init__()
        loadUi("NewJoggingTraining.ui", self)


class NewHiitTraining(QMainWindow):
    def __init__(self):
        super(NewHiitTraining, self).__init__()
        loadUi("NewHiitTraining.ui", self)


class NewYogaTraining(QMainWindow):
    def __init__(self):
        super(NewYogaTraining, self).__init__()
        loadUi("NewYogaTraining.ui", self)


# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

main_window = MainWindow()
browse_window = BrowseTrainingsWindow()
create_training_window = CreateNewTraining()
profile_window = Profile()
new_calisthenics_window = NewCalisthenicsTraining()
new_fw_window = NewFreeWeightTraining()
new_machines_window = NewMachinesTraining()
new_jogging_window = NewJoggingTraining()
new_hiit_window = NewHiitTraining()
new_yoga_window = NewYogaTraining()

# add to list of widgets to switch between windows
widget.addWidget(main_window)
widget.addWidget(browse_window)
widget.addWidget(create_training_window)
widget.addWidget(profile_window)
widget.addWidget(new_calisthenics_window)
widget.addWidget(new_fw_window)
widget.addWidget(new_machines_window)
widget.addWidget(new_jogging_window)
widget.addWidget(new_hiit_window)
widget.addWidget(new_yoga_window)

widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting the app. Bye bye! :)")
