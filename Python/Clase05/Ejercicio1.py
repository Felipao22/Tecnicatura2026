# Ejercicio: Valor dentro de un rango
valor = int(input("Ingrese un número dentro del rango o al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} está dentro del rango")
else:
    print(f"El valor {valor} no está dentro del rango")