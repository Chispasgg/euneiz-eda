import datetime
import random


class Paciente:

    def __init__(self, nombre, edad):
        print(f"Creando al paciente {nombre} con {edad} años")
        self.nombre = nombre
        self.edad = edad
        self.historial_clinico = []

    def agregar_consulta(self, consulta):
        # TODO: Implementar la lógica para agregar la consulta al historial del paciente
        print("agregar_consulta")

    def ver_historial(self):
        # TODO: Implementar la lógica para mostrar el historial del paciente
        print("ver_historial")


class Doctor:

    def __init__(self, nombre, especialidad):
        print(f"Creando al Doctor {nombre} especialista en {especialidad}")
        self.nombre = nombre
        self.especialidad = especialidad
        self.pacientes_asignados = []

    def registrar_consulta(self, paciente, consulta):
        # TODO: Implementar la lógica para registrar la consulta al paciente
        print("registrar_consulta")

    def recetar_medicamento(self, paciente, medicamento):
        # TODO: Implementar la lógica para recetar el medicamento
        print("recetar_medicamento")

# Clase Consulta


class Consulta:

    def __init__(self, fecha, sintomas, diagnostico, medicamento_recetado=None):
        print(
            f"Creando una consulta el día {fecha} con los sintomas {sintomas}")
        if medicamento_recetado:
            print(f"\t\t Tiene el medicamento recetado {medicamento_recetado}")
        self.fecha = fecha
        self.sintomas = sintomas
        self.diagnostico = diagnostico
        self.medicamento_recetado = medicamento_recetado

# Clase Hospital


class Hospital:

    def __init__(self):
        self.doctores = []
        self.pacientes = []

    def registrar_paciente(self, paciente):
        # TODO: Implementar la lógica para registrar pacientes
        print("registrar_paciente")

    def registrar_doctor(self, doctor):
        # TODO: Implementar la lógica para registrar doctores
        print("registrar_doctor")

    def buscar_paciente(self, nombre_paciente):
        # TODO: Implementar la lógica para buscar pacientes
        print("buscar_paciente")
    
    def buscar_doctor(self, nombre_doctor):
        # TODO: Implementar la lógica para buscar doctores
        print("buscar_doctor")

    def asignar_paciente_a_doctor(self, nombre_paciente, nombre_doctor):
        # TODO: Implementar la lógica para buscar y asignar pacientes a doctores
        print("asignar_paciente_a_doctor")


if __name__ == '__main__':

    # Ejemplo de uso del sistema
    # Crear el hospital
    hospital = Hospital()
    
    # Crear pacientes
    paciente1 = Paciente("Juan Perez", 30)
    paciente2 = Paciente("Maria Lopez", 25)
    
    # Registrar pacientes en el hospital
    hospital.registrar_paciente(paciente1)
    hospital.registrar_paciente(paciente2)
    
    # Crear doctores
    doctor1 = Doctor("Dr. Martinez", "Cardiología")
    doctor2 = Doctor("Dra. Gómez", "Pediatría")
    
    # Asignar pacientes a doctores
    hospital.asignar_paciente_a_doctor(paciente1, doctor1)
    hospital.asignar_paciente_a_doctor(paciente2, doctor2)
    
    # Registrar una consulta para un paciente
    consulta1 = Consulta("2024-09-09", "Dolor de pecho", "Cardiopatía leve")
    doctor1.registrar_consulta(paciente1, consulta1)
    
    # Recetar un medicamento al paciente
    doctor1.recetar_medicamento(paciente1, "Aspirina")
    
    # Ver el historial del paciente
    paciente1.ver_historial()
