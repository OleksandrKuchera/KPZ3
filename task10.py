# -*- coding: utf-8 -*-
a = float(input("Число a: "))
b = float(input("Число b: "))
c = float(input("Число c: "))
k = float(input("Введіть число k: "))

divisors = []

if a % k == 0:
    divisors.append("a")
if b % k == 0:
    divisors.append("b")
if c % k == 0:
    divisors.append("c")

if divisors:
    print('Число')
    print(k)
    print('є дільником чисел -')
    print(', '.join(divisors)) 
else:
    print('Число')
    print(k)
    print('не є дільником жодного з чисел a, b, c.')
