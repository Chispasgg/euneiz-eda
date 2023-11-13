'''
Created on 13 nov 2023

@author: chispas

Crea un montículo (heap) a partir de la lista y extrae repetidamente el elemento máximo para obtener una lista ordenada.

'''


def heapify(arr, n, i):
    largest = i  # Inicializa el índice del nodo raíz (el más grande)
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Comprueba si el hijo izquierdo existe y es mayor que el nodo raíz
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Comprueba si el hijo derecho existe y es mayor que el nodo raíz
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Si el nodo raíz no es el más grande, intercambia con el más grande y continúa heapificando
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def sort(arr):
    print("heap sort")
    n = len(arr)

    # Construye un max heap (un árbol binario donde el valor de cada nodo es mayor o igual a sus hijos)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrae elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambia el nodo raíz (más grande) con el último elemento
        heapify(arr, i, 0)  # Llama a heapify en el heap reducido
    
    return arr
