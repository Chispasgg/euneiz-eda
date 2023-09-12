# Ejercicio 3: Sistema de Gestión de Tareas

**Descripción del Problema:** 

Diseña un sistema de gestión de tareas que permita a los usuarios crear, editar, completar y eliminar tareas. Cada tarea debe tener un título, una descripción y un estado (pendiente, en progreso, completada).

**Pseudocódigo:**

```python
Clase Tarea:
    Atributos:
        - Título
        - Descripción
        - Estado (pendiente, en progreso, completada)
    Métodos:
        - Constructor (título, descripción)
        - CambiarEstado(estado)
        - EditarTarea(título, descripción)

Clase Usuario:
    Atributos:
        - Nombre
        - Lista de Tareas (lista de objetos Tarea)
    Métodos:
        - Constructor (nombre)
        - AgregarTarea(tarea)
        - EditarTarea(tarea, nuevoTítulo, nuevaDescripción)
        - CambiarEstadoTarea(tarea, nuevoEstado)
        - EliminarTarea(tarea)

Clase ListaDeTareas:
    Atributos:
        - Lista de Tareas (lista de objetos Tarea)
    Métodos:
        - Constructor ()
        - AgregarTarea(tarea)
        - EliminarTarea(tarea)
        - ObtenerTareasPorEstado(estado)
```

## Arquitectura Sugerida: Arquitectura Monolítica

### Descripción

Para un sistema de gestión de tareas simple, una arquitectura monolítica puede ser adecuada. En esta arquitectura, todos los componentes del sistema, como la interfaz de usuario, la lógica de negocio y la base de datos, se ejecutan en una sola aplicación. Esto simplifica el desarrollo inicial y es apropiado para aplicaciones pequeñas o prototipos. Sin embargo, a medida que la aplicación crece en complejidad, puede ser necesario migrar a una arquitectura más escalable, como una arquitectura de microservicios.

## Se requiere

- Pseudocodigo:
  - [ ] del método para agregar una tarea
  - [ ] del método para editar una tarea
  - [ ] del método para cambiar el estado de una tarea (pendiente, en progreso, completada)
  - [ ] del método para eliminar una tarea
- Arquitectura:
  - [ ] Definir otra alternativa a esta arquitectura y justificarla
- Implementación del método para eliminar una tarea y determinar eficiencia de este código
