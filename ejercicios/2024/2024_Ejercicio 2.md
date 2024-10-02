# Ejercicio 2: Sistema de Gestión de Paking

**Descripción del Problema:**

El sistema debe gestionar la entrada y salida de vehículos en un parking. Los usuarios pueden registrar su vehículo, obtener un tiquete de parking y pagar por el tiempo que estuvieron estacionados.

**Clases importantes**

```python
Clase Vehículo:
    Atributos:
        - Placa
        - Tipo (Coche/Moto)
    Métodos:
        - Constructor(placa, tipo)

Clase Ticket:
    Atributos:
        - Vehículo (objeto Vehículo)
        - HoraDeEntrada
        - HoraDeSalida
        - MontoAPagar
    Métodos:
        - Constructor(vehículo, hora_entrada)
        - RegistrarSalida(hora_salida)
        - CalcularMontoAPagar(tarifa)

Clase Parking:
    Atributos:
        - Capacidad
        - VehículosEstacionados (lista de objetos Ticket)
    Métodos:
        - Constructor(capacidad)
        - RegistrarEntrada(vehículo)
        - RegistrarSalida(placa)
```

## Arquitectura Sugerida

Cual es tu arquitectura sugerida para este problema

### Descripción

Define el motivo de la elección de esa arquitectura

## Se requiere

- Pseudocodigo:
  - [ ] del método para **calcular_monto_a_pagar**
- Arquitectura:
  - [ ] Definir la arquitectura y justificarla
- Implementación del método **para registrar_salida** y determinar eficiencia de este código
