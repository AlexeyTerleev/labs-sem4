from random import randint

from src.utils import *
from src.diagonal_matrix import DiagonalMatrix


def test1():
    print('\nТест 1 (построение матрицы)\n')
    lst = [randint(0, 65000) for _ in range(16)]
    matrix = DiagonalMatrix(lst)

    print(f'Обычная матрица:\n{chr(10).join(" ".join(str(el) for el in line) for line in get_normal_matrix(lst))}\n')
    print(f'Матрица с диагнальной адресацией:\n{matrix}')

    assert [get_int(x) for x in matrix] == lst


def test2():
    print('\nТест 2 (сортировка матрицы)\n')
    lst = [randint(0, 65000) for _ in range(16)]
    matrix = DiagonalMatrix(lst)

    print(f'Исходная матрица с диагнальной адресацией:\n{matrix}\n')
    matrix.sort()
    print(f'Отсортированная матрица с диагнальной адресацией:\n{matrix}')

    print(f'Исходные значения в десятичной системе:\n{lst}\nОтсортированные:\n{[get_int(x) for x in matrix]}')

    assert [get_int(x) for x in matrix] == sorted(lst, reverse=False)


def test3():
    print('\nТест 3 (логическая функция f4)\n')
    lst = [randint(0, 65000) for _ in range(16)]
    matrix = DiagonalMatrix(lst)
    print(f'Исходная матрица с диагнальной адресацией:\n{matrix}\n')
    matrix.bool_func_4(0, 1, 2)
    print(f'Матрица после проведения логической функции f4 = !x1 * x2 '
          f'(x1 - 0й стобец, x2 - 1й столбец, f4 - 2й столбец):\n{matrix}')


def test4():
    print('\nТест 4 (логическая функция f6)\n')
    lst = [randint(0, 65000) for _ in range(16)]
    matrix = DiagonalMatrix(lst)
    print(f'Исходная матрица с диагнальной адресацией:\n{matrix}\n')
    matrix.bool_func_6(0, 1, 2)
    print(f'Матрица после проведения логической функции f6 = !x1 * x2 + x1 * !x2 '
          f'(x1 - 0й стобец, x2 - 1й столбец, f4 - 2й столбец):\n{matrix}')


def test5():
    print('\nТест 5 (логическая функция f9)\n')
    lst = [randint(0, 65000) for _ in range(16)]
    matrix = DiagonalMatrix(lst)
    print(f'Исходная матрица с диагнальной адресацией:\n{matrix}\n')
    matrix.bool_func_9(0, 1, 2)
    print(f'Матрица после проведения логической функции f9 = x1 * x2 + !x1 * !x2 '
          f'(x1 - 0й стобец, x2 - 1й столбец, f4 - 2й столбец):\n{matrix}')


def test6():
    print('\nТест 6 (логическая функция f11)\n')
    lst = [randint(0, 65000) for _ in range(16)]
    matrix = DiagonalMatrix(lst)
    print(f'Исходная матрица с диагнальной адресацией:\n{matrix}\n')
    matrix.bool_func_11(0, 1, 2)
    print(f'Матрица после проведения логической функции f11 = x1 + !x2 '
          f'(x1 - 0й стобец, x2 - 1й столбец, f4 - 2й столбец):\n{matrix}')


def test7():
    print('\nТест 6 (сумма [0, 0, 1])\n')
    lst = [randint(0, 65000) for _ in range(16)]
    matrix = DiagonalMatrix(lst)
    print(f'Исходная матрица с диагнальной адресацией:\n{matrix}\n')
    matrix.sum([0, 0, 1])
    print(f'Матрица после суммы:\n{matrix}')


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()


if __name__ == '__main__':
    main()
