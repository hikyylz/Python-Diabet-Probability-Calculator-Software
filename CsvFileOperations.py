# importing csv module
import csv

# csv file name
filename = "diabetes.csv"

# initializing the titles and rows list
fields = []
rows = []

# her field ın max ve min değerlerinin listesini tutacağım liste.
AdgeValues = []   

# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)

	# extracting field names through first row
	fields = next(csvreader)

	# extracting each data row one by one
	for row in csvreader:
		
		rows.append(row)




	# get total number of rows
	size = len(rows)
	strSize = str(size)
	print("Total no. of rows: "+strSize)
