def divide_polynomials(dividend, divisor):
    # Преобразуем список коэффициентов в полиномы с наивысшей степенью в начале
    output = [0] * (len(dividend) - len(divisor) + 1)
    while len(dividend) >= len(divisor):
        # Коэффициент для текущего члена частного в GF(2) всегда будет 1, если старший коэффициент делимого не ноль
        coeff = dividend[0]
        if coeff == 0:  # Если старший коэффициент ноль, мы не можем делить
            break
        degree = len(dividend) - len(divisor)
        # Формируем полином для вычитания
        subtrahend = [coeff * x for x in divisor] + [0] * degree
        # Вычитаем (XOR) и обновляем делимое
        dividend = [a ^ b for a, b in zip(dividend + [0] * degree, subtrahend)]
        # Удаляем старший нулевой коэффициент
        while len(dividend) > 0 and dividend[0] == 0:
            dividend.pop(0)
        # Добавляем коэффициент к результату
        output[degree] = coeff
    # Остаток - это текущее делимое
    remainder = dividend
    return output, remainder

def gcd_polynomials(poly1, poly2):
    while poly2 and poly2 != [0]:
        _, remainder = divide_polynomials(poly1, poly2)
        print(f"Деление {poly1} на {poly2} даёт остаток {remainder}")
        poly1, poly2 = poly2, remainder
    # Обрезаем ведущие нули, если они есть
    while len(poly1) > 1 and poly1[0] == 0:
        poly1.pop(0)
    return poly1


# Определим многочлены из новых примеров
new_examples = [
    ([1, 0, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1]),     # 2.1
    ([1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1]),         # 2.2
    ([1, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1]),         # 2.3
    ([1, 0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1])    # 2.4
]

# Применим алгоритм Евклида к каждой паре многочленов
for i, (f1, f2) in enumerate(new_examples, 1):
    gcd = gcd_polynomials(f1, f2)
    print(f"Пример 2.{i}: НОД(F₁(x), F₂(x)) = {gcd}")
    print()