# Ejercicio 2:
# Determinar la solución lógica de la siguiente operación:
# ((3 + 5 x 8 ) < 3 and ((- 6/3 x 4 ) + 2 < 2)) or ( a > b)

# Se declaran dos variables para realizar la comparación final
a = 10
b = 5

# La expresión contiene operaciones matemáticas,
# comparaciones lógicas y operadores booleanos.

# Primero se evalúan las operaciones matemáticas,
# luego se realizan las comparaciones (< y >).
# Después se resuelve el operador lógico AND.
# Finalmente se evalúa el operador lógico OR.
resultado = ((3 + 5 * 8) < 3 and ((- 6/3 * 4) + 2 < 2) or (a > b))
print("Resultado:",resultado)