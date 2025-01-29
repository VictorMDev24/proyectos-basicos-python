#la  maquina generra un numero º aleatorio y el usuario lo adivina
import random


def num_random(x):
    
    
    print("=========================")
    print("  ¡BIENVENIDO AL JUEGO!  ")
    print("=========================")
    print("Adivina el número secreto")
    # print("Tienes 3 intentos")
    # print("El número está entre 1 y 10")
    
    
    num_random = random.randint(1, x)
    
    prediccion = 0
    
    while prediccion!= num_random :
        prediccion = int(input("Adivina el número: "))
        if prediccion < num_random:
            print(" Estas muy frio Intenta con un número más alto")
        elif prediccion > num_random:
            print(" Estas muy caliente Intenta con un número más bajo")
        else:
            print("¡Felicidades! Adivinaste el número")          
    print(f"¡Felicidades! Adivinaste el número {num_random}")
    
num_random(10)
# def juego():
#     nivel = 1
#     vidas_por_nivel = 3
    
    
#     while True:
#         if jugar_nivel(nivel, vidas_por_nivel):
#             nivel += 1
#             vidas_por_nivel += 2  # Puedes ajustar esto para hacerlo más fácil/difícil
#         else:
#             break

#     print("\n¡Gracias por jugar!")

# if __name__ == "__main__":
        
    