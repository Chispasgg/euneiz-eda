'''
Queremos construir un sistema de registro de usuarios que permita almacenar, buscar y eliminar usuarios. Cada usuario tendrá un ID único, un nombre y un correo electrónico. Para esto, implementaremos dos estructuras de datos diferentes:

    Una lista (estructura de datos lineal) para almacenar los usuarios de manera secuencial.
    Una tabla hash (diccionario en Python) para almacenar los usuarios y permitir búsquedas rápidas por el ID.

El ejercicio incluirá operaciones básicas como agregar, buscar y eliminar usuarios utilizando ambas estructuras de datos.
Estructuras de datos que se utilizarán:

    Lista (secuencial/lineal): Para almacenar los usuarios en una lista simple, donde los elementos se almacenan en orden de llegada.
    Tabla Hash: Para almacenar los usuarios en una tabla hash (usaremos un diccionario en Python) que permite buscar y eliminar usuarios por su ID en tiempo casi constante.
'''

# Clase Usuario
class Usuario:
    def __init__(self, user_id, nombre, email):
        self.user_id = user_id
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"ID: {self.user_id}, Nombre: {self.nombre}, Email: {self.email}"

# Sistema de registro de usuarios con lista (estructura lineal)


class RegistroConLista:

    usuarios = None

    def __init__(self):
        # iniciar un usuario

    def agregar_usuario(self, usuario):
        # metodo para agregar un usuario

    def buscar_usuario_por_id(self, user_id):
        # buscar un usuario

    def eliminar_usuario_por_id(self, user_id):
        # sistema para eliminar un usuario

    def mostrar_todos(self):
        # metodod para mostrar todos los usuarios

        

# Sistema de registro de usuarios con tabla hash (diccionario)
class RegistroConTablaHash:

    usuarios = None

    def __init__(self):
        # iniciar un usuario

    def agregar_usuario(self, usuario):
        # metodo para agregar un usuario

    def buscar_usuario_por_id(self, user_id):
        # buscar un usuario

    def eliminar_usuario_por_id(self, user_id):
        # sistema para eliminar un usuario

    def mostrar_todos(self):
        # metodod para mostrar todos los usuarios


# Ejemplo de uso
# Crear algunos usuarios
usuario1 = Usuario(1, "Carlos", "carlos@gmail.com")
usuario2 = Usuario(2, "Lucía", "lucia@gmail.com")
usuario3 = Usuario(3, "Pedro", "pedro@gmail.com")

print("---- Usando estructura de lista ----")
registro_lista = RegistroConLista()
registro_lista.agregar_usuario(usuario1)
registro_lista.agregar_usuario(usuario2)
registro_lista.agregar_usuario(usuario3)

print("Lista de usuarios:")
registro_lista.mostrar_todos()

# Buscar usuario por ID
print("\nBuscar usuario con ID 2:")
print(registro_lista.buscar_usuario_por_id(2))

# Eliminar usuario por ID
print("\nEliminar usuario con ID 1:")
registro_lista.eliminar_usuario_por_id(1)

print("\nLista de usuarios después de eliminar:")
registro_lista.mostrar_todos()

print("\n---- Usando estructura de tabla hash (diccionario) ----")
registro_hash = RegistroConTablaHash()
registro_hash.agregar_usuario(usuario1)
registro_hash.agregar_usuario(usuario2)
registro_hash.agregar_usuario(usuario3)

print("Lista de usuarios:")
registro_hash.mostrar_todos()

# Buscar usuario por ID
print("\nBuscar usuario con ID 2:")
print(registro_hash.buscar_usuario_por_id(2))

# Eliminar usuario por ID
print("\nEliminar usuario con ID 1:")
registro_hash.eliminar_usuario_por_id(1)

print("\nLista de usuarios después de eliminar:")
registro_hash.mostrar_todos()
