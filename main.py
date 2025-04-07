from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from dividir import dividir
from suma_avanzada import sumaavanzada

def opciones():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sumar Avanzada")
    print("6. Salir")

def start_opcion(opcion):
    if opcion == 1:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print("La suma es:", suma(a, b))
    elif opcion == 2:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print("La resta es:", resta(a, b))
    elif opcion == 3:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print("La multiplicación es:", multiplicacion(a, b))
    elif opcion == 4:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print("La división es:", dividir(a, b))
    elif opcion == 5:
        numeros = list(map(int, input("Ingrese los números separados por espacio: ").split()))
        print("La suma avanzada es:", sumaavanzada(numeros))
    elif opcion == 6:
        print("Saliendo...")
    else:
        print("Opción no válida. Intente de nuevo.")
    

def main():
    while True:
        opciones()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 6:
            break
        start_opcion(opcion)

if __name__ == "__main__":
    main()
# This code is a simple calculator that allows the user to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.