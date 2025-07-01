# Juego: Adivina el número secreto
 
import random
 
def jugar_adivina():#Las 3 ratyas de abajo tienen que estar identadas 2
    numero_secreto = random.randint(1, 10)
    intentos = 0
    encontrado = False
 
    print("Bienvenido al juego de adivinar el número")
    print("Tienes 3 intentos para encontrar el número secreto entre 1 y 10")
    
    while intentos < 3 and encontrado == False:
        respuesta = int(input("¿Cuál es tu número?: ")) #Que tiene que ser un int(input()) para escribir un número 4
    
        if respuesta == numero_secreto:
            print("¡Ganaste! Adivinaste el número")
            encontrado = True 
            break
        else:
            print("Ese no es el número.")
            intentos += 1
    
    if encontrado == False:#Faltaba dos puntos  1
        print("Perdiste, el número secreto era", numero_secreto)
        

    
jugar_adivina()
 
