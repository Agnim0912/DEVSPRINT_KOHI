import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QLabel

'''item=""
item2=""
item3=""
item4=""
item5=""
item6=""'''

class InputScreen(QDialog):
    global item, item2, item3, item4, item5, item6
    def __init__(self):
        super(InputScreen,self).__init__() 
        loadUi("input.ui", self)

        self.combo = self.findChild(QComboBox, "comboBox")
        self.combo2 = self.findChild(QComboBox, "comboBox2")
        self.combo3 = self.findChild(QComboBox, "comboBox3")
        self.combo4 = self.findChild(QComboBox, "comboBox4")
        self.combo5 = self.findChild(QComboBox, "comboBox5")
        self.combo6 = self.findChild(QComboBox, "comboBox6")
        self.label = self.findChild(QLabel, "label")

        #self.combo.currentTextChanged.connect(self.submit)
        self.But1.clicked.connect(self.submit)

    #def submit(self):
        #login = Output()
        #widget.addWidget(login)
        #widget.setCurrentIndex(widget.currentIndex()+1)
    

    def submit(self):
        print("func 2")
        item = self.combo.currentText()
        item2 = self.combo2.currentText()
        item3 = self.combo3.currentText()
        item4 = self.combo4.currentText()
        item5 = self.combo5.currentText()
        item6 = self.combo6.currentText()
        #print(item)
        '''print(item)
        print(item2)
        print(item3)
        print(item4)
        print(item5)
        print(item6)'''
        login = Output()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        #self.label.setText(item)
        
class Output(QDialog):
    global item, item2, item3, item4, item5, item6
    def __init__(self):
        super(Output, self).__init__()
        print(item)
        print(item2)
        print(item3)
        print(item4)
        print(item5)
        print(item6)
        loadUi("output.ui",self)
    


        


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
