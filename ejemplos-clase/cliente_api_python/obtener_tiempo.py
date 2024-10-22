import json
import requests
from geopy.geocoders import Nominatim

# Función para obtener la dirección con Nominatim
def obtener_direccion(latitud, longitud):
    geolocator = Nominatim(user_agent="test")
    location = geolocator.reverse(f"{latitud}, {longitud}")
    return location

# Función para obtener los datos del clima y la dirección
def obtener_clima(latitude, longitude):
    try:
        # Obtener la latitud y longitud desde la interfaz
        latitud = latitude.strip()
        longitud = longitude.strip()
        
        # Validar si los campos están vacíos
        if not latitud or not longitud:
            print("Advertencia", "Por favor, ingrese la latitud y la longitud.")
            return

        # Obtener la dirección usando Nominatim
        direccion = obtener_direccion(latitud, longitud)

        # URL de la API con los valores ingresados por el usuario
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        
        # Hacer la solicitud a la API del clima
        response = requests.get(url)
        data = response.json()

        print("lugar de las coordenadas:")
        print(json.dumps(direccion.raw, indent=4))
        print("Datos del tiempo:")
        print(json.dumps(data, indent=4))

        
    except Exception as e:
        print(f"Error al obtener los datos: {e}")


print("Obtener el clima de un lugar concreto")
latitude = input("inserta la latitud ")
longitude = input("inserta la longitud ")

obtener_clima(latitude, longitude)




