# hex values for the entire app:
# #FB98AD - pinkest pink
# #1D1D1D - charcoal
# #0C0C0C - bruce lee was a god
# #F8567B - i love pink

import sys
import copy

# sys.path.insert(0, "C:\\Users\\hanka\\PycharmProjects\\fitnessapp\\FitnessApp")

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

from FitnessApp.Calisthenics import Calisthenics
from FitnessApp.ExerciseRepetitive import ExerciseRepetitive

from FitnessApp.Exercise import Exercise

# in-between menus navigation
from FitnessApp.ExerciseTimed import ExerciseTimed
from FitnessApp.FreeWeight import FreeWeight
from FitnessApp.Hiit import Hiit
from FitnessApp.Jogging import Jogging
from FitnessApp.Machines import Machines
from FitnessApp.Yoga import Yoga


def go_to_main():
    widget.setCurrentIndex(0)  # main menu


def go_to_browse():
    widget.setCurrentIndex(1)  # browse trainings menu


def go_to_create_training():
    widget.setCurrentIndex(2)  # create new training menu


def go_to_profile():
    widget.setCurrentIndex(3)  # open profile


def go_to_edit():
    widget.setCurrentIndex(10)  # open editing training


def go_to_new_training(training):  # specific windows for all types of training
    if training == "   CALISTHENICS":
        widget.setCurrentIndex(4)
    elif training == "   FREE WEIGHTS":
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
        print("You didn't select training. Try again! :)")


# global variables storing information needed to be shared and accessed between all windows
users_trainings = []
training_to_edit = 0


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainMenu.ui", self)

        print("You are in main menu")

        # ----------- GUI CONTROLS ----------- #

        # navigation from main window to other windows
        self.browse_btn.clicked.connect(go_to_browse)
        self.create_btn.clicked.connect(go_to_create_training)
        self.profile_btn.clicked.connect(go_to_profile)


class BrowseTrainingsWindow(QMainWindow):
    def __init__(self):
        super(BrowseTrainingsWindow, self).__init__()
        loadUi("BrowseTrainingsWindow.ui", self)

        print("You are browsing your trainings")

        self.all_trainings = []
        self.all_exercises = []

        # ----------- GUI CLASS METHODS ----------- #

        # display all user's trainings when the 'refresh' button is pressed
        def show_trainings():
            self.all_trainings.clear()
            self.training_list_collection.clear()  # clear display so as not to duplicate trainings
            for training in users_trainings:
                self.all_trainings.append(training.name)
                self.training_list_collection.addItem(training.name)

        # display all selected training's exercises when the 'show' button is pressed
        def show_trainings_exercise():
            self.exercise_index = self.training_list_collection.currentRow()  # if no training selected, crashes!
            self.exercise = self.training_list_collection.currentItem().text()
            self.training = users_trainings[self.exercise_index]
            self.all_exercises = copy.deepcopy(self.training.exercise_list)  # deep copying exercises for easier access
            self.exercises_panel.clear()  # clear the display so as not to duplicate exercises
            for exer in self.all_exercises:
                print(exer.exercise_type)
                print(exer.sets)
                print(exer.reps)
                # what information is displayed depends on the type of exercise, hence the elif instructions
                if exer.exercise_type == "bw" or exer.exercise_type == "fw" or exer.exercise_type == "mach":
                    self.exercises_panel.addItem(exer.name + "   " +
                                                 str(exer.sets) + "x" + str(exer.reps))
                elif exer.exercise_type == "cardio":
                    if exer.time == 0:
                        self.exercises_panel.addItem(exer.name + "   " + str(exer.distance) + "km")
                    else:
                        self.exercises_panel.addItem(exer.name + "   " + str(exer.time) + "min")
                elif exer.exercise_type == "hiit":
                    self.exercises_panel.addItem(exer.name + "   " +
                                                 str(exer.sets) + "x" + str(exer.time) + "s")
                elif exer.exercise_type == "yoga":
                    self.exercises_panel.addItem(exer.name + "   " +
                                                 str(exer.time) + "min")

        # delete user's training
        def delete_training():
            index = self.training_list_collection.currentRow()
            del users_trainings[index]
            self.exercises_panel.clear()
            self.training_list_collection.takeItem(index)

        def pick_training_to_edit():
            global training_to_edit
            if self.training_list_collection.currentRow() != -1:
                training_to_edit = self.training_list_collection.currentRow()
            else:
                training_to_edit = 0
            print(training_to_edit)
            go_to_edit()

        # ----------- GUI CONTROLS ----------- #

        # navigation via buttons to other windows
        self.main_menu_btn.clicked.connect(go_to_main)
        self.new_training_btn.clicked.connect(go_to_create_training)
        self.edit_training_btn.clicked.connect(pick_training_to_edit)
        # self.edit_training_btn_clicked.connect(go_to_edit)

        # controls for functionalities and features
        self.refresh_btn.clicked.connect(show_trainings)
        self.show_exercise_btn.clicked.connect(show_trainings_exercise)
        self.delete_training_btn.clicked.connect(delete_training)


class CreateNewTraining(QMainWindow):
    def __init__(self):
        super(CreateNewTraining, self).__init__()
        loadUi("CreateNewTraining.ui", self)

        self.what_training = "NO TRAINING SELECTED"

        # ----------- GUI CLASS METHODS ----------- #

        # pick training to create from combo boxes (remember to press the icon)
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

        # ----------- GUI CONTROLS ----------- #

        # controls for functionalities and features
        self.bw_btn.clicked.connect(lambda: set_chosen_training(self.bw_btn))
        self.cardio_btn.clicked.connect(lambda: set_chosen_training(self.cardio_btn))
        self.wl_btn.clicked.connect(lambda: set_chosen_training(self.wl_btn))
        self.mixed_btn.clicked.connect(lambda: set_chosen_training(self.mixed_btn))
        self.next_btn.clicked.connect(lambda: go_to_new_training(self.what_training))

        # navigation via buttons to other windows
        self.main_menu_btn.clicked.connect(go_to_main)


class Profile(QMainWindow):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi("Profile.ui", self)

        # ----------- GUI CONTROLS ----------- #

        self.main_menu_btn.clicked.connect(go_to_main)


class NewCalisthenicsTraining(QMainWindow):
    def __init__(self):
        super(NewCalisthenicsTraining, self).__init__()
        loadUi("NewCalisthenicsTraining.ui", self)

        print("You are creating new calisthenics training!")

        self.reps = 0
        self.sets = 0
        self.training_title = "NEW TRAINING"
        self.exercise_name = "NEW EXERCISE"
        self.exercise_list = []

        # ----------- GUI CLASS METHODS ----------- #

        # add and display exercises
        def add_exercise_to_training():
            self.reps = self.rep_spin.value()
            self.sets = self.set_spin.value()
            if self.exercise_combo.currentIndex() != 0:
                self.exercise_name = self.exercise_combo.currentText()
                self.exercise = ExerciseRepetitive(self.exercise_name, "bw", self.sets, self.reps, 0, 0)
                self.training_list.addItem(self.exercise.name + "   " +
                                           str(self.exercise.sets) + "x" + str(self.exercise.reps))
                self.exercise_list.append(self.exercise)
            else:
                self.exercise_name = "EMPTY EXERCISE"

        # remove previously added exercise
        def remove_exercise_from_training():
            index = self.training_list.currentRow()
            del self.exercise_list[index]
            self.training_list.takeItem(index)

        # create and save prepared training
        def create_training():
            self.training_title = self.training_name.toPlainText()
            self.training = Calisthenics(self.training_title, self.exercise_list)
            users_trainings.append(self.training)

        # ----------- GUI CONTROLS ----------- #

        # controls for functionalities and features
        self.add_btn.clicked.connect(add_exercise_to_training)
        self.create_training_btn.clicked.connect(create_training)
        self.remove_training_btn.clicked.connect(remove_exercise_from_training)

        # navigation via buttons to other windows
        self.back_btn.clicked.connect(go_to_create_training)
        self.browse_btn.clicked.connect(go_to_browse)


class NewFreeWeightTraining(QMainWindow):
    def __init__(self):
        super(NewFreeWeightTraining, self).__init__()
        loadUi("NewFreeWeightTraining.ui", self)

        print("You are creating new free weight training!")

        self.reps = 0
        self.sets = 0
        self.training_title = "NEW TRAINING"
        self.exercise_name = "NEW EXERCISE"
        self.exercise_list = []

        # ----------- GUI CLASS METHODS ----------- #

        # add and display exercises
        def add_exercise_to_training():
            self.reps = self.rep_spin.value()
            print(self.reps)
            self.sets = self.set_spin.value()
            print(self.sets)
            if self.exercise_combo.currentIndex() != 0:
                self.exercise_name = self.exercise_combo.currentText()
                self.exercise = ExerciseRepetitive(self.exercise_name, "fw", self.sets, self.reps, 0, 0)
                self.training_list.addItem(self.exercise.name + "   " +
                                           str(self.exercise.sets) + "x" + str(self.exercise.reps))
                self.exercise_list.append(self.exercise)
            else:
                self.exercise_name = "EMPTY EXERCISE"

        # remove previously added exercise
        def remove_exercise_from_training():
            index = self.training_list.currentRow()
            del self.exercise_list[index]
            self.training_list.takeItem(index)

        # create and save prepared training
        def create_training():
            self.training_title = self.training_name.toPlainText()
            self.training = FreeWeight(self.training_title, self.exercise_list)
            print(self.training.name)
            users_trainings.append(self.training)

        # ----------- GUI CONTROLS ----------- #

        # controls for functionalities and features
        self.add_btn.clicked.connect(add_exercise_to_training)
        self.create_training_btn.clicked.connect(create_training)
        self.remove_training_btn.clicked.connect(remove_exercise_from_training)

        # navigation via buttons to other windows
        self.back_btn.clicked.connect(go_to_create_training)
        self.browse_btn.clicked.connect(go_to_browse)


class NewMachinesTraining(QMainWindow):
    def __init__(self):
        super(NewMachinesTraining, self).__init__()
        loadUi("NewMachinesTraining.ui", self)

        print("You are creating new machines training!")

        self.reps = 0
        self.sets = 0
        self.training_title = "NEW TRAINING"
        self.exercise_name = "NEW EXERCISE"

        self.exercise_list = []

        # ----------- GUI CLASS METHODS ----------- #

        # add and display exercises
        def add_exercise_to_training():
            self.reps = self.rep_spin.value()
            print(self.reps)
            self.sets = self.set_spin.value()
            print(self.sets)
            if self.exercise_combo.currentIndex() != 0:
                self.exercise_name = self.exercise_combo.currentText()
                self.exercise = ExerciseRepetitive(self.exercise_name, "mach", self.sets, self.reps, 0, 0)
                self.training_list.addItem(self.exercise.name + "   " +
                                           str(self.exercise.sets) + "x" + str(self.exercise.reps))
                self.exercise_list.append(self.exercise)
            else:
                self.exercise_name = "EMPTY EXERCISE"

        # remove previously added exercise
        def remove_exercise_from_training():
            index = self.training_list.currentRow()
            del self.exercise_list[index]
            self.training_list.takeItem(index)

        # create and save prepared training
        def create_training():
            self.training_title = self.training_name.toPlainText()
            self.training = Machines(self.training_title, self.exercise_list)
            print(self.training.name)
            users_trainings.append(self.training)

        # ----------- GUI CONTROLS ----------- #

        # controls for functionalities and features
        self.add_btn.clicked.connect(add_exercise_to_training)
        self.create_training_btn.clicked.connect(create_training)
        self.remove_training_btn.clicked.connect(remove_exercise_from_training)

        # navigation via buttons to other windows
        self.back_btn.clicked.connect(go_to_create_training)
        self.browse_btn.clicked.connect(go_to_browse)


class NewJoggingTraining(QMainWindow):
    def __init__(self):
        super(NewJoggingTraining, self).__init__()
        loadUi("NewJoggingTraining.ui", self)

        print("You are creating new free weight training!")

        self.time = 0
        self.distance = 0
        self.training_title = "NEW TRAINING"
        self.exercise_name = "NEW EXERCISE"
        self.exercise_list = []

        # ----------- GUI CLASS METHODS ----------- #

        # add and display exercises
        def add_exercise_to_training():
            self.time = self.min_spin.value()
            print(self.time)
            self.distance = self.kim_spin.value()
            print(self.distance)
            self.exercise_name = "JOGGING"
            if self.by_dist_btn.isChecked():
                self.exercise = ExerciseTimed(self.exercise_name, "cardio", 0, 0, 0, self.distance)
                self.training_list.addItem(self.exercise.name + "   " + str(self.exercise.distance) + "km")
            else:
                self.exercise = ExerciseTimed(self.exercise_name, "cardio", 0, 0, self.time, 0)
                self.training_list.addItem(self.exercise.name + "   " + str(self.exercise.time) + "min")
            self.exercise_list.append(self.exercise)

        # remove previously added exercise
        def remove_exercise_from_training():
            index = self.training_list.currentRow()
            del self.exercise_list[index]
            self.training_list.takeItem(index)

        # create and save prepared training
        def create_training():
            self.training_title = self.training_name.toPlainText()
            self.training = Jogging(self.training_title, self.exercise_list)
            print(self.training.name)
            users_trainings.append(self.training)

        # ----------- GUI CONTROLS ----------- #

        # controls for functionalities and features
        self.add_btn.clicked.connect(add_exercise_to_training)
        self.create_training_btn.clicked.connect(create_training)
        self.remove_training_btn.clicked.connect(remove_exercise_from_training)

        # navigation via buttons to other windows
        self.back_btn.clicked.connect(go_to_create_training)
        self.browse_btn.clicked.connect(go_to_browse)


class NewHiitTraining(QMainWindow):
    def __init__(self):
        super(NewHiitTraining, self).__init__()
        loadUi("NewHiitTraining.ui", self)

        print("You are creating new HIIT training!")

        self.time = 0
        self.sets = 0
        self.training_title = "NEW TRAINING"
        self.exercise_name = "NEW EXERCISE"
        self.exercise_list = []

        # ----------- GUI CLASS METHODS ----------- #

        # add and display exercises
        def add_exercise_to_training():
            self.time = self.secs_spin.value()
            print(self.time)
            self.sets = self.sets_spin.value()
            print(self.sets)
            if self.exercise_combo.currentIndex() != 0:
                self.exercise_name = self.exercise_combo.currentText()
                self.exercise = ExerciseTimed(self.exercise_name, "hiit", self.sets, 0, self.time, 0)
                self.training_list.addItem(self.exercise.name + "   " +
                                           str(self.exercise.sets) + "x" + str(self.exercise.time) + "s")
                self.exercise_list.append(self.exercise)
            else:
                self.exercise_name = "EMPTY EXERCISE"

        # remove previously added exercise
        def remove_exercise_from_training():
            index = self.training_list.currentRow()
            del self.exercise_list[index]
            self.training_list.takeItem(index)

        # create and save prepared training
        def create_training():
            self.training_title = self.training_name.toPlainText()
            self.training = Hiit(self.training_title, self.exercise_list)
            print(self.training.name)
            users_trainings.append(self.training)
            # go_to_browse()

        # ----------- GUI CONTROLS ----------- #

        # controls for functionalities and features
        self.add_btn.clicked.connect(add_exercise_to_training)
        self.create_training_btn.clicked.connect(create_training)
        self.remove_training_btn.clicked.connect(remove_exercise_from_training)

        # navigation via buttons to other windows
        self.back_btn.clicked.connect(go_to_create_training)
        self.browse_btn.clicked.connect(go_to_browse)


class NewYogaTraining(QMainWindow):
    def __init__(self):
        super(NewYogaTraining, self).__init__()
        loadUi("NewYogaTraining.ui", self)

        print("You are creating new yoga training!")

        self.time = 0
        self.training_title = "NEW TRAINING"
        self.exercise_name = "NEW EXERCISE"
        self.exercise_list = []

        # ----------- GUI CLASS METHODS ----------- #

        # add and display exercises
        def add_exercise_to_training():
            self.time = self.min_spin.value()
            print(self.time)
            self.exercise_name = "YOGA"

            self.exercise = ExerciseTimed(self.exercise_name, "yoga", 0, 0, self.time, 0)
            self.training_list.addItem(self.exercise.name + "   " +
                                       str(self.exercise.time) + "min")
            self.exercise_list.append(self.exercise)

        # remove previously added exercise
        def remove_exercise_from_training():
            index = self.training_list.currentRow()
            del self.exercise_list[index]
            self.training_list.takeItem(index)

        # create and save prepared training
        def create_training():
            self.training_title = self.training_name.toPlainText()
            self.training = Yoga(self.training_title, self.exercise_list)
            print(self.training.name)
            users_trainings.append(self.training)

        # ----------- GUI CONTROLS ----------- #

        # controls for functionalities and features
        self.add_btn.clicked.connect(add_exercise_to_training)
        self.create_training_btn.clicked.connect(create_training)
        self.remove_training_btn.clicked.connect(remove_exercise_from_training)

        # navigation via buttons to other windows
        self.back_btn.clicked.connect(go_to_create_training)
        self.browse_btn.clicked.connect(go_to_browse)


class EditTrainingWindow(QMainWindow):
    def __init__(self):
        super(EditTrainingWindow, self).__init__()
        loadUi("EditTrainingWindow.ui", self)

        self.exercise_title = "NEW EXERCISE"
        self.exercise_type = "NO TYPE"
        self.sets = 0
        self.reps = 0
        self.time = 0
        self.distance = 0
        self.training = None

        # ----------- GUI CLASS METHODS ----------- #

        # display all the training's exercises when the 'show' button is pressed
        # 'show' button also refreshes the panel after successfully adding exercises
        def display_exercises():
            self.training = users_trainings[training_to_edit]
            self.all_exercises = copy.deepcopy(self.training.exercise_list)
            self.exercises_panel.clear()  # clear the display so as not to duplicate exercises
            for exer in self.all_exercises:
                print(exer.exercise_type)
                print(exer.sets)
                print(exer.reps)
                # what information is displayed depends on the type of exercise, hence the elif instructions
                if exer.exercise_type == "bw" or exer.exercise_type == "fw" or exer.exercise_type == "mach":
                    self.exercises_panel.addItem(exer.name + "   " +
                                                 str(exer.sets) + "x" + str(exer.reps))
                elif exer.exercise_type == "cardio":
                    if exer.time == 0:
                        self.exercises_panel.addItem(exer.name + "   " + str(exer.distance) + "km")
                    else:
                        self.exercises_panel.addItem(exer.name + "   " + str(exer.time) + "min")
                elif exer.exercise_type == "hiit":
                    self.exercises_panel.addItem(exer.name + "   " +
                                                 str(exer.sets) + "x" + str(exer.time) + "s")
                elif exer.exercise_type == "yoga":
                    self.exercises_panel.addItem(exer.name + "   " +
                                                 str(exer.time) + "min")
            self.training_title.setPlainText(self.training.name)

        # create and add custom exercise to the training being edited
        def create_and_add_exercise():
            self.exercise_title = self.exercise_name.toPlainText()
            if self.new_ex_combo.currentIndex() != 0:
                if self.new_ex_combo.currentText() == "CALISTHENICS":
                    self.exercise_type = "bw"
                    self.reps = self.rep_spin.value()
                    self.sets = self.set_spin.value()
                    self.training.create_exercise(self.exercise_title, self.exercise_type, self.sets, self.reps, 0)
                elif self.new_ex_combo.currentText() == "FREE WEIGHTS":
                    self.exercise_type = "fw"
                    self.reps = self.rep_spin.value()
                    self.sets = self.set_spin.value()
                    self.training.create_exercise(self.exercise_title, self.exercise_type, self.sets, self.reps)
                elif self.new_ex_combo.currentText() == "HIIT":
                    self.exercise_type = "hiit"
                    self.sets = self.set_spin.value()
                    self.time = self.secs_spin.value()
                    self.training.create_exercise(self.exercise_title, self.exercise_type, self.sets, self.time, 0)
                elif self.new_ex_combo.currentText() == "JOGGING":
                    self.exercise_type = "cardio"
                    if self.by_dist_btn.isChecked():
                        self.distance = self.kim_spin.value()
                    else:
                        self.time = self.min_spin.value()
                elif self.new_ex_combo.currentText() == "MACHINES":
                    self.exercise_type = "mach"
                    self.reps = self.rep_spin.value()
                    self.sets = self.set_spin.value()
                elif self.new_ex_combo.currentText() == "YOGA":
                    self.exercise_type = "yoga"
                    self.time = self.min_spin.value()

        def remove_exercise():
            index = self.exercises_panel.currentRow()
            throwaway = self.exercises_panel.currentItem().text()
            self.all_exercises = copy.deepcopy(self.training.exercise_list)
            print(throwaway)
            for exer in self.all_exercises:
                if exer.name == throwaway:
                    index2 = self.all_exercises.index(exer)
                    self.training.remove_exercise(index2)
            for name_ex in self.training.exercise_list:
                print(name_ex.name)
            self.exercises_panel.takeItem(index)

        # ----------- GUI CONTROLS ----------- #

        # controls for functionalities and features
        self.show_exercise_btn.clicked.connect(display_exercises)
        self.add_exercise_btn.clicked.connect(create_and_add_exercise)
        self.remove_exercise_btn.clicked.connect(remove_exercise)


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
edit_training_window = EditTrainingWindow()

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
widget.addWidget(edit_training_window)

widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting the app. Bye bye! :)")
