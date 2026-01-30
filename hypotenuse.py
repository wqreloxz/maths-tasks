import math

# Считываем, что нужно найти
what_to_find = input().strip()

if what_to_find == "hyp":  # Найти гипотенузу
    # Вводятся два катета
    a = float(input())
    b = float(input())
    # Гипотенуза = √(a² + b²)
    result = math.sqrt(a ** 2 + b ** 2)
else:  # what_to_find == "kat" - Найти катет
    # Вводятся гипотенуза и известный катет
    c = float(input())  # гипотенуза
    b = float(input())  # известный катет