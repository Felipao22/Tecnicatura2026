# Ejercicio 1: Definir año bisiesto
opcion = 0

while opcion != 1:
    print("Comprobamos que el año es bisiesto")

    num = int(input("Ingrese el año: "))

    if(num % 4 == 0 and num % 100 != 0 or num % 400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
    opcion = int(input("Para finalizar ingrese la opción 1: "))
print("Fin del programa")