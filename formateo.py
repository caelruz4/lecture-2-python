a = 12000
b = 3.14164
c = 0.81

print(f"{a:,}") # 12,000 Si le aumentas el numero en la variable, aun asi se iran colocando las comas en la posicion que es 
print(f"{b:.2f}") # 3.14

# Mostrando como porcentaje
print(f"{c:.2%}") 

# Mostrando con signos
number_pos = 7
number_neg = -7
print(f"{number_pos: }")  # Outputs: " 7"
print(f"{number_neg:+}")  # Outputs: "-7"

# String Truncation
long_string = "La negra tiene tumbao"
print(f"{long_string[:10]}...")  #especifica la cantidad de letras que quiero que aparezca, -1 es para que aparezca la ultima letra 

# Binario, Octal y Hexadecimal
number = 42
print(f"{number:b}")  # Outputs: "101010"
print(f"{number:o}")  # Outputs: "52"
print(f"{number:x}")  # Outputs: "2a"
