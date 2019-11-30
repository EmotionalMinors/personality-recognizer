import arff
import csv
import os.path as path
from collections import OrderedDict 

# Extra	Emoti	Agree	Consc	Openn
OUTFILE="data/csv/newcleanset.csv"
fp = open('data/csv/cleanset.csv', 'r', encoding='ISO-8859-1')
reader = csv.reader(fp)
cleanDict = OrderedDict()
headers = next(reader)
headers.append("MaxTrait")
print(headers)
# map row id to row
for row in reader:
	cleanDict[row[0]] = row
# convert arff to csv 
arffFile = open('cleanset.arff', 'r+', encoding='UTF-8')
csvFile = arff.load(arffFile)
rows = csvFile["data"]

outFile = csv.writer(open(OUTFILE, 'w'))
personality_dict = {}
p_scores = []
textScores = []
totalScores = 0
scoresSoFar = 0

print("progress:", end="", flush=True)
for row in rows:
	# get personality scores and replace dummy character
	p_scores = row[-5:]
	row_id = path.basename(row[0]).split(".txt")[0]
	# map p scores
	personality_dict["extraversion"] = p_scores[0]
	personality_dict["neuroticism"] = p_scores[1]
	personality_dict["agreeableness"] = p_scores[2]
	personality_dict["conscientiousness"] = p_scores[3]
	personality_dict["openness"] = p_scores[4] 
	maxTrait = max(personality_dict, key = personality_dict.get)
	# add maxTrait column
	cleanDict[row_id].append(maxTrait)
	totalScores += 1
	scoresSoFar += 1
	if scoresSoFar == 100:
		print("=", end="", flush=True)
		scoresSoFar = 0
# write out dictionary to csv 
outFile.writerow(headers)
for k in cleanDict.keys():
	outFile.writerow(cleanDict[k])
print(f"\n{totalScores} rows written to {OUTFILE}")
