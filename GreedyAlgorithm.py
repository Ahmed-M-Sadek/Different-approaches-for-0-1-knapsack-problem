from item import Item

ITEMS, KNAPSACK_SIZE = [], 0

def SpecificVolume(individual):
    return individual.value / float(individual.weight)

def GreedyAlgorithm():
    sortedItemList = [(index, SpecificVolume(item)) for index, item in enumerate(ITEMS)]
    sortedItemList = sorted(sortedItemList, key=lambda x: x[1], reverse=True)

    currentValue = 0
    currentWeight = 0
    solution = [0] * len(ITEMS)

    for index, density in sortedItemList:
        if ITEMS[index].weight + currentWeight <= KNAPSACK_SIZE:
            currentValue+= ITEMS[index].value
            currentWeight+= ITEMS[index].weight
            solution[index] = 1
        if currentWeight == KNAPSACK_SIZE:
            break

    return solution, currentValue

def printSolution(solution,value):
    print("-----------------------------------------")
    print("GREEDY ALGORITHM:")
    print("For a knapsack of size: "+str(KNAPSACK_SIZE))
    if value > 0:
        print("Found solution: "+str(solution))
        print("with total value of: "+str(value))
        print("-----------------------------------------")
    else:
        print("No solution was found (empty knapsack)")

def main():
    solution, solutionValue = GreedyAlgorithm()
    printSolution(solution, solutionValue)