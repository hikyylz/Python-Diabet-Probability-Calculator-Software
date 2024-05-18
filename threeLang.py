import csv
import math



csvFileName = "diabetes_preprocessed.csv"
dataRow1 = 1
dataRow2 = 8

dataRow1_List = []
dataRow2_List = [] 

def euclidianDistance(list1, list2):
    # list correctiness check 
    if len(list1) != 9 or len(list2) != 9:
        print("list lenght wrong")
        return 
    
    # removing diabet result
    list1.pop()
    list2.pop()

    calculationSum = 0
    for counter in range(8):
        value1 = float(list1[counter])
        value2 = float(list2[counter])
        substraction =  value1 - value2
        power = math.pow(substraction, 2)
        calculationSum += power

    EcliadianDistance = math.sqrt(calculationSum)
    print("--")
    print("eclidian distance between selected point is ")
    print(EcliadianDistance)
    print("--")


with open(csvFileName, 'r') as csvfile:

    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names through first row
    fields = next(csvreader)

    # after for loop, I will be selected two example data from preprosed csv file.
    rowCounter = 1
    for data in csvreader:
        if rowCounter == dataRow1:
            dataRow1_List = data
            if len(dataRow2_List) != 0 :
                break

        if rowCounter == dataRow2:
            dataRow2_List = data
            if len(dataRow1_List) != 0 :
                break

        rowCounter+=1


euclidianDistance(dataRow1_List, dataRow2_List)
    
    



