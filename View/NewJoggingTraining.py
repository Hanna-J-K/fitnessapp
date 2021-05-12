# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewJoggingTraining.ui'
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
        self.choose_type_btn.setGeometry(QtCore.QRect(150, 30, 501, 45))
        self.choose_type_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_type_btn.setStyleSheet("border: none;\n"
"font: 20pt \"PRIMETIME\";")
        self.choose_type_btn.setObjectName("choose_type_btn")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(550, 120, 111, 81))
        font = QtGui.QFont()
        font.setFamily("PRIMETIME")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.add_btn.setFont(font)
        self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_btn.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 8pt \"PRIMETIME\";")
        self.add_btn.setObjectName("add_btn")
        self.min_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.min_spin.setGeometry(QtCore.QRect(440, 120, 51, 31))
        self.min_spin.setStyleSheet("border: 1px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.min_spin.setObjectName("min_spin")
        self.kim_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.kim_spin.setGeometry(QtCore.QRect(440, 170, 51, 31))
        self.kim_spin.setStyleSheet("border: 1px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.kim_spin.setObjectName("kim_spin")
        self.sets_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sets_btn.setGeometry(QtCore.QRect(500, 120, 41, 31))
        self.sets_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sets_btn.setStyleSheet("border: none;\n"
"font: 10pt \"PRIMETIME\";\n"
"text-align: left;\n"
"")
        self.sets_btn.setObjectName("sets_btn")
        self.reps_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reps_btn.setGeometry(QtCore.QRect(500, 170, 31, 31))
        self.reps_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reps_btn.setStyleSheet("border: none;\n"
"font: 10pt \"PRIMETIME\";\n"
"text-align: left;\n"
"")
        self.reps_btn.setObjectName("reps_btn")
        self.by_time_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.by_time_btn.setGeometry(QtCore.QRect(300, 120, 131, 41))
        self.by_time_btn.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 8pt \"PRIMETIME\";")
        self.by_time_btn.setObjectName("by_time_btn")
        self.by_dist_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.by_dist_btn.setGeometry(QtCore.QRect(300, 160, 131, 41))
        self.by_dist_btn.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 8pt \"PRIMETIME\";")
        self.by_dist_btn.setObjectName("by_dist_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 120, 161, 81))
        self.label.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 8pt \"PRIMETIME\";")
        self.label.setObjectName("label")
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
        self.choose_type_btn.setText(_translate("MainWindow", "NEW JOGGING TRAINING"))
        self.add_btn.setText(_translate("MainWindow", "ADD"))
        self.sets_btn.setText(_translate("MainWindow", "MIN"))
        self.reps_btn.setText(_translate("MainWindow", "KM"))
        self.by_time_btn.setText(_translate("MainWindow", "BY TIME"))
        self.by_dist_btn.setText(_translate("MainWindow", "BY DISTANCE"))
        self.label.setText(_translate("MainWindow", "     I WANT TO JOG"))
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