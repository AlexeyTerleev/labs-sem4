from functools import reduce

from src.Table import Table
from src.Calculate import solve
from src.Glue import get_glued


def is_important(verifiable_implicant, others_implicants, type_: str) -> bool:

    if not len(others_implicants):
        return True

    variables = [f'x{i}' for i in range(len(verifiable_implicant))]
    val = dict(zip(variables, verifiable_implicant))

    sub_formulas = [
        [f'{"!" * int(not b)}{val[a] if val[a] != 2 else a}' for a, b in zip(variables, x) if b != 2]
        for x in others_implicants
    ]

    for i in range(len(sub_formulas)):
        for j in range(len(sub_formulas[i])):
            if sub_formulas[i][j] == '!0':
                sub_formulas[i][j] = '1'
            elif sub_formulas[i][j] == '!1':
                sub_formulas[i][j] = '0'

    minimize = []

    for formula in sub_formulas:
        if not formula.count('0' if type_ == 'dis' else '1') and len(set(formula).difference({'0', '1'})):
            minimize += list(set(formula).difference({'0', '1'}))

    for val in minimize:
        if '!' + val in minimize:
            minimize = list(filter(lambda a: a != val and a != '!' + val, minimize))

    return bool(len(minimize))


def found_important(implicants: list, type_: str):

    if type_ not in ['con', 'dis']:
        raise f'Error, unknown argument value type_ = {type_}'

    important_implicants = []
    for impl in implicants:
        without = [x for x in implicants if x != impl]
        if is_important(impl, without, type_):
            important_implicants.append(impl)
    return important_implicants



class Estimated:

    @staticmethod
    def minimized_disjunctive(table: Table):
        variables = table.header[0]

        selected_rows = [x[0] for x in table.rows if x[1]]

        if not len(selected_rows):
            return None
        elif len(selected_rows) == len(table.rows):
            return 1

        impicants = found_important(get_glued(selected_rows), 'dis')

        impicants_str = [
            ' * '.join([f'{"!" * int(not c)}{v}' for c, v in zip(impicant, variables) if c != 2]
                       ) for impicant in impicants]

        return ' + '.join([f'({x})' for x in impicants_str])

    @staticmethod
    def minimized_conjunctive(table: Table):
        variables = table.header[0]

        selected_rows = [x[0] for x in table.rows if not x[1]]

        if not len(selected_rows):
            return None
        elif len(selected_rows) == len(table.rows):
            return 0

        impicants = found_important(get_glued(selected_rows), 'con')

        impicants_str = [
            ' + '.join([f'{"!" * c}{v}' for c, v in zip(impicant, variables) if c != 2]
                       ) for impicant in impicants]

        return ' * '.join([f'({x})' for x in impicants_str])


def main():
    table = Table('!x1 * !x2 * x3 + !x1 * x2 * !x3 + !x1 * x2 * x3 + x1 * x2* !x3')
    table = Table('!((!x1+!c)*(!x2*!c))')
    print(Estimated.minimized_conjunctive(table))
    print(Estimated.minimized_disjunctive(table))


if __name__ == '__main__':
    main()
