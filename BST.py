class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.numOfNodes = 0

    def findMax(self): #O(N)
        if self.root is None:
            return "Empty BST"
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.data
    
    def returnRoot(self): #O(1)
        if self.root is None:
            return "Empty BST"
        return self.root.data

    def findMin(self): #O(N)
        if self.root is None:
            return "Empty BST"
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.data
    
        
    def insert(self, data, node): #O(logN)
        if self.isEmpty():
            self.root = Node(data)
            self.numOfNodes += 1
            return
        
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                self.numOfNodes += 1
            else:
                return self.insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
                self.numOfNodes += 1
            else:
                return self.insert(data, node.right)
        else:
            return
        
    def findMinNode(self, node): #Utility function for delete
        curr = node
        while curr.left is not None:
            curr = curr.left
        
        return curr
               

    def delete(self, data, node): #O(logN) 
        if self.isEmpty():
            print("\nThe BST is empty.")
            return node
        
        if not self.find(data, node):
            print("\nData not found in BST.")
            return node
        
        if data < node.data:
            node.left = self.delete(data, node.left)
        elif data > node.data:
            node.right = self.delete(data, node.right)
        else:
            #case 1: has one child or leaf node
            if node.right is None:
                temp = node.left
                node = None
                self.numOfNodes-=1
                return temp
            elif node.left is None:
                temp = node.right
                node = None
                self.numOfNodes-=1
                return temp
            
            #case 2: has two children
            temp = self.findMinNode(node.right)
            node.data = temp.data
            node.right = self.delete(temp.data, node.right)

        return node


    def findSuccessor(self, data, node): #O(logN)
        if not self.find(data, node):
            return "not in BST."
        
        if data == self.root.data:
            return "not in BST."
        
        if data == node.data:
            if node.left:
                return node.left.data
            elif node.right:
                return node.right.data
            elif node.data == self.findMax():
                return "not in BST."
            else:
                if self.root.right:
                    return self.root.right.data
                else:
                    return "not in BST."
        elif data < node.data:
            return self.findSuccessor(data, node.left)
        elif data > node.data:
            return self.findSuccessor(data, node.right)
        
        
    def findPredecessor(self, data, node): #O(logN)
        if not self.find(data, node):
            return "not in BST."
        
        if data == self.root.data:
            return "not in BST."
        
        curr = node
        while curr:
            if data < curr.data:
                predecessor = curr
                curr = curr.left
            elif data > curr.data:
                predecessor = curr
                curr = curr.right
            elif data == curr.data:
                return predecessor.data
            
        return "not in BST."

            
    def find(self, data, node): #O(logN)
        if self.root is None:
            return False
        
        if node is not None and data == node.data:
            return True
        elif node is not None and data < node.data:
            return self.find(data, node.left)
        elif node is not None and data > node.data:
            return self.find(data, node.right)
        else:
            return False
        
    def getHeight(self, node):
        if self.isEmpty():
            return 0
        elif self.size() == 1:
            return 1
        
    def getLeafNodes(self, node):
        if self.isEmpty():
            return "Empty BST"
        if self.size() == 1:
            return self.root.data
        
        curr = node.left

    


        
    def isEmpty(self): #O(1)
        if self.size() == 0:
            return True
        
        return False
    
    def size(self): #O(1)
        return self.numOfNodes
    

    def printPreOrder(self, node): 
        if node is not None:
            print(node.data, " ",end="")
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

    
            
myObj = BST()


while(True):
    print("\n--------------------------")
    print("Enter 1: Insert data")
    print("Enter 2: Delete data")
    print("Enter 3: Return root")
    print("Enter 4: Return max node")
    print("Enter 5: Return min node")
    print("Enter 6: Find succesor")
    print("Enter 7: Print BST (preorder)")
    print("Enter 8: Return number of nodes")
    print("Enter 9: Check if empty")
    print("Enter 10: Find predecessor")
    print("Enter 11: Find height of the BST")
    print("--------------------------")

    answer = int(input("Enter answer: "))
    if answer == 1:
        data = int(input("Enter data: "))
        print("\nPreorder traversal: ", end="")
        myObj.insert(data, myObj.root)
        myObj.printPreOrder(myObj.root)
    elif answer == 2:
        data = int(input("Enter data: "))
        root = myObj.delete(data, myObj.root)
        print("Updated BST: ", end="")
        myObj.printPreOrder(root)
    elif answer == 3:
        print("\nThe root of the BST: ", myObj.returnRoot())
    elif answer == 4:
        print("\nThe max node: ", myObj.findMax())
    elif answer == 5:
        print("\nThe min node: ", myObj.findMin())  
    elif answer == 6:
        data = int(input("Enter data: "))
        print("The succesor of", data, "is", myObj.findSuccessor(data, myObj.root))
    elif answer == 7:
        print("")
        print("Preorder traversal: ", end="")
        myObj.printPreOrder(myObj.root)
    elif answer == 8:
        print("The number of nodes:", myObj.size())
    elif answer == 9:
        result = myObj.isEmpty()
        if result is True:
            print("The BST is empty")
        else:
            print("The BST is not empty")
    elif answer == 10:
        data = int(input("Enter data: "))
        print("The predecessor of", data, "is", myObj.findPredecessor(data, myObj.root))
    else:
        print("Error input")
        continue

    loop = input("\nWould you like to continue?(Y/N): ")

    if loop == 'y' or loop == 'Y':
        continue
    else:
        break




    
