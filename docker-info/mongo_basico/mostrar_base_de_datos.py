from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Obtener una lista de todos los nombres de bases de datos
all_dbs = client.list_database_names()

# mostramos todas las bases de datos que hay
print("Todos los nombres de bases de datos:")
for db_name in all_dbs:
    print(db_name)

# mostramos los datos de una base de datos
print("Mostramos los datos de una base de datos prueba-hola")
db_pruebas = client['prueba']['hola'].find({})
for x in db_pruebas:
    print(x)

# metemos datos en la base de datos de prueba hola
for x in range(30):
    client['prueba']['hola'].insert_one({"numero": x,
                                         "latitud":f"34.{x}", 
                                         "longitud":f"-2.{x}"})

# mostramos los datos de una base de datos
print("Mostramos los datos de una base de datos prueba-hola")
db_pruebas = client['prueba']['hola'].find({})
for x in db_pruebas:
    print(x)

# mostramos los datos de una base de datos mediante el filtro
print("Mostramos los datos especificos de una base de datos prueba-hola")
db_pruebas = client['prueba']['hola'].find({"numero":29})
for x in db_pruebas:
    print(x)