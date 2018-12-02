def GetCommonLetters(key, value):
    commonLetters = ""
    for i in range(0, len(key)):
        if key[i] == value[i]:
            commonLetters += key[i]
    return commonLetters

# matrix = ["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"]

file_object = open("Sources/02_01.txt", "r")
matrix = []

for line in file_object:
    matrix.append(line)

similarWords = {}
for word in matrix:
    for checkWord in matrix:
        differences = 0
        if (word == checkWord):
            continue
        else:
            for i in range(0, len(word)):
                if(word[i] != checkWord[i]):
                    differences += 1
                     
        if differences == 1:
            similarWords[word] = checkWord

commonWords = []
for word in similarWords.keys():
    commonWord = GetCommonLetters(word, similarWords[word])
    if commonWord not in commonWords:
        commonWords.append(commonWord)

print(commonWord)