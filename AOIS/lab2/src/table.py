import itertools
from prettytable import PrettyTable

from src.calc import solve, OPERATORS


def get_variables(formula: str) -> list:
    variables = []
    for x in formula:
        if x not in '() ' and x not in OPERATORS and x not in variables:
            variables.append(x)
    return variables


def get_rows(formula: str) -> list:
    variables = get_variables(formula)

    lst_rows = [dict(zip(variables, x)) for x in
                sorted(list(set(itertools.combinations('01' * len(variables), len(variables)))))]

    lst = []
    for row in lst_rows:
        curr_formula = ''.join([row.get(x, x) for x in formula])
        lst.append([[int(x) for x in row.values()], int(solve(curr_formula))])
    return lst


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
        for x in self.rows:
            table.add_row(x[0] + [x[1]])
        print(table)
