palabra = "python"
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)
# ['p', 'y', 't', 'h', 'o', 'n']

lista = [letra for letra in palabra]
print(lista)
# ['p', 'y', 't', 'h', 'o', 'n']

lista = [l for l in "python"]
print(lista)
# ['p', 'y', 't', 'h', 'o', 'n']

lista = [n for n in range(1,20,2)]
print(lista)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

lista = [ n / 2 for n in range(1,20,2)]
print(lista)
# [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

lista = [ n / 2 for n in range(1,20,2) if n * 2 > 10]
print(lista)
# [3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

lista = [n if n * 2 > 10 else "no" for n in range(1,20,2)]
print(lista)
# ['no', 'no', 'no', 7, 9, 11, 13, 15, 17, 19]

pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)
# [3.047851264858275, 6.09570252971655, 9.143553794574824, 12.1914050594331, 15.239256324291373]



