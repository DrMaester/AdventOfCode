import math
import sys

def getLines(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f]

def getDistance(position1, position2):
    return abs(position2[0] - position1[0]) + abs(position2[1] - position1[1])

def getClosest(startPosition, coords):
    shortestPosition = (0,0)
    shortestDistance = sys.maxsize
    for key in coords:
        if getDistance(startPosition, key) < shortestDistance:
            shortestDistance = getDistance(startPosition, key)
            shortestPosition = key

    return ([shortestPosition, shortestDistance])

def insertDown(coords, position, amount):
    for i in range(1, amount):
        if (position[0], position[1] - i) in coords:
            coords[(position[0], position[1] - i)] += 1
        else:
            coords[(position[0], position[1] - i)] = 1

def insertUp(coords, position, amount):
    for i in range(1, amount):
        if (position[0], position[1] + i) in coords:
            coords[(position[0], position[1] + i)] += 1
        else:
            coords[(position[0], position[1] + i)] = 1

def insertLeft(coords, position, amount):
    for i in range(1, amount):
        if (position[0] - i, position[1]) in coords:
            coords[(position[0] - i, position[1])] += 1
        else:
            coords[(position[0] - i, position[1])] = 1

def insertRight(coords, position, amount):
    for i in range(1, amount):
        if (position[0] + i, position[1]) in coords:
            coords[(position[0] + i, position[1])] += 1
        else:
            coords[(position[0] + i, position[1])] = 1

def getWireCoords(values, position):
    coords = {}
    for value in values.split(','):
        if value[0] == 'R':
            insertRight(coords, position, int(value[1:]))
            position = (position[0] + int(value[1:]), position[1])
        if value[0] == 'D':
            insertDown(coords, position, int(value[1:]))
            position = (position[0], position[1] - int(value[1:]))
        if value[0] == 'U':
            insertUp(coords, position, int(value[1:]))
            position = (position[0], position[1] + int(value[1:]))
        if value[0] == 'L':
            insertLeft(coords, position, int(value[1:]))
            position = (position[0] - int(value[1:]), position[1])

    return coords

def getIntersections(coords1, coords2):
    intersections = []

    for i in coords1.keys():
        if i in coords2.keys() and i not in intersections:
            intersections.append(i)

    return intersections

def getStepsToIntersection(intersection, currentPosition, values):
    steps = 0
    for value in values.split(','):
        if value[0] == 'R':
            for i in range(0, int(value[1:])):
                currentPosition = (currentPosition[0] + 1, currentPosition[1])
                steps += 1
                if currentPosition == intersection:
                    return steps
        if value[0] == 'D':
            for i in range(0, int(value[1:])):
                currentPosition = (currentPosition[0], currentPosition[1] - 1)
                steps += 1
                if currentPosition == intersection:
                    return steps
        if value[0] == 'U':
            for i in range(0, int(value[1:])):
                currentPosition = (currentPosition[0], currentPosition[1] + 1)
                steps += 1
                if currentPosition == intersection:
                    return steps
        if value[0] == 'L':
             for i in range(0, int(value[1:])):
                currentPosition = (currentPosition[0] - 1, currentPosition[1])
                steps += 1
                if currentPosition == intersection:
                    return steps

    return None

def firstTask():
    lines = getLines('Sources/03_01.txt')
    startPosition = (0,0)
    # lines = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
    
    coords1 = getWireCoords(lines[0], startPosition)
    coords2 = getWireCoords(lines[1], startPosition)
    intersections = getIntersections(coords1, coords2)
    print(getClosest(startPosition, intersections))

def secondTask():
    lines = getLines('Sources/03_01.txt')
    startPosition = (1,1)
    # lines = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
    
    coords1 = getWireCoords(lines[0], startPosition)
    coords2 = getWireCoords(lines[1], startPosition)
    intersections = getIntersections(coords1, coords2)
    closestSteps = sys.maxsize

    for intersection in intersections:
        steps = getStepsToIntersection(intersection, startPosition, lines[0]) + getStepsToIntersection(intersection, startPosition, lines[1])
        if steps < closestSteps:
            closestSteps = steps

    print(closestSteps)

# firstTask()
secondTask()