from item import Item
from time import time
import GeneticAlgorithm
import BranchAndBoundAlgorithm
import SimulatedAnnealing
import DynamicProgramming
import BruteForceAlgorithm
import GreedyAlgorithm
import DivideAndConquerAlgorithm
import matplotlib.pyplot as plt

def main():
    x = [i for i in range(5,26)]
    yGenA = []
    yBB = []
    ySA = []
    yDP = []
    yBF = []
    yGreed = []
    yDAC = []
    for n in range(5,26):
        ITEM_LIST, KNAPSACK_SIZE = Item.generateList(n)
        GeneticAlgorithm.ITEMS, GeneticAlgorithm.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE
        BranchAndBoundAlgorithm.ITEMS, BranchAndBoundAlgorithm.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE
        SimulatedAnnealing.ITEMS, SimulatedAnnealing.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE
        DynamicProgramming.ITEMS, DynamicProgramming.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE
        BruteForceAlgorithm.ITEMS, BruteForceAlgorithm.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE
        GreedyAlgorithm.ITEMS, GreedyAlgorithm.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE
        DivideAndConquerAlgorithm.ITEMS, DivideAndConquerAlgorithm.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE

        Item.printItemList(ITEM_LIST)

        t0 = time()
        GeneticAlgorithm.main()
        tGenA = time()
        BranchAndBoundAlgorithm.main()
        tBB = time()
        SimulatedAnnealing.main()
        tSA = time()
        DynamicProgramming.main()
        tDP = time()
        BruteForceAlgorithm.main()
        tBF = time()
        GreedyAlgorithm.main()
        tGreed = time()
        DivideAndConquerAlgorithm.main()
        tDAC = time()

        yGenA.append(tGenA-t0)
        yBB.append(tBB - tGenA)
        ySA.append(tSA - tBB)
        yDP.append(tDP - tSA)
        yBF.append(tBF - tDP)
        yGreed.append(tGreed - tBF)
        yDAC.append(tDAC - tGreed)
    plt.plot(x, yGenA, label = "Genetic")
    plt.plot(x, yBB, label = "Branch and Bound")
    plt.plot(x, ySA, label = "Simulated annealing")
    plt.plot(x, yDP, label = "Dynamic")
    plt.plot(x, yBF, label = "Brute force")
    plt.plot(x, yGreed, label = "Greedy")
    plt.plot(x, yDAC, label = "Divide and conquer")

    plt.xlabel("number of items")
    plt.ylabel("time spent")
    plt.legend()
    plt.show()

    print()
if __name__ == "__main__":
    main()