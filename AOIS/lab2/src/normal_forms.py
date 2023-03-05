from src.table import Table


def perfect_disjunctive(table: Table):
    sub_formulas = []
    for x in table.rows:
        if x[1]:
            curr = []
            for i in range(len(x[0])):
                if x[0][i]:
                    curr.append(table.header[0][i])
                else:
                    curr.append('^' + table.header[0][i])
            sub_formulas.append(f'({" * ".join(curr)})')
    return ' + '.join(sub_formulas)


def perfect_conjunctive(table: Table):
    sub_formulas = []
    for x in table.rows:
        if not x[1]:
            curr = []
            for i in range(len(x[0])):
                if not x[0][i]:
                    curr.append(table.header[0][i])
                else:
                    curr.append('^' + table.header[0][i])
            sub_formulas.append(f'({" + ".join(curr)})')
    return ' * '.join(sub_formulas)
