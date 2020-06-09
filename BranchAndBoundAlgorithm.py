from item import Item
from collections import deque
from TreeNode import Node

#Globals
ITEMS, KNAPSACK_SIZE = [], 0
def Density(individual):
    return individual.value/float(individual.weight)

def BranchAndBoundAlgorithm():
    queue = deque()

    sortedItemList = [(index, Density(item)) for index, item in enumerate(ITEMS)]
    sortedItemList = sorted(sortedItemList, key=lambda x: x[1], reverse=True)

    bestNode = Node(0, 0.0, 0.0, 0.0, [])
    root = Node(0, 0.0, 0.0, getUpperBoundValue(bestNode, sortedItemList),  [])
    queue.appendleft(root)

    while len(queue) > 0:
        currentNode = queue.pop()
        if currentNode.bound > bestNode.value:
            index = sortedItemList[currentNode.treeLevel][0]
            nextCheckedItemValue = ITEMS[index].value
            nextCheckedItemWeight = ITEMS[index].weight
            nextAddednode = Node(currentNode.treeLevel + 1, currentNode.value + nextCheckedItemValue, currentNode.weight + nextCheckedItemWeight, currentNode.bound, currentNode.selectedItems + [index])

            if nextAddednode.weight <= KNAPSACK_SIZE:
                if nextAddednode.value > bestNode.value:
                    bestNode = nextAddednode

                if nextAddednode.bound > bestNode.value:
                    queue.appendleft(nextAddednode)

            nextNotAddedNode = Node(currentNode.treeLevel + 1, currentNode.value, currentNode.weight, currentNode.bound, currentNode.selectedItems)
            nextNotAddedNode.bound = getUpperBoundValue(nextNotAddedNode, sortedItemList)
            if nextNotAddedNode.bound > bestNode.value:
                queue.appendleft(nextNotAddedNode)

    bestSolution = [0] * len(ITEMS)
    for itemBit in bestNode.selectedItems:
        bestSolution[itemBit] = 1
    return bestSolution, int(bestNode.value)


def getUpperBoundValue(node, sortedItemList):
    if node.weight >= KNAPSACK_SIZE:
        return 0
    else:
        upperBound = node.value
        weightSum = node.weight
        currentTreeLevel = node.treeLevel

        while currentTreeLevel < len(ITEMS):
            index = sortedItemList[currentTreeLevel][0]

            if weightSum + ITEMS[index].weight > KNAPSACK_SIZE:
                value = ITEMS[index].value
                weight = ITEMS[index].weight
                upperBound += (KNAPSACK_SIZE - weightSum) * value/weight
                break
            upperBound += ITEMS[index].value
            weightSum += ITEMS[index].weight
            currentTreeLevel += 1

        return upperBound

def printSolution(solution,value):
    print("-----------------------------------------")
    print("BRANCH AND BOUND ALGORITHM:")
    print("For a knapsack of size: "+str(KNAPSACK_SIZE))
    if value > 0:
        print("Found solution: "+str(solution))
        print("with total value of: "+str(value))
        print("-----------------------------------------")
    else:
        print("No solution was found (empty knapsack)")

def main():
    solution, solutionValue = BranchAndBoundAlgorithm()
    printSolution(solution, solutionValue)