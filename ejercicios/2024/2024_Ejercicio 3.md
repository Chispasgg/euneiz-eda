# Ejercicio 2: Sistema de Gestión de Restaurante

**Descripción del Problema:**

Se requiere un sistema que permita gestionar los pedidos de un restaurante. Los clientes pueden realizar pedidos de comida y bebida, mientras que el personal del restaurante puede gestionar esos pedidos y actualizar el estado de los mismos.

**Clases importantes**

```python
Clase Plato:
    Atributos:
        - Nombre
        - Precio
        - Categoría (Comida/Bebida)
    Métodos:
        - Constructor(nombre, precio, categoría)

Clase Pedido:
    Atributos:
        - Cliente
        - ListaDePlatos (lista de objetos Plato)
        - Estado (Pendiente, Preparando, Entregado)
    Métodos:
        - Constructor(cliente)
        - AgregarPlato(plato)
        - CambiarEstado(nuevo_estado)

Clase Cliente:
    Atributos:
        - Nombre
        - Pedidos (lista de objetos Pedido)
    Métodos:
        - Constructor(nombre)
        - HacerPedido(pedido)
        - VerPedidos()

Clase Restaurante:
    Atributos:
        - Menu (lista de objetos Plato)
        - Pedidos (lista de objetos Pedido)
    Métodos:
        - Constructor()
        - AgregarPlato(plato)
        - RegistrarPedido(pedido)
        - ActualizarEstadoPedido(pedido, estado)

```

## Arquitectura Sugerida

Cual es tu arquitectura sugerida para este problema

### Descripción

Define el motivo de la elección de esa arquitectura

## Se requiere

- Pseudocodigo:
  - [ ] del método para **actualizar_estado_pedido**
- Arquitectura:
  - [ ] Definir la arquitectura y justificarla
- Implementación del método **calcular_total** y determinar eficiencia de este código
