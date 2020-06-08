from item import Item
import random
import matplotlib.pyplot as plt

#Generating functions
def startPopulation():
    return [generateChromosome() for i in range(0,MAX_POPULATION_SIZE)]
def generateChromosome():
    return [random.randint(0,1) for i in range(0,len(ITEMS))]


#CONSTANTS
MAX_GENERATIONS = 1000
MAX_POPULATION_SIZE = 300
MIN_PARENT_POPULATION_RATIO = 0.2
MUTATION_CHANCE = 0.59
SELECTION_CHANCE = 0.1
DIVIDER_VALUE = 2

ITEMS, KNAPSACK_SIZE = [], 0

#Printing functions
def printSolution(currentPopulation):
    bestFitness = fitness(currentPopulation[0])
    print("-----------------------------------------")
    print("GENETIC ALGORITHM:")
    print("For a knapsack of size: "+str(KNAPSACK_SIZE))
    if bestFitness > 0:
        print("Found solution: "+str(currentPopulation[0]))
        print("with total value of: "+str(bestFitness))
        print("-----------------------------------------")
    else:
        print("No solution was found (empty knapsack)")

def plotData(x,y,textX,textY,titleText):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel=textX, ylabel=textY,
    title=titleText)
    ax.grid()
    #fig.savefig("test.png")
    plt.show()

#Fitness function for calculating accumulative value of selected items
def fitness(chromosome):
    valueSum = 0
    WeightSum = 0
    itemIndex = 0
    for inputBit in chromosome:
        if itemIndex >= len(ITEMS):
            break
        elif inputBit == 1:
            valueSum += ITEMS[itemIndex].value
            WeightSum += ITEMS[itemIndex].weight
        itemIndex += 1
    if WeightSum <= KNAPSACK_SIZE:
        return valueSum
    else:
        return -1

def getTotalWeight(chromosome):
    totalWeight = 0
    index = 0
    for bit in chromosome:
        if bit == 1:
            totalWeight+= ITEMS[index].weight
        index+=1
    return totalWeight

def selection(parentPool, probabilityList):
    chosen = parentPool[-1]
    randomChance = random.random()
    for index,probability in enumerate(probabilityList):
        if randomChance < probability:
            chosen = parentPool[index]
            break
    return chosen

def mutate(chromosome):
    index = random.randint(0,len(chromosome) - 1)
    if chromosome[index] == 0:
        chromosome[index] = 1
    else:
        chromosome[index] = 0

def newPopulationEvolution(population):

    parentPoolSize = int(MIN_PARENT_POPULATION_RATIO*len(population))
    parentPool = population[:parentPoolSize]
    nonParentPool = population[parentPoolSize:]
    for np in nonParentPool:
        if(random.random() < SELECTION_CHANCE):
            parentPool.append(np)

    fitnessSum = sum([fitness(x) for x in parentPool])
    probabilityList = []
    previousProbability = 0.0
    for index, chromosome in enumerate(parentPool):
        if fitnessSum >0:
            probability = (previousProbability+((fitness(chromosome)/fitnessSum)))
            probabilityList.append(probability)
            previousProbability = probability
        else:
            probabilityList.append(1/(len(parentPool)-1))
    children = []
    numberOfChildrenNeeded = len(population) - len(parentPool)
    while(len(children) < numberOfChildrenNeeded):
        male = selection(parentPool,probabilityList)
        female = selection(parentPool,probabilityList)
        divider = int(len(male)/DIVIDER_VALUE)
        child = male[:divider] + (female[divider:])

        if random.random() < MUTATION_CHANCE:
            mutate(child)
        children.append(child)
    parentPool.extend(children)
    return parentPool


def main():
    #generationFitnessList = []
    currentPopulation = startPopulation()
    currentPopulation.sort(key=fitness, reverse=True)
    #generationFitnessList.append(fitness(currentPopulation[0]))

    for g in range(0,MAX_GENERATIONS):
        currentPopulation.sort(key=fitness, reverse=True)
        #generationFitnessList.append(fitness(currentPopulation[0]))
        currentPopulation = newPopulationEvolution(currentPopulation)
    currentPopulation.sort(key=fitness, reverse=True)
    #Item.printItemList(ITEMS)
    printSolution(currentPopulation)
    #plotData(range(0,MAX_GENERATIONS+1),generationFitnessList,"Generation","Value","Graph for a "+str(len(ITEMS))+" item, "+str(KNAPSACK_SIZE)+" weight knapsack problem")
