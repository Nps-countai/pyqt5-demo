from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
print("Working!")


class Mywindow(QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Working")
        self.initUI()
        
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first Label")
        self.label.move(50,50)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.move(70,70)
        self.b1.clicked.connect(clicked)


    def clicked(self):
        self.label.setText("You Pressed he BUtton")






def clicked():
    print("Clicked!")

def window():
    app = QApplication(sys.argv)
    win  =Mywindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("Working")
    label = QtWidgets.QLabel(win)
    label.setText("My first Label")
    label.move(50,50)
    
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.move(70,70)
    b1.clicked.connect(clicked)
    
    
    win.show()
    sys.exit(app.exec_())
    
window()