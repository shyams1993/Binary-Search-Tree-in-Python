class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

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
                return "Not found"
            elif currentNode.value == value:
                return currentNode.value
                break
            elif value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right

    def remove(self,value):
        parentNode = None
        currentNode = self.root
        while True:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif value == currentNode.value:
                if currentNode.left == None and currentNode.right == None:
                    if currentNode is parentNode.right:
                        parentNode.right = None
                        parentNode = currentNode
                        break
                    elif currentNode is parentNode.left:
                        parentNode.left = None
                        parentNode = currentNode
                        break
                if currentNode.right != None and currentNode.right.left == None:
                    if currentNode is parentNode.left:
                        if currentNode.right.right != None:
                            parentNode.left = currentNode.right
                            currentNode.right = currentNode.right.right
                            parentNode.left.left = currentNode.left
                            break
                        if currentNode.right.right == None:
                            parentNode.left = currentNode.right
                            currentNode.right = None
                            parentNode.left.right = None
                            parentNode.left.left = currentNode.left
                            break
                    elif currentNode is parentNode.right:
                        if currentNode.right.right != None:
                            parentNode.right = currentNode.right
                            currentNode.right = currentNode.right.right
                            parentNode.right.left = currentNode.left
                            break
                        if currentNode.right.right == None:
                            parentNode.right = currentNode.right
                            currentNode.right = None
                            parentNode.right.right = None
                            parentNode.right.left = currentNode.left
                            break
                if currentNode.right != None and currentNode.right.left != None:
                    if currentNode is parentNode.left:
                        if currentNode.right.right != None:
                            parentNode.left = currentNode.right.left
                            parentNode.left.right = currentNode.right
                            currentNode.right = currentNode.right.right
                            parentNode.left.left = currentNode.left
                            currentNode.right.left = None
                            break
                        if currentNode.right.right == None:
                            parentNode.left = currentNode.right.left
                            parentNode.left.right = currentNode.right
                            currentNode.right.right = None
                            parentNode.left.left = currentNode.left
                            currentNode.right.left = None
                            break
                    elif currentNode is parentNode.right:
                        if currentNode.right.right != None:
                            parentNode.right = currentNode.right.left
                            parentNode.right.right = currentNode.right
                            currentNode.right = currentNode.right.right
                            parentNode.right.left = currentNode.left
                            parentNode.right.right.left = None
                            break
                        if currentNode.right.right == None:
                            parentNode.right = currentNode.right.left
                            parentNode.right.right = currentNode.right
                            currentNode.right.right = None
                            parentNode.right.left = currentNode.left
                            currentNode.right.left = None
                            parentNode.right.right.left = None
                            break                           
                if currentNode.right.right == None :
                    if currentNode is parentNode.left:
                        parentNode.left = currentNode.right
                        currentNode.right = None
                        if currentNode.left.left == None:
                            parentNode.left.left = currentNode.left
                        break
                    elif currentNode is parentNode.right:
                        parentNode.right = currentNode.right
                        currentNode.right = None
                        if currentNode.left.left == None:
                            parentNode.right.left = currentNode.left
                        break

                if currentNode.left.left == None :
                    if currentNode is parentNode.left:
                        parentNode.left = currentNode.left
                        currentNode.left = None
                        break
                    elif currentNode is parentNode.right:
                        parentNode.right = currentNode.right
                        currentNode.right = None
                        break
                



m = BinarySearchTree()
m.insert(50)
m.insert(45)
m.insert(40)
m.insert(35)
# m.insert(34)
m.insert(36)
m.insert(37)
m.insert(44)
m.insert(42)
m.insert(47)
m.insert(46)
m.insert(48)
m.insert(65)
m.insert(60)
m.insert(55)
m.insert(62)
m.insert(70)
m.insert(72)
m.insert(66)
# m.remove(35)
m.remove(35)
print(m.root.left.left.left.value)
