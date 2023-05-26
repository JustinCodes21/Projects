class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def prepend(self, data): #O(1)
        self.head = Node(data, self.head)
        self.size += 1

    def append(self, data): #O(N)
        if self.head is None:
            self.prepend(data)
            return

        newNode = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        
        newNode.next = curr.next
        curr.next = newNode
        self.size += 1

    def insert(self, data, index): #O(N)
        if index > self.size:
            raise IndexError

        if index == 0:
            self.prepend(data)
            return

        counter = 1
        curr = self.head
        while curr.next is not None and counter < index:
            curr = curr.next
            counter += 1
        
        newNode = Node(data)
        newNode.next = curr.next
        curr.next = newNode
        self.size += 1

    
    def delete(self, value): #O(N)

        if value == self.head.data:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head
        while curr.next is not None and curr.next.data is not value:
            curr = curr.next
        
        curr.next = curr.next.next
        self.size -= 1

    def returnHead(self):
        return self.head.data
    
    def returnTail(self):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        
        return curr.data

    def sum(self):
        curr = self.head
        sumOfNodes = 0
        while curr is not None:
            sumOfNodes += curr.data
            curr = curr.next
        
        return sumOfNodes

    def findMax(self):
        curr = self.head
        max = self.head.data
        while curr is not None:
            if curr.data > max:
                max = curr.data
            
            curr = curr.next
        
        return max

    def findMin(self):
        curr = self.head
        min = self.head.data
        while curr is not None:
            if curr.data < min:
                min = curr.data
            curr = curr.next
        
        return min

    def len(self):
        return self.size
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def makeEmpty(self):
        curr = self.head
        while curr is not None:
            curr.next = None
            curr = curr.next
        
        self.head = None
        self.size = 0

    def reverse(self):
        curr = self.head
        i = 0
        myList = []

        while curr is not None:
            myList.insert(i, curr.data)
            curr = curr.next
            i += 1
        
        temp = self.head
        while temp is not None:
            temp.data = myList.pop()
            
            temp = temp.next
            
  
    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.data, "-> ", end="")
            curr = curr.next
        print("None")
        
myObj = SinglyLinkedList()
i = 1
while i <= 4:
    myObj.append(i)
    i+=1
myObj.print()
print("Head:", myObj.returnHead(), end="")
print(" Tail:", myObj.returnTail())
myObj.reverse()
myObj.print()
#print("Reversed:", myObj.print())
print("Head:", myObj.returnHead(), end = "")
print(" Tail:", myObj.returnTail())
print("The sum of all nodes:", myObj.sum())
print("The number of nodes in the Singly Linked List:", myObj.len())

print("The max number:", myObj.findMax())
print("The min number:", myObj.findMin())