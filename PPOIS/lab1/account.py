
class Account:

    def __init__(self, num: int = 0, login: str = '', password: str = '', balance: float = 0):
        self.__id = num
        self.__login = login
        self.__password = password
        self.__balance = balance

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.__login,
            'password': self.__password,
            'balance': self.__balance
        }

    @property
    def login(self):
        return self.__login

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def id(self) -> int:
        return self.__id

    def get_access(self, password):
        return self.__password == password

    def increase_balance(self, money: float) -> None:
        self.__balance += money

    def decrease_balance(self, money: float) -> None:
        self.__balance -= money
