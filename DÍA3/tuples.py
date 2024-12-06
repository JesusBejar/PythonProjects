t = (1,2,3,4)
print(type(t))
# lists usan [] diccionarios usan {} tuples usan ()
print(t[0])
# 1
# print(t[5])
# error

t2 = (1,2,(10,20),4)
print(t2[2])
# (10, 20)
print(t2[2][0])
# 10

t2 = list(t2)
print(type(t2))
# list
# list() se usa para convertir diccionarios o tuples a listas

t2 = tuple(t2)
print(type(t2))
# tuple() se usa para convertir diccionarios o listas a tuples

t3 = (1,2,3,4,1,1,1)
a,b,c,d,e,f,g = t3
print(t3)
# (1, 2, 3, 4, 1, 1, 1)
# no sale un error por que las cantidades son iguales

print(len(t3))
# 7
print(t3.count(1))
# 4
# count() cuenta el numero de un valor especifico en un tuple, diccinario, lista

print(t3.index(2))
# inde
