import sys
from src.Table import Table
from src.PerfectForms import PerfectForms
from src.ParseExceptions import ParseFormulaBreaksException, ParseFormulaOperatorsException

from src.Quine_McCluskey import Quine_McCluskey
from src.Estimated import Estimated
from src.KarnoMap import Karno, LargeFormulaKarnoMapException


def main():

    # formula = 'a > !(b + c > (a * !c + !b))'

    if len(sys.argv) > 2 or len(sys.argv) == 1:
        print(f'Expected 1 argument, but given {len(sys.argv) - 1}')
        return

    formula = sys.argv[1]

    try:
        table = Table(formula)
    except (ParseFormulaBreaksException, ParseFormulaOperatorsException) as e:
        print(e)
        return

    print(
        f'Формула: {formula}\nТаблица истинности:\n {table.show()}'
        f'\nСДНФ: {PerfectForms.perfect_disjunctive(table)}\n'
        f'СКНФ: {PerfectForms.perfect_conjunctive(table)}\n\n'

        f'ТДНФ (расчетный метод): {Estimated.minimized_disjunctive(table)}\n'
        f'ТКНФ (расчетный метод): {Estimated.minimized_conjunctive(table)}\n\n'

        f'ТДНФ (метод Квайна-Мак-Класски): {Quine_McCluskey.minimized_disjunctive(table)}\n'
        f'ТКНФ (метод Квайна-Мак-Класски): {Quine_McCluskey.minimized_conjunctive(table)}\n'
    )
    try:
        print(
            f'ТДНФ (метод Карно): {Karno.minimized_disjunctive(table)}\n'
            f'ТКНФ (метод Карно): {Karno.minimized_conjunctive(table)}\n\n'
    
            f'Карта Карно:\n{Karno.show_k_map(table)}\n'
        )
    except LargeFormulaKarnoMapException as e:
        print(e)


if __name__ == '__main__':
    main()
