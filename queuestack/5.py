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

def reverse_list(lst):
    S = Stack()

    for elem in lst:
        S.push(elem)

    for i in range(len(lst)):
        lst[i] = S.pop()


lista = [1, 2, 3, 4, 5]
print("Antes:", lista)
reverse_list(lista)
print("Después:", lista)