import re
metaSum = 0

def getNumbers():
    # return [int(num) for num in re.findall(r'\d+', "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")]
    data = ""
    with open("Sources/08_01.txt") as file:
        data = file.readline()
    return [int(num) for num in re.findall(r'\d+', data)]

def getData(index, numbers):
    global metaSum
    childs = numbers[index]
    index += 1
    metaCount = numbers[index]
    index += 1
    lastIndex = index
    if childs > 0:
        for i in range(0, childs):
            lastIndex = getData(lastIndex, numbers)
    if metaCount > 0:
        for i in range(lastIndex, lastIndex + metaCount):    
            # print("MetaData: ", numbers[i])        
            metaSum += numbers[i]
            index = i +1 
    # print("Childs: ", childs, " - ", "MetaCount: ", metaCount, " - ", "CurrSum: ", metaSum)
    return index
    
    

def part1():
    numbers = getNumbers()
    index = 0
    lastIndex = getData(index, numbers)
    print(metaSum)

part1()