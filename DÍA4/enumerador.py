l = ["a", "b", "c"]
indice = 0

for item in l:
    print(indice, item)
    indice += 1
# 0 a
# 1 b
# 2 c

for item in enumerate(l):
    print(item)
# (0, 'a')
# (1, 'b')
# (2, 'c')

for indice,item in enumerate(l):
    print(indice,item)
# 0 a
# 1 b
# 2 c

for indice,item in enumerate(range(50,55)):
    print(indice,item)
# 1 51
# 2 52
# 3 53
# 4 54


mis_tuples = list(enumerate(l))
print(mis_tuples)
# [(0, 'a'), (1, 'b'), (2, 'c')]

mis_tuples = list(enumerate(l))
print(mis_tuples[1][0])
# 1