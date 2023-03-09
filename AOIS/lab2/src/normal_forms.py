from src.table import Table


def bin2dec(binary: list):
    dec = 0
    for i in range(len(binary)):
        dec += pow(2, i) * binary[::-1][i]
    return dec


def get_ind(table: Table):
    ind = 0
    for i in range(len(table.rows)):
        ind += pow(2, i) * table.rows[-(i + 1)][1]
    return ind


def perfect_disjunctive(table: Table):
    sub_formulas = []
    for row in table.rows:
        if row[1]:
            curr = []
            for i in range(len(row[0])):
                if row[0][i]:
                    curr.append(table.header[0][i])
                else:
                    curr.append('!' + table.header[0][i])
            sub_formulas.append(f'({" * ".join(curr)})')
    return ' + '.join(sub_formulas)


def perfect_disjunctive_bin(table: Table):
    return f'+({", ".join(["".join([str(num) for num in row[0]]) for row in table.rows if row[1]])})'


def perfect_disjunctive_desc(table: Table):
    return f"+({', '.join([str(bin2dec(row[0])) for row in table.rows if row[1]])})"


def perfect_conjunctive(table: Table):
    sub_formulas = []
    for row in table.rows:
        if not row[1]:
            curr = []
            for i in range(len(row[0])):
                if not row[0][i]:
                    curr.append(table.header[0][i])
                else:
                    curr.append('!' + table.header[0][i])
            sub_formulas.append(f'({" + ".join(curr)})')
    return ' * '.join(sub_formulas)


def perfect_conjunctive_bin(table: Table):
    return f'*({", ".join(["".join([str(num) for num in row[0]]) for row in table.rows if not row[1]])})'


def perfect_conjunctive_desc(table: Table):
    return f"*({', '.join([str(bin2dec(row[0])) for row in table.rows if not row[1]])})"
