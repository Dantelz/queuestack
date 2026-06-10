# NODO

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


# SINGLY LINKED LIST

class SinglyLinkedList:

    def __init__(self):
        self.lista = [1, 2, 3, 4, 5]
        self.head = self.lista[0]
        self.tail = self.lista[-1]

        self.nodos = []

        for i in self.lista:
            self.nodos.append(Nodo(i))

        for i in range(len(self.nodos) - 1):
            self.nodos[i].siguiente = self.nodos[i + 1]

    def append(self, elemento):
        self.lista.append(elemento)
        self.tail = self.lista[-1]
        return self.lista

    def remove(self):
        self.lista.pop()
        self.tail = self.lista[-1]
        return self.lista

    def peek(self):
        return self.head

    def isempty(self):
        return len(self.lista) == 0

    def size(self):
        return len(self.lista)


# DOUBLY LINKED LIST

class DoublyLinkedList:

    def __init__(self):
        self.lista = [1, 2, 3, 4, 5]
        self.head = self.lista[0]
        self.tail = self.lista[-1]

        self.nodos = []

        for i in self.lista:
            self.nodos.append(Nodo(i))

        for i in range(len(self.nodos) - 1):
            self.nodos[i].siguiente = self.nodos[i + 1]
            self.nodos[i + 1].anterior = self.nodos[i]

    def append(self, elemento):
        self.lista.append(elemento)
        self.tail = self.lista[-1]
        return self.lista

    def remove(self):
        self.lista.pop()
        self.tail = self.lista[-1]
        return self.lista

    def peek(self):
        return self.head

    def isempty(self):
        return len(self.lista) == 0

    def size(self):
        return len(self.lista)


# CIRCULAR SINGLY LINKED LIST

class CircularSinglyLinkedList:

    def __init__(self):
        self.lista = [1, 2, 3, 4, 5]
        self.head = self.lista[0]
        self.tail = self.lista[-1]

        self.nodos = []

        for i in self.lista:
            self.nodos.append(Nodo(i))

        for i in range(len(self.nodos) - 1):
            self.nodos[i].siguiente = self.nodos[i + 1]

        self.nodos[-1].siguiente = self.nodos[0]

    def append(self, elemento):
        self.lista.append(elemento)
        self.tail = self.lista[-1]
        return self.lista

    def remove(self):
        self.lista.pop()
        self.tail = self.lista[-1]
        return self.lista

    def peek(self):
        return self.head

    def isempty(self):
        return len(self.lista) == 0

    def size(self):
        return len(self.lista)


# CIRCULAR DOUBLY LINKED LIST

class CircularDoublyLinkedList:

    def __init__(self):
        self.lista = [1, 2, 3, 4, 5]
        self.head = self.lista[0]
        self.tail = self.lista[-1]

        self.nodos = []

        for i in self.lista:
            self.nodos.append(Nodo(i))

        for i in range(len(self.nodos) - 1):
            self.nodos[i].siguiente = self.nodos[i + 1]
            self.nodos[i + 1].anterior = self.nodos[i]

        self.nodos[-1].siguiente = self.nodos[0]
        self.nodos[0].anterior = self.nodos[-1]

    def append(self, elemento):
        self.lista.append(elemento)
        self.tail = self.lista[-1]
        return self.lista

    def remove(self):
        self.lista.pop()
        self.tail = self.lista[-1]
        return self.lista

    def peek(self):
        return self.head

    def isempty(self):
        return len(self.lista) == 0

    def size(self):
        return len(self.lista)


def main():

    # SINGLY LINKED LIST

    print("SINGLY LINKED LIST")

    l1 = SinglyLinkedList()

    for nodo in l1.nodos:

        if nodo.siguiente:
            print(f"Nodo {nodo.dato} -> apunta a -> {nodo.siguiente.dato}")

        else:
            print(f"Nodo {nodo.dato} -> apunta a -> None")

    print()


    # DOUBLY LINKED LIST

    print("DOUBLY LINKED LIST")

    l2 = DoublyLinkedList()

    for nodo in l2.nodos:

        anterior = nodo.anterior.dato if nodo.anterior else None
        siguiente = nodo.siguiente.dato if nodo.siguiente else None

        print(f"Nodo {nodo.dato} -> anterior: {anterior} | siguiente: {siguiente}")

    print()


    # CIRCULAR SINGLY LINKED LIST

    print("CIRCULAR SINGLY LINKED LIST")

    l3 = CircularSinglyLinkedList()

    for nodo in l3.nodos:

        print(f"Nodo {nodo.dato} -> apunta a -> {nodo.siguiente.dato}")

    print()


    # CIRCULAR DOUBLY LINKED LIST

    print("CIRCULAR DOUBLY LINKED LIST")

    l4 = CircularDoublyLinkedList()

    for nodo in l4.nodos:

        print(f"Nodo {nodo.dato} -> anterior: {nodo.anterior.dato} | siguiente: {nodo.siguiente.dato}")

    print()


main()