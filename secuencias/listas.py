frutas = ["manzana", "banano", "pera", "naranja", "fresa"]

# Ordena la lista en una copia
# Copiar en una lista en otra
frutas2 = frutas.copy()
frutas2.sort()
print(frutas2)

# Ver la de un índice
print(frutas[0])

# índice negativo
print(frutas[-1])

# imprimir la lista de forma inversa
print(frutas[::-1])

# Sublistas, dividiendola
print(frutas[1:3]) #agrega del elemento uno al elemento antes del 3
print(frutas[:3])
frutas.append("mango") #lo agrega al final de la lista
frutas.index("naranja") #el indice en el que aparece por primera vez naranja
frutas.count("naranja") #cuantos elementos hay en mi lista
frutas.sort() #ordena de manera ascendente
frutas.pop(2) #eliminar el elemento de tal indice
frutas.remove("naranja") #eliminar algo en especifico en toda la lista
frutas.reverse() # invertir
frutas.insert(2, "limon") #introducir en la posicion tal palabra
frutas.clear()