class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

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
        if self.root is None:
            self.root = Node(data)
            return
        
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                node.left.parent = node #set parent - helps with delete function
            else:
                self.insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
                node.right.parent = node #set parent - helps with delete function
            else:
                self.insert(data, node.right)
        else:
            return
            

    def delete(self, data, node): #O(logN) //Need to work on
        if self.root is None:
            return None
        
        if data < node.data:
            node.left = self.delete(data, node.left)
        elif data > node.data:
            node.right = self.delete(data, node.right)
        elif data == node.data:
            if node.left and node.right is None:
                return None
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            tempVal = node.right
            miniVal = tempVal.data
            while tempVal.left:
                 tempVal = tempVal.left
                 miniVal = tempVal.data
            
            node.right = self.delete(node.right, node.data)

        return node

        

    def findSuccesor(self, data, node):
        pass

    def findPredecessor(self):
        pass
        
    
        
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
        
    def deleteValue(self, value):
        return self.deleteNode(self.find(value))
    
    def deleteNode(self, node):
        #returns the node with min value in tree rooted at input node
        def minValueNode(n):
            curr = n
            while curr.left != None:
                curr = curr.left
            return curr

        #returns the number of children for the specified node
        def numChildren(n):
            numChildren = 0
            if n.left != None:
                numChildren+=1
            if n.right != None:
                numChildren+=1
            return numChildren

        #get the parent of the node to be deleted
        nodeParent = node.parent

        #get the number of children of the node to be deleted
        nodeChildren = numChildren(node)

        #break operation into different cases based on the 
        #structure of the tree & node to be deleted

        #CASE 1 (node has no children)
        if nodeChildren == 0:
            #remove reference to the node from the parent
            if nodeParent.left == node:
                nodeParent.left = None
            else:
                nodeParent.right = None
            

    def printPreOrder(self, root):
        if root is not None:
            print(root.data, " ",end="")
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)
        
        


myObj = BST()


while(True):
    print("\n--------------------------")
    print("Enter 1: Insert data")
    print("Enter 2: Delete data")
    print("Enter 3: Return root")
    print("Enter 4: Return max node")
    print("Enter 5: Return min node")
    print("Enter 6: Print BST")
    print("--------------------------")

    answer = int(input("Enter answer: "))
    if answer == 1:
        data = input("Enter data: ")
        myObj.insert(data, myObj.root)
        print("\nPreorder traversal: ", end="")
        myObj.printPreOrder(myObj.root)
    elif answer == 2:
        data = input("Enter data: ")
        print("")
        result = myObj.delete(data, myObj.root)
        print("\nPreorder traversal: ", end="")
        myObj.printPreOrder(result)
    elif answer == 3:
        print("\nThe root of the BST: ", myObj.returnRoot())
    elif answer == 4:
        print("\nThe max node: ", myObj.findMax())
    elif answer == 5:
        print("\nThe min node: ", myObj.findMin())  
    elif answer == 6:
        print("")
        print("Preorder traversal: ", end="")
        myObj.printPreOrder(myObj.root)
    else:
        print("Error input")
        continue

    loop = input("\nWould you like to continue?(Y/N): ")

    if loop == 'y' or loop == 'Y':
        continue
    else:
        break




    
