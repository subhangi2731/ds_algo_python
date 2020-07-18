class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        lastNode = Node(data)
        if self.head is None:
            self.head = lastNode
        else:
            i = self.head
            while(i.next != None):
                i = i.next
            i.next = lastNode
            lastNode.prev = i

    def prepend(self, data):
        firstNode = Node(data)
        if self.head is None:
            self.head = firstNode
        else:
            i = self.head
            i.prev = firstNode
            firstNode.next = i
            self.head = firstNode

    def add_after(self, key, data):
        i = self.head
        while(i != None):
            if(i.next is None and i.data == key):
                self.append(data)
            elif(i.data == key):
                newNode = Node(data)
                x = i.next
                i.next = newNode
                newNode.next = x
                newNode.prev = i
                x.prev = newNode
            i = i.next

    def add_before(self, key, data):
        i = self.head
        while(i != None):
            if(i.prev is None and i.data == key):
                self.prepend(data)
            elif(i.data == key):
                newNode = Node(data)
                x = i.prev
                i.prev = newNode
                newNode.prev = x
                x.next = newNode
                newNode.next = i
            i = i.next

    def delete(self, key):
        pass

    def print_list(self):
        i = self.head
        while(i != None):
            print(i.data, sep=' ')
            i = i.next


myList = DoublyLinkedList()
myList.append(3)
myList.append(5)
myList.append(7)
myList.print_list()
print('===')
myList.prepend(10)
myList.print_list()
print('===')
myList.add_after(5, 15)
myList.print_list()
print('===')
myList.add_before(7, 13)
myList.print_list()
print('===')
myList.delete(5)
myList.print_list()
print('===')
