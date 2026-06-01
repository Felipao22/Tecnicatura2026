# Ejercicio 2: Calcular la suma de "N" primeros números
N = int(input("Ingrese la cantidad de numeros a sumarse: "))
suma = 0
i = 0
for i in range(1, N + 1):
    suma += i
print(f"La suma es: {suma}")