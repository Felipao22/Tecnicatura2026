# Ejercicio 4: Área y longitud de un circulo
# Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia.
#
# Área = Pi * r**2
# Longitud = 2 * Pi * r

import math

radio = float(input("Ingresa el radio de la circunferencia: "))

# Calculamos el área y la longitud
area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

print("El valor del área de la circunferencia es:", area)
print("El valor del longitud de la circunferencia es:", longitud)