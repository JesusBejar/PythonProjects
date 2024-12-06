var1 = True
var2 = False

print(type(var1))
print(type(var2))

num = 5 > 2+3
print(type(num))
print(num)
# False

num2 = bool(5<6)
print(num2)
# True
num3 = bool(5>6)
print(num3)
# False

l = [1,2,3,4,5]
control = 7 in l
print(control)
# False