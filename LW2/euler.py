import math
def extended_gcd(a, b):
    print(f"Вычисление GCD для {a} и {b}")
    if a == 0:
        print(f"Возвращаем ({b}, 0, 1)")
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        print(f"Обновленные значения: gcd={g}, x={x}, y={y}")
        return (g, y - (b // a) * x, x)


def mod_inverse(a, m):
    print(f"Находим обратный элемент для {a} по модулю {m}")
    g, x, _ = extended_gcd(a, m)
    if g == 1:
        inverse = x % m
        print(f"Обратный элемент для {a} по модулю {m} найден: {inverse}")
        return inverse
    else:
        print(f'Внимание: Обратный элемент для {a} по модулю {m} не существует. Пропускаем.')
        return None


def chinese_remainder_theorem(a, m):
    print("Начало работы Китайской теоремы об остатках")
    M = 1
    for mod in m:
        M *= mod
        print(f"Текущий общий модуль M: {M}")

    solution = 0
    print("Начинаем вычисление решения системы сравнений")
    for i in range(len(a)):
        Mi = M // m[i]
        print(f"Модуль для {i}-го уравнения: {Mi}")
        yi = mod_inverse(Mi, m[i])
        if yi is not None:
            part_solution = a[i] * Mi * yi
            solution += part_solution
            print(f"Добавляем часть решения: {part_solution}, текущее решение: {solution}")
        else:
            print(f'Модуль {m[i]} и остаток {a[i]} исключены из расчета.')

    final_solution = solution % M
    print(f"Финальное решение системы сравнений: x ≡ {final_solution} (mod {M})")

    # Генерируем список всех решений в пределах общего модуля M
    solutions = [final_solution + i * M for i in range(0, 10)]  # Пример для 1 решения; измените диапазон по желанию

    return final_solution, M, solutions
def euler_phi(n):
    """Вычисляет значение функции Эйлера для n."""
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    print(f"Функция Эйлера для {n} равна {amount}")
    return amount

def modular_inverse_euler(a, n):
    """Находит модульный обратный для a по модулю n, используя теорему Эйлера."""
    phi_n = euler_phi(n)
    result = pow(a, phi_n - 1, n)
    print(f"Модульный обратный для {a} по модулю {n} найден: {result}")
    return result

# Задание 11
print(" \n Задание 11:")
print(f"a. 12^-1 mod 77 = {modular_inverse_euler(12, 77)}")
print(f"b. 16^-1 mod 323 = {modular_inverse_euler(16, 323)}")
print(f"c. 20^-1 mod 403 = {modular_inverse_euler(20, 403)}")

# Задание 19а
print("\nЗадание 19а:")
a = [2, 3]  # Остатки
m = [7, 9]  # Модули
solution, M, _ = chinese_remainder_theorem(a, m)
print(f"x ≡ {solution} (mod {M}) для системы сравнений x ≡ 2 mod 7 и x ≡ 3 mod 9")

# Задание 19б
print("\nЗадание 19б:")
a = [4, 0]  # Остатки
m = [5, 11]  # Модули
solution, M, _ = chinese_remainder_theorem(a, m)
print(f"x ≡ {solution} (mod {M}) для системы сравнений x ≡ 4 mod 5 и x ≡ 0 mod 11")

# Задание 19в
print("\nЗадание 19в:")
a = [7, 11]  # Остатки
m = [13, 12]  # Модули
solution, M, _ = chinese_remainder_theorem(a, m)
print(f"x ≡ {solution} (mod {M}) для системы сравнений x ≡ 7 mod 13 и x ≡ 11 mod 12")