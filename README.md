# personality-recognizer
Recognize personality of authors based on their text. "Forked" from [here](http://farm2.user.srcf.net/research/personality/recognizer)
## Requirements
- Modify the `JAVAPATH` environment variable in `PersonalityRecognizer` to point to your machine's `java` executable

- Add `LIWC.CAT` (Linguistic Inquiry and Word Counter 2001) and `mrc2.dct` (MRC Psycholinguistic Database) to the `lib` directory
## Running examples
The following Unix command computes personality scores (self-report) for each text in the examples directory, using standardized SVM models trained on written language:

`PersonalityRecognizer -i examples -d -t 2 -m 4`

## Generating newcleanset.csv
`newcleanset.csv` is the review data in `cleanset.csv` appended with the personality scores of the reviewers. To generate `newcleanset.csv`, just run:

`./run.sh`

`./run.sh` does the following:
### Generating cleanset.arff
First, `cleanset.csv` must be converted into text files to be ingested by `PersonalityRecognizer`. This is done by creating `data/txt` and running: 

`python3 python/csv_to_txt.py`

After about 5 minutes, the files should be generated. To generate `cleanset.arff` using the SVM model, the following is run: 

`./PersonalityRecognizer -i data/txt -d -a cleanset.arff -t 2 -m 4`
### Generating text_max_traits.csv
To generate the final csv, the following is run:

`python3 python/arff_to_csv.py`
