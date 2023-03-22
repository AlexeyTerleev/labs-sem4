import itertools
from prettytable import PrettyTable

from src.Calculate import solve, OPERATORS
from src.ParseExceptions import ParseFormulaOperatorsException, ParseFormulaBreaksException


def get_variables(formula: str) -> list:
    variables, curr = [], ''
    for sign in formula:
        if sign not in '() ' and sign not in OPERATORS:
            curr = curr + sign
        else:
            if curr != '' and curr not in variables:
                variables.append(curr)
            curr = ''
    if curr != '' and curr not in variables:
        variables.append(curr)
    return sorted(variables)


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

        formula = ''.join(formula.split())

        if formula.count('(') != formula.count(')'):
            raise ParseFormulaBreaksException(formula)

        if formula[0] in OPERATORS and formula[0] != '!':
            raise ParseFormulaOperatorsException(formula, 0, 1)
        if formula[-1] in OPERATORS:
            raise ParseFormulaOperatorsException(formula, len(formula) - 1, 1)

        for i in range(len(formula) - 1):
            if (formula[i] in OPERATORS and formula[i + 1] in OPERATORS and formula[i + 1] != '!') or \
                    (formula[i] == '!' and formula[i + 1] == '!') or \
                    (formula[i] == '(' and formula[i + 1] in OPERATORS and formula[i + 1] != '!') or \
                    (formula[i] in OPERATORS and formula[i + 1] == ')') or \
                    (formula[i] == ')' and formula[i + 1] == '(') or \
                    (formula[i] == ')' and formula[i + 1] == '!') or \
                    (formula[i] == ')' and formula[i + 1] != ')' and formula[i + 1] not in OPERATORS):
                raise ParseFormulaOperatorsException(formula, i, 2)

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
