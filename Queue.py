#Queue implementation using Linked List

class Node:
    def __init__(self, data=None, next=None):
        self.data= data
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self, data): #O(1)
        if self.rear is None:
            self.rear = self.front = Node(data)
            self.size += 1
            return
        
        self.rear.next = Node(data)
        self.rear = self.rear.next
        
        self.size += 1

        
    def dequeue(self): #O(1)
        if self.front is None:
            return "Queue is empty"
        data = self.front.data
        self.front = self.front.next
        self.size -= 1
        if self.front == None:
            self.rear = None
        return data

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def returnFront(self):
        if self.front is None:
            return "Queue is empty"
        return self.front.data
    
    def returnRear(self):
        if self.rear is None:
            return "Queue is empty"
        return self.rear.data
    
    def len(self):
        return self.size
    
    def makeEmpty(self):
        self.front = self.rear = None
        self.size = 0

    def print(self):
        print("\nMy queue:")
        curr = self.front
        
        while curr is not None:
            if curr == self.rear:
                print(curr.data)
                break
            print(curr.data, "<- ", end="")
            curr = curr.next
        

        
  #3 6 4      
myObj = Queue()
myObj.enqueue(4)
myObj.enqueue(6)
myObj.enqueue(3)
myObj.enqueue(99)
myObj.enqueue(7)
myObj.dequeue()
myObj.dequeue()
myObj.enqueue(8)
myObj.dequeue()


myObj.print()
print("\nThe rear of the queue: ", myObj.returnRear())
print("The front of the queue: ", myObj.returnFront())
print("The size of the queue: ", myObj.len())