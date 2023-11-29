'''
Created on 24 nov 2023

@author: chispas
'''

import random
from datetime import datetime, timedelta

ciudades_origen = [
    "Madrid", "Barcelona", "Londres", "París", "Berlín", "Roma", "Ámsterdam", "Viena", "Bruselas", "Helsinki",
    "Dublín", "Praga", "Lisboa", "Estocolmo", "Copenhague", "Atenas", "Varsovia", "Oslo", "Budapest", "Moscú",
    "Nueva York", "Los Ángeles", "Chicago", "Houston", "Toronto", "Montreal", "Vancouver", "Miami", "San Francisco",
    "Washington D.C.", "Boston", "Seattle", "Dallas", "Phoenix", "Denver", "Las Vegas", "Atlanta", "Filadelfia",
    "Austin", "Portland", "San Diego", "Honolulu", "Nashville", "Orlando", "Detroit", "San Antonio", "Minneapolis",
    "Manchester", "Birmingham", "Dublín", "Edimburgo", "Glasgow", "Leeds", "Liverpool", "Bristol", "Cardiff",
    "Amberes", "Brujas", "Gante", "Lieja", "Charleroi", "Múnich", "Hamburgo", "Fráncfort", "Colonia", "Stuttgart",
    "Düsseldorf", "Dresde", "Leipzig", "Dortmund", "Essen", "Bremen", "Hanóver", "Núremberg", "Augsburgo", "Lisboa",
    "Oporto", "Coímbra", "Faro", "Porto", "Braga", "Cascais", "Funchal", "Guimarães", "Évora", "Aveiro",
    "Génova", "Florencia", "Venecia", "Milán", "Nápoles", "Turín", "Verona", "Bolonia", "Palermo", "Ferrara",
    "Basilea", "Ginebra", "Zúrich", "Berna", "Lausana", "Lucerna", "San Sebastián", "Bilbao", "Valencia", "Málaga",
    "Sevilla", "Bilbao", "Granada", "Zaragoza", "Palma de Mallorca", "Alicante", "Murcia", "Córdoba", "Valladolid",
    "Oviedo", "Santiago de Compostela", "Gijón", "Pamplona", "Vigo", "Cádiz", "Helsinki", "Turku", "Tampere",
    "Espoo", "Rovaniemi", "Oulu", "Jyväskylä", "Vantaa", "Lahti", "Kuopio", "Joensuu", "Porvoo", "Vaasa",
    "Tallin", "Tartu", "Pärnu", "Narva", "Kohtla-Järve", "Vilna", "Kaunas", "Klaipėda", "Šiauliai", "Panevėžys",
    "Riga", "Daugavpils", "Liepāja", "Jelgava", "Ventspils", "Tukums", "Valmiera", "Jūrmala", "Madrid", "Barcelona",
    "Londres", "París", "Berlín", "Roma", "Ámsterdam", "Viena", "Bruselas", "Helsinki", "Dublín", "Praga", "Lisboa",
    "Estocolmo", "Copenhague", "Atenas", "Varsovia", "Oslo", "Budapest", "Moscú", "Nueva York", "Los Ángeles", "Chicago",
    "Houston", "Toronto", "Montreal", "Vancouver", "Miami", "San Francisco", "Washington D.C.", "Boston", "Seattle",
    "Dallas", "Phoenix", "Denver", "Las Vegas", "Atlanta", "Filadelfia", "Austin", "Portland", "San Diego", "Honolulu",
    "Nashville", "Orlando", "Detroit", "San Antonio", "Minneapolis", "Manchester", "Birmingham", "Dublín", "Edimburgo",
    "Glasgow", "Leeds", "Liverpool", "Bristol", "Cardiff", "Amberes", "Brujas", "Gante", "Lieja", "Charleroi",
    "Múnich", "Hamburgo", "Fráncfort", "Colonia", "Stuttgart", "Düsseldorf", "Dresde", "Leipzig", "Dortmund",
    "Essen", "Bremen", "Hanóver", "Núremberg", "Augsburgo", "Lisboa", "Oporto", "Coímbra", "Faro", "Porto",
    "Braga", "Cascais", "Funchal", "Guimarães", "Évora", "Aveiro", "Génova", "Florencia", "Venecia", "Milán",
    "Nápoles", "Turín", "Verona", "Bolonia", "Palermo", "Ferrara", "Basilea", "Ginebra", "Zúrich", "Berna",
    "Lausana", "Lucerna", "San Sebastián", "Bilbao", "Valencia", "Málaga", "Sevilla", "Bilbao", "Granada",
    "Zaragoza", "Palma de Mallorca", "Alicante", "Murcia", "Córdoba", "Valladolid", "Oviedo", "Santiago de Compostela",
    "Gijón", "Pamplona", "Vigo", "Cádiz", "Helsinki", "Turku", "Tampere", "Espoo", "Rovaniemi", "Oulu", "Jyväskylä",
    "Vantaa", "Lahti", "Kuopio", "Joensuu", "Porvoo", "Vaasa", "Tallin", "Tartu", "Pärnu", "Narva", "Kohtla-Järve",
    "Vilna", "Kaunas", "Klaipėda", "Šiauliai", "Panevėžys", "Riga", "Daugavpils", "Liepāja", "Jelgava", "Ventspils",
    "Tukums", "Valmiera", "Jūrmala"
]

ciudades_destino = [
    "Tokio", "Pekín", "Nueva Delhi", "Mumbai", "Singapur", "Seúl", "Shanghái", "Bangkok", "Hong Kong", "Taipéi",
    "Manila", "Yakarta", "Kuala Lumpur", "Hanoi", "Ciudad de Ho Chi Minh", "Islamabad", "Karachi", "Lahore", "Bangalore",
    "Chennai", "Bogotá", "Ciudad de México", "Lima", "Santiago de Chile", "Buenos Aires", "San Pablo", "Río de Janeiro",
    "Brasilia", "Lima", "Quito", "Guayaquil", "Asunción", "La Paz", "Montevideo", "Caracas", "San José", "San Salvador",
    "Managua", "Tegucigalpa", "Guatemala", "Panamá", "Tashkent", "Kabul", "Biskek", "Dusambé", "Astana", "Bishkek",
    "Dushanbe", "Ulan Bator", "Naypyidaw", "Phnom Penh", "Vientiane", "Malé", "Doha", "Kuwait City", "Mascate",
    "Manama", "Riad", "Abu Dhabi", "Kathmandu", "Muscat", "Manama", "Sanaa", "Bagdad", "Jerusalén", "Teherán",
    "Amán", "Beirut", "Damasco", "Ankara", "Roma", "París", "Londres", "Madrid", "Berlín", "Viena", "Ámsterdam",
    "Bruselas", "Estocolmo", "Copenhague", "Helsinki", "Varsovia", "Dublín", "Praga", "Lisboa", "Budapest", "Atenas",
    "Bucarest", "Berna", "Oslo", "Belgrado", "Reikiavik", "Sofía", "Minsk", "Zagreb", "Skopie", "Tirana", "Ljubljana",
    "Podgorica", "Nicosia", "Bakú", "Ereván", "Tbilisi", "Chisinau", "Vilna", "Tallin", "Bratislava", "Riga", "Hanoi",
    "Yakarta", "Kuala Lumpur", "Pnom Penh", "Vientiane", "Malé", "Bangkok", "Bandar Seri Begawan", "Manila", "Singapur",
    "Phnom Penh", "Vientiane", "Naypyidaw", "Yakarta", "Bangkok", "Singapur", "Kuala Lumpur", "Manila", "Hanói",
    "Yangon", "Phnom Penh", "Vientiane", "Bandar Seri Begawan", "Dili", "Malé", "Thimphu", "Islamabad", "Nueva Delhi",
    "Katmandú", "Colombo", "Daca", "Kabul", "Teherán", "Biskek", "Dusambé", "Taskent", "Ashgabat", "Astana", "Bishkek",
    "Dushanbe", "Ulan Bator", "Minsk", "Chisinau", "Yerevan", "Tbilisi", "Baku", "Tashkent", "Dushanbe", "Ashgabat",
    "Astana", "Ulan Bator", "Kathmandu", "Islamabad", "Dhaka", "Colombo", "Male", "Thimphu", "Kabul", "Tehran",
    "Bishkek", "Dushanbe", "Tashkent", "Ashgabat", "Nur-Sultan", "Ulaanbaatar", "Pyongyang", "Seúl", "Tokyo",
    "Beijing", "Taipei", "Manila", "Hanoi", "Bangkok", "Vientiane", "Kuala Lumpur", "Singapore", "Jakarta", "Bandar Seri Begawan",
    "Dili", "Pyongyang", "Seoul", "Tokyo", "Beijing", "Taipei", "Manila", "Hanoi", "Bangkok", "Vientiane", "Kuala Lumpur",
    "Singapore", "Jakarta", "Bandar Seri Begawan", "Dili", "Pyongyang", "Seoul", "Tokyo", "Beijing", "Taipei", "Manila",
    "Hanoi", "Bangkok", "Vientiane", "Kuala Lumpur", "Singapore", "Jakarta", "Bandar Seri Begawan", "Dili"
]


class Vuelo:

    def __init__(self, numero, origen, destino, fecha_salida, asientos_disponibles):
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.fecha_salida = fecha_salida
        self.asientos_disponibles = asientos_disponibles


class Usuario:

    def __init__(self, nombre, reservas):
        self.nombre = nombre
        self.reservas = reservas


class Aeropuerto:

    def __init__(self, vuelos):
        self.vuelos = vuelos

    def reservarAsiento(self, origen, destino, fecha, usuario):
        # TODO: implementar
    
    def obtener_info_vuelos(self):
        ciudades_origen = set()
        ciudades_destino = set()
        fechas_disponibles = set()

        for vuelo in self.vuelos:
            ciudades_origen.add(vuelo['origen'])
            ciudades_destino.add(vuelo['destino'])
            fechas_disponibles.add(vuelo['fecha_salida'])

        return ciudades_origen, ciudades_destino, fechas_disponibles
    
    def obtener_posibles_destinos(self, ciudad_origen):
        posibles_destinos = []
        for vuelo in self.vuelos:
            if vuelo['origen'] == ciudad_origen:
                posibles_destinos.append((vuelo['destino'], vuelo['fecha_salida'], vuelo['numero']))
        return posibles_destinos


# Función para generar una lista de vuelos con valores aleatorios
def generar_vuelos(num_vuelos):
    lista_vuelos = []
    for _ in range(num_vuelos):
        numero_vuelo = f"Vuelo {random.randint(1000, 9999)}"
        origen = random.choice(ciudades_origen)
        destino = random.choice(ciudades_destino)
        
        # origen = random.choice(["ciudad a", "ciudad b", "ciudad c"])
        # destino = random.choice(["ciudad x", "ciudad y", "ciudad z"])
        
        fecha_salida = (datetime.now() + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')
        asientos_disponibles = [[random.choice(["Ocupado", "Disponible"]) for _ in range(6)] for _ in range(10)]

        vuelo = Vuelo(numero_vuelo, origen, destino, fecha_salida, asientos_disponibles)
        lista_vuelos.append(vuelo.__dict__)

    return lista_vuelos


if __name__ == '__main__':
    # Generar lista de vuelos y crear objetos Aeropuerto
    lista_vuelos = generar_vuelos(5)
    aeropuerto = Aeropuerto(lista_vuelos)
    
    # Ejemplo de impresión de los datos generados
    print("Vuelos generados:")
    # for vuelo in aeropuerto.vuelos:
    #     print(vuelo)
    
    ciudades_origen, ciudades_destino, fechas_disponibles = aeropuerto.obtener_info_vuelos()

    print("Ciudades de origen:", ciudades_origen)
    print("Ciudades de destino:", ciudades_destino)
    print("Fechas disponibles:", fechas_disponibles)
    
    continuar = True
    while continuar:
        origen = input("> Ciudad Origen: ")
        destinos = aeropuerto.obtener_posibles_destinos(origen)
        for destino_posible in destinos:
            print(destino_posible)
        destino = input("> Ciudad Destino: ")
        fecha = input("> Fecha del vuelo YYYY-MM-DD: ")
        usuario = input("> Nombre del usuario: ")
        
        # creamos el usuario
        usuario1 = Usuario(usuario, [])
        aeropuerto.reservarAsiento(origen, destino, fecha, usuario1)  # Intenta reservar en el vuelo 001

