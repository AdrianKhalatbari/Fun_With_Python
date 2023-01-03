# Represents the node of the list.    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateList:
    # Declaring head and tail pointer as null.    
    def __init__(self):
        self.count = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

        # This function will add the new node at the end of the list.    

    def add(self, data):
        newNode = Node(data)
        # Checks if the list is empty.    
        if self.head.data is None:
            # If list is empty, both head and tail would point to new node.    
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # tail will point to new node.    
            self.tail.next = newNode
            # New node will become new tail.    
            self.tail = newNode
            # Since, it is circular linked list tail will point to head.    
            self.tail.next = self.head

            # This function will count the nodes of circular linked list    

    def countNodes(self):
        current = self.head
        self.count = self.count + 1
        while (current.next != self.head):
            self.count = self.count + 1
            current = current.next
        print("Count of nodes present in circular linked list: "),
        print(self.count)

    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            # Prints each node by incrementing pointer.
            print('\nThe nodes are: ')
            print(current.data, end=', ')
            while (current.next != self.head):
                current = current.next
                print(current.data, end=', ')

    def size(self):
        current = self.head
        size = 1
        while self.head != current.next:
            size = size + 1
            current = current.next
        return size

    def reverseDisplay(self, current):
        # Checks if the next node is head, if yes then prints it.
        if (current.next == self.head):
            print('\nThe reverse list is: ')
            print(current.data, end=', ')
            return
            # Recursively calls the reverse function
        self.reverseDisplay(current.next)
        print(current.data, end=', ')

    # delete a node from the beginning of the Circular Linked List
    def deleteStart(self):
        if self.head == None:
            return
        else:
            if self.head != self.tail:
                self.head = self.head.next
                self.tail.next = self.head
            else:
                self.head = self.tail = Node

    # delete a node from the end of the Circular Linked List
    def deleteEnd(self):
        if self.tail == None:
            return
        else:
            if self.head != self.tail:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                self.tail = current
                self.tail.next = self.head
            else:
                self.head = self.tail = Node

    # delete a node from the middle of the Circular Linked List
    def deleteMid(self):
        if self.tail == None:
            return
        else:
            if self.size() % 2 == 0:
                middle = self.size() / 2
            else:
                middle = (self.size() + 1) / 2
            if self.head != self.tail:
                current = None
                temp = self.head
                for i in range(0, int(middle) - 1):
                    current = temp
                    temp = temp.next
                if current != None:
                    current.next = temp.next
                    temp = None
                else:
                    self.tail = self.head = temp.next
                    self.tail.next = self.head
                    temp = None

    def maxMinNode(self):
        current = self.head
        max = int(self.head.data)
        min = int(self.head.data)
        while self.head != current.next:
            temp = current.data
            if int(temp) > max:
                max = int(temp)
            if int(temp) < min:
                min = int(temp)
            current = current.next
        print('\nThe min and max are: ')
        print(min, max)

    def addAtStart(self, data):
        newNode = Node(data)
        temp = self.head
        newNode.next = temp
        self.tail.next = newNode
        self.head = newNode

    def addAtEnd(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.tail.next = self.head

    def addInMid(self, data):
        newNode = Node(data)
        if self.size() % 2 == 0:
            middle = self.size() / 2
        else:
            middle = (self.size() + 1) / 2
        current = self.head
        for i in range(0, int(middle) - 1):
            current = current.next
        temp = current.next
        current.next = newNode
        newNode.next = temp

    def removeDuplicate(self):
        current = self.head
        if (self.head == None):
            print("List is empty")
        else:
            while True:
                temp = current
                index = current.next
                while (index != self.head):
                    if index.data == current.data:
                        temp.next = index.next
                    else:
                        temp = index
                    index = index.next
                current = current.next
                if current.next == self.head:
                    break

    def search(self, element):
        current = self.head
        index = 1
        flag = False
        while current.next != self.head:
            if current.data == element:
                flag = True
                break
            else:
                index += 1
                current = current.next
        if flag == True:
            print('\nElement is present in the list at the position:', str(index))
        else:
            print('\nElement is not present in the list')

    def sortList(self):
        current = self.head
        while True:
            index = current.next
            while index != self.head:
                if current.data > index.data:
                    temp = current.data
                    current.data = index.data
                    index.data = temp
                index = index.next
            current = current.next
            if current.next == self.head:
                break


class CircularLinkedList:
    cl = CreateList()
    # Adds data to the list    
    cl.add(1)
    cl.add(2)
    cl.add(4)
    cl.add(7)
    cl.add(6)
    cl.add(3)
    # Displays all the nodes present in the list
    cl.display()
    # Displays count of nodes
    # cl.countNodes()
    # cl.reverseDisplay(cl.head)
    # ////////////////////delete from start
    # cl.deleteStart()
    # cl.display()
    # ////////////////////delete from end
    # cl.deleteEnd()
    # cl.display()
    # ////////////////////delete from middle
    # cl.deleteMid()
    # cl.display()
    # ////////////////////Find min and max
    # cl.maxMinNode()
    # ////////////////////Python program to insert a new node at the start of the Circular Linked List
    # cl.addAtStart(6)
    # cl.display()
    # ////////////////////Python program to insert a new node at the end of the Circular Linked List
    # cl.addAtEnd(8)
    # cl.display()
    # ////////////////////Python program to insert a new node at the middle of the Circular Linked List
    # cl.addInMid(5)
    # cl.display()
    # ////////////////////Python program to remove duplicate elements from a Circular Linked List
    # cl.removeDuplicate()
    # cl.display()
    # ////////////////////Python program to search an element in a Circular Linked List
    # cl.search(2)
    # ////////////////////Python program to sort elements from a Circular Linked List
    cl.sortList()
    cl.display()