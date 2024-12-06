from random import *

c = 0
nom = input("Ingresa tu nombre: ")
num_r = (randint(1,101))
print(num_r)
print("Tienes ocho intentos para adivinar el numero secreto")
while c < 8:
    a = int(input("Cual es el numero secreto: "))
    c = c + 1
    if a <= 0 or a >= 100:
        print("no es valido tu adivinaza. el numero tiene que estar entre 0-100")
        pass
    elif a < num_r:
        print("tu adinivanza es muy bajo, adivina otra vez")
    elif a > num_r:
        print("tu adinivanza es muy alto, adivina otra vez")
    elif a == num_r:
        print("Has ganado, felicidades!")
        print(f"Tomo {c} intentos para adivinar el numero")
        break
