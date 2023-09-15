# Ejercicio 8: Gestión de Compras de Alimentos

**Descripción del Problema:**

Crea un sistema que permita a los clientes de un supermercado realizar compras de alimentos en línea, agregar productos a un carrito y realizar el pago.

**Pseudocódigo:**

```python
Clase Cliente:
    Atributos:
        - Nombre
        - Carrito de Compras (lista de ProductosComestibles)
    Métodos:
        - Constructor (nombre)
        - AgregarAlCarrito(producto)
        - RealizarPago()

Clase CarritoDeCompras:
    Atributos:
        - Lista de ProductosComestibles
    Métodos:
        - Constructor ()
        - AgregarProducto(producto)
        - EliminarProducto(producto)
```

## Arquitectura Sugerida

Cual es tu arquitectura sugerida para este problema

### Descripción

Define el motivo de la elección de esa arquitectura

## Se requiere

- Pseudocodigo:
  - [ ] del método para agregar al carrito un articulo
  - [ ] del método para realizar el pago de todos los articulos del carrito
- Arquitectura:
  - [ ] Definir la arquitectura y justificarla
- Implementación del método **realizar el pago de todos los articulos del carrito** y determinar eficiencia de este código
