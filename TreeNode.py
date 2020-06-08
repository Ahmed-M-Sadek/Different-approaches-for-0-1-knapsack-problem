class Node:
    def __init__(self, treeLevel, value, weight, bound, selectedItems):
        self.treeLevel = treeLevel
        self.value = value
        self.weight = weight
        self.bound = bound
        self.selectedItems = selectedItems

    def print(self):
        print("Node with selected items "+str(self.selectedItems)+" has value and Weight of "+str(self.value)+", "+str(self.weight)+" and bound at "+str(self.bound))

