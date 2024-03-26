# -*- coding: utf-8 -*-
x = float(input("Введіть число x: "))
y = float(input("Введіть число y: "))
temp = (x+y)**2
if x < y:
    x = (x + y) / 2
    y = temp
else:
    y = (x + y) / 2
    x = temp

print("Після заміни:")
print("x =", x)
print("y =", y)
