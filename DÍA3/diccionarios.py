# la diferencia entre un diccionario y una lista es que
# la lista tiene un indice, las entradas tienen un numero
# asignado para poder ubicarlo, no es asi con un diccionario
d = {"c1":"v1", "c2":"v2", "c3":"v3"}
print(d)
print(type(d))

resultado = d["c1"]
print(resultado)
# v1

paciente = {"nombre":"Cesar", "peso":100, "altura":5}
consulta = paciente["nombre"]
# Cesar
consulta2 = paciente["peso"]
# 100
consulta3 = paciente["altura"]
# 5
print(consulta)
print(consulta2)
print(consulta3)

d2 = {"c1":55, "c2":[100, 200, 300], "c3":{"x1":10, "x2":20}}
print(d2)
print(d2["c1"])
# 55
print(d2["c2"])
# [100, 200, 300]
print(d2["c3"])
# {'x1': 10, 'x2': 20}
print(d2["c2"][1])
# 200
print(d2["c3"]["x1"])
# 10

d3 = {"v1":["a", "b", "c"], "v2":["d", "e", "f"]}
print(d3["v2"][1])
# e

d4 = {1:"1", 2:"b", 3:"c"}
print(d4)
# {1: '1', 2: 'b', 3: 'c'}
d4[4] = "d"
print(d4)
# {1: '1', 2: 'b', 3: 'c', 4: 'd'}
# es posible modificar/cambiar un diccionario
d4[2] = "B"
print(d4)
# {1: '1', 2: 'B', 3: 'c', 4: 'd'}

print(d.keys())
# dict_keys(['c1', 'c2', 'c3'])
print(d4.keys())
# dict_keys([1, 2, 3, 4])
# para ver todas las keys de un diccionario

print(d.values())
# dict_values(['v1', 'v2', 'v3'])
print(d4.values())
# dict_values(['1', 'B', 'c', 'd'])
# # para ver todas los valores de un diccionario

print(d.items())
# dict_items([('c1', 'v1'), ('c2', 'v2'), ('c3', 'v3')])
print(d4.items())
# dict_items([(1, '1'), (2, 'B'), (3, 'c'), (4, 'd')])
# para ver todo lo que hay en un diccionario






