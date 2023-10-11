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
        self.b1.clicked.connect(self.clicked)


    def clicked(self):
        self.label.setText("You Pressed he BUtton")
        self.update()
    
    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win  =Mywindow()      
    win.show()
    sys.exit(app.exec_())
    
window()