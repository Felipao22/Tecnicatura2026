'''
# En esta clase veremos la sentencia if/else
condicion = 10
if condicion == True:
    print("Condición verdadera")
elif condicion == False:
    print("Condición falsa")
else:
    print("Condición sin especificar")
'''
'''
# Ejercicio: Conversión de número a texto
num = int(input("Ingrese un numero en el rango del 1 al 3: "))
numTexto = ''

if num == 1:
    numTexto = "Número uno"
elif num == 2:
    numTexto = "Numero dos"
elif num == 3:
    numTexto = "Número tres"
else:
    numTexto = "Has ingresado un número fuera de rango"
print(f'EL número ingresado es: {num} - {numTexto}')
'''
condicion = False
print("Condición verdadera") if condicion else print("Condición falsa")