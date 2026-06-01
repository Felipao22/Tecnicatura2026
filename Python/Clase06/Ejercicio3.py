# Ejercicio 3:
# Intercambiar el valor de dos variables.
# Por ejemplo:
# a = 10        a = 5
# b = 5         b = 10

a = 10
b = 5
# Mostramos los valores originales
print("Valor de a:", a)
print("Valor de b:", b)

print("Ahora intercambiamos los valores")
# Guardamos el valor de a en aux
aux = a
# b pasa a tener el valor de a
a = b
# b recupera el valor original de a
b = aux

print("Nuevo valor de a:", a)
print("Nuevo valor de b:", b)
