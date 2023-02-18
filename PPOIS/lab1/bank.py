from screens import BankScreens

from account import Account
class Bank:

    def __init__(self, accounts: list, cards: list):
        self.__accounts = accounts
        self.__cards = cards

        self.__access = False

        self.start()


    def start(self) -> None:
        while True:
            match BankScreens.selection_screen():
                case '1':
                    BankScreens.add_account_screen(self.__accounts)
                    account = self.__accounts[-1]
                    self.__access = True
                case '2':
                    account = BankScreens.find_account_screen(self.__accounts)
                    self.__access = BankScreens.get_access_screen(account)
                case '3':
                    break
                case _:
                    raise Exception('invalid command')

            if self.__access:
                BankScreens.add_card_screen(account, self.__cards)
                self.__access = False
