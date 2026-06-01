# Ejercicio 5: Sistema de calificaciones

calificacion = float(input("Ingrese un valor del 0 al 10: "))

if 9 <= calificacion <= 10:
    mensaje = "A"
elif 8 <= calificacion < 9:
    mensaje = "B"
elif 7 <= calificacion < 8:
    mensaje = "C"
elif 6 <= calificacion < 7:
    mensaje = "D"
elif 0 <= calificacion < 6:
    mensaje = "F"
else:
    mensaje = "El valor ingresado es incorrecto."

print(f"Para su nota {calificacion}, su calificación es: {mensaje}")