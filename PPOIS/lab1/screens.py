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

def print_message(message: str, static: bool, delay: float = 1) -> None:
    print_hello()
    if static:
        print(message)
        input('Для продолжени нажмите любую клавишу ')
    else:
        print(message, flush=True)
        os.system(f'sleep {delay}')

class ATMScreens:
    @staticmethod
    def selection_screen():
        print_hello()
        x = input('1 - Снять деньги\n'
                  '2 - Положить деньги\n'
                  '3 - Проверить баланс\n'
                  '4 - Назад\n\n')
        processing()
        return x
    @staticmethod
    def input_pin_screen(card: Card) -> bool:
        print_hello()
        for i in range(5):
            pin = input('Введите PIN-код: ')

            processing()

            if card.get_access(pin):
                print_message('Доступ разрешен\n', False)
                return True
            else:
                print_hello()
                print(f'Неверный PIN-код\nПопробуйте еще раз (попыток осталось: {5 - (i + 1)})\n')

        raise Exception('access error')

    @staticmethod
    def check_balance_screen(card: Card):
        print_message(f'Баланс на карте: {card.account.balance}\n', True)

    @staticmethod
    def put_money_screen(card: Card, repo: Repository) -> None:
        print_hello()
        money = float(input('Введите сумму для пополнения: '))
        if money <= 0:
            raise Exception('invalid amount')

        card.account.increase_balance(money)
        repo.put_money(money)

        processing()

        print_message('Операция проведена успешно!\n', False)

    @staticmethod
    def get_money_screen(card: Card, repo: Repository) -> None:
        print_hello()

        if not card.account.balance:
            print_message('Для начала нужно пополнить баланс!\n', False)
            return

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

        print_message('Операция проведена успешно!\n', False)

class BankScreens:

    @staticmethod
    def selection_screen() -> str:
        print_hello()
        x = input('1 - Создать счет\n'
                '2 - Привязать карту\n'
                '3 - Назад\n\n')
        processing()
        return x

    @staticmethod
    def add_card_screen(a: Account, cards: list):
        print_hello()
        match input(f'Хотите привязать новую карту к счету {a.login}? (y/n) '):
            case 'y':
                pin = input('Введите PIN (4 цифры): ')
                if len(pin) != 4 or not pin.isdigit():
                    raise Exception('invalid value')
                cards.append(Card(pin, a))

                processing()
                print_message(f'Зарегистрирова новая карта:\n\n'
                      f'\tНомер карты: {cards[-1].number}\n'
                      f'\tСрок обслуживания до: {cards[-1].date}\n'
                      f'\tCVV: {cards[-1].cvv}\n', True)

            case 'n':
                pass
            case _:
                raise Exception('invalid command')

    @staticmethod
    def find_account_screen(accounts: list) -> Account:
        while True:
            print_hello()
            login = input('Введите логин: ')

            processing()

            for x in accounts:
                if x.login == login:
                    return x

            print_message(f'Счета с таким логином не существует\nПопробуйте еще раз', False)

    @staticmethod
    def get_access_screen(account: Account) -> bool:

        print_hello()

        for i in range(5):

            password = input('Введите пароль: ')

            processing()
            print_hello()

            if account.get_access(password):
                print('Доступ разрешен\n', flush=True)
                return True
            else:
                print(f'Неверный пароль\nПопробуйте еще раз (попыток осталось: {5 - (i + 1)})')
        raise Exception('access error')

    @staticmethod
    def add_account_screen(accounts: list):

        print_hello()

        while True:
            login = input('Придумайте логин: ')

            processing()
            print_hello()

            if not [x.login for x in accounts].count(login):
                break

            print('Этот логин уже занят, придумайте другой')

        password = input('Придумайте пароль: ')
        a = Account(login, password)
        accounts.append(a)
        processing()
        print_message(f'Создан счет:\n\n\tЛогин: {login}\n\tПароль: {password}\n', True)