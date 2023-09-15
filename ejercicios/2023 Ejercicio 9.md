# Ejercicio 9: Análisis de Preferencias Alimenticias

**Descripción del Problema:**

Diseña un sistema que permita a un supermercado analizar las preferencias de compra de sus clientes en productos alimenticios para mejorar su oferta y promociones.

**Pseudocódigo:**

```python
Clase Cliente:
    Atributos:
        - Nombre
        - Lista de Compras (lista de ProductosComestibles)
        - ProductosPreferentes (PreferenciasCliente)
    Métodos:
        - Constructor (nombre)
        - AgregarCompra(producto)

Clase PreferenciasCliente:
    Atributos:
        - ProductosPreferidos
    Métodos:
        - Constructor ()
        - ObtenerProductosPreferidos(productos)
        - AgregarProductoComprado(producto)

Clase Supermercado:
    Atributos:
        - Lista de Clientes
    Métodos:
        - Constructor ()
        - AnalizarPreferencias()
```

## Arquitectura Sugerida

Cual es tu arquitectura sugerida para este problema

### Descripción

Define el motivo de la elección de esa arquitectura

## Se requiere

- Pseudocodigo:
  - [ ] del método para analizar las preferencias de los clientes
  - [ ] del método para agregar un nuevo producto comprado por el usuario
- Arquitectura:
  - [ ] Definir la arquitectura y justificarla
- Implementación del método **analizar las preferencias de los clientes** y determinar eficiencia de este código
