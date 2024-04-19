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


# Система сравнений №1 и №2
a1 = [2, 15, 5]
m1 = [5, 17, 12]

a2 = [8, 13, 4]
m2 = [6, 35, 11]

# Решение системы сравнений №1
print("\nРешение системы сравнений №1:")
solution1, M1, solutions1 = chinese_remainder_theorem(a1, m1)
print(f"Решение системы сравнений №1: x ≡ {solution1} (mod {M1}), Еще решения: {solutions1}")

# Решение системы сравнений №2
print("\nРешение системы сравнений №2:")
solution2, M2, solutions2 = chinese_remainder_theorem(a2, m2)
print(f"Решение системы сравнений №2: x ≡ {solution2} (mod {M2}), Еще решения: {solutions2}")