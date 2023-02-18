from screens import *


class ATM:

    def __init__(self, repository: Repository, card: Card):

        self.__repository = repository
        self.__access = False
        self.__card = card

        self.start()

    def enter_pin(self) -> None:
        self.__access = Screen.input_pin_screen(self.__card)

    def main_menu(self) -> int:
        return Screen.selection_screen()

    def put_money(self) -> None:
        Screen.put_money_screen(self.__card, self.__repository)

    def get_money(self) -> None:
        Screen.get_money_screen(self.__card, self.__repository)

    def check_balance(self) -> None:
        Screen.check_balance_screen(self.__card)

    def start(self) -> None:

        self.enter_pin()

        if self.__access:

            while True:

                x = self.main_menu()
                match x:
                    case 1:
                        self.get_money()
                    case 2:
                        self.put_money()
                    case 3:
                        self.check_balance()
                    case 4:
                        self.__access = False
                        break
                    case _:
                        ...
