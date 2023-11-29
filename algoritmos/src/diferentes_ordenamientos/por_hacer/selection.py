'''
Created on 13 nov 2023

@author: chispas

Encuentra el elemento mínimo en cada pasada y lo coloca en su posición correcta.

'''


def sort(arr):
    print("selection sort")
    print("Por hacer....")
    n = len(arr)
    
    # Recorrer todos los elementos de la lista
    for i in range(n):
        # Buscar el elemento mínimo en la parte no ordenada de la lista
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
    
        # Intercambia el elemento mínimo encontrado con el primer elemento
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr
