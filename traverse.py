class Tree:
    def __init__(self, val, numChildren):
        self.val = int(val)
        self.numChildren = int(numChildren)
        self.children = []
    def readChildren(self):
        for i in range(self.numChildren):
            nextVal = input("next Value: ")
            nextNum = input("next numChildren: ")
            newChild = Tree(nextVal, nextNum)
            self.children.append(newChild)
            newChild.readChildren()
    def printChildren(self):
        for i in range(self.numChildren):
            self.children[i].printChildren();
        print("%d %d" % (self.val, self.numChildren))
        



nextVal = input("next Value: ")
nextNum = input("next numChildren: ")
root = Tree(nextVal, nextNum)
root.readChildren()
root.printChildren()
a = 0

        