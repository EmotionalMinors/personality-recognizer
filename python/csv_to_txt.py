import os
import csv

OUTPATH = "data/txt/"
FILENAME = "data/csv/cleanset.csv"
csvFile = open(FILENAME, "rU", encoding='ISO-8859-1')
reader = csv.reader(csvFile, delimiter=',')
next(reader)
totalCreated = 0
createdSoFar = 0
print("progress:", end="", flush=True)
for row in reader:
	title = ":".join(row[1].split(":", 2)[:2]).replace("/", ":")
	f = open(os.path.join(OUTPATH, title + ".txt"), "w+")
	f.write(row[11])
	createdSoFar += 1
	totalCreated += 1
	if createdSoFar == 100:
		print("=", end="", flush=True)
		createdSoFar = 0
print(f"\n{totalCreated} rows written to {totalCreated} files in {OUTPATH}")
