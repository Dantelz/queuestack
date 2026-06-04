class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty")
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            raise Exception("Empty")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue({self._data})"

Q = Queue()

for i in range(1, 33):
    Q.enqueue(i)


for _ in range(10):
    Q.first()

exitosos = 0
fallidos = 0

for _ in range(10):
    try:
        Q.dequeue()
        exitosos += 1
    except Exception:
        fallidos += 1

while len(Q) > 0:
    Q.dequeue()

for _ in range(5):
    try:
        Q.dequeue()
        exitosos += 1
    except Exception:
        fallidos += 1

print(f"Dequeue exitosos: {exitosos}")   
print(f"Dequeue fallidos: {fallidos}")   
print(f"Tamaño final de Q: {32 - exitosos}")  