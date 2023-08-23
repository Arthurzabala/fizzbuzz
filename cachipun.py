import random
import math

n = input("ingrese numero de juego ")
def jugar():

    usuario = input("Elige una opcion: 1 PIEDRA ,2 PAPEL, 3 TIJERA ")
    
    if usuario > '3':
        return usuario

    elementos = ['1','2','3']
    computador = random.choice(elementos)

    if usuario == computador:
        return (0,usuario,computador)   
    
    if is_ganador(usuario,computador):
        return (1,usuario,computador)
    
    return (-1,usuario,computador)

    
def is_ganador(jugador , oponente):
    
    if (jugador == '1' and oponente == '3') or (jugador == '3' and oponente =='2') or (jugador =='2' and oponente =='1'):
        return True
    return False

def el_mejor_jugador(n):
    puntos_jugador = 0 
    puntos_computador = 0
    para_ganar = math.ceil(n/2)
    
    while puntos_jugador < para_ganar and puntos_computador < para_ganar:

        resultado, usuario, computador = jugar()

        # Empate
        if resultado == 0:
            print ("ES UN EMPATE. TU Y EL COMPUTADOR HAN ELEGIDO{}".format(usuario))

        #Ganas
        elif resultado == 1:
            puntos_jugador +=1
            print ("GANASTE TU HASTA ELEJIDO {} Y EL COMPUTADOR {}".format(usuario, computador))

        #Perdiste
        else: 
            puntos_computador +=1
            print("PERDISTE  TU HAS ELEJIDO {} Y EL COMPUTADOR {}".format(usuario, computador))

    if puntos_jugador > puntos_computador:
        print ("HAS GANADO HAS HECHO LOS  MEJORES DE {} JUEGOS.  ERES UN CAMPEON".format(n))
    else:
        print("HAS PERDIDO EL COMPUTADOR HA HECHO LOS MEJOR DE  {} JUEGOS SUERTE PARA LA PROXIMA".format(n))

if __name__ == "__main__":
    el_mejor_jugador(5)