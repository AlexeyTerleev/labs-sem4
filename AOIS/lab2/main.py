from src.table import Table
from src import normal_forms


def main():
    formula = input('Enter formula: ')
    # '^((b + ^c) * ^(^b * ^c))'

    table = Table(formula)

    table.show()

    print(f'СДНФ: {normal_forms.perfect_disjunctive(table)}')
    print(f'СКНФ: {normal_forms.perfect_conjunctive(table)}')


if __name__ == '__main__':
    main()
