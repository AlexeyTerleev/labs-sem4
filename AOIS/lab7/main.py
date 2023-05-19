from src.match_search import match_search
from src.boolean_search import boolean_search
from src.utils import get_binary, get_int


def main():
    lst = [4, 10, 1, 2, 7]
    bin_lst = [get_binary(x) for x in lst]

    print(bin_lst)
    res = boolean_search(bin_lst,
                         lambda a, b, c, d, e, f, g, h: (not a) and (not b) and (not c) and (not d) and (
                             not e) and f and g and h)

    print('Boolean search (func = !a * !b * !c * !d * !e * f * g * h)')
    print(f'num = {get_int(res)} (bin num = {res})')

    num = 3
    res = match_search(get_binary(3), bin_lst)
    print(f'Match search num = {num} (bin num = {get_binary(num)})')
    print(f'num = {get_int(res)} (bin num = {res})')


if __name__ == '__main__':
    main()
