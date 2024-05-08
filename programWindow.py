from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QWidget,
)
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.answers = []
        self.answersStatus = False
        self.lineGap = 50
        self.componentGap = 250
        self.setGeometry(200,200,700,700)
        self.setWindowTitle("Diabet Application")
        
        if not self.answersStatus:
            self.initUI()
        else:
            self.Label1 = QtWidgets.QLabel(self)
            self.Label1.setText("answers atandi")
            self.Label1.move(0,0)


    


    def initUI(self):
        # pregnancie info retrieving..
        self.definitionLabel1 = QtWidgets.QLabel(self)
        self.definitionLabel1.setText ("-Pregnancies-")
        self.definitionLabel1.move(0, 0)

        self.textField1=QtWidgets.QLineEdit(self)
        self.textField1.move(self.componentGap, 0)

        # Glucose info retrieving..
        self.definitionLabel2 = QtWidgets.QLabel(self)
        self.definitionLabel2.setText ("-Glucose-")
        self.definitionLabel2.move(0, self.lineGap)

        self.textField2=QtWidgets.QLineEdit(self)
        self.textField2.move(self.componentGap, self.lineGap)

        # BloodPressure info retrieving..
        self.definitionLabel3 = QtWidgets.QLabel(self)
        self.definitionLabel3.setText ("-BloodPressure-")
        self.definitionLabel3.move(0, self.lineGap*2)

        self.textField3=QtWidgets.QLineEdit(self)
        self.textField3.move(self.componentGap, self.lineGap*2)

        # SkinThickness info retrieving..
        self.definitionLabel4 = QtWidgets.QLabel(self)
        self.definitionLabel4.setText ("-SkinThickness-")
        self.definitionLabel4.move(0, self.lineGap*3)

        self.textField4=QtWidgets.QLineEdit(self)
        self.textField4.move(self.componentGap, self.lineGap*3)

        # Insulin info retrieving..
        self.definitionLabel5 = QtWidgets.QLabel(self)
        self.definitionLabel5.setText ("-Insulin-")
        self.definitionLabel5.move(0, self.lineGap*4)

        self.textField5=QtWidgets.QLineEdit(self)
        self.textField5.move(self.componentGap, self.lineGap*4)

        # BMI info retrieving..
        self.definitionLabel6 = QtWidgets.QLabel(self)
        self.definitionLabel6.setText ("-BMI-")
        self.definitionLabel6.move(0, self.lineGap*5)

        self.textField6=QtWidgets.QLineEdit(self)
        self.textField6.move(self.componentGap, self.lineGap*5)

        # DiabetesPedigreeFunction info retrieving..
        self.definitionLabel7 = QtWidgets.QLabel(self)
        self.definitionLabel7.setText("-DiabetesPedigreeFunction-")
        self.definitionLabel7.adjustSize()
        self.definitionLabel7.move(0, self.lineGap*6)

        self.textField7=QtWidgets.QLineEdit(self)
        self.textField7.move(self.componentGap, self.lineGap*6)

        # Age info retrieving..
        self.definitionLabel8 = QtWidgets.QLabel(self)
        self.definitionLabel8.setText ("-Age-")
        self.definitionLabel8.move(0, self.lineGap*7)

        self.textField8=QtWidgets.QLineEdit(self)
        self.textField8.move(self.componentGap, self.lineGap*7)

        # recieve data button at buttom
        self.recieveDataButton = QtWidgets.QPushButton(self)
        self.recieveDataButton.setText("Submit  ")
        self.recieveDataButton.move(0, self.lineGap*9)
        self.recieveDataButton.clicked.connect(self.recieveDataButtonClicked)


    def recieveDataButtonClicked(self):
        self.answers = []
        self.recieveData()
        self.answersStatus = self.checkAnswers(self.answers)
        print(self.answersStatus)
        


    def recieveData(self):
        dataPregnancies = self.textField1.text()
        dataGlucose = self.textField2.text()
        dataBloodPressure = self.textField3.text()
        dataSkinThickness = self.textField4.text()
        dataInsulin = self.textField5.text()
        dataBMI = self.textField6.text()
        dataDiabetesPedigreeFunction = self.textField7.text()
        dataAge = self.textField8.text()
        

        self.answers.append(dataPregnancies)
        self.answers.append(dataGlucose)
        self.answers.append(dataBloodPressure)
        self.answers.append(dataSkinThickness)
        self.answers.append(dataInsulin)
        self.answers.append(dataBMI)
        self.answers.append(dataDiabetesPedigreeFunction)
        self.answers.append(dataAge)

    # answers sayısal değer değilse false return eder. 
    def checkAnswers(self, AnswersList):

        # answers değerlerini sayısal ifadeye dönüştürülüyor mu diye çalışıyoruz ilk olarak.
        try:
            size=len(self.answers)
            for i in range(size):
                if self.answers[i].replace(".", "", 1).isdigit():
                    if "." in self.answers[i]:  # Eğer öğe bir float sayı ise
                        self.answers[i] = float(self.answers[i])
                    else:  # Eğer öğe bir tam sayı ise
                        self.answers[i] = int(self.answers[i])
                else:
                    return False

        except Exception as e:
            print("girilen değerler sayisal değilmiş.")
            return False


        #blank textfield check
        for value in AnswersList:
            if value == "":
                return False
            
        return True

        

    






