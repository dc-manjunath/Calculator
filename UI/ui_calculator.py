from PyQt6 import QtWidgets, QtGui, QtCore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 266)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)
        self.btn_division = QtWidgets.QPushButton(self.centralwidget)
        self.btn_division.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_division.setObjectName("btn_division")
        self.gridLayout.addWidget(self.btn_division, 0, 3, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 0, 4, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mul.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_mul.setObjectName("btn_mul")
        self.gridLayout.addWidget(self.btn_mul, 1, 3, 1, 1)
        self.btn_brackets_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_brackets_left.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_brackets_left.setObjectName("btn_brackets_left")
        self.gridLayout.addWidget(self.btn_brackets_left, 1, 4, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sub.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_sub.setObjectName("btn_sub")
        self.gridLayout.addWidget(self.btn_sub, 2, 3, 1, 1)
        self.btn_brackets_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_brackets_right.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_brackets_right.setObjectName("btn_brackets_right")
        self.gridLayout.addWidget(self.btn_brackets_right, 2, 4, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 3, 0, 1, 1)
        self.btn_00 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_00.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_00.setObjectName("btn_00")
        self.gridLayout.addWidget(self.btn_00, 3, 1, 1, 1)
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        self.btn_point.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_point.setObjectName("btn_point")
        self.gridLayout.addWidget(self.btn_point, 3, 2, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 3, 3, 1, 1)
        self.btn_result = QtWidgets.QPushButton(self.centralwidget)
        self.btn_result.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_result.setFont(font)
        self.btn_result.setObjectName("btn_result")
        self.gridLayout.addWidget(self.btn_result, 3, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "简单计算器"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_division.setText(_translate("MainWindow", "/"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_mul.setText(_translate("MainWindow", "*"))
        self.btn_brackets_left.setText(_translate("MainWindow", "("))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_brackets_right.setText(_translate("MainWindow", ")"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_00.setText(_translate("MainWindow", "00"))
        self.btn_point.setText(_translate("MainWindow", "."))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_result.setText(_translate("MainWindow", "="))

