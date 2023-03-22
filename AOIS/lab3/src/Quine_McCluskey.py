from functools import reduce

from src.Table import Table
from src.Calculate import solve


def get_glued(constituents: list) -> list:
    out = []

    for i in range(len(constituents[0])):
        curr = start_glue(constituents)
        constituents = delete_duplicate(curr[0])
        out += curr[1]

    return out + constituents


def start_glue(constituents):
    out, final = [], []
    for i in range(len(constituents)):
        used = False
        for j in range(len(constituents)):
            glue_res = glue(constituents[i], constituents[j])
            if glue_res is not None:
                out.append(glue_res)
                used = True
        if not used:
            final.append(constituents[i])
    return out, final


def glue(first_constituent, second_constituent):
    out = []
    count = 0
    for i in range(len(first_constituent)):
        if first_constituent[i] != second_constituent[i]:
            count += 1
            out.append(2)
        else:
            out.append(first_constituent[i])

    return out if count == 1 else None


def contains(lst1, lst2):
    for x in lst1:
        flag = True
        for i in range(len(x)):
            if x[i] != lst2[i]:
                flag = False
                break
        if flag:
            return True
    return False


def delete_duplicate(lst):
    out = []
    for x in lst:
        if not contains(out, x):
            out.append(x)
    return out


def delete_unused(constituents, implicants):
    usage_table = [
        [solve(
            '*'.join([f'{"!" * int(not c)}{v}' for c, v in zip(constituent, variables) if v != 2])
        ) for constituent in constituents] for variables in implicants]

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

        impicants = delete_unused([x[0] for x in table.rows if x[1]], get_glued([x[0] for x in table.rows if x[1]]))

        impicants_str = [
            ' * '.join([f'{"!" * int(not c)}{v}' for c, v in zip(impicant, variables) if c != 2]
                       ) for impicant in impicants]

        return ' + '.join([f'({x})' for x in impicants_str])

    @staticmethod
    def minimized_conjunctive(table: Table):
        variables = table.header[0]

        impicants = delete_unused([x[0] for x in table.rows if not x[1]], get_glued([x[0] for x in table.rows if not x[1]]))

        impicants_str = [
            ' * '.join([f'{"!" * c}{v}' for c, v in zip(impicant, variables) if c != 2]
                       ) for impicant in impicants]

        return ' + '.join([f'({x})' for x in impicants_str])
