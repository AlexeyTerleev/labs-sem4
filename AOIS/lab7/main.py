from src.match_search import match_search
from src.boolean_search import boolean_search


def main():
    lst = [4, 10, 1, 2, 7]
    print(
        list(boolean_search(lst,
                            lambda a, b, c, d, e, f, g, h: (not a) and (not b) and (not c) and (not d) and (
                                not e) and f and g and h)))
    print(match_search(3, lst))


if __name__ == '__main__':
    main()
