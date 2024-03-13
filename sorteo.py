import random
import time

alumno = ""
alumnos = []
while alumno != "salir":
    alumno = input("Ingrese nombre de alumno (Escriba 'salir' para terminar de cargar): ")
    if alumno != "salir":
        alumnos.append(alumno)

continuar = "si"
while continuar !="no":
    continuar = input("Desea sortear?(si/no):")
    if continuar == "si":        
        numero = random.randint(0,len(alumnos)-1)   
        print("Alumno elegido:",alumnos[numero])
    elif continuar == "no": 
        break
    else:
        print("Debe ingresar una opción correcta (si/no)!!!")
print("Gracias por participar del sorteo 😊!")
    
    


    