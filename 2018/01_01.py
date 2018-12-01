fileObject = open("01_01.txt", "r")
numbers = []

for line in fileObject:
    numbers.append(int(line))

result = 0
for number in numbers:
    result += number

print(result)