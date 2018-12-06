import re
import operator

XSize = 400
YSize = 400

def getCoords():
    raw = """78, 335
74, 309
277, 44
178, 286
239, 252
118, 354
170, 152
75, 317
156, 318
172, 45
138, 162
261, 195
306, 102
282, 67
53, 141
191, 237
352, 180
95, 247
353, 357
201, 327
316, 336
57, 43
119, 288
299, 328
125, 327
187, 186
121, 151
121, 201
43, 67
76, 166
238, 148
326, 221
219, 207
237, 160
345, 244
321, 346
48, 114
304, 80
265, 216
191, 92
54, 75
118, 260
336, 249
81, 103
290, 215
300, 246
293, 59
150, 274
296, 311
264, 286
""".splitlines()

    return [tuple(map(int, coord)) for coord in [re.match(r'(\d+)\, (\d+)', line).groups() for line in raw]]

def getDistance(x1, y1, x2, y2):
    return abs(abs((x2 - x1)) + abs((y2 - y1)))

def isInfinite(x,y):
    if x == 0 or y == 0 or x == XSize-1 or y == YSize-1:
        return True
    return False

names = iter("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
coords = {next(names):coord for coord in getCoords()}

field = {}
infinites = []

for y in range(0, XSize):
    for x in range(0, YSize):
        # print(x, " - " , y)
        shortestDistance = []
        multipleDistances = []
        for key in coords.keys():
            distance = getDistance(coords[key][0], coords[key][1], x, y)
            if shortestDistance:
                if distance < shortestDistance[1]:
                    shortestDistance.clear()
                    shortestDistance.append(key)
                    shortestDistance.append(distance)
                    multipleDistances.clear()
                elif distance == shortestDistance[1]:
                    multipleDistances.append((x,y))
            else:
                shortestDistance.append(key)
                shortestDistance.append(distance)
        # print(shortestDistance)
        if (x,y) in coords.values():
            key = [key for key,value in coords.items() if value == (x,y)][0]
            if(key in field.keys()):
                field[key] += 1                
            else:
                field[key] = 1
            if isInfinite(x,y):
                if key not in infinites:
                    infinites.append(key)
            # print(key, end=" ")
        elif (x,y) in multipleDistances:
            # print(".", end=" ")
            pass
        else:
            # print(shortestDistance[0], end=" ")
            if(shortestDistance[0] in field.keys()):
                field[shortestDistance[0]] += 1
            else:
                field[shortestDistance[0]] = 1
            if isInfinite(x,y):
                if shortestDistance[0] not in infinites:
                    infinites.append(shortestDistance[0])
    # print()
sorted_by_value = sorted(field.items(), key=lambda kv: kv[1])
[print(item) for item in sorted_by_value if item[0] not in infinites]