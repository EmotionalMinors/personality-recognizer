# personality-recognizer
Recognize personality of authors based on their text. "Forked" from [here](http://farm2.user.srcf.net/research/personality/recognizer)
## Required
Modify the `JAVAPATH` environment variable in `PersonalityRecognizer` to point to your machine's `java` executable
## Running Examples
The following Unix command computes personality scores (self-report) for each text in the examples directory, using standardized SVM models trained on written language:

`PersonalityRecognizer -i examples -d -t 2 -m 4`

The output of this command can be found in the file output.txt.
## Generating cleanset.arff
First, cleanset.csv must be converted into text files to be ingested by PersonalityRecognizer. This is done by creating `data/txt` and running: 

`python3 python/csv_to_txt.py`

After about 5 minutes, the files should be generated. To generate cleanset.arff using the SVM model, just run: 

`./PersonalityRecognizer -i data/conv -d -a cleanset.arff -t 2 -m 4`
## Generating text_max_traits.csv
To generate the final csv, just run:

`python3 python/arff_to_csv.py`
