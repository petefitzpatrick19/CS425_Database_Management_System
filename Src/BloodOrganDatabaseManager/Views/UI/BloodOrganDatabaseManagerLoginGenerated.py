# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/pete/Documents/GitHub/CS425_Database_Management_System/Src/BloodOrganDatabaseManager/Views/UI/BloodOrganDatabaseManagerLoginGenerated.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BloodOrganDatabaseManagerLogin(object):
    def setupUi(self, BloodOrganDatabaseManagerLogin):
        BloodOrganDatabaseManagerLogin.setObjectName("BloodOrganDatabaseManagerLogin")
        BloodOrganDatabaseManagerLogin.resize(456, 232)
        self.centralwidget = QtWidgets.QWidget(BloodOrganDatabaseManagerLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pass_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_lbl.setFont(font)
        self.pass_lbl.setObjectName("pass_lbl")
        self.gridLayout.addWidget(self.pass_lbl, 3, 0, 1, 1)
        self.pass_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_line_edit.setFont(font)
        self.pass_line_edit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pass_line_edit.setObjectName("pass_line_edit")
        self.gridLayout.addWidget(self.pass_line_edit, 3, 1, 1, 1)
        self.user_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_line_edit.setFont(font)
        self.user_line_edit.setObjectName("user_line_edit")
        self.gridLayout.addWidget(self.user_line_edit, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.enter_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enter_btn.setFont(font)
        self.enter_btn.setObjectName("enter_btn")
        self.gridLayout_2.addWidget(self.enter_btn, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 2)
        self.user_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_lbl.setFont(font)
        self.user_lbl.setObjectName("user_lbl")
        self.gridLayout.addWidget(self.user_lbl, 2, 0, 1, 1)
        self.login_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_lbl.setFont(font)
        self.login_lbl.setObjectName("login_lbl")
        self.gridLayout.addWidget(self.login_lbl, 1, 0, 1, 1)
        self.main_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.main_lbl.setFont(font)
        self.main_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.main_lbl.setObjectName("main_lbl")
        self.gridLayout.addWidget(self.main_lbl, 0, 0, 1, 2)
        BloodOrganDatabaseManagerLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BloodOrganDatabaseManagerLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 21))
        self.menubar.setObjectName("menubar")
        BloodOrganDatabaseManagerLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BloodOrganDatabaseManagerLogin)
        self.statusbar.setObjectName("statusbar")
        BloodOrganDatabaseManagerLogin.setStatusBar(self.statusbar)

        self.retranslateUi(BloodOrganDatabaseManagerLogin)
        QtCore.QMetaObject.connectSlotsByName(BloodOrganDatabaseManagerLogin)

    def retranslateUi(self, BloodOrganDatabaseManagerLogin):
        _translate = QtCore.QCoreApplication.translate
        BloodOrganDatabaseManagerLogin.setWindowTitle(_translate("BloodOrganDatabaseManagerLogin", "MainWindow"))
        self.pass_lbl.setText(_translate("BloodOrganDatabaseManagerLogin", "Password:"))
        self.enter_btn.setText(_translate("BloodOrganDatabaseManagerLogin", "Enter"))
        self.enter_btn.setShortcut(_translate("BloodOrganDatabaseManagerLogin", "Return"))
        self.user_lbl.setText(_translate("BloodOrganDatabaseManagerLogin", "Username:"))
        self.login_lbl.setText(_translate("BloodOrganDatabaseManagerLogin", "Login:"))
        self.main_lbl.setText(_translate("BloodOrganDatabaseManagerLogin", "Blood and Organ Donation Management System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BloodOrganDatabaseManagerLogin = QtWidgets.QMainWindow()
    ui = Ui_BloodOrganDatabaseManagerLogin()
    ui.setupUi(BloodOrganDatabaseManagerLogin)
    BloodOrganDatabaseManagerLogin.show()
    sys.exit(app.exec_())
