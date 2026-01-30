import math

r = float(input())
command = int(input())

if command == 1:  # длина окружности
    print(2 * math.pi * r)
elif command == 2:  # площадь круга
    print(math.pi * r ** 2)
elif command == 3:  # площадь поверхности сферы
    print(4 * math.pi * r ** 2)