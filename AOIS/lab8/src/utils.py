from typing import Tuple, List


def get_binary(num_int: int, length: int = 16) -> Tuple[int]:
    out = []
    while num_int > 0:
        out.append(num_int % 2)
        num_int = num_int // 2
    while len(out) < length:
        out.append(0)
    return tuple(out[::-1])


def get_int(bin_num: Tuple[int]) -> int:
    result = 0
    for i, x in enumerate(bin_num[::-1]):
        result += pow(2, i) if x else 0
    return result


def get_normal_matrix(matrix_int: List[int], size: int = 16):
    matrix_bin = [[0 for _ in range(size)] for _ in range(size)]
    for i, num in enumerate(matrix_int):
        matrix_bin[i] = get_binary(matrix_int[i])
    return matrix_bin


def print_matrix(matrix):
    for line in matrix:
        print(' '.join([str(el) for el in line]))


def sum_binary(first, second):
    out, flag = [], False
    for i, pair in enumerate(zip(first[::-1], second[::-1])):
        if pair[0] and pair[1]:
            if flag:
                out.append(1)
            else:
                out.append(0)
            flag = True
        elif pair[0] or pair[1]:
            if flag:
                out.append(0)
            else:
                out.append(1)
        else:
            if flag:
                out.append(1)
            else:
                out.append(0)
            flag = False
    if flag:
        out.append(1)
    else:
        out.append(0)
    return out[::-1]


def compare(first: List[int], second: List[int]):
    for pair in zip(first, second):
        if pair[0] > pair[1]:
            return True
        elif pair[0] < pair[1]:
            return False
    return False


