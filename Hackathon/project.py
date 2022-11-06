import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QLabel
from PyQt5.QtGui import QIcon
import sqlite3

r=6

class InputScreen(QDialog):
    def __init__(self):
        super(InputScreen,self).__init__() 
        loadUi("input.ui", self)

        self.combo = self.findChild(QComboBox, "comboBox")
        self.combo2 = self.findChild(QComboBox, "comboBox2")
        self.combo3 = self.findChild(QComboBox, "comboBox3")
        self.combo4 = self.findChild(QComboBox, "comboBox4")
        self.combo5 = self.findChild(QComboBox, "comboBox5")
        self.combo6 = self.findChild(QComboBox, "comboBox6")

        #self.combo.currentTextChanged.connect(self.submit)
        self.But1.clicked.connect(self.submit)

    def submit(self):
        global item, item2, item3, item4, item5, item6
        print("func 2")
        item = self.combo.currentText()
        item2 = self.combo2.currentText()
        item3 = self.combo3.currentText()
        item4 = self.combo4.currentText()
        item5 = self.combo5.currentText()
        item6 = self.combo6.currentText()
        login = Output()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        #self.label.setText(item)
        
class Output(QDialog):
    def __init__(self):
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        super(Output, self).__init__()
        loadUi("output.ui",self)
        print(type(item))
        #print(type(int(item2)))
        print(item3)
        print(item4)
        print(item5)
        print(item6)
        t=''
        c.execute('''SELECT Recipe from coffee 
                    WHERE Temperature="{}" AND Expresso="{}" AND Coffee="{}" AND Milk="{}" AND water="{}" AND Extra="{}"'''.format(item, item2, item3, item4, item5, item6))
        conn.commit()
        a = c.fetchall()
        self.label = self.findChild(QLabel, "label")
        if(a==[]):
            self.label.setText('No Recipes Found')
        else:
            for u in a:
                for j in u:
                    t=j+''
            self.label.setText(t)
        conn.close()
        #t=item+item2+item3+item4+item5+item6
        self.But2.clicked.connect(self.submit)
    
    def submit(submit):
        login = InputScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


        


app = QApplication(sys.argv)
welcome = InputScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setWindowTitle("Kohi")
widget.setWindowIcon(QIcon("k.png"))
widget.setFixedHeight(800)
widget.setFixedWidth(1100)
widget.show()
try:
    app.exec()
except:
    print("Exiting...")