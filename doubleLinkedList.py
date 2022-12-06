class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head= None
        self.tail = None
    
    def addNode(self,data):

        newNode = Node(data)

        if (self.head == None):
            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None
    
    def display(self):
        current = self.head
        if(self.head == None):
            print("list is empty")
            return
        print("nodes of doubly link list is :")
        while(current != None):
            print(current.data)
            current= current.next

dList = DoublyLinkedList()

dList.addNode(3)
dList.addNode(5)
dList.addNode(1)
dList.addNode(7)
dList.addNode(78)

dList.display()