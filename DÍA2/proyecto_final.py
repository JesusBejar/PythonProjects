# calculadora de comisiones
e1 = input("Cual es tu nombre?: ")
e1ventas = input("Ingresa tu numero de ventas: ")
e1ventas_float = float(e1ventas)
e1_comision = round(e1ventas_float * .13,2)
print(f"Hola {e1} tu comision es ${e1_comision}")


