import random
import time

print("*****PARTICIPANTES*****")
with open("alumnos.txt", "r") as alumno:
    alumnos = alumno.read().split("\n")
    print(alumnos)

continuar = "si"
while continuar != 'no':
    continuar = input("Desea sortear? (si/no): ")

    if continuar == "si":
    
        numero = random.randint(0,len(alumnos)-1)
        print("*****SORTEO******")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Alumno sorteado: ",alumnos[numero])
    elif continuar == "no":
        break        
    else:
        print("Debe ingresar una opción correcta (si/no)")


print("Gracias por participar del sorteo 😊")
