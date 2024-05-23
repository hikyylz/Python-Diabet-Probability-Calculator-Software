
# bu file çalıştırıldığında diabet application i çalışacaktır.
# csvfile operations.py file yardımıyla csv file handling işlemleri yürütülüyor sadece.

import csv
import math
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QWidget
)

class CSVFileOperations:
    def __init__(self):
            # csv file name
        csvFileName = "diabetes.csv"
        preprocedCsvFileName= "diabetes_preprocessed.csv"


        # her field ın max ve min değerlerini tutacağım dict.
        self.AdgeValues = {
            "MaxPregnancies":None,
            "MinPregnancies":None,
            "MaxGlucose": None,
            "MinGlucose":None,
            "MaxBloodPressure": None,
            "MinBloodPressure":None,
            "MaxSkinThickness": None,
            "MinSkinThickness":None,
            "MaxInsulin": None,
            "MinInsulin":None,
            "MaxBMI": None,
            "MinBMI":None,
            "MaxDiabetesPedigreeFunction": None,
            "MinDiabetesPedigreeFunction":None,
            "MaxAge": None,
            "MinAge":None,
            
        } 
        # reading csv file
        with open(csvFileName, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                self.dicValuesSort(row)
    
        csvfile.close()
    
        # reading csv file
        with open(csvFileName, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            f = open(preprocedCsvFileName, "w")
            f.write(','.join(map(str, fields)) + '\n')
            f.close()

            #preproced data set uploading
            for row in csvreader:
                self.writeFile(row, preprocedCsvFileName)

            csvfile.close()


     

    def makeRowNumeric(self, row):
        for i in range(8):
            if "." in row[i]:  # Eğer öğe bir float sayı ise
                row[i] = float(row[i])
            else:  # Eğer öğe bir tam sayı ise
                row[i] = int(row[i])
                


    def dicValuesSort(self, row):
        if len(row) !=9:
            return
        self.makeRowNumeric(row)
        
        self.dicValuesSortFor(row[0], "MaxPregnancies", "MinPregnancies")
        self.dicValuesSortFor(row[1], "MaxGlucose", "MinGlucose")
        self.dicValuesSortFor(row[2], "MaxBloodPressure", "MinBloodPressure")
        self.dicValuesSortFor(row[3], "MaxSkinThickness", "MinSkinThickness")
        self.dicValuesSortFor(row[4], "MaxInsulin", "MinInsulin")
        self.dicValuesSortFor(row[5], "MaxBMI", "MinBMI")
        self.dicValuesSortFor(row[6], "MaxDiabetesPedigreeFunction", "MinDiabetesPedigreeFunction")
        self.dicValuesSortFor(row[7], "MaxAge", "MinAge")


    def dicValuesSortFor(self, value, maxName, minName):
        if self.AdgeValues[maxName] is None or value > self.AdgeValues[maxName]:
            self.AdgeValues[maxName] = value
        
        if self.AdgeValues[minName] is None or value < self.AdgeValues[minName]:
            self.AdgeValues[minName] = value


    def preprocesRowData(self, data):
        newData = []
        adgeValuesList = list(self.AdgeValues.values())
        valueCounter = 0

        for value in data:
            try:
                max = adgeValuesList[valueCounter]
                min = adgeValuesList[valueCounter+1]
                valueCounter += 2
                top = value - min
                bottom = max - min
                newValue = top / bottom
            except IndexError:
                # outcame değeri için var bu exception
                newValue = value

            except Exception as e:
                print("preprosesing created problem")
                return None

            newData.append(newValue)
        return newData


    def writeFile(self, data, toFilename):
        with open(toFilename, 'a') as newcsvFile:
            self.makeRowNumeric(data)
            data = self.preprocesRowData(data)

            if data == None:
                return
            
            newcsvFile.write(','.join(map(str, data)) + '\n')
            newcsvFile.close()


class Node:
    def __init__(self, distance, result):
        self.distance = distance
        self.result = result
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, distance, result):
        new_node = Node(distance, result)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        
        # Orta noktayı bul
        mid = self.find_mid(head)
        mid_next = mid.next
        mid.next = None

        # Sol ve sağ yarılarda tekrar merge sort uygula
        left = self.merge_sort(head)
        right = self.merge_sort(mid_next)

        # Birleştirme işlemi
        return self.merge(left, right)

    def find_mid(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow



    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.distance < right.distance:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    def setDiabetResults(self, nbr):
        # belirttiğim sayıda data seti içerisinden user ın diabet olma ihtimalini hesaplamak için resultları çekiyorum.
        counter = 0
        current_node = self.head
        diabetResultList = []

        while counter < nbr and current_node != None:
            diabetResultList.append(current_node.result)
            current_node = current_node.next
            counter += 1
        
        return diabetResultList




class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.EclidianDistanceResultList = LinkedList()
        self.csvFileManager = CSVFileOperations()
        self.AdgeValues = self.csvFileManager.AdgeValues
        self.dataSetSpaceSize = "5"
        self.answers = []
        self.preprosedAnswers = []
        self.answersStatus = False
        self.warnUser = False
        self.lineGap = 50
        self.componentGap = 250
        self.setGeometry(200,200,700,500)
        self.setWindowTitle("Diabet Application")

        self.initUI()


    def ResultsPage(self, diabetResultProbabilty):
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

        RowLayout  = QHBoxLayout()
        self.diabetResultLabel = QLabel(self)
        self.diabetResultLabel.setText("Probabilty of being diabet is " + str(diabetResultProbabilty) + " %   ")
        RowLayout.addWidget(self.diabetResultLabel, 1)
        MainLayout.addLayout(RowLayout)

        MainLayout.addStretch(1)
        MainWidget.setLayout(MainLayout)
        self.setCentralWidget(MainWidget)   



    def initUI(self):
        MainWidget = QWidget()
        MainLayout = QVBoxLayout()

        if self.warnUser:
            RowLayout1 = QHBoxLayout()
            self.warnningLabel = QLabel(self)
            self.warnningLabel.setText("- - - Type proper values ! - - - ")
            RowLayout1.addWidget(self.warnningLabel, 1)
            MainLayout.addLayout(RowLayout1)


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

        # dataSetSpace info retrieving..
        RowLayout1 = QHBoxLayout()
        self.definitionLabel9 = QtWidgets.QLabel(self)
        self.definitionLabel9.setText ("-            Data set space size :")
        self.textField9=QtWidgets.QLineEdit(self)

        RowLayout1.addWidget(self.definitionLabel9, 1)
        RowLayout1.addWidget(self.textField9, 2)
        MainLayout.addLayout(RowLayout1)

        ## ekranı genişletiyor.
        MainLayout.addStretch(1) 

        # recieve data button at buttom
        RowLayout1 = QHBoxLayout()
        self.recieveDataButton = QtWidgets.QPushButton(self)
        self.recieveDataButton.setText("Submit  ")
        self.recieveDataButton.clicked.connect(self.recieveDataButtonClicked)

        RowLayout1.addWidget(self.recieveDataButton, 1)
        MainLayout.addLayout(RowLayout1)

        MainWidget.setLayout(MainLayout)
        self.setCentralWidget(MainWidget)


    def makeAnsersPreproced(self):
        adgeValuesList = list(self.AdgeValues.values())
        valueCounter = 0

        for value in self.answers:
            try:
                max = adgeValuesList[valueCounter]
                min = adgeValuesList[valueCounter+1]
                valueCounter += 2
                top = value - min
                bottom = max - min
                newValue = top / bottom

            except Exception as e:
                print("preprosesing created problem")
                return None

            self.preprosedAnswers.append(newValue)

    def euclidianDistance(self, list1, list2):
        # list correctiness check 
        if len(list1) != 8 or len(list2) != 8:
            print("list lenght wrong")
            return 
        
        calculationSum = 0
        for counter in range(8):
            value1 = float(list1[counter])
            value2 = float(list2[counter])
            substraction =  value1 - value2
            power = math.pow(substraction, 2)
            calculationSum += power

        EcliadianDistance = math.sqrt(calculationSum)
        return EcliadianDistance
        


    def appendResultToLinkedList(self, distance, diabetResult):
        self.EclidianDistanceResultList.append(distance, diabetResult)

    

    def calculateDistances(self):
        # self.preprosed list1
        # csv dosyasındaki veri satırları da list2 olacaktır.
        # bu iki listeyi d hesaplaması inin euclidianDistance methoduna vereceğim
        # reading csv file
        csvFileName = "diabetes_preprocessed.csv"
        
        with open(csvFileName, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            #preproced data set uploading
            for row in csvreader:
                diabetResult = row.pop()
                distance = self.euclidianDistance(self.preprosedAnswers, row)
                self.appendResultToLinkedList(distance, diabetResult )
                # her row ile user answers d hesaplaması yapılacak.

            csvfile.close()


    def evaluateUserDiabetResult(self):
        if self.dataSetSpaceSize == "":
            dataSetNbr = 5
        else:
            dataSetNbr = int(self.dataSetSpaceSize)

        self.EclidianDistanceResultList.head = self.EclidianDistanceResultList.merge_sort(self.EclidianDistanceResultList.head)
        # llist deki ilk 5 elemanın diabet resultlarını % yeşklinde ekranda göstereceğim
        diabetResultSpace = self.EclidianDistanceResultList.setDiabetResults(dataSetNbr)
        pozitifResultCounter = 0
        for result in diabetResultSpace:
            if result == "1":
                pozitifResultCounter+=1

        probabily = 100*pozitifResultCounter / dataSetNbr
        return probabily


        


    def recieveDataButtonClicked(self):
        self.answers = []
        self.recieveData()
        self.answersStatus = self.checkAnswers(self.answers)

        if self.answersStatus:
            self.warnUser = False
            # diabet olup olmadığı hesaplanmalı burada.
            self.makeAnsersPreproced()
            self.calculateDistances()
            diabetProbabilty = self.evaluateUserDiabetResult()
            self.ResultsPage(diabetProbabilty)
        else:
            # hatalı input girilmiş.
            self.warnUser = True
            self.initUI()


        

    def recieveData(self):
        dataPregnancies = self.textField1.text()
        dataGlucose = self.textField2.text()
        dataBloodPressure = self.textField3.text()
        dataSkinThickness = self.textField4.text()
        dataInsulin = self.textField5.text()
        dataBMI = self.textField6.text()
        dataDiabetesPedigreeFunction = self.textField7.text()
        dataAge = self.textField8.text()
        self.dataSetSpaceSize = self.textField9.text()
        
        self.answers.append(dataPregnancies)
        self.answers.append(dataGlucose)
        self.answers.append(dataBloodPressure)
        self.answers.append(dataSkinThickness)
        self.answers.append(dataInsulin)
        self.answers.append(dataBMI)
        self.answers.append(dataDiabetesPedigreeFunction)
        self.answers.append(dataAge)


    def dicValuesSortFor(self, value, maxName, minName):
        if value > self.AdgeValues[maxName]:
            return False
        elif  value < self.AdgeValues[minName]:
            return False
        return True

    def dicValuesSort(self, row):
        answersSuitability = []
        answersSuitability.append(self.dicValuesSortFor(row[0], "MaxPregnancies", "MinPregnancies"))  
        answersSuitability.append(self.dicValuesSortFor(row[1], "MaxGlucose", "MinGlucose"))
        answersSuitability.append(self.dicValuesSortFor(row[2], "MaxBloodPressure", "MinBloodPressure"))
        answersSuitability.append(self.dicValuesSortFor(row[3], "MaxSkinThickness", "MinSkinThickness"))
        answersSuitability.append(self.dicValuesSortFor(row[4], "MaxInsulin", "MinInsulin"))
        answersSuitability.append(self.dicValuesSortFor(row[5], "MaxBMI", "MinBMI"))
        answersSuitability.append(self.dicValuesSortFor(row[6], "MaxDiabetesPedigreeFunction", "MinDiabetesPedigreeFunction"))
        answersSuitability.append(self.dicValuesSortFor(row[7], "MaxAge", "MinAge"))
        for flag in answersSuitability:
            if not flag:
                return False
        return True


    def check_values_in_range(self, AnswerList):
        # answerlist aralıktaysa true döndür.
        return self.dicValuesSort(AnswerList)
        

    def checkAnswers(self, AnswersList):
        # answers değerlerini sayısal ifadeye dönüştürülüyor mu diye çalışıyoruz ilk olarak.
        try:
            size=len(AnswersList)
            for i in range(size):
                if AnswersList[i].replace(".", "", 1).isdigit():
                    if "." in AnswersList[i]:  # Eğer öğe bir float sayı ise
                        AnswersList[i] = float(AnswersList[i])
                    else:  # Eğer öğe bir tam sayı ise
                        AnswersList[i] = int(AnswersList[i])
                else:
                    return False

        except Exception as e:
            return False

        #blank textfield check
        for value in AnswersList:
            if value == "":
                return False
        
        # user input csv dosyasındaki değerlerin arasında mı kontrolu.
        flag = self.check_values_in_range(AnswersList)
        if not flag:
            return False

        self.answers = AnswersList
        return True
    

DiabetApp = QApplication(sys.argv)
win = MyWindow()
win.show()
DiabetApp.exec()  ## bu satırdan sonra window u kapatmadığım sürece işlem yapamıyorum.
