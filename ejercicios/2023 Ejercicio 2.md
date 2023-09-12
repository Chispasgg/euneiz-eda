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
```

## Arquitectura Sugerida: Arquitectura de Microservicios

### Descripción

En esta arquitectura, el sistema de reservas de vuelos se divide en microservicios independientes que gestionan funciones específicas. Por ejemplo, hay un microservicio para la gestión de vuelos, otro para la gestión de asientos y otro para la gestión de reservas. Cada microservicio se ejecuta de manera independiente y se comunica con otros a través de API. Esto permite una escalabilidad y mantenimiento más sencillos, ya que cada parte del sistema se puede desarrollar, desplegar y escalar por separado.

## Se requiere

- Pseudocodigo:
  - [ ] del método para buscar vuelos disponibles
  - [ ] del método para realizar una reserva de asiento en un vuelo
  - [ ] del método para cancelar una reserva de asiento en un vuelo
- Arquitectura:
  - [ ] Definir otra alternativa a esta arquitectura y justificarla
- Implementación del método para realizar una reserva de asiento en un vuelo y determinar eficiencia de este código
