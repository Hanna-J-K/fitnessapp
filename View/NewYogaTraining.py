# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewYogaTraining.ui'
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
        self.choose_type_btn.setGeometry(QtCore.QRect(190, 30, 331, 31))
        self.choose_type_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_type_btn.setStyleSheet("border: none;\n"
"font: 20pt \"PRIMETIME\";")
        self.choose_type_btn.setObjectName("choose_type_btn")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(550, 130, 111, 61))
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
        self.min_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.min_spin.setGeometry(QtCore.QRect(400, 140, 61, 31))
        self.min_spin.setStyleSheet("border: 1px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.min_spin.setObjectName("min_spin")
        self.mins_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mins_btn.setGeometry(QtCore.QRect(480, 140, 41, 31))
        self.mins_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mins_btn.setStyleSheet("border: none;\n"
"font: 10pt \"PRIMETIME\";\n"
"text-align: left;\n"
"")
        self.mins_btn.setObjectName("mins_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 120, 181, 81))
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
        self.remove_training_btn.setGeometry(QtCore.QRect(510, 340, 161, 71))
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
        self.training_name.setGeometry(QtCore.QRect(190, 230, 291, 61))
        self.training_name.setStyleSheet("font: 12pt \"PRIMETIME\";")
        self.training_name.setObjectName("training_name")
        self.training_list = QtWidgets.QListWidget(self.centralwidget)
        self.training_list.setGeometry(QtCore.QRect(190, 280, 291, 241))
        self.training_list.setStyleSheet("font: 10pt;")
        self.training_list.setObjectName("training_list")
        self.browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browse_btn.setGeometry(QtCore.QRect(510, 440, 161, 71))
        self.browse_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse_btn.setStyleSheet("background-color: #1D1D1D;border: 3px solid #FB98AD;\n"
"font: 8pt \"PRIMETIME\";")
        self.browse_btn.setObjectName("browse_btn")
        self.create_training_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_training_btn.setGeometry(QtCore.QRect(510, 240, 161, 71))
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
        self.choose_type_btn.setText(_translate("MainWindow", "NEW YOGA TRAINING"))
        self.add_btn.setText(_translate("MainWindow", "ADD"))
        self.mins_btn.setText(_translate("MainWindow", "MIN"))
        self.label.setText(_translate("MainWindow", "          SESSION TIME"))
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
