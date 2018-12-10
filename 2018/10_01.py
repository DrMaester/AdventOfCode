import re
import os
import time
import blist
def getLines():
#     raw = """position=< 9,  1> velocity=< 0,  2>
# position=< 7,  0> velocity=<-1,  0>
# position=< 3, -2> velocity=<-1,  1>
# position=< 6, 10> velocity=<-2, -1>
# position=< 2, -4> velocity=< 2,  2>
# position=<-6, 10> velocity=< 2, -2>
# position=< 1,  8> velocity=< 1, -1>
# position=< 1,  7> velocity=< 1,  0>
# position=<-3, 11> velocity=< 1, -2>
# position=< 7,  6> velocity=<-1, -1>
# position=<-2,  3> velocity=< 1,  0>
# position=<-4,  3> velocity=< 2,  0>
# position=<10, -3> velocity=<-1,  1>
# position=< 5, 11> velocity=< 1, -2>
# position=< 4,  7> velocity=< 0, -1>
# position=< 8, -2> velocity=< 0,  1>
# position=<15,  0> velocity=<-2,  0>
# position=< 1,  6> velocity=< 1,  0>
# position=< 8,  9> velocity=< 0, -1>
# position=< 3,  3> velocity=<-1,  1>
# position=< 0,  5> velocity=< 0, -1>
# position=<-2,  2> velocity=< 2,  0>
# position=< 5, -2> velocity=< 1,  2>
# position=< 1,  4> velocity=< 2,  1>
# position=<-2,  7> velocity=< 2, -2>
# position=< 3,  6> velocity=<-1, -1>
# position=< 5,  0> velocity=< 1,  0>
# position=<-6,  0> velocity=< 2,  0>
# position=< 5,  9> velocity=< 1, -2>
# position=<14,  7> velocity=<-2,  0>
# position=<-3,  6> velocity=< 2, -1>
# """.splitlines()

    file_object = open("Sources/10_01.txt")
    raw = []
    for line in file_object:
        raw.append(line)

    return raw

def move(stars):
    for star in stars:
        star[0] += star[2]
        star[1] += star[3]

def part1():

    stars = blist.blist()

    for line in getLines():
        posX, posY, velX, velY = re.findall(r'([-]?\d+)', line)
        # print("Position: ", posX, "|", posY, "  Velocity: ", velX, "|", velY)
        stars.append(blist.blist([int(posX), int(posY), int(velX), int(velY)]))

    # print(stars)

    minX= 0
    minY= 0
    maxX= 0
    maxY= 0
    seconds = 0
    closeFormation = False    
    while(closeFormation == False):
        valuesX = [star[0] for star in stars]
        valuesY = [star[1] for star in stars]

        if max(valuesX) - min(valuesX) < 100:
            closeFormation = True
            minX = min(valuesX)
            minY = min(valuesY)
            maxX = max(valuesX)
            maxY = max(valuesY)

        move(stars)
        seconds += 1
    
    # print(stars)
    counter = 0
    while(counter < 10):
        # time.sleep(2)
        # os.system("cls")
        print("second: ", seconds)
        for y in range(minY, maxY):
            for x in range(minX, maxX):
                if True in [True for star in stars if star[0] == x and star[1] == y]:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()
        move(stars)
        seconds += 1
        counter += 1

    print(stars)

part1()