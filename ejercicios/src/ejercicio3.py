'''
Created on 24 nov 2023

@author: chispas
'''

import random
import string


class Tarea:

    def __init__(self, titulo, descripcion, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def editar_tarea(self, nuevo_titulo, nueva_descripcion):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion


class ListaDeTareas:

    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, tarea):
        self.lista_tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        self.lista_tareas = [t for t in self.lista_tareas if t.titulo != tarea.titulo]

    def obtener_tareas_por_estado(self, estado):
        return [t for t in self.lista_tareas if t.estado == estado]


class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_tareas = ListaDeTareas()

    def agregar_tarea(self, tarea):
        self.lista_tareas.append(tarea)

    def editar_tarea(self, tarea, nuevo_titulo, nueva_descripcion):
        for t in self.lista_tareas:
            if t.titulo == tarea.titulo:
                t.editar_tarea(nuevo_titulo, nueva_descripcion)
                break

    def cambiar_estado_tarea(self, tarea, nuevo_estado):
        for t in self.lista_tareas:
            if t.titulo == tarea.titulo:
                t.cambiar_estado(nuevo_estado)
                break

    def eliminar_tarea_por_titulo(self, titulo):
        print("TODO")

    def eliminar_tarea_por_estado(self, estado):
        print("TODO")


def generar_tarea_aleatoria():
    estados = ["pendiente", "en progreso", "completada"]
    titulo = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    descripcion = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    estado = random.choice(estados)
    return Tarea(titulo, descripcion, estado)


def generar_usuarios_tareas(cantidad_usuarios, cantidad_tareas_por_usuario):
    usuarios = []

    for i in range(cantidad_usuarios):
        usuario = Usuario(f"Usuario-{i + 1}")

        for _ in range(cantidad_tareas_por_usuario):
            tarea = generar_tarea_aleatoria()
            usuario.lista_tareas.agregar_tarea(tarea)

        usuarios.append(usuario)

    return usuarios


def mostrar_datos(usuarios):
    # Mostrar información de los usuarios generados
    for usuario in usuarios:
        print(f"Usuario: {usuario.nombre}")
        for tarea in usuario.lista_tareas.lista_tareas:
            print(f"Título: {tarea.titulo}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}")
        print()


if __name__ == '__main__':
    # Ejemplo de uso para generar 3 usuarios con 4 tareas cada uno
    cantidad_usuarios = 5
    cantidad_tareas_por_usuario = 2
    usuarios_generados = generar_usuarios_tareas(cantidad_usuarios, cantidad_tareas_por_usuario)
    
    print(" - Usuarios y sus tareas")
    print("==================================================")
    continuar = True
    while continuar:
        mostrar_datos(usuarios_generados)
        titulo_tarea = input(" Titulo de la tarea a borrar: ")
        estado_tarea = input(" Estado de la tarea a borrar: ")
        for usuario in usuarios_generados:
            # Eliminar tarea por título
            usuario.eliminar_tarea_por_titulo(titulo_tarea)
            
            # Eliminar tarea por estado
            usuario.eliminar_tarea_por_estado(estado_tarea)
        
        print("==================================================")
        print(" - Usuarios y sus tareas")
        mostrar_datos(usuarios_generados)
        print("==================================================")
        terminar = input(" Quieres terminar: [s/n] ")
        if terminar == 's':
            continuar = False
    print("FIN")
