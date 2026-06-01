'''
a = int(input("Ingrese el valor de un número: "))
print(f"El residuo de la división es: {a % 2}")
if(a % 2 == 0):
    print(f"El valor de a es {a} es un número PAR")
else:
    print(f"El valor de a es {a} es un número IMPAR")
'''
edadAdulto = 18
edadPersona = int(input("Ingrese el valor de edad: "))
if(edadPersona >= edadAdulto):
    print(f"Su edad es: {edadPersona} años, es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, es menor de edad")