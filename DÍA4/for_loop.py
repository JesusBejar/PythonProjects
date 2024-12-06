lista = ["a", "b", "c", "d"]
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"{numero_letra} : {letra}")
# 1 : a
# 2 : b
# 3 : c
# 4 : d

l2 = ["juan", "hyrum", "miguel", "jorge", "tae"]
for nombre in l2:
    if nombre.startswith("j"):
        print(nombre)
# juan
# jorge

numeros = [1,2,3,4,5,6]
valor = 0

for n in numeros:
    valor = valor + n
    print(valor)

print(valor)
# 21


palabra = "python"
for letra in palabra:
    print(letra)
# p
# y
# t
# h
# o
# n
for letra in "python":
    print(letra)
# p
# y
# t
# h
# o
# n
for objecto in [[1,2], [3,4], [5,6]]:
    print(objecto)
# [1, 2]
# [3, 4]
# [5, 6]

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)
# 1
# 2
# 3
# 4
# 5
# 6

dic = {"c1":"v1", "c2":"v2", "c3":"v3", "c4":"v4"}
for item in dic:
    print(item)
# c1
# c2
# c3
# c4
# imprime todos los keys

dic = {"c1":"v1", "c2":"v2", "c3":"v3", "c4":"v4"}
for item in dic.values():
    print(item)
# v1
# v2
# v3
# v4
# imprime todos los values

dic = {"c1":"v1", "c2":"v2", "c3":"v3", "c4":"v4"}
for item in dic.items():
    print(item)
# ('c1', 'v1')
# ('c2', 'v2')
# ('c3', 'v3')
# ('c4', 'v4')
# imprime todo

dic = {"c1":"v1", "c2":"v2", "c3":"v3", "c4":"v4"}
for a,b in dic.items():
    print(a,b)
# c1 v1
# c2 v2
# c3 v3
# c4 v4