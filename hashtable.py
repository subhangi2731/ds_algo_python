class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self,key,value):
        a = self.get_hash(key)
        found = False
        for i,el in enumerate(self.arr[a]):
            if(len(el)==2 and el[0]==key):
                self.arr[a][i]=(key,value)
                found=True
                break
        if not found:
            self.arr[a].append((key,value))

    def get_value(self,key):
        a = self.get_hash(key)
        for el in self.arr[a]:
            if(el[0]==key):
                print(self.arr[a])

    def delete(self,key):
        a = self.get_value(key)
        for i, el in enumerate(self.arr):
            if(el[0]==key):
                self.arr[a][i]=None

t=HashTable()
t.add('march 6',28)
t.add('march 6',34)
t.add('march 17',11)
print(t.arr)