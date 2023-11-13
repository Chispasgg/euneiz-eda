'''
Created on 13 nov 2023

@author: chispas

Divide la lista en subconjuntos basados en un pivote, y luego ordena recursivamente cada subconjunto.

'''


def sort(arr, inicial=True):
    if inicial:
        print("quick sort")
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return sort(less, False) + [pivot] + sort(greater, False)
