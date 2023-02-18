import os
import time

from card import Card
from account import Account
from repository import Repository


def print_hello() -> None:
    os.system('clear')
    print('---------------------------\n'
          'Вас приветствует АльфаБанк!\n'
          '---------------------------\n', flush=True)

def processing() -> None:
    print('Обработка ', end='', flush=True)
    for j in range(3):
        os.system('sleep .2')
        print('.', end='', flush=True)
    os.system('sleep .2')
class ATMScreens:
    @staticmethod
    def selection_screen():
        print_hello()
        x = input('Выберите операцию:\n'
                         '1 - Снять деньги\n'
                         '2 - Положить деньги\n'
                         '3 - Проверить баланс\n'
                         '4 - Назад\n')
        processing()
        return x
    @staticmethod
    def input_pin_screen(card: Card) -> bool:
        print_hello()
        for i in range(5):
            pin = input('Введите PIN-код: ')

            processing()
            print_hello()

            if card.get_access(pin):
                print('Доступ разрешен\n', flush=True)
                time.sleep(1)
                return True
            else:
                print(f'Неверный PIN-код\nПопробуйте еще раз (попыток осталось: {5 - (i + 1)})\n')

        raise Exception('access error')

    @staticmethod
    def check_balance_screen(card: Card):
        print_hello()
        print(f'Баланс на карте: {card.account.balance}\n')
        input('Для продолжени нажмите любую клавишу ')

    @staticmethod
    def put_money_screen(card: Card, repo: Repository) -> None:
        print_hello()
        money = float(input('Введите сумму для пополнения: '))
        if money <= 0:
            raise Exception('invalid amount')

        card.account.increase_balance(money)
        repo.put_money(money)

        processing()
        print_hello()

        print('Операция проведена успешно!\n', flush=True)
        time.sleep(1)

    @staticmethod
    def get_money_screen(card: Card, repo: Repository) -> None:
        print_hello()
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

        processing()
        print_hello()

        print('Операция проведена успешно!\n', flush=True)
        time.sleep(1)

class BankScreens:

    @staticmethod
    def selection_screen() -> str:
        print_hello()
        x = input('Выберите операцию:\n'
                '1 - Создать счет\n'
                '2 - Привязать карту\n'
                '3 - Назад\n')
        processing()
        return x

    @staticmethod
    def add_card_screen(a: Account, cards: list):

        match input(f'Хотите привязать новую карту к счету {a.login}? (y/n)'):
            case 'y':
                pin = input('Введите PIN (4 цифры)')
                if len(pin) != 4 or not pin.isdigit():
                    raise Exception('invalid value')
                cards.append(Card(pin, a))
            case 'n':
                pass
            case _:
                raise Exception('invalid command')

    @staticmethod
    def find_account_screen(accounts: list) -> Account:
        while True:
            login = input('Введите логин: ')
            for x in accounts:
                if x.login == login:
                    return x
            print(f'Неверный логин\nПопробуйте еще раз')

    @staticmethod
    def get_access_screen(account: Account) -> bool:
        for i in range(5):
            password = input('Введите пароль: ')
            if account.get_access(password):
                print('Доступ разрешен\n', flush=True)
                return True
            else:
                print(f'Неверный пароль\nПопробуйте еще раз (попыток осталось: {5 - (i + 1)})\n')
        raise Exception('access error')

    @staticmethod
    def add_account_screen(accounts: list):
        login = input('Придумайте логин: ')
        while [x.login for x in accounts].count(login):
            print('Этот логин уже занят, придумайте другой')
            login = input('Придумайте логин: ')
        password = input('Придумайте пароль: ')
        a = Account(login, password)
        accounts.append(a)