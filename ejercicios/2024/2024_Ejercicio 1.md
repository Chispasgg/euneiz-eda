## Ejercicio 1: Sistema de Gestión de Hospital

**Descripción del Problema:**

Se requiere el diseño de un sistema de gestión de hospital que permita a los doctores gestionar las citas de los pacientes, así como al personal administrativo manejar el registro de pacientes y doctores. El sistema debe permitir a los doctores registrar consultas, recetar medicamentos y realizar un seguimiento del historial clínico del paciente.

**Clases importantes**

```python
Clase Paciente:
    Atributos:
        - Nombre
        - Edad
        - HistorialClínico (lista de objetos Consulta)
    Métodos:
        - Constructor (nombre, edad)
        - AgregarConsulta(consulta)
        - VerHistorial()

Clase Doctor:
    Atributos:
        - Nombre
        - Especialidad
        - PacientesAsignados (lista de objetos Paciente)
    Métodos:
        - Constructor (nombre, especialidad)
        - RegistrarConsulta(paciente, consulta)
        - RecetarMedicamento(paciente, medicamento)

Clase Consulta:
    Atributos:
        - Fecha
        - Síntomas
        - Diagnóstico
        - MedicamentoRecetado
    Métodos:
        - Constructor(fecha, síntomas, diagnóstico, medicamento)
    
Clase Hospital:
    Atributos:
        - Doctores (lista de objetos Doctor)
        - Pacientes (lista de objetos Paciente)
    Métodos:
        - Constructor ()
        - RegistrarPaciente(paciente)
        - AsignarPacienteADoctor(paciente, doctor)
```

## Arquitectura Sugerida

Cual es tu arquitectura sugerida para este problema

### Descripción

Define el motivo de la elección de esa arquitectura

## Se requiere

- Pseudocodigo:
  - [ ] del método para **recetar_medicamento**
- Arquitectura:
  - [ ] Definir la arquitectura y justificarla
- Implementación del método **para asignar_paciente_a_doctor** y determinar eficiencia de este código
