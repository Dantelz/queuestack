class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# -------------------------
# SINGLY LINKED LIST
# -------------------------

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # Agregar nodo al final
    def append(self, dato):

        nuevo_nodo = Nodo(dato)

        # Si la lista está vacía
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo

        # Si la lista ya tiene nodos
        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo

    # Eliminar el último nodo
    def remove_last(self):

        # Lista vacía
        if self.head is None:
            return None

        # Si hay un solo nodo
        if self.head == self.tail:
            dato = self.head.dato
            self.head = None
            self.tail = None
            return dato

        actual = self.head

        # Llegar al penúltimo nodo
        while actual.siguiente != self.tail:
            actual = actual.siguiente

        dato = self.tail.dato

        actual.siguiente = None
        self.tail = actual

        return dato

    # Eliminar el primer nodo
    def remove_first(self):

        # Lista vacía
        if self.head is None:
            return None

        dato = self.head.dato

        # Si hay un solo nodo
        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.siguiente

        return dato

    # Mostrar lista
    def print_list(self):

        actual = self.head

        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print("None")

    # Ver tamaño
    def size(self):

        contador = 0
        actual = self.head

        while actual is not None:
            contador += 1
            actual = actual.siguiente

        return contador

    # Ver si está vacía
    def isempty(self):
        return self.head is None


# -------------------------
# STACK
# -------------------------

class Stack:

    def __init__(self):
        self.lista = SinglyLinkedList()

    # Push = agregar arriba
    def push(self, dato):
        self.lista.append(dato)

    # Pop = sacar arriba
    def pop(self):
        return self.lista.remove_last()

    # Ver elemento superior
    def peek(self):

        if self.lista.tail is not None:
            return self.lista.tail.dato

        return None

    # Ver tamaño
    def size(self):
        return self.lista.size()

    # Ver si está vacía
    def isempty(self):
        return self.lista.isempty()

    # Mostrar stack
    def print_stack(self):
        self.lista.print_list()


# -------------------------
# QUEUE
# -------------------------

class Queue:

    def __init__(self):
        self.lista = SinglyLinkedList()

    # Enqueue = agregar al final
    def enqueue(self, dato):
        self.lista.append(dato)

    # Dequeue = sacar el primero
    def dequeue(self):
        return self.lista.remove_first()

    # Ver el primero
    def peek(self):

        if self.lista.head is not None:
            return self.lista.head.dato

        return None

    # Ver tamaño
    def size(self):
        return self.lista.size()

    # Ver si está vacía
    def isempty(self):
        return self.lista.isempty()

    # Mostrar queue
    def print_queue(self):
        self.lista.print_list()


print("===== STACK =====")

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:")
stack.print_stack()

print("Pop:")
print(stack.pop())

print("Stack después del pop:")
stack.print_stack()

print("Peek:")
print(stack.peek())

print("Size:")
print(stack.size())

print("¿Está vacía?")
print(stack.isempty())


print("\n===== QUEUE =====")

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:")
queue.print_queue()

print("Dequeue:")
print(queue.dequeue())

print("Queue después del dequeue:")
queue.print_queue()

print("Peek:")
print(queue.peek())

print("Size:")
print(queue.size())

print("¿Está vacía?")
print(queue.isempty())