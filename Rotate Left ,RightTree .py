class OurCSCE310Tree:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


    def getParent(self):
        return self.parent

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getValue(self):
        return self.value

    def setParent(self, par):
        self.parent = par

    def setLeft(self, lft):
        self.left = lft
        if lft:
            lft.setParent(self)

    def setRight(self, rght):
        self.right = rght
        if rght:
            rght.setParent(self)

    def setValue(self, val):
        self.value = val

    def insert(self, val):
        if self.value is None:
            self.value = val
        else:
            if val < self.value:
                if self.left is None:
                    self.left = OurCSCE310Tree(val, parent=self)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = OurCSCE310Tree(val, parent=self)
                else:
                    self.right.insert(val)

    def printPreorder(self):
        if self.value is not None:
            print(self.value, end=' ')
        if self.left is not None:
            self.left.printPreorder()
        if self.right is not None:
            self.right.printPreorder()

    def printInorder(self):
        if self.left is not None:
            self.left.printInorder()
        if self.value is not None:
            print(self.value, end=' ')
        if self.right is not None:
            self.right.printInorder()

    def printPostorder(self):
        if self.left is not None:
            self.left.printPostorder()
        if self.right is not None:
            self.right.printPostorder()
        if self.value is not None:
            print(self.value, end=' ')


    def rotateLeft(self):
        rightChild = self.getRight()
        if rightChild is None:
            return

        self.setRight(rightChild.getLeft())
        if self.getRight():
            self.getRight().setParent(self)

        rightChild.setLeft(self)

        rightChild.setParent(self.getParent())
        if rightChild.getParent():
            if rightChild.getParent().getLeft() == self:
                rightChild.getParent().setLeft(rightChild)
            elif rightChild.getParent().getRight() == self:
                rightChild.getParent().setRight(rightChild)

        self.setParent(rightChild)

    def rotateRight(self):
        leftChild = self.getLeft()
        if leftChild is None:
            return
        self.setLeft(leftChild.getRight())
        if self.getLeft():
            self.getLeft().setParent(self)

        leftChild.setRight(self)

        leftChild.setParent(self.getParent())
        if leftChild.getParent():
            if leftChild.getParent().getLeft() == self:
                leftChild.getParent().setLeft(leftChild)
            elif leftChild.getParent().getRight() == self:
                leftChild.getParent().setRight(leftChild)

        self.setParent(leftChild)

    def deleteNode(self, key):
        if key < self.getValue():
            if self.getLeft():
                self.getLeft().deleteNode(key)
        elif key > self.getValue():
            if self.getRight():
                self.getRight().deleteNode(key)
        else:
            if self.getLeft() and self.getRight():
                successor = self.getRight()
                while successor.getLeft():
                    successor = successor.getLeft()
                self.setValue(successor.getValue())
                successor.deleteNode(successor.getValue())
            elif self.getLeft() or self.getRight():
                child = self.getLeft() if self.getLeft() else self.getRight()
                self.setValue(child.getValue())
                self.setLeft(child.getLeft())
                self.setRight(child.getRight())
            else:
                if self.getParent():
                    if self.getParent().getLeft() == self:
                        self.getParent().setLeft(None)
                    else:
                        self.getParent().setRight(None)
                self.__del__()

# TEST HERE
tree = OurCSCE310Tree()
tree.insert(45)
tree.insert(34)
tree.insert(71)
tree.insert(14)
tree.insert(35)
tree.insert(50)
tree.insert(86)
tree.insert(96)


tree.printPreorder()
print("\n")
tree.printInorder()
print("\n")
tree.printPostorder()