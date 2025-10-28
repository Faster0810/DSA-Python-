import ctypes

class Mylist:

    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self._make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
        result = ""
        for i in range(self.n):
            result += str(self.A[i]) + ","

        return "["+result[:-1]+"]"


    @staticmethod
    def _make_array(capacity):
        return (capacity * ctypes.py_object)()

    def __getitem__(self, index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            raise IndexError


    def append(self, item):
        if self.n == self.size:

            self.__resize(self.size*2)

        self.A[self.n] = item
        self.n += 1
        return self.n

    def pop(self, index):
        if self.n == 0:
            return "Empty list"
        if not 0<=index<self.n:
            raise IndexError("Index out of range")
        self.n = self.n-1
        return self.A[self.n-2]


    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "Value not found"

    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in (self.n.pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n+1
        return self.n


    def __resize(self, new_capacity):
        B = self._make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.size = new_capacity


