x = 10
y = 5
print("mis numeros son " + str(x) + " y " + str(y))

print("mis numeros son {} y {}".format(x, y))

print("la suma de {} y {} es {}".format(x, y, x+y))

color = "rojo"
matricula = 700
print(f"el color es {color} y la matricula es {matricula}")


puntos_anteriores = 875
puntos_nuevos = 350
puntos_total = puntos_anteriores + puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_total} puntos")
print(type(puntos_anteriores))
print(type(puntos_nuevos))