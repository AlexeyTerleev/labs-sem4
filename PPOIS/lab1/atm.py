from screens import ATMScreens

from repository import Repository
from card import Card

class ATM:

    def __init__(self, repository: Repository, card: Card):

        self.__repository = repository
        self.__access = False
        self.__card = card

        self.start()

    def start(self) -> None:

        self.__access = ATMScreens.input_pin_screen(self.__card)

        if self.__access:
            while True:
                x = ATMScreens.selection_screen()
                match x:
                    case '1':
                        ATMScreens.get_money_screen(self.__card, self.__repository)
                    case '2':
                        ATMScreens.put_money_screen(self.__card, self.__repository)
                    case '3':
                        ATMScreens.check_balance_screen(self.__card)
                    case '4':
                        self.__access = False
                        break
                    case _:
                        raise Exception('invalid command')
