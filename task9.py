# -*- coding: utf-8 -*-
a = float(input("Число a: "))
b = float(input("Число b: "))
c = float(input("Число c: "))

integer_count = 0
if a.is_integer():
    integer_count += 1
if b.is_integer():
    integer_count += 1
if c.is_integer():
    integer_count += 1

print("Кількість цілих чисел серед a, b, c:")
print(integer_count)