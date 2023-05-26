class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data): #O(1)
        self.top = Node(data, self.top)
        self.size += 1
    
    def pop(self): #O(1)
        oldTop = self.top.data
        self.top = self.top.next
        self.size -= 1
        return oldTop
    
    def peek(self): #O(1)
        return self.top.data

    def isEmpty(self):
        if self.size == 0:
            return True
        else: 
            return False
    
    def makeEmpty(self):
        self.top = None
        self.size = 0
        
    
    def print(self):
        curr = self.top
        while curr:
            print(curr.data, " ", end="")
            curr = curr.next
            




myObj = Stack()
print("\nMy stack")
myObj.push(1)
myObj.push(3)
myObj.push(5)
myObj.push(7)
myObj.push(11)
print("------------------------")
myObj.print()
print("\n------------------------")
print("The top of the stack: ", myObj.peek())
myObj.pop()
print("After popping one element the new top is: ", myObj.peek())
myObj.push(100)
print("After pushing the value 100 onto the stack the new top is: ", myObj.peek())
myObj.print()
print("\nIs the stack empty?: ", myObj.isEmpty())
print("Make the stack empty: ", myObj.makeEmpty())
print("Is the stack empty?: ", myObj.isEmpty())
myObj.print()
