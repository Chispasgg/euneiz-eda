'''
Created on 15 nov 2023

@author: chispas
'''

import random
import json

# Listas con valores para títulos, autores y géneros de ejemplo
titulos = ["El señor de los anillos",
           "Cien años de soledad",
           "1984",
           "Orgullo y prejuicio",
           "Don Quijote de la Mancha"]
autores = ["J.R.R. Tolkien",
           "Gabriel García Márquez",
           "George Orwell",
           "Jane Austen",
           "Miguel de Cervantes",
           "euneiz"]
generos = ["Fantasía",
           "Realismo mágico",
           "Distopía",
           "Romance",
           "Novela clásica",
           "test"]


# Genera una lista de diccionarios con valores aleatorios
def generar_lista(num_elementos):
    lista = []
    for _ in range(num_elementos):
        diccionario = {
            'Titulo': random.choice(titulos),
            'Autor': random.choice(autores),
            'Genero': random.choice(generos),
            'Disponible': random.choice([True, False])
        }
        lista.append(diccionario)
    return lista


def buscar_libro(lista_libros, titulo, autor, genero):
    # iniciamos la variable resultado
    libros_encontrados = []
    
    
    
    # devolvemos la lsita de libros que hemos encontrado
    return libros_encontrados


if __name__ == '__main__':
    # Genera una lista de 5 diccionarios de ejemplo
    lista_libros = generar_lista(100000)
    print(f"El numero de libros que tenemos es de {len(lista_libros)}")
    titulo_a_buscar = input("Titulo a buscar ")
    autor_a_buscar = input("Autor a buscar ")
    genero_a_buscar = input("Genero a buscar ")
    
    print(" Parametros de busqueda")
    print(f"Titulo: {titulo_a_buscar}")
    print(f"Autor:  {autor_a_buscar}")
    print(f"Genero: {genero_a_buscar}")
    
    libros_buscados = buscar_libro(lista_libros,
                                 titulo_a_buscar,
                                 autor_a_buscar,
                                 genero_a_buscar)
    print(f"Se han encontrado {len(libros_buscados)} libros de {len(lista_libros)} totales")
    mostrar = input("quieres mostrarlos? [y/n] ")
    if mostrar == 'y':
        for l in libros_buscados:
            print(json.dumps(l, indent=2))
    print("FIN")

