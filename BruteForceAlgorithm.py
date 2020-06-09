from item import Item

#Globals
ITEMS, KNAPSACK_SIZE = [], 0

def getValueAndWeightWithNewList(individual):
    value = 0
    weight = 0
    newList = []
    for index,bit in enumerate(individual):
        bit = int(bit)
        if bit == 1:
            value+= ITEMS[index].value
            weight+= ITEMS[index].weight
        newList.append(bit)
    return value, weight, newList

def BruteForceAlgorithm():
    bestSolution = []
    bestSolutionValue = -1

    currentSolution = bestSolution
    currentSolutionValue = bestSolutionValue

    for number in range(0,pow(2,len(ITEMS))):
        currentSolution = list(format(number, '0{}b'.format(len(ITEMS))))
        currentSolutionValue, weight, currentSolution = getValueAndWeightWithNewList(currentSolution)
        if weight <= KNAPSACK_SIZE and currentSolutionValue > bestSolutionValue:
            bestSolution = currentSolution
            bestSolutionValue = currentSolutionValue

    return bestSolution, bestSolutionValue

def printSolution(solution, value):
    print("-----------------------------------------")
    print("BRUTE FORCE ALGORITHM:")
    print("For a knapsack of size: "+str(KNAPSACK_SIZE))
    if value > 0:
        print("Found solution: "+str(solution))
        print("with total value of: "+str(value))
        print("-----------------------------------------")
    else:
        print("No solution was found (empty knapsack)")

def main():
    solution, solutionValue = BruteForceAlgorithm()
    printSolution(solution,solutionValue)
