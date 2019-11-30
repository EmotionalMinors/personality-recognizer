import os
import csv

outPath = "data/text_files/"
fileName = "data/csv/cleanset.csv"
csvFile = open(fileName, "rU", encoding='ISO-8859-1')
reader = csv.reader(csvFile, delimiter=',')
next(reader)
for row in reader:
	print(row[1], row[11])
	f = open(os.path.join(outPath, row[1] + ".txt"), "w+")
	f.write(row[11])
	break
