from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QWidget
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
        # .csv dosyası önce okunmalı user inputlarından önce.
        self.initUI()

        

    def UI2(self):
        MainWidget = QWidget()
        MainLayout = QVBoxLayout()
        
        itemCounter = 1
        for value in self.answers:
            RowLayout  = QHBoxLayout()
            self.valueLabel = QLabel(self)
            self.valueCounterLabel = QLabel(self)
            self.valueCounterLabel.setText(str(itemCounter)+". value = ")
            self.valueLabel.setText(str(value))
            itemCounter+=1
            RowLayout.addWidget(self.valueCounterLabel, 1)
            RowLayout.addWidget(self.valueLabel, 2)
            MainLayout.addLayout(RowLayout)

        MainLayout.addStretch(1)
        MainWidget.setLayout(MainLayout)
        self.setCentralWidget(MainWidget)   



    def initUI(self):
        MainWidget = QWidget()
        MainLayout = QVBoxLayout()

        # pregnancie info retrieving..
        RowLayout1 = QHBoxLayout()
        self.definitionLabel1 = QLabel(self)
        self.definitionLabel1.setText("-Pregnancies-")
        self.textField1=QLineEdit(self)

        RowLayout1.addWidget(self.definitionLabel1, 1)
        RowLayout1.addWidget(self.textField1, 2)
        MainLayout.addLayout(RowLayout1)


        # Glucose info retrieving..
        RowLayout1 = QHBoxLayout()
        self.definitionLabel2 = QtWidgets.QLabel(self)
        self.definitionLabel2.setText ("-Glucose-")
        self.textField2=QtWidgets.QLineEdit(self)
        
        RowLayout1.addWidget(self.definitionLabel2, 1)
        RowLayout1.addWidget(self.textField2, 2)
        MainLayout.addLayout(RowLayout1)


        # BloodPressure info retrieving..
        RowLayout1 = QHBoxLayout()
        self.definitionLabel3 = QtWidgets.QLabel(self)
        self.definitionLabel3.setText ("-BloodPressure-")
        self.textField3=QtWidgets.QLineEdit(self)

        RowLayout1.addWidget(self.definitionLabel3, 1)
        RowLayout1.addWidget(self.textField3, 2)
        MainLayout.addLayout(RowLayout1)


        # SkinThickness info retrieving..
        RowLayout1 = QHBoxLayout()
        self.definitionLabel4 = QtWidgets.QLabel(self)
        self.definitionLabel4.setText ("-SkinThickness-")
        self.textField4=QtWidgets.QLineEdit(self)

        RowLayout1.addWidget(self.definitionLabel4, 1)
        RowLayout1.addWidget(self.textField4, 2)
        MainLayout.addLayout(RowLayout1)


        # Insulin info retrieving..
        RowLayout1 = QHBoxLayout()
        self.definitionLabel5 = QtWidgets.QLabel(self)
        self.definitionLabel5.setText ("-Insulin-")
        self.textField5=QtWidgets.QLineEdit(self)

        RowLayout1.addWidget(self.definitionLabel5, 1)
        RowLayout1.addWidget(self.textField5, 2)
        MainLayout.addLayout(RowLayout1)


        # BMI info retrieving..
        RowLayout1 = QHBoxLayout()
        self.definitionLabel6 = QtWidgets.QLabel(self)
        self.definitionLabel6.setText ("-BMI-")
        self.textField6=QtWidgets.QLineEdit(self)

        RowLayout1.addWidget(self.definitionLabel6, 1)
        RowLayout1.addWidget(self.textField6, 2)
        MainLayout.addLayout(RowLayout1)


        # DiabetesPedigreeFunction info retrieving..
        RowLayout1 = QHBoxLayout()
        self.definitionLabel7 = QtWidgets.QLabel(self)
        self.definitionLabel7.setText("-DiabetesPedigreeFunction-")
        self.textField7=QtWidgets.QLineEdit(self)

        RowLayout1.addWidget(self.definitionLabel7, 1)
        RowLayout1.addWidget(self.textField7, 2)
        MainLayout.addLayout(RowLayout1)


        # Age info retrieving..
        RowLayout1 = QHBoxLayout()
        self.definitionLabel8 = QtWidgets.QLabel(self)
        self.definitionLabel8.setText ("-Age-")
        self.textField8=QtWidgets.QLineEdit(self)

        RowLayout1.addWidget(self.definitionLabel8, 1)
        RowLayout1.addWidget(self.textField8, 2)
        MainLayout.addLayout(RowLayout1)


        # recieve data button at buttom
        RowLayout1 = QHBoxLayout()
        self.recieveDataButton = QtWidgets.QPushButton(self)
        self.recieveDataButton.setText("Submit  ")
        self.recieveDataButton.clicked.connect(self.recieveDataButtonClicked)

        RowLayout1.addWidget(self.recieveDataButton, 1)
        MainLayout.addLayout(RowLayout1)


        MainWidget.setLayout(MainLayout)
        self.setCentralWidget(MainWidget)




    def recieveDataButtonClicked(self):
        self.answers = []
        self.recieveData()
        self.answersStatus = self.checkAnswers(self.answers)
        print(self.answersStatus)
        if self.answersStatus:
            self.UI2()
        else:
            self.initUI()

        # eğer value lar sayısalsa ekranda değişiklikler yapılacak
        # eğer değerler sayısal değilse tekrardan girsin değerleri.

        

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

        

    






