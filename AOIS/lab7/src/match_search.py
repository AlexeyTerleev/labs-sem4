from typing import List
from src.utils import get_binary


def match(first: int, second: int) -> int:
    return len([x for x in zip(get_binary(first), get_binary(second)) if x[0] == x[1]])


def match_search(num: int, lst: List[int]) -> int:
    if not len(lst):
        raise ValueError
    result, match_num = lst[0], match(num, lst[0])
    for x in lst[1:]:
        if match_num < match(num, x):
            result, match_num = x, match(num, x)
    return result
