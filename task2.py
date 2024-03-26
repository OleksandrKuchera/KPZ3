# -*- coding: utf-8 -*-
x1 = float(input("Число x1: "))
y1 = float(input("Число y1: "))
x2 = float(input("Число x2: "))
y2 = float(input("Число y2: "))

distance_A = (x1 ** 2 + y1 ** 2) ** 0.5
distance_B = (x2 ** 2 + y2 ** 2) ** 0.5

if distance_A < distance_B:
    print("Точка A знаходиться ближче до початку координат.")
elif distance_B < distance_A:
    print("Точка B знаходиться ближче до початку координат.")
else:
    print("Точка A і точка B знаходяться на однаковій відстані до початку координат.")