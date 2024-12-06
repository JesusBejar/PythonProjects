from pathlib import Path, PurePath

carpeta = Path("/Users/israelbejar/PycharmProjects/Project1/DÍA6/prueba.txt")
path_perfecto = PurePath(carpeta)
print(path_perfecto)
# /Users/israelbejar/PycharmProjects/Project1/DÍA6/prueba.txt

if not carpeta.exists():
    print("ese archivo no existe")
else:
    print("muy bien, si existe el archivo")

print(carpeta.read_text())
# que mira, chabon??
print(carpeta.stem)
# prueba
# .stem se usa para saber si el archivo todavia existe o no