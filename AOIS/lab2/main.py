import sys
from src.table import Table
from src import normal_forms
from src.ParseExceptions import ParseFormulaBreaksException, ParseFormulaOperatorsException


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
        f'\nСДНФ: {normal_forms.perfect_disjunctive(table)}\n'
        f'СКНФ: {normal_forms.perfect_conjunctive(table)}\n\n'
        
        f'СДНФ (бинарная): {normal_forms.perfect_disjunctive_bin(table)}\n'
        f'СКНФ (бинарная): {normal_forms.perfect_conjunctive_bin(table)}\n\n'
        
        f'СДНФ (десятичная): {normal_forms.perfect_disjunctive_desc(table)}\n'
        f'СКНФ (десятичная): {normal_forms.perfect_conjunctive_desc(table)}\n\n'
        
        f'Индекс: {normal_forms.get_ind(table)}'
    )


if __name__ == '__main__':
    main()
