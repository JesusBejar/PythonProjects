from pathlib import Path
base = Path.home()
print(base)
# /Users/israelbejar
guia = Path("Barcelona", "Sagrada_Familia.txt")
print(guia)
# Barcelona/Sagrada_Familia

completo = Path(base, "Barcelona", "Sagrada_Familia.txt")
print(completo)
# /Users/israelbejar/Barcelona/Sagrada_Familia.txt
# esto se llama una ruta relativa

mas_completo = Path(base, "Europea", "España", "Barcelona", "Sagrada_Familia.txt")
print(mas_completo)
# esto se llama una ruta absoluta
# /Users/israelbejar/Europea/España/Barcelona/Sagrada_Familia.txt
print(mas_completo.parent)
# /Users/israelbejar/Europea/España/Barcelona
print(mas_completo.parent.parent)
# /Users/israelbejar/Europea/España


mas_completo2 = mas_completo.with_name("Dios_Divino.txt")
print(mas_completo2)
# /Users/israelbejar/Europea/España/Barcelona/Dios_Divino.txt


guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob("*.txt"):
    print(txt)
# este loop sirve para encontrar todos archivos que terminan con .txt
# en el directorio "Europa"

guia = Path("Users", "israelbejar", "Europea", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espana = guia.relative_to(Path("Europa", "España"))
print(en_europa)
# España/Barcelona/Dios_Divino.txt
print(en_espana)
# Barcelona/Sagrada_Familia.txt



