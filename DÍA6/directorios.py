import os
from pathlib import Path

carpeta = Path("Users\\MacOS\\Desktop\\Project1\\DÍA6\\texto.txt")
archivo = carpeta / "texto.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())

ruta = os.getcwd()
print(ruta)
# /Users/israelbejar/PycharmProjects/Project1/DÍA6
elemento = os.path.basename(ruta)
print(elemento)
# DÍA6

elemento = os.path.split(ruta)
print(elemento)
# ('/Users/israelbejar/PycharmProjects/Project1', 'DÍA6')

os.rmdir("insert pathway to eliminate directory here")

archivo = open("Users\\MacOS\\Desktop\\Project1\\DÍA6\\texto.txt")
print(archivo.read())
# holamundoaquiestoyhola holahola holabienvenidobienvenidobienvenido


ruta2 = os.chdir("insert pathway here")
# chdir te permite cambiar de directorio

archivo = open("orto_archivo.txt")
print(archivo.read())

ruta3 = os.makedirs("insert pathway here")
# makedir te permite crear directorios nuevos
