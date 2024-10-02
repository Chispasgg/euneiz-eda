# Clase Vehículo
class Vehiculo:

    def __init__(self, placa, tipo):
        self.placa = placa
        self.tipo = tipo  # 'Coche' o 'Moto'


# Clase Ticket
class Ticket:

    def __init__(self, vehiculo, hora_entrada):
        self.vehiculo = vehiculo
        self.hora_entrada = hora_entrada
        self.hora_salida = None
        self.monto_a_pagar = 0

    def registrar_salida(self, hora_salida):
        # TODO: Implementar la lógica para registrar la salida del vehículo
        print("registrar_salida")

    def calcular_monto_a_pagar(self, tarifa):
        # TODO: Implementar la lógica para calcular el monto a pagar
        print("calcular_monto_a_pagar")


# Clase Parking
class Parking:

    def __init__(self, capacidad, tarifa):
        self.capacidad = capacidad
        self.tarifa = tarifa  # Tarifa por hora
        self.vehiculos_estacionados = []  # Lista de tickets activos

    def registrar_entrada(self, vehiculo, hora_entrada):
        # TODO: Implementar la lógica para registrar la entrada del vehículo
        print("registrar_entrada")

    def registrar_salida(self, placa, hora_salida):
        # TODO: Implementar la lógica para registrar la salida del vehículo
        print("registrar_salida")


if __name__ == '__main__':
    # Ejemplo de uso del sistema
    # Crear el Parking con una capacidad y una tarifa por hora
    parking = Parking(capacidad=10, tarifa=2.5)

    # Crear vehículos
    vehiculo1 = Vehiculo("ABC123", "Coche")
    vehiculo2 = Vehiculo("XYZ987", "Moto")

    # Registrar la entrada de vehículos
    parking.registrar_entrada(vehiculo1, 10.00)  # Hora de entrada: 10:00 AM
    parking.registrar_entrada(vehiculo2, 11.00)  # Hora de entrada: 11:00 AM

    # Registrar la salida de vehículos
    parking.registrar_salida("ABC123", 14.00)  # Hora de salida: 14:00 PM
    parking.registrar_salida("XYZ987", 15.00)  # Hora de salida: 15:00 PM
