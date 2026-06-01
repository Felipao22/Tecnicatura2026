"""
Ejercicio 4: Suponga que se tiene un conjunto de calificaciones de un grupo
de 10 alumnos.
Realizar un algoritmo para calcular las calificaciones promedio y la calificación
más baja.
"""

suma = 0
calificacionBaja = 9999

for i in range(1, 11):
    calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))

    suma += calificacion

    if calificacion < calificacionBaja:
        calificacionBaja = calificacion

calificacionPromedio = suma / 10

print(f"La calificación promedio es: {calificacionPromedio}")
print(f"La calificación más baja es: {calificacionBaja}")