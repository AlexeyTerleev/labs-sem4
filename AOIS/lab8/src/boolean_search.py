from inspect import signature
from typing import Tuple, List, Callable


def boolean_search(bin_lst: List[Tuple[int]], boolean_func: Callable):
    for x in bin_lst:
        if len(x) != len(signature(boolean_func).parameters):
            raise ValueError
    for x in bin_lst:
        if boolean_func(*x):
            return x
