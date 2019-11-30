import arff
import csv
import os.path as path
from collections import OrderedDict 

CLEANSET_CSV_PATH = 'data/csv/cleanset.csv'
CLEANSET_ARFF_PATH = 'cleanset.arff'
CLEANSET_CSV_ENCODING = 'ISO-8859-1'
CLEANSET_ARFF_ENCODING = 'UTF-8'
PERSONALITY_HEADER = 'MaxTrait'
OUTFILE = 'data/csv/newcleanset.csv'

def get_dict_and_header():
	fp = open(CLEANSET_CSV_PATH, 'r', encoding = CLEANSET_CSV_ENCODING)
	reader = csv.reader(fp)
	clean_dict = OrderedDict()
	header = next(reader)
	header.append(PERSONALITY_HEADER)	
	# map row id to row
	for row in reader:
		clean_dict[row[0]] = row
	return clean_dict, header

def get_recognized_rows(): 
	arff_file = open(CLEANSET_ARFF_PATH, 'r+', encoding = CLEANSET_ARFF_ENCODING)
	csv_file = arff.load(arff_file)
	return csv_file["data"]

def hydrate_dict(clean_dict, rows):
	p_dict = {}
	p_scores = []
	for row in rows:
		# get personality scores and filename
		p_scores = row[-5:]
		row_id = path.basename(row[0]).split(".txt")[0]
		# map p scores
		p_dict["extraversion"] = p_scores[0]
		p_dict["neuroticism"] = p_scores[1]
		p_dict["agreeableness"] = p_scores[2]
		p_dict["conscientiousness"] = p_scores[3]
		p_dict["openness"] = p_scores[4] 
		max_trait = max(p_dict, key = p_dict.get)
		# add maxTrait column using filename
		clean_dict[row_id].append(max_trait)

def write_out_dict(clean_dict, header):
	outfile = csv.writer(open(OUTFILE, 'w'))
	outfile.writerow(header)
	for k in clean_dict.keys():
		outfile.writerow(clean_dict[k])
	print(f"{len(clean_dict.values())} rows written to {OUTFILE}")

if __name__ == "__main__":
	clean_dict, header = get_dict_and_header()
	rows = get_recognized_rows()
	hydrate_dict(clean_dict, rows)
	write_out_dict(clean_dict, header)
