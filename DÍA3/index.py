# usar index() y rindex()
texto = "Esta es una prueba"
resultado = texto[0] #E
print(resultado)
resultado2 = texto[-5] #r
print(resultado2)

resultado3 = texto.index("n") #9
print(resultado3)
resultado4 = texto.index("E") #0
print(resultado4)
# resultado5 = texto.index("z") #error
# print(resultado5)
# buscar palabras enteras
resultado6 = texto.index("es") #5
print(resultado6)
#empieza a buscar desde lugar 5
resultado7 = texto.index("a", 5) #10
print(resultado7)
#empieza a buscar desde lugar 11 hasta lugar 18
resultado8 = texto.index("a", 11, 18) #17
print(resultado8)
# rindex busca de igual manera pero al reves (derecha a izquierda)
resultado9 = texto.rindex("a") #17
print(resultado9)



