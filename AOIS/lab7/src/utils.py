from typing import Tuple


def get_binary(num_int: int, length: int = 8) -> Tuple[int]:
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
