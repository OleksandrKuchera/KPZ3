# -*- coding: utf-8 -*-

num1 = float(input("Перше число: "))
num2 = float(input("Друге число: "))
num3 = float(input("Третє число: "))

if num1 >= 0:
    num1_resoult = num1 ** 2
else:
    num1_resoult = num1 ** 4

if num2 >= 0:
    num2_resoult = num2 ** 2
else:
    num2_resoult = num2 ** 4

if num3 >= 0:
    num3_resoult = num3 ** 2
else:
    num3_resoult = num3 ** 4

print("Результат:")
print(num1_resoult)
print(num2_resoult)
print(num3_resoult)
