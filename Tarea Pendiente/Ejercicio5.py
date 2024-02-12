#JUEGO ADIVINA NUMERO
import random

def generar_numero_aleatorio():
    return random.randint(1, 50)

def pedir_adivinanza():
    return int(input("Adivina el número: "))

def indicar_mayor_o_menor(numero, numero_secreto):
    if numero < numero_secreto:
        print("El número es mayor.")
    elif numero > numero_secreto:
        print("El número es menor.")

def contar_intentos(intentos):
    print("Intentos realizados:", intentos)

def juego_adivina_numero():
    numero_secreto = generar_numero_aleatorio()
    intentos_maximos = 8
    intentos_realizados = 0

    print("Bienvenido al juego de adivinar el número!")
    print("Tienes que adivinar un número entre 1 y 50.")

    while intentos_realizados < intentos_maximos:
        intento = pedir_adivinanza()
        intentos_realizados += 1

        if intento == numero_secreto:
            print("¡Felicidades! ¡Has adivinado el número en", intentos_realizados, "intentos!")
            return
        else:
            indicar_mayor_o_menor(intento, numero_secreto)
            contar_intentos(intentos_realizados)

    print("¡Lo siento! Has agotado todos tus intentos. El número era:", numero_secreto)

juego_adivina_numero()
