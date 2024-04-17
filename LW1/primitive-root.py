def find_primitive_root(modulo):
    primitive_roots = []
    for candidate in range(2, modulo):
        powers = set()
        intermediate_values = []
        is_primitive_root = True
        for power in range(1, modulo):
            result = (candidate ** power) % modulo
            intermediate_values.append(result)
            if result in powers:
                is_primitive_root = False
                break
            powers.add(result)
        if is_primitive_root:
            primitive_roots.append((candidate, intermediate_values))
    return primitive_roots


def main():
    moduli = [7, 11, 13, 19, 23]

    for modulo in moduli:
        print(f"Модуль: {modulo}")
        roots = find_primitive_root(modulo)
        for root, intermediate_values in roots:
            print(f"Первообразный корень {root} (по модулю {modulo}): {intermediate_values}")
        print()


main()
