from item import Item

ITEMS, KNAPSACK_SIZE = [], 0

def DivideAndConquerAlgorithm(capacity, itemPointer):

    if itemPointer == 0 or capacity == 0 :
        return 0

    if (ITEMS[itemPointer-1].weight > capacity):
        return DivideAndConquerAlgorithm(capacity, itemPointer-1)

    else:
        return max(ITEMS[itemPointer-1].value + DivideAndConquerAlgorithm(capacity-ITEMS[itemPointer-1].weight, itemPointer-1), DivideAndConquerAlgorithm(capacity, itemPointer-1))

def printSolutionValue(value):
    print("-----------------------------------------")
    print("DIVIDE AND CONQUER ALGORITHM:")
    print("For a knapsack of size: "+str(KNAPSACK_SIZE))
    if value > 0:
        print("Found a solution with total value of: "+str(value))
        print("-----------------------------------------")
    else:
        print("No solution was found (empty knapsack)")

def main():
    solutionValue = DivideAndConquerAlgorithm(KNAPSACK_SIZE, len(ITEMS))
    printSolutionValue(solutionValue)