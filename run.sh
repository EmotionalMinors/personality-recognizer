#!/bin/bash
if [[ $1 == "csv" ]]; then
	python3 python3/csv_to_txt.py
else
if [[ $1 == "arff" ]]; then
	python3 python3/arff_to_csv.py
else
if [[ $1 == "rec" ]]; then
	./PersonalityRecognizer -i data/txt -d -a cleanset.arff -t 2 -m 4
else 
	python3 python3/csv_to_txt.py
	./PersonalityRecognizer -i data/txt -d -a cleanset.arff -t 2 -m 4
	python3 python3/arff_to_csv.py
fi
fi
fi
