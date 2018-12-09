import re
import blist

def getNextIndex(index, circle, change):
    newIndex = index + change
    if newIndex < 0:
        return getNextIndex(len(circle), circle, newIndex)
    elif newIndex > len(circle) -1:
        return getNextIndex(0, circle, newIndex - len(circle))
    else:
        return newIndex

def part1():

    line = "418 players; last marble is worth 71339 points"
    playerCount, lastMarble = [int(value) for value in re.findall(r'\d+', line)]
    lastMarble *= 100
    players = [i+1 for i in range(0, playerCount)]
    circle = blist.blist([0])
    scores = {player:0 for player in players}
    currPlayer = 1
    index = 1
    count = 0

    for marble in range(1, lastMarble):
        if marble % int((lastMarble / 100)) == 0:
            count += 1
            print(count, "% Done")

        if currPlayer > playerCount:
            currPlayer = 1

        if len(circle) == 1:
            circle.append(marble)
            currPlayer += 1
            continue

        if marble % 23 == 0:
            rmIndex = getNextIndex(index, circle, -7)
            scores[currPlayer] += marble
            scores[currPlayer] += circle[rmIndex]
            index = rmIndex
            del circle[rmIndex]
            # circle = circle[0:rmIndex] + circle[rmIndex+1:]
        else:
            newIndex = getNextIndex(index, circle, 2)
            if newIndex == 0:
                circle.append(marble)
                index = len(circle) -1
            else:
                circle.insert(newIndex, marble)
                index = newIndex
        
        if marble >= lastMarble:
            break
        else:
            currPlayer += 1
            continue

    # nextTurn(players, 1, 1, 1, circle, scores, lastMarble)
    [print("Player: ", k, " - Score: ", v) for k,v in scores.items() if v == max(scores.values())]
    # [print("Player: ", k, " - Score: ", v) for k,v in scores.items()]

part1()