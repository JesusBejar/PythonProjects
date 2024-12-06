monedas = 5

while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas = monedas - 1
else:
    print("se me acabo el dinero")
# tengo 5 monedas
# tengo 4 monedas
# tengo 3 monedas
# tengo 2 monedas
# tengo 1 monedas
# se me acabo el dinero

respuesta = "s"
while respuesta == "s":
    respuesta = input("quieres seguir? s/n ")
else:
    print("gracias por participar")

n = input("ingresa tu nombre")
for l in n:
    if l == "r":
        break
    print(l)