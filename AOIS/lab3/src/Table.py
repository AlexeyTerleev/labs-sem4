import itertools
from functools import reduce
from typing import List, Dict

from prettytable import PrettyTable

from src.Calculate import solve, OPERATORS
from src.ParseExceptions import ParseFormulaOperatorsException, ParseFormulaBreaksException, HeadersNumberException


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


def get_result(formula: str, combination: Dict[str, str]) -> bool:
    curr_formula = formula
    for key, value in combination.items():
        curr_formula = curr_formula.replace(key, value)
    return solve(curr_formula)


def get_rows(formulas: List[str], variables: str) -> list:

    lst_combinations = [dict(zip(variables, combination)) for combination in
                        sorted(list(set(itertools.combinations('01' * len(variables), len(variables)))))]

    lst_rows = []
    for combination in lst_combinations:
        lst_rows.append([[int(x) for x in combination.values()],
                         [int(get_result(formula, combination)) for formula in formulas]])
    return lst_rows


def formula_check(formula: str) -> None:
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


class Table:

    def __init__(self, formulas: List[str], output_headers: List[str]):

        for formula in formulas:
            formula_check(formula)

        variables = []
        for formula in formulas:
            variables = list(set(variables + get_variables(formula)))
        variables = sorted(variables)

        if len(output_headers) != len(formulas):
            raise HeadersNumberException

        self.__formulas = formulas
        self.__header = [variables, output_headers]
        self.__rows = get_rows(formulas, variables)

    @property
    def header(self):
        return self.__header

    @property
    def rows(self):
        return self.__rows

    def show(self):
        table = PrettyTable(self.__header[0] + self.__header[1])
        for row in self.rows:
            table.add_row(row[0] + row[1])
        return table
