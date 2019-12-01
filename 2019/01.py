import math

def firstTask():
    fileObject = open("Sources/01_01.txt", "r")
    numbers = []

    for line in fileObject:
        numbers.append(int(line))

    sum = 0

    for number in numbers:
        sum += math.floor(number / 3) - 2

    print(sum)

def getFuelFuel(lastfuel):
    fuelfuel = math.floor(lastfuel / 3) - 2
    if fuelfuel <= 0:
        return 0
    else:
        return fuelfuel + getFuelFuel(fuelfuel)

def secondTask():
    fileObject = open("Sources/01_01.txt", "r")
    numbers = []

    for line in fileObject:
        numbers.append(int(line))

    sum = 0

    for number in numbers:
        sum += getFuelFuel(number)

    print(sum)

secondTask()