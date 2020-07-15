class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        firstNode = Node(data)
        if(self.head == None):
            self.head = firstNode
        else:
            i = self.head
            self.head = firstNode
            firstNode.next = i

    def insert_at_last(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            i = self.head
            while(i.next != None):
                i = i.next
            i.next = newNode

    def delete_first(self):
        if(self.head == None):
            print("Cannot delete, linked list is empty")
        else:
            self.head = self.head.next

    def print_list(self):
        if(self.head == None):
            print("Cannot print, linked list is empty")
        else:
            p = self.head
            while(p != None):
                print(p.data, sep=' ')
                p = p.next

    def insert_multiple(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_at_last(i)

    def count_length(self):
        c = 0
        i = self.head
        while(i != None):
            c += 1
            i = i.next
        return c

    def delete_at_index(self, index):
        if(index == 0 or index > self.count_length()):
            print("Cannot delete, wrong index")
        elif(index == 0):
            self.delete_first()
        else:
            c = 0
            i = self.head
            while(i != None):
                if(c == index-1):
                    i.next = i.next.next
                c += 1
                i = i.next

    def insert_at_index(self, index, data):
        if(index > self.count_length()):
            print("Cannot insert, wrong index")
        elif(index == 0):
            self.insert_at_beginning(data)
        else:
            c = 0
            i = self.head
            while(i != None):
                if(c == index-1):
                    node = Node(data)
                    x = i.next
                    i.next = node
                    node.next = x
                c += 1
                i = i.next


myList = SinglyLinkedList()
myList.insert_at_last(10)
myList.insert_at_last(5)
myList.print_list()
print('===')
myList.delete_first()
myList.print_list()
print('===')
myList.insert_at_beginning(15)
myList.print_list()
print('===')
myList.insert_multiple([1, 2, 3, 4, 5, 6])
myList.print_list()
print('===')
print(myList.count_length())
myList.delete_at_index(3)
myList.print_list()
print('===')
myList.insert_at_index(0, 23)
myList.insert_at_index(3, 18)
myList.print_list()
