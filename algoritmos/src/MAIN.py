
'''
Created on 13 nov 2023

@author: chispas
'''
import datetime
# implementados
from diferentes_ordenamientos.implementados import quick, heap, tree, tim, smooth
 
# por hacer
from diferentes_ordenamientos.por_hacer import bubble, insertion, selection, merge
import copy


def __ejecutar_algoritmos(unsorted_list_original, listado_de_algoritmos, texto):
    unsorted_list = copy.deepcopy(unsorted_list_original)
    print(f"ejecutando {texto}")
    for algoritmo in listado_de_algoritmos:
        inicio = datetime.datetime.now()
        
        # Aplicar el ordenamiento bubble
        sorted_list = algoritmo.sort(unsorted_list)
        fin = datetime.datetime.now()
        print(f"Inicio:     {inicio}")
        print(f"Fin:        {fin}")
        print(f"Diferencia: {fin-inicio}")
        
        print("Lista ordenada:", sorted_list)
    

if __name__ == "__main__":
    # Cargar la lista desde un archivo externo
    file_path = "../data/array_pequeño.txt"
    
    try:
        with open(file_path, "r") as file:
            unsorted_list_original = [int(num) for num in file.read().split()]
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no se encontró.")
        exit()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        exit()

    print("Lista no ordenada:", unsorted_list_original)
    
    lista_algoritmos_implementados = [quick, heap, tree, tim, smooth]
    lista_algoritmos_por_hacer = [bubble, insertion, selection, merge]
    __ejecutar_algoritmos(unsorted_list_original, lista_algoritmos_implementados, "implementados")
    print("------------------------")
    __ejecutar_algoritmos(unsorted_list_original, lista_algoritmos_por_hacer, "por hacer")
