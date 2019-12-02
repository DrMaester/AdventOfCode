def getLines(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f]

def getInitNumbers():
    lines = getLines('Sources/02_01.txt')
    line = "1,9,10,3,2,3,11,0,99,30,40,50"
    numbers = [int(num) for num in lines[0].split(',')]
    
    return numbers

def replaceNounAndVerb(numbers, noun, verb):
    numbers[1] = noun
    numbers[2] = verb
    return numbers

def firstTask():
    numbers = replaceNounAndVerb(getInitNumbers(),12,2)
    opcodeIndex = 0

    while numbers[opcodeIndex] == 1 or numbers[opcodeIndex] == 2:
        if numbers[opcodeIndex] == 1:
            numbers[numbers[opcodeIndex + 3]] = numbers[numbers[opcodeIndex + 1]] + numbers[numbers[opcodeIndex + 2]]
        elif numbers[opcodeIndex] == 2:
            numbers[numbers[opcodeIndex + 3]] = numbers[numbers[opcodeIndex + 1]] * numbers[numbers[opcodeIndex + 2]]
        
        opcodeIndex += 4

    print(numbers[0])

def secondTask():
    noun = 0
    verb = 0
    result = 0

    for x in range(0,99):
        noun = x
        for y in range(0,99):
            verb = y 
            numbers = replaceNounAndVerb(getInitNumbers(), noun, verb)
            opcodeIndex = 0
            while numbers[opcodeIndex] == 1 or numbers[opcodeIndex] == 2:
                if numbers[opcodeIndex] == 1:
                    numbers[numbers[opcodeIndex + 3]] = numbers[numbers[opcodeIndex + 1]] + numbers[numbers[opcodeIndex + 2]]
                elif numbers[opcodeIndex] == 2:
                    numbers[numbers[opcodeIndex + 3]] = numbers[numbers[opcodeIndex + 1]] * numbers[numbers[opcodeIndex + 2]]
                
                opcodeIndex += 4

            result = numbers[0]
            if result == 19690720:
                break
        
        if result == 19690720:
            break

    print(f"noun is {noun} and verb is {verb}")
    print(f"result = {100 * noun + verb}")

# firstTask()
secondTask()