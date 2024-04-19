
def multiply_polynomials(poly1, poly2):
    # Инициализируем результат произведения нулями
    result = [0] * (len(poly1) + len(poly2) - 1)
    # Умножаем полиномы по модулю 2
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] ^= poly1[i] * poly2[j]  # XOR для сложения коэффициентов
    # Обрезаем ведущие нули
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    return result

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

# Примеры из задачи
examples = [
    ([1, 0, 1, 1], [1, 1]),  # F(x) = x^3 + x + 1, G(x) = x + 1
    ([1, 0, 1], [1, 1]),     # F(x) = x^2 + 1, G(x) = x + 1
    ([1, 0, 1, 0, 1], [1, 0, 1]),  # F(x) = x^3 + x^2 + 1, G(x) = x^2 + 1
    ([1, 0, 0, 1, 1], [1, 0, 1]),  # F(x) = x^4 + x^2 + 1, G(x) = x^2 + x + 1
    ([1, 0, 0, 1, 1], [1, 1]),     # F(x) = x^4 + x^2 + x + 1, G(x) = x + 1
    ([1, 0, 1, 1, 0, 1], [1, 1, 1]),
]

# Выполнение операций для каждого примера
for i, (f, g) in enumerate(examples, start=1):
    print(f"Пример {i}.")

    # Сложение
    # print("Сложение многочленов:")
    # sum_result = add_polynomials(f, g)
    # print(f"Сумма: {sum_result}\n")

    print(f"Многочлен F(x): {f}")
    print(f"Многочлен G(x): {g}")

    # Умножение
    print("Умножение многочленов:")
    mult_result = multiply_polynomials(f, g)
    print(f"Произведение: {mult_result}\n")

    # Деление
    print("Деление многочленов:")
    quotient, remainder = divide_polynomials(f, g)
    print(f"Частное: {quotient}, Остаток: {remainder}\n")

    # Разделитель между примерами
    print("-" * 50)