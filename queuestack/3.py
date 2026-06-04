class Stack:
    def __init__(self):
        self._data = []

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack vacío")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Exception("Stack vacío")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"


def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())



S = Stack()
for val in [4, 3, 2, 1]:  
    S.push(val)

T = Stack()
print("S antes:", S)
transfer(S, T)
print("S después:", S)
print("T después:", T) 