'''
Created on 13 nov 2023

@author: chispas

Construye un árbol binario de búsqueda con los elementos y luego realiza un recorrido en orden para obtener la lista ordenada.

'''
import sys

# Aumenta el límite de profundidad de recursión
# # https://stackoverflow.com/questions/14222416/recursion-in-python-runtimeerror-maximum-recursion-depth-exceeded-while-callin
sys.setrecursionlimit(10 ** 6)


class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def in_order_traversal(root, sorted_list):
    if root:
        in_order_traversal(root.left, sorted_list)
        sorted_list.append(root.key)
        in_order_traversal(root.right, sorted_list)


def sort(arr):
    
    print("tree sort")
    root = None
    for key in arr:
        root = insert(root, key)

    sorted_list = []
    in_order_traversal(root, sorted_list)
    return sorted_list
