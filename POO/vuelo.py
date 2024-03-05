class Vuelo:
    def __init__(self, numero_vuelo, aerolinea, capacidad_maxima):
        self.numero_vuelo = numero_vuelo
        self.aerolinea = aerolinea
        self.capacidad_maxima = capacidad_maxima
        self.pasajeros = []

    def obtener_informacion(self):
        return f"Vuelo {self.numero_vuelo} de {self.aerolinea}. Capacidad máxima: {self.capacidad_maxima} pasajeros."

    def agregar_pasajero(self, nombre_pasajero):
        if len(self.pasajeros) < self.capacidad_maxima:
            self.pasajeros.append(nombre_pasajero)
            return f"{nombre_pasajero} ha sido añadido al vuelo {self.numero_vuelo}."
        else:
            return "El vuelo está completo. No se puede añadir más pasajeros."
        
    # imprimir pasajeros
    def imprimir_pasajeros(self):
        print("Pasajeros en el vuelo:")
        for pasajero in self.pasajeros:
            print(pasajero)


# Crear un objeto Vuelo
vuelo1 = Vuelo(numero_vuelo="V123", aerolinea="Ejemplo Airlines", capacidad_maxima=4)

print(vuelo1.obtener_informacion())

# Agregar pasajeros al vuelo
print(vuelo1.agregar_pasajero("Alice"))
print(vuelo1.agregar_pasajero("Bob"))
print(vuelo1.agregar_pasajero("Charlie"))

print(vuelo1.agregar_pasajero("Dave"))
# Intentar meter a uno más de la capacidad maxima
# print(vuelo1.agregar_pasajero("Katie"))

# Obtener información actualizada del vuelo
print(vuelo1.obtener_informacion())
vuelo1.imprimir_pasajeros()
