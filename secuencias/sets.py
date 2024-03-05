s = set() # crea un conjunto vacio
# Otra forma de iniciar set
a = {1, 2, 3, 4}
b = {}
# Ojo: No confundir set con diccionario
# print(type(s))
# print(type(a))
# print(type(b))

s.add(1) # agrega un elemento
s.add(2)
s.add(3)
s.add(4)
print(s)

s.remove(2) # elimina un elemento
s.discard(1) # elimina un elemento no tira error si no lo encuentra
print(s)
# No puedo acceder mediante un índice
# print(s[0])
# Update para añadir mas de un elemento
s.update([5, 6, 7])


# Union
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = s1.union(s2)
# s3 = s1 | s2
print(s3)

# Intersección
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = s1.intersection(s2)
# s3 = s1 & s2
print(s3)

# Diferencia
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = s1.difference(s2)
# s3 = s1 - s2
print(s3)