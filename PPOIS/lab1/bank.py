from account import Account
from card import Card


class Bank:

    def __init__(self, accounts: list, cards: list):
        self.__accounts = accounts
        self.__cards = cards
        self.menu()

    def add_account(self):
        login = input('Придумайте логин: ')
        while [x.login for x in self.__accounts].count(login):
            print('Этот логин уже занят, придумайте другой')
            login = input('Придумайте логин: ')
        password = input('Придумайте пароль: ')
        a = Account(login, password)
        self.__accounts.append(a)

    def get_access(self) -> Account:
        login = input('Введите логин: ')
        a = None
        for x in self.__accounts:
            if x.login == login:
                a = x
        if a is None:
            raise Exception('unknown account')

        for i in range(5):
            password = input('Введите пароль: ')
            if a.get_access(password):
                print('Доступ разрешен\n', flush=True)
                return a
            else:
                print(f'Неверный пароль\nПопробуйте еще раз (попыток осталось: {5 - (i + 1)})\n')

    def add_card(self, a: Account):

        match input(f'Хотите привязать новую карту к аккаунту {a.login}? (y/n)'):
            case 'y':
                pin = input('Введите PIN (4 цифры)')
                if len(pin) != 4:
                    raise Exception('invalid value')
                self.__cards.append(Card(pin, a))
            case 'n':
                pass
            case _:
                raise Exception('unknown command')


    def menu(self):
        while True:
            x = int(input("1 - Создать аккаунт\n2 - Привязать карту\n"))
            match x:
                case 1:
                    self.add_account()
                    self.add_card(self.__accounts[-1])
                case 2:
                    self.add_card(self.get_access())
                case 3:
                    break
                case _:
                    ...


