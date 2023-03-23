from functools import reduce

from src.Table import Table
from src.Calculate import solve
from src.Glue import get_glued


def delete_unused(constituents, implicants):

    usage_table = [
        [solve(
            '*'.join([f'{"!" * int(not c)}{v}' for c, v in zip(constituent, variables) if v != 2])
        ) for constituent in constituents] for variables in implicants]

    if not len(usage_table):
        return []

    repeatable = []
    for i in range(len(usage_table[0])):
        count = 0
        for j in range(len(usage_table)):
            count += int(usage_table[j][i])
        repeatable.append(bool(count - 1))

    uniq_lines_ind = []
    for i in range(len(usage_table)):
        for j in range(len(repeatable)):
            if usage_table[i][j] and not repeatable[j]:
                uniq_lines_ind.append(i)

    for x in uniq_lines_ind:
        for i in range(len(usage_table[0])):
            for j in range(len(usage_table)):
                if j not in uniq_lines_ind and usage_table[x][i]:
                    usage_table[j][i] = False

    important_implicants = []
    for i in range(len(usage_table)):
        if reduce(lambda a, b: a or b, usage_table[i]):
            important_implicants.append(implicants[i])

    return important_implicants


class Quine_McCluskey:

    @staticmethod
    def minimized_disjunctive(table: Table):
        variables = table.header[0]

        selected_rows = [x[0] for x in table.rows if x[1]]

        if not len(selected_rows):
            return None
        elif len(selected_rows) == len(table.rows):
            return 1

        impicants = delete_unused(selected_rows, get_glued(selected_rows))

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

        impicants = delete_unused(selected_rows, get_glued(selected_rows))

        impicants_str = [
            ' + '.join([f'{"!" * c}{v}' for c, v in zip(impicant, variables) if c != 2]
                       ) for impicant in impicants]

        return ' * '.join([f'({x})' for x in impicants_str])
