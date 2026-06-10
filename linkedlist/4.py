class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # Agregar nodo al final
    def append(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo

    # Insertar un nodo después de otro nodo
    def insert_after(self, dato_anterior, nuevo_dato):
        actual = self.head

        while actual is not None:

            if actual.dato == dato_anterior:
                nuevo_nodo = Nodo(nuevo_dato)

                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo

                if actual == self.tail:
                    self.tail = nuevo_nodo

                return

            actual = actual.siguiente

        print("Nodo no encontrado")

    def search(self, dato):
        actual = self.head

        while actual is not None:

            if actual.dato == dato:
                return True

            actual = actual.siguiente

        return False

    # Ordenar nodos de menor a mayor
    def sort(self):
        actual = self.head

        while actual is not None:

            indice = actual.siguiente

            while indice is not None:

                if actual.dato > indice.dato:
                    actual.dato, indice.dato = indice.dato, actual.dato

                indice = indice.siguiente

            actual = actual.siguiente

    def delete(self, dato):

        if self.head is None:
            return

        # Si el nodo a eliminar es el primero
        if self.head.dato == dato:
            self.head = self.head.siguiente

            if self.head is None:
                self.tail = None

            return

        actual = self.head

        while actual.siguiente is not None:

            if actual.siguiente.dato == dato:

                if actual.siguiente == self.tail:
                    self.tail = actual

                actual.siguiente = actual.siguiente.siguiente
                return

            actual = actual.siguiente

        print("Nodo no encontrado")

    def print_list(self):
        actual = self.head

        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print("None")

    def size(self):
        contador = 0
        actual = self.head

        while actual is not None:
            contador += 1
            actual = actual.siguiente

        return contador

    def isempty(self):
        return self.head is None


lista = SinglyLinkedList()

lista.append(5)
lista.append(2)
lista.append(8)
lista.append(1)

print("Lista original:")
lista.print_list()

lista.insert_after(2, 7)

print("\nLista después de insertar 7 después de 2:")
lista.print_list()

print("\n¿Existe el 8?")
print(lista.search(8))

lista.sort()

print("\nLista ordenada:")
lista.print_list()

lista.delete(5)

print("\nLista después de eliminar 5:")
lista.print_list()

print("\nTamaño de la lista:")
print(lista.size())

print("\n¿La lista está vacía?")
print(lista.isempty())