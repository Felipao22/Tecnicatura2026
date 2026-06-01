#Califica tu dia

calificacion = int(input("¿Cómo estuvo tu día (1 al 10)? "))

if 1 <= calificacion <= 10:
    print("Tu día estuvo de: ", calificacion)

    if calificacion >= 9:
        print("¡Excelente día!")
    elif calificacion >= 7:
        print("Buen día")
    elif calificacion >= 5:
        print("Día regular")
    else:
        print("Día difícil")
else:
    print("Por favor ingrese un número del 1 a l 10.")
