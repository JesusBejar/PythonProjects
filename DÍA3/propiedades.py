# propiedades de strs
nombre = "Israel"
nombre[0] = "E"
print(nombre)
# error
# los strs son inmutables

n1 = "Isr"
n2 = "ael"
nc = n1 + n2
print(nc)
# Israel

nc2 = (n1 * 5)
print(nc2)
# IsrIsrIsrIsrIsr

poema = "Cada vez que pienso en ti, mis ojos rompen en llanto; y muy triste me pregunto, ¿por qué te quiero tanto?"
print("llanto" in poema)
# True
# esto es un booleano, las respuestas pueden ser True o False
print("Miguel" in poema)
# False
print("Miguel" not in poema)
# True
print("llanto" not in poema)
# False

print(len(poema))
# cuenta los caracteres que ocupa el str
# 105