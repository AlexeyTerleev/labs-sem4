from account import Account


class Card:

    def __init__(self, number: int = 0, cvv: int = 0, date: str = '', pin: int = 1111, account: Account = Account()):
        self.__number = number
        self.__cvv = cvv
        self.__date = date
        self.__pin = pin
        self.__account = account

    def as_dict(self):
        return {
            'number': self.__number,
            'cvv': self.cvv,
            'date': self.date,
            'pin': self.__pin,
            'account_id': self.account.id
        }

    @property
    def number(self) -> int:
        return self.__number

    @property
    def cvv(self) -> int:
        return self.__cvv

    @property
    def date(self) -> str:
        return self.__date

    @property
    def account(self) -> Account:
        return self.__account

    def get_access(self, pin: int):
        return self.__pin == pin
