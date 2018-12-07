import re
from collections import defaultdict

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getLines():
    raw = """Step B must be finished before step X can begin.
Step V must be finished before step F can begin.
Step K must be finished before step C can begin.
Step S must be finished before step D can begin.
Step C must be finished before step A can begin.
Step H must be finished before step X can begin.
Step Q must be finished before step W can begin.
Step X must be finished before step F can begin.
Step J must be finished before step R can begin.
Step D must be finished before step O can begin.
Step F must be finished before step P can begin.
Step M must be finished before step Z can begin.
Step R must be finished before step I can begin.
Step Y must be finished before step O can begin.
Step G must be finished before step Z can begin.
Step Z must be finished before step P can begin.
Step O must be finished before step L can begin.
Step A must be finished before step P can begin.
Step U must be finished before step L can begin.
Step L must be finished before step W can begin.
Step P must be finished before step W can begin.
Step I must be finished before step W can begin.
Step E must be finished before step N can begin.
Step W must be finished before step N can begin.
Step T must be finished before step N can begin.
Step G must be finished before step E can begin.
Step K must be finished before step T can begin.
Step I must be finished before step T can begin.
Step V must be finished before step H can begin.
Step W must be finished before step T can begin.
Step M must be finished before step A can begin.
Step C must be finished before step W can begin.
Step B must be finished before step Y can begin.
Step Y must be finished before step N can begin.
Step L must be finished before step N can begin.
Step M must be finished before step R can begin.
Step L must be finished before step I can begin.
Step J must be finished before step N can begin.
Step K must be finished before step M can begin.
Step O must be finished before step U can begin.
Step P must be finished before step N can begin.
Step Y must be finished before step I can begin.
Step V must be finished before step Q can begin.
Step H must be finished before step R can begin.
Step M must be finished before step P can begin.
Step K must be finished before step L can begin.
Step J must be finished before step A can begin.
Step D must be finished before step F can begin.
Step Q must be finished before step P can begin.
Step C must be finished before step H can begin.
Step U must be finished before step I can begin.
Step A must be finished before step T can begin.
Step C must be finished before step P can begin.
Step U must be finished before step T can begin.
Step O must be finished before step T can begin.
Step O must be finished before step I can begin.
Step S must be finished before step I can begin.
Step Z must be finished before step E can begin.
Step Y must be finished before step T can begin.
Step K must be finished before step O can begin.
Step O must be finished before step A can begin.
Step Z must be finished before step T can begin.
Step Z must be finished before step U can begin.
Step U must be finished before step P can begin.
Step P must be finished before step I can begin.
Step S must be finished before step W can begin.
Step S must be finished before step P can begin.
Step S must be finished before step Q can begin.
Step C must be finished before step E can begin.
Step G must be finished before step U can begin.
Step D must be finished before step L can begin.
Step K must be finished before step S can begin.
Step R must be finished before step O can begin.
Step C must be finished before step G can begin.
Step V must be finished before step G can begin.
Step A must be finished before step W can begin.
Step Z must be finished before step O can begin.
Step J must be finished before step O can begin.
Step F must be finished before step E can begin.
Step U must be finished before step E can begin.
Step E must be finished before step W can begin.
Step M must be finished before step O can begin.
Step C must be finished before step U can begin.
Step G must be finished before step P can begin.
Step C must be finished before step I can begin.
Step Z must be finished before step A can begin.
Step C must be finished before step J can begin.
Step Q must be finished before step R can begin.
Step E must be finished before step T can begin.
Step F must be finished before step Y can begin.
Step Z must be finished before step N can begin.
Step I must be finished before step N can begin.
Step X must be finished before step E can begin.
Step I must be finished before step E can begin.
Step Q must be finished before step O can begin.
Step R must be finished before step L can begin.
Step K must be finished before step W can begin.
Step Y must be finished before step L can begin.
Step M must be finished before step I can begin.
Step F must be finished before step O can begin.
Step A must be finished before step E can begin.
""".splitlines()
    return raw

def getNextAvailable(done, required, busyWorker):
    availables = [key for key,value in required.items() if key not in done and False not in [False for value in required[key] if value not in done]
    and key not in [busySteps[0] for busySteps in busyWorker.values()]]

    # foo = [busySteps[0] for busySteps in busyWorker.values()]
    return availables

def setWork(busyWorker, worker, step):
    time = abc.index(step) + 61
    busyWorker[worker] = [step, time]

def part2():
    required = defaultdict(list)
    steps = []
    for line in getLines():
        cprev, cnext = re.findall(r' (\w) ', line)
        if cnext in required.keys():
            if cprev not in required[cnext]:
                required[cnext].append(cprev)
        else:
            required[cnext].append(cprev)
        if cprev not in steps:
            steps.append(cprev)

    roots = [step for step in steps if step not in [key for key in required.keys()]]    
    for root in roots:
        required[root] = []

    availableWorker = [1,2,3,4,5]
    freeWorker = availableWorker
    busyWorker = {}
    done = []
    available = roots
    second = 0
    while(len(done) < len(required)):
        freeWorker = [worker for worker in availableWorker if worker not in busyWorker.keys()]
        available.sort()
        for worker in freeWorker:
            if available:
                setWork(busyWorker, worker, available[0])
                available = available[1:]

        freeWorker = [worker for worker in availableWorker if worker not in busyWorker.keys()]

        doneWorker = []
        if busyWorker:
            for worker in busyWorker:
                if busyWorker[worker][1] == 1:
                    done.append(busyWorker[worker][0])
                    doneWorker.append(worker)
                else:
                    busyWorker[worker][1] -= 1
        
        busyWorker = dict([[k,v] for k,v in busyWorker.items() if k not in doneWorker])

        available = getNextAvailable(done, required, busyWorker)
        # [available.append(char) for char in roots if char not in done and char not in available and ]
        second += 1
    
    print(second)
part2()