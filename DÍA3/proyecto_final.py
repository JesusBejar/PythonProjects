
texto = input("Por favor ingresa un texto: ")
letras = input("Por favor ingresa tres letras: ")
# print(texto)
# print(letras)
# print(l_lista)

# 1 cuantas veces aparece cada letra en el texto
l_lista = list(letras)
letra1_cuenta = texto.lower().count(l_lista[0])
letra2_cuenta = texto.lower().count(l_lista[1])
letra3_cuenta = texto.lower().count(l_lista[2])
print(f"{l_lista[0]} aparece {letra1_cuenta} veces el tu texto")
print(f"{l_lista[1]} aparece {letra2_cuenta} veces el tu texto")
print(f"{l_lista[2]} aparece {letra3_cuenta} veces el tu texto")

# 2 cuantas letras hay en el texto
texto_letra_cuenta = len(texto)
print(f"Hay {texto_letra_cuenta} letras en tu texto")

# 3 primera y ultima letra del texto
p_l = texto[0]
print(f"La primera letra de tu texto es {p_l}")
u_l = texto[-1]
print(f"La ultima letra de tu texto es {u_l}")

# 4 el texto al reves
t_ar = texto[::-1]
print(f"Este es tu texto al reves: {t_ar}")

#5 sale la palabra "python" en tu texto
p_s_n = "Python" in texto
print(f"Python se ecuentra en tu texto: {p_s_n}")







