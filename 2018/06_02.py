import re

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

coords = getCoords()

region = []
for x in range(0, 400):
    for y in range(0, 400):
        distances = []     
        for coord in coords:
            distance  = getDistance(x, y, coord[0], coord[1])
            distances.append(distance)
            # print(x, " | ", y, " -> ", coord[0], " | ", coord[1], " = ", distance)
        if sum(distances) < 10000:
            region.append((x,y))
print(len(region))