fileObject = open("01_02.txt", "r")
numbers = []

for line in fileObject:
    numbers.append(int(line))

counter = {}
isCalibrated = False
calibratedNumber = 0

frequence = 0
while isCalibrated == False:
    for number in numbers:
        frequence += number
        if frequence in counter.keys():
            isCalibrated = True
            calibratedNumber = frequence
        else:
            counter[frequence] = 1
    
        if(isCalibrated):
            break
            
print(calibratedNumber)