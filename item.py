import random
from prettytable import PrettyTable

IS_RANDOM_NUMBER_OF_ITEMS = False
IS_RANDOM_KNAPSACK_SIZE = True
MAX_NUMBER_OF_ITEMS = 20
MAX_KNAPSACK_SIZE = 100
MIN_KNAPSACK_SIZE = 20
WEIGHT_UPPERLIMIT = 20
VALUE_UPPERLIMIT = 20

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def print(self):
        print("value = "+str(self.value)+", Weight = "+str(self.weight))
    @staticmethod
    def printItemList(Items):
        table = PrettyTable(['Item', 'Value', 'Weight'])
        counter = 1
        for Item in Items:
            table.add_row([counter, Item.value ,Item.weight])
            counter+=1
        print(table)

    @staticmethod
    def generateList(number = MAX_NUMBER_OF_ITEMS, capacity = MIN_KNAPSACK_SIZE):
        itemList = []
        if IS_RANDOM_NUMBER_OF_ITEMS:
            starting = 1
        else:
            starting = number
        if IS_RANDOM_KNAPSACK_SIZE:
            KNAPSACK_SIZE = random.randint(MIN_KNAPSACK_SIZE, MAX_KNAPSACK_SIZE)
        else:
            KNAPSACK_SIZE = capacity
        print(starting)
        itemList = [Item(random.randint(1,VALUE_UPPERLIMIT),random.randint(1,WEIGHT_UPPERLIMIT)) for i in range(0,random.randint(starting,MAX_NUMBER_OF_ITEMS))]
        return itemList, KNAPSACK_SIZE

