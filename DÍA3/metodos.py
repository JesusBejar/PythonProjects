# usar varios metodos (funciones)
# upper()   lower()
# split()   join()
# find()    replace()
texto = "Este es mi texto, me llamo Israel"
resultado = texto.upper()
print(resultado)
# ESTE ES MI TEXTO, ME LLAMO ISRAEL

resultado = texto.lower()
print(resultado)
# este es mi texto, me llamo israel

resultado = texto.split()
print(resultado)
# separa y guarda las palabras en una lista
# ['Este', 'es', 'mi', 'texto,', 'me', 'llamo', 'Israel']

resultado = texto.split("t")
print(resultado)
# t es el separador
# ['Es', 'e es mi ', 'ex', 'o, me llamo Israel']

a = "Yo"
b = "soy"
c = "el"
d = "grandmaster"
e = "de"
f = "ajedrez"
g = " ".join([a,b,c,d,e,f])
print(g)
# junta y guarda las palabras como una string
# Yo soy el grandmaster de ajedrez

a = "Yo"
b = "soy"
c = "el"
d = "grandmaster"
e = "de"
f = "ajedrez"
g = "-".join([a,b,c,d,e,f])
print(g)
# Yo-soy-el-grandmaster-de-ajedrez

resultado = texto.find("m")
print(resultado)
# cuenta cuantos strings estan en la oracion

resultado = texto.replace("Israel", "Hyrum")
print(resultado)
# reemplaza ciertas palabras o letras
# Este es mi texto, me llamo Hyrum
resultado = texto.replace("e", "x")
print(resultado)
# Estx xs mi txxto, mx llamo Israxl

resultado = texto.replace("texto", "libro").replace("Israel","Joe")
print(resultado)
# para cambiar varias palabras a la misma vez
# Este es mi libro, me llamo Joe






