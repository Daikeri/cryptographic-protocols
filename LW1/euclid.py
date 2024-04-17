def extended_gcd_steps(a, b):
    steps = []

    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2:
        q = r1 // r2
        r = r1 % r2

        s = s1 - q * s2
        t = t1 - q * t2

        steps.append((q, r1, r2, r, s1, s2, s, t1, t2, t))

        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t

    return steps


def solve_diophantine_equation(a, b, c):
    steps = extended_gcd_steps(a, b)

    for step in steps:
        print(f"q = {step[0]}, r1 = {step[1]}, r2 = {step[2]}, r = {step[3]}, "
              f"s1 = {step[4]}, s2 = {step[5]}, s = {step[6]}, "
              f"t1 = {step[7]}, t2 = {step[8]}, t = {step[9]}")

    d, x, y = steps[-1][2], steps[-1][5], steps[-1][8]

    if c % d == 0:
        x *= c // d
        y *= c // d
        return x, y
    else:
        return None


# Пример использования
a, b, c = 18, 35, 36
result = solve_diophantine_equation(a, b, c)

if result:
    print(f"Решение уравнения {a}x + {b}y = {c}: x = {result[0]}, y = {result[1]}")
else:
    print("Уравнение не имеет целочисленных решений.")
