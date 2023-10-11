# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(60, 120, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.comboBox1.setFont(font)
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(400, 120, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.comboBox2.setFont(font)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(200, 360, 261, 71))
        self.Button1.setObjectName("Button1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 280, 121, 41))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Button1.clicked.connect(self.pressed)
        # self.comboBox1.addItem("Hello")
        # index = self.comboBox1.findText("Hello", QtCore.Qt.MatchFixedString)
        # self.comboBox1.setCurrentIndex(index)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "1"))
        self.Button1.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "X XOR Y = "))
    
    def pressed(self):
        x = int(self.comboBox1.currentText())
        y = int(self.comboBox2.currentText())
        xor = (x and not y) or (not x and y)
        self.label.setText("X xor Y" + " : "+str(xor))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
