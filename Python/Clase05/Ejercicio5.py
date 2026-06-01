# Ejercicio: Tienda de libros
print("Ingrese los siguiente datos del libro: ")
nombre = input("Ingrese el nombre del libro: ")
id = int(input("Ingrese el ID del libro: "))
precio = float(input("Ingrese el precio del libro: "))
envioGratuito = input("Indicar si el libro tiene envio gratuito (True/False): ")
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = "EL valor es incorrecto, debe escribir True o False"
print(f'''
    Nombre: {nombre}
    ID: {id}
    precio: $ {precio}
    envioGratuito?: {envioGratuito}
''')