nombres = ["juan", "hyrum", "israel"]
edades = [24, 26, 23]
paises = ["argentina", "peru", "usa"]

listas_combinadas = zip(nombres, edades)
print(listas_combinadas)
# <zip object at 0x10905be40>

listas_combinadas = list(zip(nombres, edades))
print(listas_combinadas)
# [('juan', 24), ('hyrum', 26), ('israel', 23)]

listas_combinadas = list(zip(nombres, edades, paises))
print(listas_combinadas)
# [('juan', 24, 'argentina'), ('hyrum', 26, 'peru'), ('israel', 23, 'usa')]

for n,e,p in listas_combinadas:
    print(f"{n} tienen {e} años y es de {p}")
# juan tienen 24 años y es de argentina
# hyrum tienen 26 años y es de peru
# israel tienen 23 años y es de usa
