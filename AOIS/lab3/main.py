import sys
from src.Table import Table
from src.PerfectForms import PerfectForms
from src.ParseExceptions import ParseFormulaBreaksException, ParseFormulaOperatorsException
from src.Utilities import print_normal_forms

from src.Quine_McCluskey import Quine_McCluskey
from src.Estimated import Estimated
from src.KarnoMap import Karno, LargeFormulaKarnoMapException


def main():

    formulas, headers = None, None

    # formulas = ['a > !((b + c) > (a * c + b))']
    # headers = ['res']
    #
    formulas = [
        '(!a*!b*p)+(!a*b*!p)+(a*!b*!p)+(a*b*p)',
        '(!a*b*p)+(a*!b*p)+(a*b*!p)+(a*b*p)',
    ]
    headers = ['res', 'tran']
    #
    # formulas = [
    #     '(!x1*!x2*!x3*!x4)+(!x1*!x2*!x3*x4)+(!x1*!x2*x3*!x4)+(!x1*!x2*x3*x4)'
    #     '+(!x1*x2*!x3*!x4)+(!x1*x2*!x3*x4)+(!x1*x2*x3*!x4)',
    #
    #     '(!x1*!x2*x3*x4)+(!x1*x2*!x3*!x4)+(!x1*x2*!x3*x4)+(!x1*x2*x3*!x4)',
    #
    #     '(!x1*!x2*!x3*x4)+(!x1*!x2*x3*!x4)+(!x1*x2*!x3*x4)+(x1*!x2*!x3*x4)+(!x1*x2*x3*!x4)',
    #
    #     '(!x1*!x2*!x3*!x4)+(!x1*!x2*x3*!x4)+(!x1*x2*!x3*!x4)+(x1*!x2*!x3*!x4)'
    #     '+(x1*!x2*!x3*x4)+(!x1*x2*x3*!x4)'
    # ]

    try:
        table = Table(formulas, headers)
    except (ParseFormulaBreaksException, ParseFormulaOperatorsException) as e:
        print(e)
        return

    print('Формулы:')
    for header, formula in zip(table.header[1], formulas):
        print(f'{header} = {formula}')
    print(f'Таблица истинности:\n{table.show()}\n')
    print(
        f'СДНФ:\n{print_normal_forms(PerfectForms.perfect_disjunctive(table))}\n'
        # f'СКНФ:\n{print_normal_forms(PerfectForms.perfect_conjunctive(table))}\n'
        # f'\n'
        # f'ТДНФ (расчетный метод):\n{print_normal_forms(Estimated.minimized_disjunctive(table))}\n'
        # f'ТКНФ (расчетный метод):\n{print_normal_forms(Estimated.minimized_conjunctive(table))}\n'
        # f'\n'
        # f'ТДНФ (метод Квайна-Мак-Класски):\n{print_normal_forms(Quine_McCluskey.minimized_disjunctive(table))}\n'
        # f'ТКНФ (метод Квайна-Мак-Класски):\n{print_normal_forms(Quine_McCluskey.minimized_conjunctive(table))}\n'
    )
    try:
        print(
            f'ТДНФ (метод Карно):\n{print_normal_forms(Karno.minimized_disjunctive(table))}\n'
            # f'ТКНФ (метод Карно):\n{print_normal_forms(Karno.minimized_conjunctive(table))}\n\n'
            #
            # f'Карта Карно:\n{print_normal_forms(Karno.show_k_map(table))}\n'
        )
    except LargeFormulaKarnoMapException as e:
        print(e)


if __name__ == '__main__':
    main()
