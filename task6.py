# -*- coding: utf-8 -*-
a = int(input("Число a: "))
b = int(input("Число b: "))

if a != b:
    if a > b:
        b = a
    else:
        a = b
else:
    a = 0
    b = 0

print("Результат:")
print("a =", a)
print("b =", b)
