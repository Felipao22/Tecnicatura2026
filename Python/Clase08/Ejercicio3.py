# Ejercicio 3: Leer 10 números e imprimir cuántos son positivos,
# cuántos negativos y cuántos neutros.

conteoPositivos = 0
conteoNegativos = 0
conteoNeutros = 0

for i in range(1, 11):
    num = int(input(f"Ingrese el número {i}: "))

    if num == 0:
        conteoNeutros += 1
    elif num > 0:
        conteoPositivos += 1
    else:
        conteoNegativos += 1

print(f"La cantidad de positivos es: {conteoPositivos}")
print(f"La cantidad de negativos es: {conteoNegativos}")
print(f"La cantidad de neutros es: {conteoNeutros}")