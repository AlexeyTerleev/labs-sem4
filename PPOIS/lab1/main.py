from card import Card
from account import Account
from repository import Repository
from atm import ATM
from bank import Bank

import json
import os


def main() -> None:
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

    except FileNotFoundError:
        accounts, cards, repository = [], [], Repository(2500)

    while True:
        os.system('clear')
        match int(input('1 - Операции с банкоматом\n2 - Создать счет\n3 - Выход\n')):
            case 1:
                print('Выберите карту:\n')
                for i in range(len(cards)):
                    print(f'{i}) {cards[i].number}')
                ATM(repository, cards[int(input())])
            case 2:
                Bank(accounts, cards)
            case 3:
                break

    dct = {
        'accounts': [x.as_dict() for x in accounts],
        'cards': [x.as_dict() for x in cards],
        'repo': repository.money,

        'card_id_tf': Card.id_tf,
        'account_id_tf': Account.id_tf
    }

    with open('data.json', 'w') as outfile:
        json.dump(dct, outfile)


if __name__ == '__main__':
    main()
'''Добавить регистрацию карт + перевести все в csv и pandas'''
