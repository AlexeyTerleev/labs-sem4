from typing import List, Tuple


def match(first: Tuple[int], second: Tuple[int]) -> int:
    return len([x for x in zip(first, second) if x[0] == x[1]])


def match_search(bin_num: Tuple[int], lst: List[Tuple[int]]) -> Tuple[int]:
    if not len(lst):
        raise ValueError
    result, match_num = lst[0], match(bin_num, lst[0])
    for x in lst[1:]:
        if match_num < match(bin_num, x):
            result, match_num = x, match(bin_num, x)
    return tuple(result)
