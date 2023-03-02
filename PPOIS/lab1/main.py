from card import Card
from account import Account
from repository import Repository
from atm import ATM
from bank import Bank

import json
import sys


def read_data() -> tuple:
    try:
        with open('data.json') as f:
            data = json.load(f)

        accounts = [Account(x['login'], x['password'], x['balance'], x['id']) for x in data['accounts']]

        cards = []
        for x in data['cards']:
            for y in accounts:
                if y.id == x['account_id']:
                    cards.append(Card(x['pin'], y, x['number'], x['cvv'], x['date']))
                    break
        repository = Repository(data['repo'])
        Card.id_tf, Account.id_tf = data['card_id_tf'], data['account_id_tf']

        atm = ATM(repository=repository, cards=cards, access=data['atm-state']['access'])
        if data['atm-state']['inserted']:
            for i in range(len(cards)):
                if cards[i].number == data['atm-state']['card-number']:
                    atm = ATM(repository=repository, cards=cards, card=cards[i], access=data['atm-state']['access'])

        bank = Bank(accounts, cards)
        if data['bank-state']['logged']:
            for i in range(len(accounts)):
                if accounts[i].id == data['bank-state']['account-id']:
                    bank = Bank(accounts, cards, accounts[i])

    except (FileNotFoundError, KeyError, json.decoder.JSONDecodeError):
        accounts, cards, repository = [], [], Repository(2500)
        atm = ATM(repository, cards)
        bank = Bank(accounts, cards)

    return accounts, cards, repository, atm, bank


def write_data(accounts: list, cards: list, repository: Repository, atm: ATM, bank: Bank):
    dct = {
        'accounts': [x.as_dict() for x in accounts],
        'cards': [x.as_dict() for x in cards],
        'repo': repository.money,

        'card_id_tf': Card.id_tf,
        'account_id_tf': Account.id_tf,

        'atm-state': atm.as_dict(),
        'bank-state': bank.as_dict()
    }

    with open('data.json', 'w') as outfile:
        json.dump(dct, outfile, indent=4)


def main():
    accounts, cards, repository, atm, bank = read_data()

    main_args = '\t-atm\n' \
                '\t-bank'

    atm_args = f'\t-insert-card (card number)\n' \
               f'\t-extract-card\n' \
               f'\t-input-pin (PIN-code)\n' \
               f'\t-balance\n' \
               f'\t-put-money (amount)\n' \
               f'\t-get-money (amount)'

    bank_args = f'\t-register-acc (login) (password)\n' \
                f'\t-login (login) (password)\n' \
                f'\t-logout\n' \
                f'\t-register-card (PIN-code)' \

    try:

        match sys.argv[1]:
            case '-atm':
                try:
                    match sys.argv[2]:
                        case '-insert-card':
                            atm.insert_card(sys.argv[3])
                        case '-extract-card':
                            atm.extract_card()
                        case '-input-pin':
                            atm.input_pin(sys.argv[3])
                        case '-balance':
                            atm.card_balance()
                        case '-put-money':
                            atm.put_money(sys.argv[3])
                        case '-get-money':
                            atm.get_money(sys.argv[3])
                        case _:
                            print(f'Неизвестный флаг:\n\t{sys.argv[2]}\n'
                                  f'Возможные флаги:\n' + atm_args)
                except IndexError:
                    print('Отсутствуют флаги, возможные флаги:\n' + atm_args)
            case '-bank':
                try:
                    match sys.argv[2]:
                        case '-register-acc':
                            bank.register_acc(sys.argv[3], sys.argv[4])
                        case '-login':
                            bank.login(sys.argv[3], sys.argv[4])
                        case '-logout':
                            bank.logout()
                        case '-register-card':
                            bank.register_card(sys.argv[3])
                        case _:
                            print(f'Неизвестный флаг:\n\t{sys.argv[2]}\n'
                                  f'Возможные флаги:\n' + bank_args)
                except IndexError:
                    print('Отсутствуют флаги, возможные флаги:\n' + bank_args)
            case _:
                print(f'Неизвестный флаг:\n\t{sys.argv[1]}\n'
                      f'Возможные флаги:\n' + main_args)
    except IndexError:
        print('Отсутствуют флаги, возможные флаги:\n' + main_args)

    write_data(accounts, cards, repository, atm, bank)


if __name__ == '__main__':
    main()
