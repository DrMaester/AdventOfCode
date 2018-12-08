import re
from collections import defaultdict
nodes = {}

def getNumbers():
    # return [int(num) for num in re.findall(r'\d+', "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")]
    data = ""
    with open("Sources/08_01.txt") as file:
        data = file.readline()
    return [int(num) for num in re.findall(r'\d+', data)]

def getData(index, numbers):
    nodeIndex = index
    nodes[nodeIndex] = []
    childs = numbers[index]
    nodes[nodeIndex].append(childs)
    index += 1
    metaCount = numbers[index]
    index += 1
    lastIndex = index
    if childs > 0:
        for i in range(0, childs):
            nodes[nodeIndex].append(lastIndex)
            lastIndex= getData(lastIndex, numbers)
    if metaCount > 0:
        for i in range(lastIndex, lastIndex + metaCount):
            nodes[nodeIndex].append(numbers[i])
            index = i +1
    return index

def getValue(index):
    childs = nodes[index][0]
    value = 0
    if childs == 0:
        return sum(nodes[index][1:])
    else:
        childIndexes = nodes[index][nodes[index][0]+1:]
        for childIndex in childIndexes:
            if childIndex <= childs:
                value += getValue(nodes[index][childIndex])
    return value

def part2():
    numbers = getNumbers()
    getData(0, numbers)
    print(getValue(0))

part2()