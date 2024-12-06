# fragmentar strings [1:2:3]
texto = "ABCDEFGHIJKLMPNOQRS"
f1 = texto[1]
print(f1)
# B

f2 = texto[1:5]
print(f2)
# BCDE

f3 = texto[1:]
print(f3)
# hasta donde se pueda BCDEFGHIJKLMPNOQRS

f4 = texto[:5]
print(f4)
# hasta donde se pueda pero al reves ABCDE

f5 = texto[1:10:2]
print(f5)
# brinca cada otra letra hasta llegar a lugar 10 BDFHJ

f6 = texto[::3]
print(f6)
# brinca cada dos letras hasta donde se pueda ADGJMOS

f7 = texto[::-1]
print(f7)
# todas las letras pero al reves SRQONPMLKJIHGFEDCBA
