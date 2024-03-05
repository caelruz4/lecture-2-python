
gatito = {
    'nombre': 'Oreo',
    'color': 'negro',
    'origen': 'UNI',
    'edad': 5,
    'alimentacion': ['carne', 'leche']
}

# Acceder a un valor por su clave
print(gatito['nombre'])
# Añadir par clave-valor
gatito['raza'] = 'siamés'

# Claves del diccionario
print(gatito.keys())

# Valores del diccionario
print(gatito.values())

# Pares clave-valor
print(gatito.items())
# Comprobar si una clave existe
print('nombre' in gatito)

# Get 
print(gatito.get('nombre'))
#Borrar clave
gatito.pop('raza')
print(gatito)