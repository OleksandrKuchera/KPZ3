# -*- coding: utf-8 -*-
a = float(input("Число a: "))
b = float(input("Число b: "))
c = float(input("Число c: "))

count_negatives = 0
if a < 0:
    count_negatives += 1
if b < 0:
    count_negatives += 1
if c < 0:
    count_negatives += 1

print("Кількість негативних чисел серед a, b, c:")
print(count_negatives)