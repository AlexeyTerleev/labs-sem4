class ParseFormulaBreaksException(Exception):
    def __init__(self, formula: str):
        self.__formula = formula

    def __str__(self):
        return f'\033[31mError, number of opening brackets: {self.__formula.count("(")}, ' \
               f'\033[31mand closing brackets: {self.__formula.count(")")}'


class ParseFormulaOperatorsException(Exception):
    def __init__(self, formula: str, pos: int, length: int):
        self.__formula = formula
        self.__pos = pos
        self.__length = length

    def __str__(self):
        return f'\033[31mError while parse formula: ' \
               f'\033[36m\n{self.__formula}\n' \
               f'\033[31m{"-" * self.__pos}' \
               f'{"^" * self.__length}' \
               f'{"-" * (len(self.__formula) - self.__length - self.__pos)}' \
               f'\033[37m'
