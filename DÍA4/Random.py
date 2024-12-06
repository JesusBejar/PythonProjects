
from random import *

aleantorio = randint(1,50)
print(aleantorio)
# 48
a = round(uniform(1,5),1)
print(a)
# 4.6

aleantorio = random()
print(aleantorio)
# 0.9573629850840983

colores = ["azul", "rojo", "verde", "rosa", "morado"]
aleantorio = choice(colores)
print(aleantorio)
# verde

numeros = list(range(5,50,5))
print(numeros)
# [5, 10, 15, 20, 25, 30, 35, 40, 45]

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
# [35, 5, 30, 45, 40, 20, 10, 25, 15]
