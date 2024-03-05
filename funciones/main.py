def cuadrado(numero):
    cuadrado = numero ** 2 # Operador de potencia ** 2
    return cuadrado

def main():
    numero = float(input("Ingrese un número: "))

    resultado = cuadrado(numero)
    print(f"El cuadrado de {numero} es: {resultado}")

# Llamar a la función main si el script se ejecuta directamente
if __name__ == "__main__":
    main()
