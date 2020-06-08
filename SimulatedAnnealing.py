from item import Item
import math
import random

#CONSTANTS
ALPHA = 0.85
INITIAL_TEMPERATURE = 125
STEPS = 30000

#Globals
ITEMS, KNAPSACK_SIZE = [], 0

def initializeFirstSolution():
    solution = []
    possibleIndices = [x for x in range(len(ITEMS))]
    while len(possibleIndices) > 0:
        index = random.randint(0, len(possibleIndices) - 1)
        itemIndex = possibleIndices.pop(index)
        if calculateEnergy(solution + [itemIndex])[1] <= KNAPSACK_SIZE:
            solution.append(itemIndex)
        else:
            break
    return solution

def simulatedAnnealing():
    initialSolution = initializeFirstSolution()
    bestValue, solution = startSimulation(initialSolution)
    bestSolutionCompilation = [0 for x in range(0, len(ITEMS))]
    for index in solution:
        bestSolutionCompilation[index] = 1
    return bestValue, bestSolutionCompilation

def calculateEnergy(individual):
    value, weight = 0, 0
    for itemIndex in individual:
        weight += ITEMS[itemIndex].weight
        value += ITEMS[itemIndex].value
    return value, weight

def getMoveList(individual):
    moveList = []
    for index in range(0, len(ITEMS)):
        if index not in individual:
            possibleMove = individual.copy()
            possibleMove.append(index)
            if calculateEnergy(possibleMove)[1] <= KNAPSACK_SIZE:
                moveList.append(possibleMove)
    for index in range(0,len(individual)):
        possibleMove = individual.copy()
        possibleMove.remove(possibleMove[index])
        if possibleMove not in moveList:
            moveList.append(possibleMove)
    return moveList

def startSimulation(solution):
    temperature = INITIAL_TEMPERATURE

    bestSolution = solution
    bestValue = calculateEnergy(solution)[0]

    currentSolution = solution
    while True:
        currentValue = calculateEnergy(bestSolution)[0]
        for i in range(0, STEPS):
            moves = getMoveList(currentSolution)
            if len(moves) == 0:
                continue
            index = random.randint(0, len(moves) - 1)
            randomChoice = moves[index]
            change = calculateEnergy(randomChoice)[0] - bestValue
            if change > 0:
                bestSolution = randomChoice
                bestValue = calculateEnergy(bestSolution)[0]
                currentSolution = randomChoice
            else:
                if math.exp(change / float(temperature)) > random.random():
                    currentSolution = randomChoice

        temperature *= ALPHA
        if currentValue >= bestValue or temperature <= 0:
            break
    return bestValue, bestSolution

def printSolution(solution,value):
    print("-----------------------------------------")
    print("SIMULATED ANNEALING ALGORITHM:")
    print("For a knapsack of size: "+str(KNAPSACK_SIZE))
    if value > 0:
        print("Found solution: "+str(solution))
        print("with total value of: "+str(value))
        print("-----------------------------------------")
    else:
        print("No solution was found (empty knapsack)")

def main():
    solutionValue, solution = simulatedAnnealing()
    printSolution(solution,solutionValue)