import arff
import numpy as np

# Extra	Emoti	Agree	Consc	Openn
OUTFILE="data/csv/text_max_traits.csv"
arffFile = open('cleanset.arff', 'r+', encoding='UTF-8')
csvFile = arff.load(arffFile)
# rows = np.asarray(csvFile["data"][0])
rows = csvFile["data"]
personality_dict = {}
p_scores = []
textScores = []
totalScores = 0
scoresSoFar = 0
print("progress:", end="", flush=True)
for row in rows:
	p_scores = row[-5:]
	fileName = row[0]
	personality_dict["extraversion"] = p_scores[0]
	personality_dict["neuroticism"] = p_scores[1]
	personality_dict["agreeableness"] = p_scores[2]
	personality_dict["conscientiousness"] = p_scores[3]
	personality_dict["openness"] = p_scores[4] 
	personality = max(personality_dict,key= personality_dict.get)
	fp = open(fileName, "r")
	text = fp.read()
	textScores.append([text.replace(",", " "), personality])
	totalScores += 1
	scoresSoFar += 1
	if scoresSoFar == 100:
		print("=", end="", flush=True)
		scoresSoFar = 0
textScores = np.asarray(textScores)
np.savetxt(OUTFILE, textScores, delimiter=',', header='text,MaxTrait', comments="", fmt='%s')
print(f"\n{totalScores} rows written to {OUTFILE}")
