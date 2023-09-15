# Ejercicio 2: Sistema de Reservas de Vuelos

**Descripción del Problema:**

Diseña un sistema de reservas de vuelos que permita a los usuarios buscar vuelos disponibles, seleccionar asientos y realizar reservas. Los usuarios deben poder ver la disponibilidad de vuelos en función de la fecha, origen y destino.

**Pseudocódigo:**

```python
Clase Vuelo:
    Atributos:
        - Número de Vuelo
        - Origen
        - Destino
        - Fecha de Salida
        - Asientos Disponibles (matriz de asientos)
    Métodos:
        - Constructor (número de vuelo, origen, destino, fecha de salida, número de filas, número de columnas)
        - MostrarAsientosDisponibles()
        - ReservarAsiento(fila, columna)

Clase Usuario:
    Atributos:
        - Nombre
        - Reservas (lista de objetos Vuelo)
    Métodos:
        - Constructor (nombre)
        - BuscarVuelo(origen, destino, fecha)
        - SeleccionarVuelo(vuelo)
        - RealizarReserva(vuelo, fila, columna)
        - CancelarReserva(vuelo)

Clase Aeropuerto:
    Atributos:
        - Vuelos (lista de objetos Vuelo)
    Métodos:
        - Constructor ()
        - AgregarVuelo(vuelo)
        - EliminarVuelo(vuelo)
        - BuscarVuelo(origen, destino, fecha)
        - ReservarAsiento(origen, destino, fecha, usuario)
```

## Arquitectura Sugerida

Cual es tu arquitectura sugerida para este problema

### Descripción

Define el motivo de la elección de esa arquitectura

## Se requiere

- Pseudocodigo:
  - [ ] del método para buscar vuelos disponibles
  - [ ] del método para realizar una reserva de asiento en un vuelo
  - [ ] del método para cancelar una reserva de asiento en un vuelo
- Arquitectura:
  - [ ] Definir la arquitectura y justificarla
- Implementación del método **para realizar una reserva de asiento en un vuelo** y determinar eficiencia de este código
