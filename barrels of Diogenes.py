import math

# Ввод данных
radius = float(input())  # радиус дна бочки
height = float(input())  # высота бочки

# Вычисление объема: V = π * r² * h
volume = math.pi * (radius ** 2) * height

# Вывод результата с округлением до 4 знаков после запятой
print(f"{volume:.4f}")