from item import Item

#Globals
ITEMS, KNAPSACK_SIZE = [], 0

def DynamicSolution():
    solution = [0 for item in ITEMS]
    dataTable = [[0 for index in range(0, KNAPSACK_SIZE + 1)] for itemIndex in range(0,len(ITEMS) + 1)]
    for rowIndex in range(0,len(dataTable)):
        for coloumnIndex in range(0, len(dataTable[0])):
            maxSide = ITEMS[rowIndex - 1].value + dataTable[rowIndex-1][coloumnIndex - ITEMS[rowIndex - 1].weight] if coloumnIndex >= ITEMS[rowIndex - 1].weight else 0
            dataTable[rowIndex][coloumnIndex] = 0 if rowIndex == 0 or coloumnIndex == 0 else max(dataTable[rowIndex-1][coloumnIndex],maxSide)

    solutionvalue = dataTable[-1][-1]
    currentValue = solutionvalue
    for currentIndex in range(len(dataTable) - 1,-1,-1):
        if currentValue in dataTable[currentIndex] and currentValue not in dataTable[currentIndex - 1]:
            solution[currentIndex - 1] = 1
            currentValue-= ITEMS[currentIndex - 1].value
        if currentValue == 0:
            break
    return solution, solutionvalue

def printSolution(solution,value):
    print("-----------------------------------------")
    print("DYNAMIC ALGORITHM:")
    print("For a knapsack of size: "+str(KNAPSACK_SIZE))
    if value > 0:
        print("Found solution: "+str(solution))
        print("with total value of: "+str(value))
        print("-----------------------------------------")
    else:
        print("No solution was found (empty knapsack)")

def main():
    solution, value = DynamicSolution()
    printSolution(solution,value)