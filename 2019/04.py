import re

def isNeverDecreasing(number):
    lastNumber = 0
    for digit in str(number):
        if int(digit) < int(lastNumber):
            return False
        lastNumber = digit

    return True

def hasTwoAdjacentSameNumbers(number):
    lastNumber = 0
    for digit in str(number):
        if int(digit) == int(lastNumber):
            return True
        lastNumber = digit

    return False
    
def hasTwoAdjacentSameNumbers2(number):
    num = str(number)
    matches = re.findall('00+|11+|22+|33+|44+|55+|66+|77+|88+|99+', num)
    if matches and min([len(match) for match in matches])==2:
        return True
    else:
        return False

def meetsCriteria(number):
    if isNeverDecreasing(number) and hasTwoAdjacentSameNumbers(number):
        return True
    return False

def meetsCriteria2(number):
    if isNeverDecreasing(number) and hasTwoAdjacentSameNumbers2(number):
        return True
    return False

def firstTask():
    min = 353096
    max = 843212
    count = 0
    for number in range(min, max + 1):
        if meetsCriteria(number):
            count += 1

    print(count)

def secondTask():
    min = 353096
    max = 843212
    count = 0
    for number in range(min, max + 1):
        if meetsCriteria2(number):
            count += 1

    print(count)

# firstTask()
secondTask()