a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if D < 0:
    print("None")
elif D == 0:
    x = -b / (2 * a)
    # Выводим ровно как в примере: -1.0
    print(f"{x:.1f}")
else:
    sqrt_D = D ** 0.5
    x1 = (-b - sqrt_D) / (2 * a)
    x2 = (-b + sqrt_D) / (2 * a)