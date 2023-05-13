from typing import Tuple


def get_binary(num_int: int, length: int = 8) -> Tuple:
    out = []
    while num_int > 0:
        out.append(num_int % 2)
        num_int = num_int // 2
    while len(out) < length:
        out.append(0)
    return tuple(out[::-1])
