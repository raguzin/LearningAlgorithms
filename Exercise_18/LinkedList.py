class LinkedList:
    def __init__(self):
        self._begin = None
    
    def insert (self, x):
        self._begin = [x, self._begin]
    
    def pop (self):
        assert self._begin is not None, "List is empty"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x


a = LinkedList()
for i in range(1,6):
    x = int(input("Input x: "))
    a.insert(x)
for i in range(1,6):
    print(a.pop())

