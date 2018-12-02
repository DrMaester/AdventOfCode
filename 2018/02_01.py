# matrix = ["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]
matrix = []

file_object = open("Sources/02_01.txt", "r")
for line in file_object:
    matrix.append(line)

checksum = 1

checksumCounter = {}
for word in matrix:
    letterCounter = {}
    for char in word:
        if char in letterCounter.keys():
            letterCounter[char] += 1
        else:
            letterCounter[char] = 1

    hasCounted = []
    for count in letterCounter.values():
        if count in checksumCounter.keys() and count not in hasCounted:
            checksumCounter[count] += 1
            hasCounted.append(count)
        elif count > 1 and count not in hasCounted:
            checksumCounter[count] = 1
            hasCounted.append(count)
    
for count in checksumCounter.values():
    checksum *= count

print(checksum)