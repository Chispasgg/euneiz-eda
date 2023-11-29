'''
Created on 13 nov 2023

@author: chispas

Compara y intercambia elementos adyacentes hasta que todos los elementos estén en su posición correcta.

'''


def sort(arr):
    
    print("bubble sort")
    print("Por hacer....")
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
