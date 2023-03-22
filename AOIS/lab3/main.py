import sys
from src.Table import Table
from src.PerfectForms import PerfectForms
from src.ParseExceptions import ParseFormulaBreaksException, ParseFormulaOperatorsException

from src.Quine_McCluskey import Quine_McCluskey


def main():

    # formula = '!(x1 > (x3 * x1) * !(!x2 + !x3))'

    if len(sys.argv) > 2 or len(sys.argv) == 1:
        print(f'Expected 1 argument, but given {len(sys.argv) - 1}')
        return

    try:
        table = Table(sys.argv[1])
    except (ParseFormulaBreaksException, ParseFormulaOperatorsException) as e:
        print(e)
        return

    print('Таблица истинности: ')
    table.show()
    print(
        f'\nСДНФ: {PerfectForms.perfect_disjunctive(table)}\n'
        f'СКНФ: {PerfectForms.perfect_conjunctive(table)}\n\n'
        f'ТДНФ (метод Квайна-Мак-Класски): {Quine_McCluskey.minimized_disjunctive(table)}\n'
        f'ТКНФ (метод Квайна-Мак-Класски): {Quine_McCluskey.minimized_conjunctive(table)}\n\n'
    )


if __name__ == '__main__':
    main()
