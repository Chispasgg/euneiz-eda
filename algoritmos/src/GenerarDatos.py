'''
Created on 13 nov 2023

@author: chispas
'''

import random

if __name__ == '__main__':
    pass

    # Número de elementos en la lista
    num_elements = 1000
    
    # Generar una lista de números aleatorios
    random_list = [random.randint(1, num_elements) for _ in range(num_elements)]
    
    # Escribir la lista en un archivo
    file_path = "../data/array_pequeño.txt"
    with open(file_path, "w") as file:
        for number in random_list:
            file.write(str(number) + "\n")
    
    print(f"Se ha generado el archivo '{file_path}' con números aleatorios.")
