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


def clear_stack(S):
    if not S.is_empty():
        S.pop()
        clear_stack(S)


S2 = Stack()
for val in [1, 2, 3, 4, 5]:
    S2.push(val)

print("\nS2 antes de clear:", S2)
clear_stack(S2)
print("S2 después de clear:", S2)