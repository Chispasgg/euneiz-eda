'''
Created on 13 nov 2023

@author: chispas

Divide la lista en dos mitades, las ordena por separado y luego las combina en una sola lista ordenada.

'''


def sort(arr, inicial=True):
    if inicial:
        print("merge sort")
        print("Por hacer....")
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el índice medio del array
        left_half = arr[:mid]  # Divide el array en mitades izquierda y derecha
        right_half = arr[mid:]
        
        left_half = sort(left_half, False)  # Ordena la mitad izquierda
        right_half = sort(right_half, False)  # Ordena la mitad derecha
        
        # Combina las mitades ordenadas
        i = j = k = 0  # Inicializa índices para recorrer las tres listas
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Copia los elementos restantes de left_half, si los hay
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Copia los elementos restantes de right_half, si los hay
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
    return arr
