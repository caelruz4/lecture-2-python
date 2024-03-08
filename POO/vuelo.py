class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, capacidad_maxima):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad_maxima = capacidad_maxima
        self.pasajeros = []
    
    def __str__(self):
        return f"Vuelo {self.numero_vuelo} de {self.origen} a {self.destino}. Capacidad máxima: {self.capacidad_maxima} pasajeros."

    def obtener_informacion(self):
        return f"Vuelo {self.numero_vuelo} de {self.origen} a {self.destino}. Capacidad máxima: {self.capacidad_maxima} pasajeros."

    def agregar_pasajero(self, nombre_pasajero):
        if len(self.pasajeros) < self.capacidad_maxima:
            self.pasajeros.append(nombre_pasajero)
            return f"{nombre_pasajero} ha sido añadido al vuelo {self.numero_vuelo}."
        else:
            return "El vuelo está completo. No se puede añadir más pasajeros."
        
    def imprimir_pasajeros(self):
        print("Pasajeros en el vuelo:")
        for pasajero in self.pasajeros:
            print(pasajero, end=', ')

# Crear un objeto Vuelo con origen y destino
vuelo1 = Vuelo(numero_vuelo="V123", origen="Ciudad A", destino="Ciudad B", capacidad_maxima=4)
# Agregar pasajeros al vuelo
print(vuelo1.agregar_pasajero("Alice"))
print(vuelo1.agregar_pasajero("Bob"))
print(vuelo1.agregar_pasajero("Charlie"))

print(vuelo1.agregar_pasajero("Dave"))  # Intentar añadir uno más de la capacidad máxima
# print(vuelo1.agregar_pasajero("Katie"))

# Obtener información actualizada del vuelo
print("\n>>> INFORMACIÓN DEL VUELO <<<")
print(vuelo1)
print("\n>>> PASAJEROS <<<")
vuelo1.imprimir_pasajeros()
