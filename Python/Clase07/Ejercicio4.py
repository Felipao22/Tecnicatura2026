#Ejercicio 4: Etapas de vida
edad = int(input("Ingrese su edad: "))
mensaje = None
if 0 <= edad <= 9:
    mensaje = "La infancia es increíble y bella"
elif 10 <= edad <= 19:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad <= 29:
    mensaje = "Amor y comienza el trabajo"
elif 30 <= edad <= 39:
    mensaje = "Comienza la adultez con más responsabilidades y estabilidad."
elif 40 <= edad <= 49:
    mensaje = "Es una etapa de madurez, experiencia y consolidación profesional."
elif 50 <= edad <= 59:
    mensaje = "La experiencia acumulada permite afrontar la vida con mayor confianza."
elif 60 <= edad <= 69:
    mensaje = "Es tiempo de disfrutar los logros alcanzados y mantener una vida activa."
elif 70 <= edad <= 79:
    mensaje = "La sabiduría y las vivencias se convierten en un valioso legado."
elif 80 <= edad <= 99:
    mensaje = "Una etapa para compartir experiencias, recuerdos y disfrutar de la familia."
elif edad >= 100:
    mensaje = "¡Felicitaciones! Has alcanzado una edad extraordinaria llena de historias y aprendizajes."
else:
    mensaje = "La edad ingresada no es válida."
print(f"Para su edad {edad}, {mensaje}")