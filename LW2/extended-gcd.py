def extended_gcd(a, b):
    print(f"Вычисление GCD для {a} и {b}")
    if a == 0:
        print(f"Возвращаем ({b}, 0, 1)")
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        print(f"Обновленные значения: gcd={g}, x={x}, y={y}")
        return (g, y - (b // a) * x, x)


def solve_extended_gcd(a, b):
    gcd, s, t = extended_gcd(a, b)
    print(f"Для чисел {a} и {b} НОД = {gcd}, коэффициенты s = {s}, t = {t}")

# Задание 16а: НОД и коэффициенты для чисел 4 и 7
print("Задание 16а:")
solve_extended_gcd(4, 7)

# Задание 16б: НОД и коэффициенты для чисел 291 и 42
print("\nЗадание 16б:")
solve_extended_gcd(291, 42)

# Задание 16в: НОД и коэффициенты для чисел 84 и 320
print("\nЗадание 16в:")
solve_extended_gcd(84, 320)

# Задание 16г: НОД и коэффициенты для чисел 400 и 60
print("\nЗадание 16г:")
solve_extended_gcd(400, 60)