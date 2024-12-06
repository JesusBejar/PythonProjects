s = set((1,2,3,4,5))
print(type(s))
# <class 'set'>
print(s)
# {1, 2, 3, 4, 5}
# no se pueden repetir valores identicos en los sets
# igual que los diccionarios, los sets no tiene indice

print(len(s))
# 5
print(3 in s)
# True

s2 = {6,7,8}
s3 = {9,10,11}
s4 = s2.union(s3)
print(s4)
# {6, 7, 8, 9, 10, 11}

s4.add(12)
print(s4)
# {6, 7, 8, 9, 10, 11, 12}

s4.remove(10)
print(s4)
# {6, 7, 8, 9, 11, 12}

s4.discard(11)
print(s4)
# {6, 7, 8, 9, 12}
# discard() no es lo mismo que remove()??

s4.pop()
print(s4)
# {7, 8, 9, 12}
# eliminar el valor en el primer lugar

s4.clear()
print(s4)
# set()
# vacia completamente el set
