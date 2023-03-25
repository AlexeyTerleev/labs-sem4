from functools import reduce
from src.Table import Table
from src.Glue import glue


def bin2dec(binary: list) -> int:
    dec = 0
    for i in range(len(binary)):
        dec += 2 ** i * binary[::-1][i]
    return dec


def grey_code(num: int) -> list:
    if num > 2:
        raise 'Im to lazy to do this ^_^ (grey_code)'
    if not num:
        raise 'num = 0'

    if num == 1:
        return [[0], [1]]
    elif num == 2:
        return [[0, 0], [0, 1], [1, 1], [1, 0]]


def build_karno_map(table: Table):
    arity = len(table.header[0])

    if arity not in [2, 3, 4]:
        print('I am too lazy to do this ^_^ (build_karno_map)')
        return

    height = arity // 2
    width = (arity + 1) // 2

    cols_header = grey_code(width)
    rows_header = grey_code(height)

    k_map = [[0] * len(cols_header) for i in range(len(rows_header))]

    for i in range(len(k_map)):
        for j in range(len(k_map[i])):
            k_map[i][j] = table.rows[bin2dec(rows_header[i] + cols_header[j])][1]

    return k_map


def get_index(delta, pos, length) -> int:
    return delta + pos if delta + pos < length else (delta + pos) - length


def get_used_table(k_map) -> list:
    return [[0 for y in x] for x in k_map]


def edit_used(used, pos_x, pos_y, width, height) -> list:
    for i in range(height):
        for j in range(width):
            used[get_index(i, pos_y, len(used))][get_index(j, pos_x, len(used[i]))] = 1
    return used


def check_used(used, pos_x, pos_y, width, height) -> bool:
    for i in range(height):
        for j in range(width):
            if used[get_index(i, pos_y, len(used))][get_index(j, pos_x, len(used[i]))] == 0:
                return True
    return False


def check_lacuna(k_map, pos_x, pos_y, width, height, value) -> bool:
    for i in range(height):
        for j in range(width):
            y = get_index(i, pos_y, len(k_map))
            x = get_index(j, pos_x, len(k_map[i]))
            if k_map[y][x] != value:
                return False
    return True


# value: 1 for disjunctive, 0 for conjunctive
def found_lacunas(k_map: list, value: int) -> list:
    lacunas = []

    height = len(k_map)
    width = len(k_map[0])

    lacunas_widths = [x for x in range(width + 1) if x and x % 2 == 0 or x == 1]
    lacunas_heights = [x for x in range(height + 1) if x and x % 2 == 0 or x == 1]

    lacunas_sizes = []

    for width in lacunas_widths[::-1]:
        for height in lacunas_heights[::-1]:
            lacunas_sizes.append((width, height))

    used = get_used_table(k_map)

    for size in lacunas_sizes:
        for i in range(len(k_map)):
            for j in range(len(k_map[i])):
                if check_lacuna(k_map, j, i, size[0], size[1], value) and check_used(used, j, i, size[0], size[1]):
                    lacunas.append((j, i, size[0], size[1]))
                    used = edit_used(used, j, i, size[0], size[1])

    return lacunas


def get_minimized(implicants: list) -> list:
    curr = implicants[0]
    for impl in implicants:
        for i in range(len(impl)):
            if curr[i] != impl[i]:
                curr[i] = 2
    return curr


def get_impl_from_lacunas(lacunas: list, k_map: list) -> list:
    impl = []

    cols_header = grey_code(len(k_map[0]) // 2)
    rows_header = grey_code(len(k_map) // 2)

    for lacuna in lacunas:
        impicants = []
        for i in range(lacuna[3]):
            for j in range(lacuna[2]):
                impicants.append(
                    rows_header[get_index(lacuna[1], i, len(rows_header))] +
                    cols_header[get_index(lacuna[0], j, len(cols_header))]
                )
        impl.append(get_minimized(impicants))

    return impl


class Karno:

    @staticmethod
    def minimized_disjunctive(table: Table):

        selected_rows = [x[0] for x in table.rows if x[1]]

        if not len(selected_rows):
            return None
        elif len(selected_rows) == len(table.rows):
            return 1

        k_map = build_karno_map(table)
        variables = table.header[0]
        impicants = get_impl_from_lacunas(found_lacunas(k_map, 1), k_map)

        impicants_str = [
            ' * '.join([f'{"!" * (not c)}{v}' for c, v in zip(impicant, variables) if c != 2]
                       ) for impicant in impicants]
        return ' + '.join([f'({x})' for x in impicants_str])

    @staticmethod
    def minimized_conjunctive(table: Table):

        selected_rows = [x[0] for x in table.rows if not x[1]]

        if not len(selected_rows):
            return None
        elif len(selected_rows) == len(table.rows):
            return 0

        k_map = build_karno_map(table)
        variables = table.header[0]
        impicants = get_impl_from_lacunas(found_lacunas(k_map, 0), k_map)

        impicants_str = [
            ' + '.join([f'{"!" * c}{v}' for c, v in zip(impicant, variables) if c != 2]
                       ) for impicant in impicants]

        return ' * '.join([f'({x})' for x in impicants_str])
