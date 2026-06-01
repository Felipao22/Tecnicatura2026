# Ejercicio 3: Calcular estación del año
mes = int(input("Ingrese el numero del mes: "))
estacion = None
if 1 >= mes <= 3:
    estacion = "Verano"
elif 4 <= mes <= 6:
    estacion = "Otoño"
elif 7 <= mes <= 9:
    estacion = "Invierno"
elif 10 <= mes <= 12:
   estacion = "Primavera"
else:
    print("Número del mes inválido")
print(f"Para el mes {mes} la estación es: {estacion}")