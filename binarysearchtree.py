class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.__dict__)

    def insert(self,value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if currentNode.left == None:
                        currentNode.left = newNode
                        return
                    else:
                        currentNode = currentNode.left
                elif value > currentNode.value:
                    if currentNode.right == None:
                        currentNode.right = newNode
                        return
                    else:
                        currentNode = currentNode.right

    def lookup(self,value):
        currentNode = self.root
        while True:
            if currentNode == None:
                return "Node doesn't exist"
            elif value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            elif value == currentNode.value:
                return currentNode.value
                break

    def remove(self,value):
        currentNode = self.root
        parentNode = None
        while currentNode != None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif currentNode.value == value:
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                        break
                    elif currentNode.value < parentNode.value:
                        parentNode.left = currentNode.left
                        break
                    elif currentNode.value > parentNode.value:
                        parentNode.right = currentNode.left
                        break
                elif currentNode.right.left == None:
                    if parentNode == None:
                        self.root = currentNode.right
                        break
                    elif currentNode.value < parentNode.value:
                        parentNode.left = currentNode.right
                        break
                    elif currentNode.value > parentNode.value:
                        parentNode.right = currentNode.right
                        break
                else:
                    leftmost = currentNode.right.left
                    leftmostparent = currentNode.right
                    while leftmost.left != None:
                        leftmostparent = leftmost
                        leftmost = leftmost.left
                    leftmostparent.left =  leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right
                    if parentNode == None:
                        self.root = leftmost
                        break
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                            break
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
                            break





m = BinarySearchTree()
m.insert(100)
m.insert(50)
m.insert(40)
m.insert(20)
m.insert(75)
m.insert(80)
m.insert(60)
m.insert(55)
m.insert(65)
m.remove(50)
print(m.root.left.right.left.left.value)
