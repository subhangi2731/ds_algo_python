class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self,key,value):
        a = self.get_hash(key)
        self.arr[a] = value

    def get_value(self,key):
        a = self.get_hash(key)
        print(self.arr[a])

t=HashTable()
print(t.get_hash('apple'))
t.add('march',28)
print(t.arr)
t.get_value('march')