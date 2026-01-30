def solve_linear(a, b):
    if a == 0:
        if b == 0:
            return "Бесконечное количество решений"
        else:
            return "Нет решений"
    
    x = -b / a
    return x

val_a = float(input("Введите a: "))
val_b = float(input("Введите b: "))

result = solve_linear(val_a, val_b)
print(f"Результат: {result}")