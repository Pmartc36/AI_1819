import random
import time
import sys
sys.setrecursionlimit(50000)
backtrack = 0

def initialState(n):
    thisList = []
    for i in range(0, n):
        thisList.append(-1)
    return thisList
def cspMinConflicts(state, currentRowNum, listOfPos):
    if currentRowNum == len(state):
        return state
    conflictCols = []
    for collumn in range(0, len(state)):

    for collumn in range(0, len(state)):    #POSSIBLE IMPROVEMENT #O(N) Try a different starting position
        shouldPass = False
        for queen in listOfPos:             #POSSIBLE IMPROVEMENT O(N^2)
            if currentRowNum == queen[0]:
                shouldPass = True
            if collumn == queen[1]:
                shouldPass = True
            if queen[0] + queen[1] == currentRowNum + collumn:
                shouldPass = True
            if collumn - queen[1] == currentRowNum - queen[0]:
                shouldPass = True
        if shouldPass == True:
                continue
        state[currentRowNum] = collumn
        listOfPos.append((currentRowNum, collumn))
        result = csp(state.copy(), currentRowNum+1, listOfPos.copy())   #POSSIBLE IMPROVEMENT: Maybe decrease recursive calls?
        if result is not None:
            return result
        else:
            listOfPos = listOfPos[:-1] #O(N) Use of data structure other than list
    return None
def cspRandVarVal(state, listOfPos, setOfRandRows, numRowsVisited): #state is a list
    if numRowsVisited == len(state):
        return state
    currentRowNum = 0
    if len(state) != 0:
        currentRowNum = random.randint(0, len(state)-1)
    while currentRowNum in setOfRandRows:
        currentRowNum = random.randint(0, len(state) - 1)
    setOfRandRows.add(currentRowNum)
    dictTriedStates = dict()
    numTrue = 0
    for col in range(0, len(state)):
        dictTriedStates[col] = False
    while numTrue != len(state):    #POSSIBLE IMPROVEMENT #O(N) Try a different starting position
        numCols = len(state)-1
        collumn = random.randint(0, numCols)
        while dictTriedStates[collumn] == True:
            collumn = random.randint(0, len(state)-1)
        for queen in listOfPos:             #POSSIBLE IMPROVEMENT O(N^2)
            if currentRowNum == queen[0]:
                dictTriedStates[collumn] = True
            if collumn == queen[1]:
                dictTriedStates[collumn] = True
            if queen[0] + queen[1] == currentRowNum + collumn:
                dictTriedStates[collumn] = True
            if collumn - queen[1] == currentRowNum - queen[0]:
                dictTriedStates[collumn] = True
        if dictTriedStates[collumn] == True:
            numTrue += 1
            continue
        state[currentRowNum] = collumn
        listOfPos.append((currentRowNum, collumn))
        result = cspRandVar(state.copy(), listOfPos.copy(), setOfRandRows.copy(), numRowsVisited+1)   #POSSIBLE IMPROVEMENT: Maybe decrease recursive calls?
        if result is not None:
            return result
        else:
            numTrue += 1
            dictTriedStates[collumn] = True
            listOfPos = listOfPos[:-1] #O(N) Use of data structure other than list
    return None
def cspRandVar(state, listOfPos, setOfRandRows, numRowsVisited): #state is a list
    if numRowsVisited == len(state):
        return state
    currentRowNum = 0
    if len(state) != 0:
        currentRowNum = random.randint(0, len(state)-1)
    while currentRowNum in setOfRandRows:
        currentRowNum = random.randint(0, len(state) - 1)
    setOfRandRows.add(currentRowNum)
    for collumn in range(0, len(state)):    #POSSIBLE IMPROVEMENT #O(N) Try a different starting position
        shouldPass = False
        for queen in listOfPos:             #POSSIBLE IMPROVEMENT O(N^2)
            if currentRowNum == queen[0]:
                shouldPass = True
            if collumn == queen[1]:
                shouldPass = True
            if queen[0] + queen[1] == currentRowNum + collumn:
                shouldPass = True
            if collumn - queen[1] == currentRowNum - queen[0]:
                shouldPass = True
        if shouldPass == True:
                continue
        state[currentRowNum] = collumn
        listOfPos.append((currentRowNum, collumn))
        result = cspRandVar(state.copy(), listOfPos.copy(), setOfRandRows.copy(), numRowsVisited+1)   #POSSIBLE IMPROVEMENT: Maybe decrease recursive calls?
        if result is not None:
            return result
        else:
            listOfPos = listOfPos[:-1] #O(N) Use of data structure other than list
    return None
def cspRandValue(state, currentRowNum, listOfPos):
    if currentRowNum == len(state):
        return state
    dictTriedStates = dict()
    numTrue = 0
    for col in range(0, len(state)):
        dictTriedStates[col] = False
    while numTrue != len(state):    #POSSIBLE IMPROVEMENT #O(N) Try a different starting position
        numCols = len(state)-1
        collumn = random.randint(0, numCols)
        while dictTriedStates[collumn] == True:
            collumn = random.randint(0, len(state)-1)
        for queen in listOfPos:             #POSSIBLE IMPROVEMENT O(N^2)
            if currentRowNum == queen[0]:
                dictTriedStates[collumn] = True
            if collumn == queen[1]:
                dictTriedStates[collumn] = True
            if queen[0] + queen[1] == currentRowNum + collumn:
                dictTriedStates[collumn] = True
            if collumn - queen[1] == currentRowNum - queen[0]:
                dictTriedStates[collumn] = True
        if dictTriedStates[collumn] == True:
            numTrue += 1
            continue
        state[currentRowNum] = collumn
        listOfPos.append((currentRowNum, collumn))
        result = cspRandValue(state.copy(), currentRowNum+1, listOfPos.copy())   #POSSIBLE IMPROVEMENT: Maybe decrease recursive calls?
        if result is not None:
            return result
        else:
            numTrue += 1
            dictTriedStates[collumn] = True
            listOfPos = listOfPos[:-1] #O(N) Use of data structure other than list
    return None
def csp(state, currentRowNum, listOfPos): #state is a list
    if currentRowNum == len(state):
        return state
    for collumn in range(0, len(state)):    #POSSIBLE IMPROVEMENT #O(N) Try a different starting position
        shouldPass = False
        for queen in listOfPos:             #POSSIBLE IMPROVEMENT O(N^2)
            if currentRowNum == queen[0]:
                shouldPass = True
            if collumn == queen[1]:
                shouldPass = True
            if queen[0] + queen[1] == currentRowNum + collumn:
                shouldPass = True
            if collumn - queen[1] == currentRowNum - queen[0]:
                shouldPass = True
        if shouldPass == True:
                continue
        state[currentRowNum] = collumn
        listOfPos.append((currentRowNum, collumn))
        result = csp(state.copy(), currentRowNum+1, listOfPos.copy())   #POSSIBLE IMPROVEMENT: Maybe decrease recursive calls?
        if result is not None:
            return result
        else:
            listOfPos = listOfPos[:-1] #O(N) Use of data structure other than list
    return None
#def test_code():
#    print(cspRandValue(initialState(int(sys.argv[1])), 0, []))
#    solve_time = 0
#    size = 8
#    while solve_time < 2:
#        start = time.perf_counter()
#        state = cspRandVarVal(initialState(size), [], set(), 0)
#        end = time.perf_counter()
#        size += 1
#        solve_time = end - start
#    print("For size %s, the time was %s." % (size, solve_time))
if __name__ == '__main__':
    print(cspRandValue(initialState(int(sys.argv[1])), 0, []))
