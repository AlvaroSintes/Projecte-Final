import random

def pex1():
    continuar=1
    while continuar ==1:
        print("Bienvenido a Mistermind")
        print("Elije la dificultad del juego <1=Facil, 2=Dificil, 3=Muy dificil")
        dificultad= int(input("Elija el numero de dificultad: "))

        if dificultad == 1:
            cant_digitos = 3
        elif dificultad == 2:
            cant_digitos = 4
        elif dificultad == 3:
            cant_digitos = 5

        digitos = ('0','1','2','3','4','5','6','7','8','9')
        codigo = ''

        for i in range(cant_digitos):
            elegido = random.choice(digitos)
            while elegido in codigo:
                elegido = random.choice(digitos)
            codigo = codigo + elegido
            
        print("Tienes que adivinar un codigo de",cant_digitos,"digitos distintos")
        propuesta = input("Que codigo propones?: ")

        intentos = 1
        while propuesta != codigo:
            intentos = intentos + 1
            aciertos = 0
            concidencias = 0
            for i in range(cant_digitos):
                if propuesta[i] == codigo[i]:
                    aciertos = aciertos + 1
                elif propuesta[i] in codigo:
                    concidencias = concidencias + 1
            print("Tu propuesta(",propuesta,") tiene ",aciertos,"aciertos y ",concidencias,"coincidencias")
            propuesta = input("Propon otro codigo: ")
        print("FELICIDADES! adivinaste el codigo en ",intentos,"intentos")
        continuar = int(input("Desea seguir jugando? <1=si, 0=no>: "))