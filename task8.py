# -*- coding: utf-8 -*-
a = float(input("Число a: "))
b = float(input("Число b: "))
c = float(input("Число c: "))

positive_count = 0
if a > 0:
    positive_count += 1
if b > 0:
    positive_count += 1
if c > 0:
    positive_count += 1

print("Кількість додатних чисел серед a, b, c:")
print( positive_count)