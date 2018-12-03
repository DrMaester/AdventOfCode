import re

# matrix = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
file_object = open("Sources/03_01.txt","r")
matrix = []
for line in file_object:
	matrix.append(line)

field = {}

for i in range(0, len(matrix)):

	IDRaw = re.findall('#[0-9]+', matrix[i])[0]
	PosRaw = re.findall('[0-9]+,[0-9]+', matrix[i])[0]
	SizeRaw = re.findall('[0-9]+x[0-9]+', matrix[i])[0]
	
	ID = re.findall('[0-9]+', IDRaw)
	Pos = re.findall('[0-9]+', PosRaw)
	Size = re.findall('[0-9]+', SizeRaw)

	# print("ID: ", ID, "- Pos: ", Pos, "- Size: ", Size)

	for x in range(int(Pos[0]), int(Pos[0]) + int(Size[0])):
		for y in range(int(Pos[1]), int(Pos[1]) + int(Size[1])):
			if (x, y) in field.keys():
				field[(x,y)] += 1
			else:
				field[(x,y)] = 1

counter = 0
for item in field.keys():
	if field[item] > 1:
		counter += 1

print(counter)