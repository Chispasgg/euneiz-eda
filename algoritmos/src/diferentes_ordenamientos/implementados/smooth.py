'''
Created on 13 nov 2023

@author: chispas

Es una variante del Heapsort que utiliza un montículo especial llamado montículo de Dijkstra para lograr una eficiencia adicional.

'''


def sift_down(heap, start, end, width):
    root = start
    while root * width + 1 <= end:
        child = root * width + 1

        if child + 1 <= end and heap[child] < heap[child + 1]:
            child += 1

        if child <= end and heap[root] < heap[child]:
            heap[root], heap[child] = heap[child], heap[root]
            root = child
        else:
            return


def sort(arr):
    print("smooth sort")
    width = 2

    while width < len(arr):
        for i in range((len(arr) - 1 - width) // width):
            sift_down(arr, i * width, (i + 2) * width - 1, width)

        if (len(arr) - 1) % width != 0:
            sift_down(arr, (len(arr) - 1 - width) // width * width, len(arr) - 1, width)

        width *= 2

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, 0, i - 1, width // 2)
