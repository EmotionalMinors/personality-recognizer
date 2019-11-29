# personality-recognizer
recognize personality of authors based on their text
## Instructions
Modify the `JAVAPATH` environment variable in `PersonalityRecognizer` to point to your machine's `java` executable
## Examples
The following Unix command computes personality scores (self-report) for each text in the examples directory, using standardized SVM models trained on written language:

`PersonalityRecognizer -i examples -d -t 2 -m 4`

The output of this command can be found in the file output.txt.
