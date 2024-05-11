# importing csv module
import csv

# csv file name
filename = "diabetes.csv"

# initializing the titles and rows list
fields = []
rows = []

# her field ın max ve min değerlerinin listesini tutacağım liste.
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

def makeRowNumeric(row):
    for i in range(8):
        if "." in row[i]:  # Eğer öğe bir float sayı ise
            row[i] = float(row[i])
        else:  # Eğer öğe bir tam sayı ise
            row[i] = int(row[i])
                


def dicValuesSort(row):
    if len(row) !=9:
        return
    makeRowNumeric(row)
    
    dicValuesSortFor(row[0], "MaxPregnancies", "MinPregnancies")
    dicValuesSortFor(row[1], "MaxGlucose", "MinGlucose")
    dicValuesSortFor(row[2], "MaxBloodPressure", "MinBloodPressure")
    dicValuesSortFor(row[3], "MaxSkinThickness", "MinSkinThickness")
    dicValuesSortFor(row[4], "MaxInsulin", "MinInsulin")
    dicValuesSortFor(row[5], "MaxBMI", "MinBMI")
    dicValuesSortFor(row[6], "MaxDiabetesPedigreeFunction", "MinDiabetesPedigreeFunction")
    dicValuesSortFor(row[7], "MaxAge", "MinAge")



def dicValuesSortFor(value, maxName, minName):
    if AdgeValues[maxName] is None or value > AdgeValues[maxName]:
        AdgeValues[maxName] = value
    
    if AdgeValues[minName] is None or value < AdgeValues[minName]:
        AdgeValues[minName] = value



# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        dicValuesSort(row)

        
        

