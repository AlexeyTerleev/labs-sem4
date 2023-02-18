import os
import time

from card import Card
from repository import Repository


class Screen:

    @staticmethod
    def print_hello() -> None:
        os.system('clear')
        print('---------------------------\n'
              'Вас приветствует АльфаБанк!\n'
              '---------------------------\n', flush=True)

    @staticmethod
    def processing() -> None:
        print('Обработка ', end='', flush=True)
        for j in range(3):
            os.system('sleep .2')
            print('.', end='', flush=True)
        os.system('sleep .2')

    @staticmethod
    def input_pin_screen(card: Card) -> bool:
        Screen.print_hello()
        for i in range(5):
            pin = input('Введите PIN-код: ')

            Screen.processing()
            Screen.print_hello()

            if card.get_access(pin):
                print('Доступ разрешен\n', flush=True)
                time.sleep(1)
                return True
            else:
                print(f'Неверный PIN-код\nПопробуйте еще раз (попыток осталось: {5 - (i + 1)})\n')

        raise Exception('access error')

    @staticmethod
    def selection_screen():
        Screen.print_hello()
        x = int(input('Выберите операцию:\n'
                         '1) Снять деньги\n'
                         '2) Положить деньги\n'
                         '3) Проверить баланс\n'
                         '4) Выход\n'))
        Screen.processing()
        return x

    @staticmethod
    def check_balance_screen(card: Card):
        Screen.print_hello()
        print(f'Баланс на карте: {card.account.balance}\n')
        input('Для продолжени нажмите любую клавишу ')

    @staticmethod
    def put_money_screen(card: Card, repo: Repository) -> None:
        Screen.print_hello()
        money = float(input('Введите сумму для пополнения: '))
        if money <= 0:
            raise Exception('invalid amount')

        card.account.increase_balance(money)
        repo.put_money(money)

        Screen.processing()
        Screen.print_hello()

        print('Операция проведена успешно!\n', flush=True)
        time.sleep(1)

    @staticmethod
    def get_money_screen(card: Card, repo: Repository) -> None:
        Screen.print_hello()
        print(f'Остаток на счете: {card.account.balance}\nДоступно к обналичиванию: {repo.money}')

        money = int(input('Введите сумму для вывода: '))
        if money <= 0:
            raise Exception('invalid amount')
        if money > card.account.balance:
            raise Exception('insufficient funds')
        if money > repo.money:
            raise Exception('Insufficient funds in storage')

        repo.get_money(money)
        card.account.decrease_balance(money)

        Screen.processing()
        Screen.print_hello()

        print('Операция проведена успешно!\n', flush=True)
        time.sleep(1)

