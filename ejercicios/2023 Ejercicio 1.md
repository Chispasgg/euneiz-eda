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

## Arquitectura Sugerida

Cual es tu arquitectura sugerida para este problema

### Descripción

Define el motivo de la elección de esa arquitectura

## Se requiere

- Pseudocodigo:
  - [ ] del método para buscar un libro por título, autor o género
  - [ ] del método para tomar prestado un libro
  - [ ] del método para devolver un libro
- Arquitectura:
  - [ ] Definir la arquitectura y justificarla
- Implementación del método **buscar un libro por título, autor o género** y determinar eficiencia de este código
