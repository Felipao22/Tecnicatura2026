suma = 0

for i in range(1,6):
    print(f"Salario del empleado {i}")
    horas = int(input("Ingrese las horas trabajadas: "))
    tarifa = float(input("Ingrese la tarifa por hora: "))
    salario = horas * tarifa
    print(f"EL salario es: {salario}")
    suma += salario
print(f"La suma de todos los salarios es: {suma}")