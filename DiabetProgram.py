from PyQt5.QtWidgets import QApplication
import sys
from programWindow import MyWindow


class DiabetProgram():

    def __init__(self):
        pass

    def diabetProgramStart(self):
        self.showAplicationWindow()

    def showAplicationWindow(self):
        DiabetApp = QApplication(sys.argv)
        win = MyWindow()
        win.show()
        DiabetApp.exec()  ## bu satırdan sonra window u kapatmadığım sürece işlem yapamıyorum.


myDiabetProgram = DiabetProgram()
myDiabetProgram.diabetProgramStart()