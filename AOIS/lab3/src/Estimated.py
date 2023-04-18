from src.Table import Table
from src.Glue import get_glued


def is_important(verifiable_implicant, others_implicants, type_: str) -> bool:
    if not len(others_implicants):
        return True

    variables = [f'x{i}' for i in range(len(verifiable_implicant))]
    val = dict(zip(variables, verifiable_implicant))

    sub_formulas = [
        [f'{"!" * int((not b) if type_ == "dis" else b)}{val[a] if val[a] != 2 else a}' for a, b in zip(variables, x) if b != 2]
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

        # Experimental
        elif len(formula) != len([x for x in verifiable_implicant if x != 2]):
            return True

    for v in minimize:
        if '!' + v in minimize:
            minimize = list(filter(lambda a: a != v and a != '!' + v, minimize))

    return bool(len(minimize))


def found_important(implicants: list, type_: str):
    if type_ not in ['con', 'dis']:
        raise f'Error, unknown argument value type_ = {type_}'

    delta = 0
    important_implicants = []
    for i in range(len(implicants)):
        without = [x for x in implicants if x != implicants[i - delta]]
        if is_important(implicants[i - delta], without, type_):
            important_implicants.append(implicants[i - delta])
        else:
            implicants.pop(i - delta)
            delta += 1
    return important_implicants


class Estimated:

    @staticmethod
    def minimized_disjunctive(table: Table):
        variables = table.header[0]

        result = []
        for i in range(len(table.rows[0][1])):
            selected_rows = [x[0] for x in table.rows if x[1][i]]

            if not len(selected_rows):
                return None
            elif len(selected_rows) == len(table.rows):
                return 1

            impicants = found_important(get_glued(selected_rows), 'dis')

            impicants_str = [
                ' * '.join([f'{"!" * int(not c)}{v}' for c, v in zip(impicant, variables) if c != 2]
                           ) for impicant in impicants]

            result.append((table.header[1][i], ' + '.join([f'({x})' for x in impicants_str])))

        return result

    @staticmethod
    def minimized_conjunctive(table: Table):
        variables = table.header[0]

        result = []
        for i in range(len(table.rows[0][1])):
            variables = table.header[0]

            selected_rows = [x[0] for x in table.rows if not x[1][i]]

            if not len(selected_rows):
                return None
            elif len(selected_rows) == len(table.rows):
                return 0

            impicants = found_important(get_glued(selected_rows), 'con')

            impicants_str = [
                ' + '.join([f'{"!" * c}{v}' for c, v in zip(impicant, variables) if c != 2]
                           ) for impicant in impicants]

            result.append((table.header[1][i], ' * '.join([f'({x})' for x in impicants_str])))

        return result
