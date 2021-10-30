import sys
import math


"""
Получение коэффициентов
"""
def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except IndexError:
        print(prompt)
        coef_str = input()

    try:
        coef = float(coef_str)
    except ValueError:
        while True:
            print('Необходимо ввести число!')
            print(prompt)
            try:
                coef = float(input())
                return coef
            except ValueError:
                pass
    return coef


"""
Вычисление корней квадратного уравнения
"""
def get_square_roots(a, b, c):
    d = b * b - 4 * a * c
    result = []
    if d == 0.0:
        root = -b/(2.0 * a)
        result.append(root)
    elif d > 0:
        sqD = math.sqrt(d)
        root1 = (-b + sqD)/(2.0 * a)
        root2 = (-b - sqD)/(2.0 * a)
        result.append(root1)
        result.append(root2)
    return result


"""
Вычисление корней биквадратного уравнения
"""
def get_biquad_roots(a, b, c):
    sqRoots = get_square_roots(a, b, c)
    result = []
    for root in sqRoots:
        if root > 0:
            result.append(round(math.sqrt(root), 3))
            result.append(round(-math.sqrt(root), 3))
        elif root == 0: result.append(root)
    return result


"""
Вывод корней уравнения
"""
def print_roots(roots):
    if len(roots) == 0:
        print('Нет корней')
    elif len(roots) == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len(roots) == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len(roots) == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len(roots) == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(
            roots[0], roots[1], roots[2], roots[3]))


def main():
    a = get_coef(1, 'Введите коэффициент A:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    print_roots(get_biquad_roots(a, b, c))


if __name__ == "__main__":
    main()
