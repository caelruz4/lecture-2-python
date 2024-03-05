# main.py

from funciones_calculadora import *

def main():
    print("¡Bienvenido a la calculadora!")

    while True:
        print("\nOpciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Calcular Cuadrado")
        print("6. Salir")

        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == '6':
            print("¡Hasta luego!")
            break

        try:
            if opcion in ['1', '2', '3', '4', '5']:
                if opcion in ['1', '2', '3', '4']:
                    num1 = float(input("Ingrese el primer número: "))
                    num2 = float(input("Ingrese el segundo número: "))

                if opcion == '1':
                    print("Resultado:", +sumar(num1, num2))
                elif opcion == '2':
                    print("Resultado:", +restar(num1, num2))
                elif opcion == '3':
                    print("Resultado:", multiplicar(num1, num2))
                elif opcion == '4':
                    print("Resultado:", dividir(num1, num2))
                elif opcion == '5':
                    num = float(input("Ingrese el número para calcular su cuadrado: "))
                    print("Resultado:", calcular_cuadrado(num))
                else:
                    print("Opción no válida. Por favor, ingrese un número del 1 al 7.")

            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 7.")

        except ValueError:
            print("Error: Ingrese números válidos.")

if __name__ == "__main__":
    main()
