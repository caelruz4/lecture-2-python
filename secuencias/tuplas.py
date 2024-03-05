# Crear una tupla
mi_tupla = (1, 2, 3, 4, 5)

# Acceder a elementos de la tupla
print(mi_tupla[0])  # Salida: 1

# Obtener la longitud de la tupla
print(len(mi_tupla))  # Salida: 5

print(mi_tupla.index(3))  # Salida: 2
print(mi_tupla.count(4))  # Salida: 1

# Concatenar tuplas
otra_tupla = (6, 7, 8)
nueva_tupla = mi_tupla + otra_tupla
print(nueva_tupla)  # Salida: (1, 2, 3, 4, 5, 6, 7, 8)