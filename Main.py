import GeneticAlgorithm
import BranchAndBoundAlgorithm
import SimulatedAnnealing
import DynamicProgramming
import BruteForce
from item import Item

def main():
    ITEM_LIST, KNAPSACK_SIZE = Item.generateList()

    GeneticAlgorithm.ITEMS, GeneticAlgorithm.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE
    BranchAndBoundAlgorithm.ITEMS, BranchAndBoundAlgorithm.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE
    SimulatedAnnealing.ITEMS, SimulatedAnnealing.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE
    DynamicProgramming.ITEMS, DynamicProgramming.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE
    BruteForce.ITEMS, BruteForce.KNAPSACK_SIZE  = ITEM_LIST, KNAPSACK_SIZE

    Item.printItemList(ITEM_LIST)

    GeneticAlgorithm.main()
    BranchAndBoundAlgorithm.main()
    SimulatedAnnealing.main()
    DynamicProgramming.main()

    print()
if __name__ == "__main__":
    main()