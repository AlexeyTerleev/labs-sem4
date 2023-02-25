from repository import Repository
from card import Card

class ATM:

    def __init__(self, repository: Repository, cards: list, card: Card = None, access: bool = False):

        self.__repository = repository
        self.__cards = cards

        self.__access = access

        self.__inserted = False
        if card is not None:
            self.__inserted = True
        self.__card = card

    def as_dict(self) -> dict:
        number = None
        if self.__inserted:
            number = self.__card.number
        dct = {
            "inserted": self.__inserted,
            "card-number": number,
            "access": self.__access
        }
        return dct

    @property
    def inserted(self):
        return self.__inserted

    @property
    def card(self):
        return self.__card

    def insert_card(self, card_num):

        if self.__inserted:
            print(f'В банкомат уже вставлена карта {self.card.number}!')
            return

        for card in self.__cards:
            if card.number == card_num:
                self.__inserted = True
                self.__card = card
                print(f'Карта {card.number} вставлена!')

        if not self.inserted:
            print(f'Карты {card_num} не существует!')

    def extract_card(self):

        if not self.__inserted:
            print('В банкомате не вставлена карта!')
            return

        self.__access = False

        card = self.__card

        self.__inserted = False
        self.__card = None

        print(f'Карта {card.number} была извлечена')

    def input_pin(self, pin: str):

        if not self.__inserted:
            print(f'Для начала вставьте карту!')
            return

        if self.__access:
            print(f'Вы уже разблокировали карту!')
            return

        if len(pin) != 4:
            print('PIN - код должен состоять из 4 цифр!')
            return

        if not pin.isdigit():
            print('PIN - код должен состоять только из цифр!')
            return

        if self.__card.get_access(pin):
            self.__access = True
            print('Доступ разрешен')
        else:
            print('Неверный PIN-код')

    def card_balance(self):

        if not self.__inserted:
            print(f'Для начала вставьте карту!')
            return

        if not self.__access:
            print(f'Для начала введите PIN - код!')
            return

        print(f'Баланс на карте {self.__card.number}: {self.__card.account.balance}')

    def put_money(self, money_str: str):

        if not self.__inserted:
            print(f'Для начала вставьте карту!')
            return

        if not self.__access:
            print(f'Для начала введите PIN - код!')
            return

        if not money_str.isdigit():
            print('Сумма должна быть положительным числом!')
            return

        money = int(money_str)

        if money <= 0:
            print(f'Сумма должна быть больше нуля!')
            return

        self.__card.account.increase_balance(money)
        self.__repository.put_money(money)

        print('Операция проведена успешно!')

    def get_money(self, money_str: str):

        if not self.__inserted:
            print(f'Для начала вставьте карту!')
            return

        if not self.__access:
            print(f'Для начала введите PIN - код!')
            return

        if not money_str.isdigit():
            print('Сумма должна быть положительным числом!')
            return

        money = int(money_str)

        if money <= 0:
            print(f'Сумма должна быть больше нуля!')
            return
        if money > self.__card.account.balance:
            print(f'Недостаточно средств на счете (остаток на счете {self.__card.account.balance})')
            return
        if money > self.__repository.money:
            print(f'Недостаточно купюр в банкомате (доступно к обналичиванию {self.__repository.money})')

        self.__repository.get_money(money)
        self.__card.account.decrease_balance(money)

        print('Операция проведена успешно!')
