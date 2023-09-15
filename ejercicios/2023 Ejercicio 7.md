# Ejercicio 7: Sistema de Gestión de Inventario

**Descripción del Problema:**

Diseña un sistema que permita a un supermercado gestionar su inventario de productos comestibles, incluyendo la gestión de fechas de caducidad y reabastecimiento.

**Pseudocódigo:**

```python
Clase ProductoComestible:
    Atributos:
        - Nombre
        - Fecha de Caducidad
        - Stock
    Métodos:
        - Constructor (nombre, fecha_caducidad, stock)
        - VerificarCaducidad()
        - ReabastecerStock(cantidad)

Clase Supermercado:
    Atributos:
        - Nombre
        - Lista de ProductosComestibles
    Métodos:
        - Constructor (nombre)
        - AgregarProducto(producto)
        - EliminarProducto(producto)
        - VerificarCaducidades()
```

## Arquitectura Sugerida

Cual es tu arquitectura sugerida para este problema

### Descripción

Define el motivo de la elección de esa arquitectura

## Se requiere

- Pseudocodigo:
  - [ ] del método para agregar un producto
  - [ ] del método para eliminar un producto
  - [ ] del método para verificar la caducidad de todos los productos del supermercado
- Arquitectura:
  - [ ] Definir la arquitectura y justificarla
- Implementación del método **verificar la caducidad de todos los productos del supermercado** y determinar eficiencia de este código
