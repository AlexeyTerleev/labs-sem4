from src.utils import *
from src.diagonal_matrix import DiagonalMatrix

from random import randint


def main():
    lst = [randint(0, 256) for _ in range(16)]
    lst = [45035, 223, 191, 223, 63, 14, 80, 86, 239, 44, 207, 75, 48, 3, 38, 174]
    print(lst)
    print_matrix(get_normal_matrix(lst))
    print()

    diagonal_matrix_bin = DiagonalMatrix(lst)
    print_matrix(diagonal_matrix_bin.matrix)

    assert [get_int(diagonal_matrix_bin[i]) for i in range(16)] == lst
    print()

    diagonal_matrix_bin.sum([0, 0, 0])
    print_matrix(diagonal_matrix_bin.matrix)


if __name__ == '__main__':
    main()
