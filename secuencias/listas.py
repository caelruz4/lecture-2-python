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
print(frutas[1:3])
print(frutas[:3])
frutas.append("mango")
frutas.index("naranja")
frutas.count("naranja")
frutas.sort()
frutas.pop(2)
frutas.remove("naranja")
frutas.reverse() # invertir
frutas.insert(2, "limon")
frutas.clear()