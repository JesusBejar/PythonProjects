serie = "N-02"
if serie == "M-01":
    print("phone 1")
elif serie == "P-03":
    print("phone 2")
elif serie == "N-02":
    print("phone 3")
else:
    print("producto no existe")

match serie:
    case "M-01":
        print("phone 1")
    case "P-03":
        print("phone 2")
    case "N-02":
        print("phone 3")
    case _:
        print("producto no existe")


cliente = {"nombre":"federico",
           "edad":35,
           "empleo":"instructor"}
pelicula = {"titulo":"Matrix",
            "ficha_tecnica":{"protagonista":"Neo",
                              "director":"wachoski brothers"}}
elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "empleo": empleo}:
            print("es un cliente")
            print(nombre, edad, empleo)
        case {"titulo":titulo,
              "ficha_tecnica": {"protagonista":protagonista,
                               "director":director}}:
            print("esta es un pelicula")
            print(titulo, protagonista, director)
        case _:
            print("no sé")


