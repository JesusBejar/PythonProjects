l1 = ["a", "b", "c"]
l2 = ["d", "e", "f"]
print(type(l1))
# class = list
resultado = len(l1)
print(resultado)
# 3
resultado = l1[0]
print(resultado)
# a

print(l1+l2)
l3 = (l1+l2)
print(l3)
# ['a', 'b', 'c', 'd', 'e', 'f']

# l3[0] = "alfa"
print(l3)
#['alfa', 'b', 'c', 'd', 'e', 'f']

l3.append("g")
print(l3)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

elim = l3.pop(0)
print(l3)
print(elim)
# ['b', 'c', 'd', 'e', 'f', 'g']
# a

l4 = ["d", "a", "c", "b"]
l4.sort()
print(l4)
# ['a', 'b', 'c', 'd']
# organiza caracteres desordenados

l5 = l4.sort()
print(type(l5))
# class = Nonetype??
# sort() no devuelve/regresa nada
# no le puedes asignar a un variable diferente

l4.reverse()
print(l4)
# ['d', 'c', 'b', 'a']
# organiza la lista en orden opuesto
# igual que sort() no devuele/regresa

