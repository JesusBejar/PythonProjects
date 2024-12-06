mi_archivo = open("texto.txt")

# print(mi_archivo)
# <_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>

todas = mi_archivo.readlines()
print(todas)
# ['soy linea n1\n', 'soy n2\n', 'soy el n3']

for l in mi_archivo:
    print(f"Aqui dice " + l)
# Aqui dice soy linea n1
#
# Aqui dice soy n2
#
# Aqui dice soy el n3

print(mi_archivo)
# nada

print(mi_archivo.read())
# soy linea n1
# soy n2
# soy el n3

linea = mi_archivo.readline()
print(linea)
# soy linea n1

print(linea)
print(linea)
print(linea)
# soy linea n1
#
# soy linea n1
#
# soy linea n1

linea = mi_archivo.readline()
print(linea)

linea = mi_archivo.readline()
print(linea)

linea = mi_archivo.readline()
print(linea)
# soy linea n1
#
# soy n2
#
# soy el n3

linea = mi_archivo.readline()
print(linea.rstrip())

linea = mi_archivo.readline()
print(linea.rstrip())

linea = mi_archivo.readline()
print(linea.rstrip())
#soy linea n1
# soy n2
# soy el n3
