# Ejercicio 1: Sistema de Gestión de Biblioteca

**Descripción del Problema:** 

Se requiere el diseño de un sistema de gestión de biblioteca que permita a los usuarios buscar y tomar prestados libros, así como a los bibliotecarios administrar el inventario y las transacciones de préstamo. El sistema debe permitir a los usuarios buscar libros por título, autor o género, y realizar un seguimiento de cuándo deben devolverlos.

**Clases importantes**

```python
Clase Libro:
    Atributos:
        - Título
        - Autor
        - Género
        - Disponible (booleano)
    Métodos:
        - Constructor (título, autor, género)
        - MarcarComoDisponible()
        - MarcarComoNoDisponible()

Clase Usuario:
    Atributos:
        - Nombre
        - LibrosPrestados (lista de objetos Libro)
    Métodos:
        - Constructor (nombre)
        - BuscarLibro(título, autor, género)
        - TomarPrestadoLibro(libro)
        - DevolverLibro(libro)

Clase Biblioteca:
    Atributos:
        - Inventario (lista de objetos Libro)
    Métodos:
        - Constructor ()
        - AgregarLibro(libro)
        - EliminarLibro(libro)
        - BuscarLibro(título, autor, género)
```

## Arquitectura Sugerida: Arquitectura Cliente-Servidor

### Descripción

En esta arquitectura, el sistema de gestión de biblioteca consta de dos componentes principales: el cliente y el servidor. El servidor almacena la base de datos de libros y gestiona las operaciones de préstamo y devolución. El cliente proporciona una interfaz de usuario para que los usuarios busquen libros, realicen transacciones de préstamo y devolución, y administren sus cuentas. La comunicación entre el cliente y el servidor se realiza a través de solicitudes y respuestas, utilizando protocolos de red como HTTP.

## Se requiere

- Pseudocodigo:
  - [ ] del método para buscar un libro por título, autor o género
  - [ ] del método para tomar prestado un libro
  - [ ] del método para devolver un libro
- Arquitectura:
  - [ ] Definir otra alternativa a esta arquitectura y justificarla
- Implementación del método buscar un libro por título, autor o género y determinar eficiencia de este código
