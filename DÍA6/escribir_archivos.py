# READ
mi_archivo = open("texto.txt", "r")
print(mi_archivo.read())
# archivo.close()


# WRITE
mi_archivo = open("texto.txt", "w")
# archivo.write("soy la nueva linea")
# soy la nueva linea
mi_archivo.writelines(["hola", "mundo", "aqui", "estoy"])
# holamundoaquiestoy

lista = ["hola", "mundo", "como", "estas?"]
for p in lista:
    mi_archivo.writelines(p + '\n')
mi_archivo.close()

# ALTER??
mi_archivo = open("texto.txt", "a")
mi_archivo.write("bienvenido")
mi_archivo.close()

