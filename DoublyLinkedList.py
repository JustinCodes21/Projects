class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self,data): #O(1)
        if self.head is None:
            self.head = self.tail = Node(data)
            self.size += 1
            return
        
        self.head = Node(data, self.head, None)
        self.size += 1

    def append(self, data): #O(1)
        if self.head is None:
            self.prepend(data)
            return
        
        newNode = Node(data)
        newNode.next = self.tail.next
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def insert(self, data, index): #O(N)
        
        if index > self.size:
            raise IndexError

        if index == 0: #insert at beginning
            self.prepend(data)
            return
        if index == self.size: #insert at end
            self.append(data)
            return

        counter = 1
        curr = self.head

        while curr.next is not None and counter < index:
            curr = curr.next
            counter += 1
        
        newNode = Node(data)
        newNode.next = curr.next
        newNode.prev = curr
        curr.next.prev = newNode
        curr.next = newNode
        self.size += 1
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def delete(self, data):
        if self.isEmpty():
            raise ValueError

        if data == self.head.data: #O(1)
            if self.size == 1:
                self.head = self.tail = None
                self.size -= 1
                return 
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return
        if data is self.tail.data: #O(1)
            self.tail.prev.next = None
            self.tail = self.tail.prev
            
            self.size -= 1
            return
        
        curr = self.head
        while curr.next.data is not data and curr.next is not None: #O(N)
            curr = curr.next
        curr.next.next.prev = curr
        curr.next = curr.next.next
        self.size -= 1

    
    def returnTail(self):
        if self.tail is None:
            return "Empty list"
        return self.tail.data
    
    def returnHead(self):
        if self.head is None:
            return "Empty list"
        return self.head.data
        
    def len(self):
        return self.size

    def print(self):
        if self.head is None:
            print("None")
            return

        curr = self.head
        print("None <- ", end="")
        while curr is not None:
            if curr.next is None:
                print(curr.data, "-> ", end="")
                break
            print(curr.data, "<-> ", end="")
            curr = curr.next
        print("None")

if __name__ == "__main__":
    myObj = DoublyLinkedList()
    print("\nMy doubly linked list:")
    myObj.prepend(6)
    
    myObj.print()
    
    
    while True:
        
        print("\nMy doubly linked list:")
        myObj.print()
        print("")
        print("------------------------------")
        print("Enter 1 to prepend a value")
        print("Enter 2 to append a value")
        print("Enter 3 to insert a value")
        print("Enter 4 to delete a value")
        print("Enter 5 to return the tail")
        print("Enter 6 to returh the head")
        print("Enter 7 to return the size")
        print("------------------------------")
        answer = int(input("Enter your choice: "))

        if answer == 1:
            answer = int(input("Enter data: "))
            myObj.prepend(answer)
            print("\nUpdated doubly linked list:")
            myObj.print()
        elif answer == 2:
            answer = int(input("Enter data: "))
            myObj.append(answer)
            print("\nUpdated doubly linked list: ")
            myObj.print()
        elif answer == 3:
            data = int(input("Enter data: "))
            index = int(input("Enter index to insert data: "))
            myObj.insert(data, index)
            print("\nUpdated doubly linked list: ")
            myObj.print()
        elif answer == 4:
            num = int(input("Enter data: "))
            myObj.delete(num)
            myObj.print()
        elif answer == 5:
            print("\nThe tail of the doubly linked list: ", myObj.returnTail())
        elif answer == 6:
            print("\nThe head of the doubly linked list: ", myObj.returnHead())
        elif answer == 7:
            print("\nThe number of nodes: ", myObj.len())

        else:
            print("\nInput unexpected")
            continue


        response = input("\nWould you like to go again?(Y/N): ")
        if response == 'y' or response == 'Y':
            continue
        else:
            break

    
