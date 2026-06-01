# Para usar una referencia como deseamos el tipo de la variable
# se hace por ej: a: str

# Tipos int, float, string, bool
x = 10
print(x)
print(type(x))
x = "Hola mundo"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas
miGrupoFavorito = "Rammstein:"
caracteristicas = "The best rock band"
print("Mi banda favorita es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tipos Booleanos (bool)
miBooleano = 1 > 2
print(miBooleano)

if(miBooleano):
    print("El resultado es verdadero")
else:
    print("El resultado es falso")


# Procesar la entrada del usuario
# función input regresar un dato tipo string
resultado = input("Ingrese un número: ")
print(resultado)

# Conversión de la entrada de datos
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ",int(resultado))
