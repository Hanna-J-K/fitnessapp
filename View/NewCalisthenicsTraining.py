# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewCalisthenicsTraining.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("border: 10px solid #FB98AD;background-color: #0C0C0C;\n"
"color: #FB98AD;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choose_type_btn = QtWidgets.QPushButton(self.centralwidget)
        self.choose_type_btn.setGeometry(QtCore.QRect(120, 20, 571, 41))
        self.choose_type_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_type_btn.setStyleSheet("border: none;\n"
"font: 20pt \"PRIMETIME\";")
        self.choose_type_btn.setObjectName("choose_type_btn")
        self.exercise_combo = QtWidgets.QComboBox(self.centralwidget)
        self.exercise_combo.setGeometry(QtCore.QRect(170, 120, 171, 81))
        self.exercise_combo.setAcceptDrops(False)
        self.exercise_combo.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 8pt \"PRIMETIME\";text-align: center;")
        self.exercise_combo.setObjectName("exercise_combo")
        self.exercise_combo.addItem("")
        self.exercise_combo.addItem("")
        self.exercise_combo.addItem("")
        self.exercise_combo.addItem("")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(520, 130, 111, 61))
        font = QtGui.QFont()
        font.setFamily("PRIMETIME")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.add_btn.setFont(font)
        self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_btn.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 12pt \"PRIMETIME\";")
        self.add_btn.setObjectName("add_btn")
        self.set_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.set_spin.setGeometry(QtCore.QRect(370, 120, 61, 31))
        self.set_spin.setStyleSheet("border: 1px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.set_spin.setObjectName("set_spin")
        self.rep_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.rep_spin.setGeometry(QtCore.QRect(370, 170, 61, 31))
        self.rep_spin.setStyleSheet("border: 1px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.rep_spin.setObjectName("rep_spin")
        self.sets_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sets_btn.setGeometry(QtCore.QRect(450, 120, 41, 31))
        self.sets_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sets_btn.setStyleSheet("border: none;\n"
"font: 10pt \"PRIMETIME\";\n"
"text-align: left;\n"
"")
        self.sets_btn.setObjectName("sets_btn")
        self.reps_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reps_btn.setGeometry(QtCore.QRect(450, 170, 41, 31))
        self.reps_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reps_btn.setStyleSheet("border: none;\n"
"font: 10pt \"PRIMETIME\";\n"
"text-align: left;\n"
"")
        self.reps_btn.setObjectName("reps_btn")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(20, 20, 81, 41))
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 8pt \"PRIMETIME\";")
        self.back_btn.setObjectName("back_btn")
        self.remove_training_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_training_btn.setGeometry(QtCore.QRect(480, 340, 161, 71))
        font = QtGui.QFont()
        font.setFamily("PRIMETIME")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.remove_training_btn.setFont(font)
        self.remove_training_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_training_btn.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 8pt \"PRIMETIME\";")
        self.remove_training_btn.setObjectName("remove_training_btn")
        self.training_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.training_name.setGeometry(QtCore.QRect(160, 230, 291, 61))
        self.training_name.setStyleSheet("font: 12pt \"PRIMETIME\";")
        self.training_name.setObjectName("training_name")
        self.training_list = QtWidgets.QListWidget(self.centralwidget)
        self.training_list.setGeometry(QtCore.QRect(160, 280, 291, 241))
        self.training_list.setStyleSheet("font: 10pt;")
        self.training_list.setObjectName("training_list")
        self.browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browse_btn.setGeometry(QtCore.QRect(480, 440, 161, 71))
        self.browse_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse_btn.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 8pt \"PRIMETIME\";")
        self.browse_btn.setObjectName("browse_btn")
        self.create_training_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_training_btn.setGeometry(QtCore.QRect(480, 240, 161, 71))
        font = QtGui.QFont()
        font.setFamily("PRIMETIME")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.create_training_btn.setFont(font)
        self.create_training_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_training_btn.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 8pt \"PRIMETIME\";")
        self.create_training_btn.setObjectName("create_training_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.choose_type_btn.setText(_translate("MainWindow", "NEW CALISTHENICS TRAINING"))
        self.exercise_combo.setItemText(0, _translate("MainWindow", "CHOOSE EXERCISE"))
        self.exercise_combo.setItemText(1, _translate("MainWindow", "PUSH UP"))
        self.exercise_combo.setItemText(2, _translate("MainWindow", "SIT UP"))
        self.exercise_combo.setItemText(3, _translate("MainWindow", "SQUAT"))
        self.add_btn.setText(_translate("MainWindow", "ADD"))
        self.sets_btn.setText(_translate("MainWindow", "sets"))
        self.reps_btn.setText(_translate("MainWindow", "reps"))
        self.back_btn.setText(_translate("MainWindow", "BACK"))
        self.remove_training_btn.setText(_translate("MainWindow", "REMOVE EXERCISE"))
        self.training_name.setPlainText(_translate("MainWindow", "Training name"))
        self.browse_btn.setText(_translate("MainWindow", "BROWSE TRAININGS"))
        self.create_training_btn.setText(_translate("MainWindow", " CREATE TRAINING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
