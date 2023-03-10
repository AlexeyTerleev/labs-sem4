import itertools
from prettytable import PrettyTable

from src.calc import solve, OPERATORS


def get_variables(formula: str) -> list:
    variables, curr = [], ''
    for sign in formula:
        if sign not in '() ' and sign not in OPERATORS:
            curr = curr + sign
        else:
            if curr != '' and curr not in variables:
                variables.append(curr)
            curr = ''
    if curr != '':
        variables.append(curr)
    return variables


def get_rows(formula: str) -> list:
    variables = get_variables(formula)

    lst_combinations = [dict(zip(variables, combination)) for combination in
                        sorted(list(set(itertools.combinations('01' * len(variables), len(variables)))))]

    lst_rows = []
    for combination in lst_combinations:
        curr_formula = formula
        for key, value in combination.items():
            curr_formula = curr_formula.replace(key, value)
        lst_rows.append([[int(x) for x in combination.values()], int(solve(curr_formula))])
    return lst_rows


class Table:

    def __init__(self, formula: str):
        self.__formula = formula
        self.__header = [get_variables(formula), 'result']
        self.__rows = get_rows(formula)

    @property
    def header(self):
        return self.__header

    @property
    def rows(self):
        return self.__rows

    def show(self):
        table = PrettyTable(self.__header[0] + [self.__header[1]])
        for row in self.rows:
            table.add_row(row[0] + [row[1]])
        print(table)
