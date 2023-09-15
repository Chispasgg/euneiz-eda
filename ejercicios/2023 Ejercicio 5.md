# Ejercicio 5: Gestión de Rutas Marítimas

**Descripción del Problema:** 

Crea un sistema que permita a las navieras gestionar y planificar rutas marítimas para sus embarcaciones, teniendo en cuenta la distancia, condiciones climáticas y costos.

**Pseudocódigo:**

```python
Clase RutaMaritima:
    Atributos:
        - Origen
        - Destino
        - Distancia
        - CondicionesClimaticas
    Métodos:
        - Constructor (origen, destino, distancia, condiciones_climaticas)
        - CalcularCosto()

Clase Naviera:
    Atributos:
        - Nombre
        - Lista de RutasMaritimas
    Métodos:
        - Constructor (nombre)
        - AgregarRuta(ruta)
        - EliminarRuta(ruta)
```

## Arquitectura Sugerida

Cual es tu arquitectura sugerida para este problema

### Descripción

Define el motivo de la elección de esa arquitectura

## Se requiere

- Pseudocodigo:
  - [ ] del método para calcular el costo de una ruta
  - [ ] del método para agregar una ruta
  - [ ] del método para eliminar una ruta
- Arquitectura:
  - [ ] Definir la arquitectura y justificarla
- Implementación del método **agregar una ruta** y determinar eficiencia de este código
