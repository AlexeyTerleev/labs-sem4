from inspect import signature
from src.utils import get_binary


def boolean_search(lst, boolean_func):
    for x in lst:
        if len(get_binary(x)) != len(signature(boolean_func).parameters):
            raise ValueError
    return (x for x in lst if boolean_func(*get_binary(x)))
