# Ejercicio 4: Sistema de Gestión de Puertos

**Descripción del Problema:**

Diseña un sistema que permita a los operadores de puertos registrar y gestionar la entrada y salida de buques, programar atraques y descargas, y calcular tarifas según el tipo y tamaño de la embarcación.

**Clases importantes**

```python
Clase Puerto:
    Atributos:
        - Nombre
        - Lista de BuquesAtraque
    Métodos:
        - Constructor (nombre)
        - ProgramarAtraque(buque)
        - RegistrarDescarga(buque, carga)
        - CalcularTarifa(buque)

Clase Buque:
    Atributos:
        - Nombre
        - Tipo
        - Tamaño
    Métodos:
        - Constructor (nombre, tipo, tamaño)
        - CargarCarga(carga)

Clase Carga:
    Atributos:
        - Nombre
        - Peso
    Métodos:
        - Constructor (nombre, peso)
```

## Arquitectura Sugerida

Cual es tu arquitectura sugerida para este problema

### Descripción

Define el motivo de la elección de esa arquitectura

## Se requiere

- Pseudocodigo:
  - [ ] del método para calcular la tarifa de un buque
  - [ ] del método para Registrar la descarga de un buque
  - [ ] del método para programar un atraque de un buque
- Arquitectura:
  - [ ] Definir la arquitectura y justificarla
- Implementación del método **calcular la tarifa de un buque** y determinar eficiencia de este código
