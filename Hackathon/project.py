import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QLabel

class InputScreen(QDialog):
    def __init__(self):
        super(InputScreen,self).__init__() 
        loadUi("input.ui", self)
        self.combo = self.findChild(QComboBox, "comboBox")
        self.label = self.findChild(QLabel, "label")
        self.But1.clicked.connect(self.submit)
    
    def submit(self):
        print("func submit")
        self.combo.currentTextChanged.connect(self.combo_selected)
    

    def combo_selected(self):
        print("func 2")
        item = self.combo.currentText()
        self.label.setText(item)
        
    


        


app = QApplication(sys.argv)
welcome = InputScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1100)
widget.show()
try:
    app.exec()
except:
    print("Exiting...")