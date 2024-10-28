import requests
from geopy.geocoders import Nominatim

# Clase para obtener la dirección a partir de la latitud y longitud usando Nominatim
class Localizador:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = None

    def obtener_direccion(self):
        try:
            geolocator = Nominatim(user_agent="test")
            location = geolocator.reverse(f"{self.latitud}, {self.longitud}")
            self.direccion = location.address if location else "Dirección no encontrada"
        except Exception as e:
            print(f"Error al obtener la dirección: {e}")
            self.direccion = "Error al obtener la dirección"
        return self.direccion


# Clase para obtener el clima (temperatura y velocidad del viento) de Open-Meteo
class Clima:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.temperatura = None
        self.velocidad_viento = None

    def obtener_datos_climaticos(self):
        '''
        # url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&current_weather=true"
        ----------------------------------------------------
        {'latitude': 52.52, 'longitude': 13.419998, 'generationtime_ms': 0.04792213439941406, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 38.0, 'current_weather_units': {'time': 'iso8601', 'interval': 'seconds', 'temperature': '°C', 'windspeed': 'km/h', 'winddirection': '°', 'is_day': '', 'weathercode': 'wmo code'}, 'current_weather': {'time': '2024-10-28T13:30', 'interval': 900, 'temperature': 15.6, 'windspeed': 6.9, 'winddirection': 227, 'is_day': 1, 'weathercode': 3}}
        ----------------------------------------------------

        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        ----------------------------------------------------
        {'latitude': 52.52, 'longitude': 13.419998, 'generationtime_ms': 0.18095970153808594, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 38.0, 'current_weather_units': {'time': 'iso8601', 'interval': 'seconds', 'temperature': '°C', 'windspeed': 'km/h', 'winddirection': '°', 'is_day': '', 'weathercode': 'wmo code'}, 'current_weather': {'time': '2024-10-28T13:30', 'interval': 900, 'temperature': 15.6, 'windspeed': 6.9, 'winddirection': 227, 'is_day': 1, 'weathercode': 3}, 'hourly_units': {'time': 'iso8601', 'temperature_2m': '°C', 'relative_humidity_2m': '%', 'wind_speed_10m': 'km/h'}, 'hourly': {'time': ['2024-10-28T00:00', '2024-10-28T01:00', '2024-10-28T02:00', '2024-10-28T03:00', '2024-10-28T04:00', '2024-10-28T05:00', '2024-10-28T06:00', '2024-10-28T07:00', '2024-10-28T08:00', '2024-10-28T09:00', '2024-10-28T10:00', '2024-10-28T11:00', '2024-10-28T12:00', '2024-10-28T13:00', '2024-10-28T14:00', '2024-10-28T15:00', '2024-10-28T16:00', '2024-10-28T17:00', '2024-10-28T18:00', '2024-10-28T19:00', '2024-10-28T20:00', '2024-10-28T21:00', '2024-10-28T22:00', '2024-10-28T23:00', '2024-10-29T00:00', '2024-10-29T01:00', '2024-10-29T02:00', '2024-10-29T03:00', '2024-10-29T04:00', '2024-10-29T05:00', '2024-10-29T06:00', '2024-10-29T07:00', '2024-10-29T08:00', '2024-10-29T09:00', '2024-10-29T10:00', '2024-10-29T11:00', '2024-10-29T12:00', '2024-10-29T13:00', '2024-10-29T14:00', '2024-10-29T15:00', '2024-10-29T16:00', '2024-10-29T17:00', '2024-10-29T18:00', '2024-10-29T19:00', '2024-10-29T20:00', '2024-10-29T21:00', '2024-10-29T22:00', '2024-10-29T23:00', '2024-10-30T00:00', '2024-10-30T01:00', '2024-10-30T02:00', '2024-10-30T03:00', '2024-10-30T04:00', '2024-10-30T05:00', '2024-10-30T06:00', '2024-10-30T07:00', '2024-10-30T08:00', '2024-10-30T09:00', '2024-10-30T10:00', '2024-10-30T11:00', '2024-10-30T12:00', '2024-10-30T13:00', '2024-10-30T14:00', '2024-10-30T15:00', '2024-10-30T16:00', '2024-10-30T17:00', '2024-10-30T18:00', '2024-10-30T19:00', '2024-10-30T20:00', '2024-10-30T21:00', '2024-10-30T22:00', '2024-10-30T23:00', '2024-10-31T00:00', '2024-10-31T01:00', '2024-10-31T02:00', '2024-10-31T03:00', '2024-10-31T04:00', '2024-10-31T05:00', '2024-10-31T06:00', '2024-10-31T07:00', '2024-10-31T08:00', '2024-10-31T09:00', '2024-10-31T10:00', '2024-10-31T11:00', '2024-10-31T12:00', '2024-10-31T13:00', '2024-10-31T14:00', '2024-10-31T15:00', '2024-10-31T16:00', '2024-10-31T17:00', '2024-10-31T18:00', '2024-10-31T19:00', '2024-10-31T20:00', '2024-10-31T21:00', '2024-10-31T22:00', '2024-10-31T23:00', '2024-11-01T00:00', '2024-11-01T01:00', '2024-11-01T02:00', '2024-11-01T03:00', '2024-11-01T04:00', '2024-11-01T05:00', '2024-11-01T06:00', '2024-11-01T07:00', '2024-11-01T08:00', '2024-11-01T09:00', '2024-11-01T10:00', '2024-11-01T11:00', '2024-11-01T12:00', '2024-11-01T13:00', '2024-11-01T14:00', '2024-11-01T15:00', '2024-11-01T16:00', '2024-11-01T17:00', '2024-11-01T18:00', '2024-11-01T19:00', '2024-11-01T20:00', '2024-11-01T21:00', '2024-11-01T22:00', '2024-11-01T23:00', '2024-11-02T00:00', '2024-11-02T01:00', '2024-11-02T02:00', '2024-11-02T03:00', '2024-11-02T04:00', '2024-11-02T05:00', '2024-11-02T06:00', '2024-11-02T07:00', '2024-11-02T08:00', '2024-11-02T09:00', '2024-11-02T10:00', '2024-11-02T11:00', '2024-11-02T12:00', '2024-11-02T13:00', '2024-11-02T14:00', '2024-11-02T15:00', '2024-11-02T16:00', '2024-11-02T17:00', '2024-11-02T18:00', '2024-11-02T19:00', '2024-11-02T20:00', '2024-11-02T21:00', '2024-11-02T22:00', '2024-11-02T23:00', '2024-11-03T00:00', '2024-11-03T01:00', '2024-11-03T02:00', '2024-11-03T03:00', '2024-11-03T04:00', '2024-11-03T05:00', '2024-11-03T06:00', '2024-11-03T07:00', '2024-11-03T08:00', '2024-11-03T09:00', '2024-11-03T10:00', '2024-11-03T11:00', '2024-11-03T12:00', '2024-11-03T13:00', '2024-11-03T14:00', '2024-11-03T15:00', '2024-11-03T16:00', '2024-11-03T17:00', '2024-11-03T18:00', '2024-11-03T19:00', '2024-11-03T20:00', '2024-11-03T21:00', '2024-11-03T22:00', '2024-11-03T23:00'], 'temperature_2m': [8.7, 8.2, 7.7, 7.1, 7.4, 7.5, 7.4, 8.0, 9.1, 10.5, 12.2, 14.3, 14.8, 15.5, 15.7, 15.2, 14.5, 14.0, 14.0, 13.9, 13.7, 13.4, 13.2, 12.9, 12.6, 12.5, 12.4, 12.3, 12.1, 12.0, 12.0, 12.1, 12.5, 13.0, 13.5, 14.2, 14.7, 14.7, 14.6, 14.4, 14.1, 13.7, 13.3, 13.1, 13.0, 12.9, 12.6, 12.2, 12.4, 12.5, 12.5, 12.5, 12.5, 12.5, 12.4, 12.6, 12.9, 13.7, 14.0, 14.6, 14.8, 14.7, 14.9, 14.7, 14.1, 13.5, 13.0, 12.3, 12.0, 11.9, 11.2, 10.5, 9.8, 9.6, 9.3, 9.3, 9.2, 9.3, 9.1, 9.3, 10.1, 11.3, 12.8, 14.2, 14.9, 15.1, 14.7, 14.3, 13.8, 13.3, 12.9, 12.6, 12.3, 12.1, 11.9, 11.8, 11.7, 11.6, 11.6, 11.6, 11.6, 11.5, 11.5, 11.7, 12.0, 12.4, 12.9, 13.4, 13.8, 13.9, 13.9, 13.8, 13.5, 13.1, 12.8, 12.5, 12.3, 12.1, 11.9, 11.8, 11.6, 11.5, 11.3, 11.2, 11.2, 11.2, 11.2, 11.0, 10.5, 10.1, 10.2, 10.5, 10.5, 10.2, 9.6, 8.7, 7.5, 6.0, 4.7, 3.7, 3.0, 2.4, 1.9, 1.6, 1.3, 1.1, 1.0, 0.9, 0.7, 0.6, 0.7, 1.1, 1.8, 2.8, 4.3, 6.0, 7.2, 7.7, 7.6, 7.2, 6.1, 4.7, 3.4, 2.6, 2.1, 1.6, 1.3, 1.1], 'relative_humidity_2m': [97, 97, 97, 100, 100, 100, 100, 100, 94, 90, 87, 83, 83, 81, 82, 85, 90, 93, 92, 88, 84, 85, 86, 86, 87, 85, 88, 86, 87, 89, 92, 92, 90, 88, 86, 82, 80, 81, 82, 85, 88, 89, 92, 93, 93, 95, 96, 97, 97, 96, 96, 96, 96, 95, 96, 94, 90, 84, 83, 82, 82, 80, 78, 81, 85, 88, 91, 94, 95, 93, 94, 95, 96, 95, 95, 94, 93, 92, 93, 94, 91, 85, 78, 72, 71, 72, 76, 79, 81, 82, 83, 84, 85, 86, 87, 87, 88, 89, 89, 89, 88, 86, 84, 83, 82, 81, 79, 77, 76, 75, 75, 76, 77, 79, 81, 83, 85, 86, 87, 87, 87, 87, 87, 86, 85, 84, 83, 80, 73, 67, 62, 58, 54, 51, 48, 48, 53, 61, 68, 71, 73, 75, 76, 77, 78, 78, 78, 77, 76, 74, 72, 69, 65, 61, 57, 54, 53, 55, 58, 63, 68, 75, 80, 84, 86, 88, 89, 90], 'wind_speed_10m': [3.6, 3.7, 1.8, 4.0, 3.1, 5.8, 5.9, 6.5, 6.3, 5.4, 4.7, 5.9, 6.1, 7.1, 6.6, 6.0, 5.4, 6.4, 7.6, 8.5, 8.9, 9.4, 10.4, 9.4, 8.9, 9.6, 8.8, 8.9, 8.2, 8.1, 7.5, 7.3, 7.9, 7.6, 10.7, 11.4, 10.4, 10.6, 6.7, 5.8, 6.4, 6.7, 6.1, 6.5, 6.7, 7.0, 6.6, 5.4, 6.7, 6.7, 6.9, 6.9, 6.2, 7.2, 7.4, 10.1, 9.8, 14.0, 14.0, 12.8, 12.7, 9.9, 9.8, 8.0, 8.0, 7.3, 6.5, 5.9, 6.4, 5.8, 6.2, 5.6, 5.5, 5.5, 5.0, 4.7, 4.0, 3.7, 4.2, 3.9, 5.1, 5.7, 7.8, 9.0, 10.9, 11.3, 11.4, 11.0, 11.0, 10.9, 10.9, 10.7, 11.0, 11.3, 12.2, 13.0, 13.9, 14.1, 14.4, 14.4, 14.0, 13.8, 13.6, 13.8, 14.8, 15.1, 14.8, 14.1, 13.5, 13.1, 12.6, 11.9, 10.8, 9.5, 8.0, 6.9, 6.2, 6.0, 6.6, 7.4, 8.2, 8.9, 9.7, 10.0, 10.2, 10.0, 9.8, 13.6, 13.0, 12.1, 11.5, 11.3, 10.7, 10.2, 8.9, 7.7, 6.5, 5.0, 4.0, 3.9, 4.1, 4.4, 4.3, 4.4, 4.6, 4.6, 4.6, 4.6, 4.6, 4.8, 4.8, 4.9, 5.4, 5.5, 5.5, 5.2, 4.7, 4.1, 3.3, 2.9, 2.9, 3.3, 3.3, 3.3, 2.9, 2.9, 2.9, 3.3]}}
        ----------------------------------------------------
        '''
        try:
            # URL de la API de Open-Meteo
            # url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&current_weather=true"
            url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
            
            # Hacer la solicitud a la API
            response = requests.get(url)
            data = response.json()

            # print("----------------------------------------------------")
            # print(data)
            # print("----------------------------------------------------")


            if response.status_code == 200 and "current_weather" in data:
                current_weather = data["current_weather"]
                self.temperatura = current_weather["temperature"]
                self.velocidad_viento = current_weather["windspeed"]
            else:
                print("Error: No se pudieron obtener los datos climáticos.")
                self.temperatura, self.velocidad_viento = "Desconocido", "Desconocido"
        except Exception as e:
            print(f"Error al obtener los datos climáticos: {e}")
            self.temperatura, self.velocidad_viento = "Error", "Error"
        return self.temperatura, self.velocidad_viento


# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación
class GestorDeDatosClimaticos:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.localizador = Localizador(latitud, longitud)
        self.clima = Clima(latitud, longitud)

    def obtener_informacion(self):
        # Obtener la dirección
        direccion = self.localizador.obtener_direccion()
        print(f"Dirección: {direccion}")
        
        # Obtener los datos climáticos
        temperatura, velocidad_viento = self.clima.obtener_datos_climaticos()
        print(f"Temperatura: {temperatura}°C")
        print(f"Velocidad del viento: {velocidad_viento} km/h")

# Ejemplo de uso
if __name__ == "__main__":
    # Coordenadas del usuario
    latitud = input("inserta la latitud ")
    longitud = input("inserta la longitud ")

    # Crear el gestor de datos y obtener la información
    gestor = GestorDeDatosClimaticos(latitud, longitud)
    gestor.obtener_informacion()