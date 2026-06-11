class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, dato):

        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo

        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo

    def print_list(self):

        actual = self.head

        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print("None")

    # Detectar ciclo (Algoritmo de Floyd)
    def has_cycle(self):

        tortuga = self.head
        liebre = self.head

        while liebre is not None and liebre.siguiente is not None:

            # La tortuga avanza de a 1 nodo
            tortuga = tortuga.siguiente

            # La liebre avanza de a 2 nodos
            liebre = liebre.siguiente.siguiente

            # Si se encuentran, hay ciclo
            if tortuga == liebre:
                return True

        # Si la liebre llega a None, no hay ciclo
        return False

lista = SinglyLinkedList()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

print("¿La lista tiene ciclo?")
print(lista.has_cycle())

# Crear ciclo manualmente
# El último nodo apunta al nodo con dato 2
lista.tail.siguiente = lista.head.siguiente

print("\n¿La lista tiene ciclo ahora?")
print(lista.has_cycle())