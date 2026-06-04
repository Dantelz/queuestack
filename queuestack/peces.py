def peces_vivos(A, B):
    stack = []
    vivos_arriba = 0

    for i in range(len(A)):
        tamaño = A[i]
        direccion = B[i]

        if direccion == 1:
            stack.append(tamaño)
        else:
            sobrevive = True

            while stack:
                if stack[-1] > tamaño:
                    sobrevive = False
                    break
                else:
                    stack.pop()

            if sobrevive:
                vivos_arriba += 1

    return vivos_arriba + len(stack)


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

resultado = peces_vivos(A, B)

print("Cantidad de peces vivos:", resultado)