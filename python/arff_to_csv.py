import arff

# Extra	Emoti	Agree	Consc	Openn
arffFile = open('cleanset.arff', 'r+', encoding='UTF-8')
csvFile = arff.load(arffFile)
print(csvFile)
