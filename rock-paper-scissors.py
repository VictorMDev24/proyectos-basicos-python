#crea piedra papel o tijeras  con if else y elif
while  True  :
    a = int(input("jugador 1: piedra =1, papel = 2, tijeras = 3: "))
    b = int(input("jugador 2: piedra =1, papel = 2, tijeras = 3: "))
    
#jugador 1 
    if a == 1 and b == 3:
        print("jugador 1 gana piedra vence a tijeras")
    elif a == 2 and b == 1:
        print("jugador 1 gana papel vence a piedra")
    elif a == 3 and b == 2:
        print("jugador 1 gana tijeras vence a papel")
#jugador 2                 
    elif  b == 1 and a == 3:
        print("jugador 2 gana piedra vence a tijeras")
    elif b == 2 and a == 1:
        print("jugador 2 gana papel vence a piedra")
    elif b == 3 and a == 2:
        print("jugador 2 gana tijeras vence a papel")   
    elif a < 1 or a > 3 or b < 1 or b > 3:
        print("error")
    elif a >= 1 and a <= 3 and b >= 1 and b <= 3:
        print("empate")   
#pregunta si quiere seguir jugando

    if input("quieres seguir jugando? si o no: ") == "no":
        break
    print("fin del juego") 
