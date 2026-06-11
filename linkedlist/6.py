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

    def reverse(self):

        anterior = None
        actual = self.head
        siguiente = None

        # El head actual pasará a ser el tail
        self.tail = self.head

        while actual is not None:

            # Guardar referencia al siguiente nodo
            siguiente = actual.siguiente

            # Invertir el puntero
            actual.siguiente = anterior

            # Avanzar variables
            anterior = actual
            actual = siguiente

        # El último nodo recorrido pasa a ser el nuevo head
        self.head = anterior


lista = SinglyLinkedList()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

print("Lista original:")
lista.print_list()

lista.reverse()

print("\nLista invertida:")
lista.print_list()