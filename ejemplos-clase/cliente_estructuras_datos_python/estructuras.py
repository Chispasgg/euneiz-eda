'''
Vamos a construir un sistema de gestión de tareas pendientes que permita a los usuarios agregar, eliminar y manejar las tareas de diferentes maneras usando:

    Lista (estructura secuencial/lineal) para almacenar las tareas en el orden en que fueron agregadas.
    Cola (FIFO - First In, First Out) para manejar tareas en el orden en que llegaron.
    Pila (LIFO - Last In, First Out) para manejar tareas de manera inversa, donde la última tarea agregada se completa primero.
    Tabla hash (diccionario) para almacenar las tareas con un ID único, facilitando el acceso y eliminación rápida de tareas.
'''


# Clase Tarea
class Tarea:
    def __init__(self, id_tarea, descripcion):
        self.id_tarea = id_tarea
        self.descripcion = descripcion

    def __str__(self):
        return f"ID: {self.id_tarea}, Descripción: {self.descripcion}"

# Estructura 1: Lista (secuencial/lineal)
class ListaDeTareas:

    tareas = None

    def __init__(self):

    def agregar_tarea(self, tarea):

    def eliminar_tarea(self, id_tarea):

    def mostrar_tareas(self):



# Estructura 2: Pila (LIFO)
class PilaDeTareas:

    pila = None

    def __init__(self):

    def agregar_tarea(self, tarea):

    def completar_tarea(self):

    def mostrar_pila(self):

        
# Estructura 3: Cola (FIFO)
class ColaDeTareas:

    cola = None

    def __init__(self):

    def agregar_tarea(self, tarea):

    def completar_tarea(self):

    def mostrar_cola(self):


# Estructura 4: Tabla Hash (diccionario)
class TablaHashDeTareas:

    tareas = None

    def __init__(self):

    def agregar_tarea(self, tarea):

    def eliminar_tarea(self, id_tarea):

    def mostrar_tareas(self):

# Ejemplo de uso con las diferentes estructuras
# Crear algunas tareas
tarea1 = Tarea(1, "Estudiar para el examen de matemáticas.")
tarea2 = Tarea(2, "Comprar comestibles.")
tarea3 = Tarea(3, "Llamar a mamá.")
tarea4 = Tarea(4, "Terminar el proyecto de programación.")

print("\n---- Lista de tareas ----")
lista = ListaDeTareas()
lista.agregar_tarea(tarea1)
lista.agregar_tarea(tarea2)
lista.agregar_tarea(tarea3)
lista.mostrar_tareas()

print("\nEliminar tarea con ID 2 de la lista:")
lista.eliminar_tarea(2)
lista.mostrar_tareas()

print("\n---- Pila de tareas (LIFO) ----")
pila = PilaDeTareas()
pila.agregar_tarea(tarea1)
pila.agregar_tarea(tarea2)
pila.agregar_tarea(tarea3)
pila.mostrar_pila()

print("\nCompletar tarea de la pila:")
pila.completar_tarea()
pila.mostrar_pila()

print("\n---- Cola de tareas (FIFO) ----")
cola = ColaDeTareas()
cola.agregar_tarea(tarea1)
cola.agregar_tarea(tarea2)
cola.agregar_tarea(tarea3)
cola.mostrar_cola()

print("\nCompletar tarea de la cola:")
cola.completar_tarea()
cola.mostrar_cola()

print("\n---- Tabla hash de tareas (diccionario) ----")
tabla_hash = TablaHashDeTareas()
tabla_hash.agregar_tarea(tarea1)
tabla_hash.agregar_tarea(tarea2)
tabla_hash.agregar_tarea(tarea3)
tabla_hash.agregar_tarea(tarea4)
tabla_hash.mostrar_tareas()

print("\nEliminar tarea con ID 3 de la tabla hash:")
tabla_hash.eliminar_tarea(3)
tabla_hash.mostrar_tareas()
