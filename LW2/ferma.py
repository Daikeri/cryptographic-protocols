def fermat_theorem(a, p, power=1):
    if power == -1:  # Для модульной инверсии
        power = p - 2
    result = pow(a, power, mod=p)
    return result

# Задание 9
print("Задание 9:")
print(f"a. 5^15 mod 13 = {fermat_theorem(5, 13, 15)}")
print(f"b. 15^18 mod 17 = {fermat_theorem(15, 17, 18)}")
# c. Поскольку 456 делится на 17, результат будет 0
print("c. 456^17 mod 17 = 0")
print(f"d. 145 mod 101 = {145 % 101}")

# Задание 10
print("\nЗадание 10:")
print(f"a. 5^-1 mod 13 = {fermat_theorem(5, 13, -1)}")
print(f"b. 15^-1 mod 17 = {fermat_theorem(15, 17, -1)}")
print(f"c. 27^-1 mod 41 = {fermat_theorem(27, 41, -1)}")
print(f"d. 70^-1 mod 101 = {fermat_theorem(70, 101, -1)}")