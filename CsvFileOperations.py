# importing csv module
import csv


class CSVFileOperations:
    def __init__(self):
            # csv file name
        csvFileName = "diabetes.csv"
        preprocedCsvFileName= "diabetes_preprocessed.csv"


        # her field ın max ve min değerlerini tutacağım dict.
        AdgeValues = {
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