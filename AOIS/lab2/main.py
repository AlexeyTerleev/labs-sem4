import sys
from src.table import Table
from src import normal_forms


def main():

    if len(sys.argv) > 2 or len(sys.argv) == 1:
        print(f'Expected 1 argument, but given {len(sys.argv) - 1}')
        return

    formula = sys.argv[1]
    # formula = '!((x2 + !x3) * !(!x2 * !x3))'

    table = Table(formula)

    table.show()
    print(
        f'СДНФ: {normal_forms.perfect_disjunctive(table)}\n'
        f'СКНФ: {normal_forms.perfect_conjunctive(table)}\n\n'
        
        f'СДНФ (бинарная): {normal_forms.perfect_disjunctive_bin(table)}\n'
        f'СКНФ (бинарная): {normal_forms.perfect_conjunctive_bin(table)}\n\n'
        
        f'СДНФ (десятичная): {normal_forms.perfect_disjunctive_desc(table)}\n'
        f'СКНФ (десятичная): {normal_forms.perfect_conjunctive_desc(table)}\n\n'
        
        f'Индекс: {normal_forms.get_ind(table)}'
    )


if __name__ == '__main__':
    main()
