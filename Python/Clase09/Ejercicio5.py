num = int(input("Ingrese un numero: "))

while num <= 0:
    print("Error: debe ingresar un número mayor que 0")
    num = int(input("Ingrese un numero: "))
i = 1
factorial = 1
while i <= num:
    factorial *= i
    i += 1
print(f"El factorial del numero {num} es: {factorial}")
