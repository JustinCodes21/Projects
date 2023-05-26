class Node:
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next
    

class CircularLinkedList:
    def __init__(self):
        
        self.tail = None
        self.size = 0

    def prepend(self, data): #O(1)
        
        if self.tail is None:
            newNode = Node(data)
            self.tail = newNode
            newNode.next = self.tail
            self.size += 1
            return
        
        newNode = Node(data)
        newNode.next = self.tail.next
        self.tail.next = newNode
        self.size += 1
    
    def append(self, data): #O(1)
        if self.tail is None:
            self.prepend(data)
            return

        newNode = Node(data)
        newNode.next = self.tail.next
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def delete(self, data):#O(N)
        
        curr = self.tail
        while curr.next is not None and curr.next.data is not data:
            curr = curr.next
        
        curr.next = curr.next.next
        self.size -= 1

    def len(self):
        return self.size

    def print(self):
        curr = self.tail.next
        if self.size == 0:
            print("None -> points back to None (Circular)")
            return
        print("\nMy circular linked list: ")
        while curr:
            print(curr.data, "-> ", end="")
            curr = curr.next
            if curr == self.tail.next:
                break
        print("points back to", curr.data, "(Circular)\n")
        
myObj = CircularLinkedList()
myObj.prepend('A')
myObj.prepend('B')
myObj.prepend('C')
myObj.append('D')
myObj.prepend('E')
myObj.append('F')
myObj.prepend("Z")
myObj.print()


print("Number of nodes:", myObj.len())