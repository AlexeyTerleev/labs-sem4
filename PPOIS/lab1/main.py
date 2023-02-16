from card import Card
from account import Account
from repository import Repository
from atm import ATM

import json
import os


def main() -> None:
    try:
        with open('data.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = json.loads('{"accounts":[],"cards":[],"repo": 5000}')

    accounts = [Account(x['id'], x['balance']) for x in data['accounts']]
    cards = []

    for x in data['cards']:
        for y in accounts:
            if y.id == x['account_id']:
                cards.append(Card(x['number'], x['cvv'], x['date'], x['pin'], y))
                break

    repository = Repository(data['repo'])

    while True:
        os.system('clear')
        match int(input('1 - Операции с банкоматом\n2 - Создать счет\n')):
            case 1:
                print('Выберите карту:\n')
                for i in range(len(cards)):
                    print(f'{i}) {cards[i].number}')
                ATM(repository, cards[int(input())])
            case 2:
                x = int(input("1 - Создать аккаунт\n2 - Привязать курту\n"))
                if x == 1:

                    login = input('Придумайте логин: ')
                    while [x.login for x in accounts].count(login):
                        print('Этот логин уже занят, придумайте другой')
                        login = input('Придумайте логин: ')
                    password = input('Придумайте пароль: ')
                    a = Account(100, login, password)
                    accounts.append(a)
                    print('Хотите првязать новую карту к этому аккаунту?')

                elif x == 2:

                    login = input('Введите логин: ')
                    for x in accounts:
                        if x.login == login:
                            a = x

                    password = input('Введите пароль: ')
                    while not x.get_access(password):
                        password = input('Неверный пароль, попробуйте еще раз: ')

            case 3:
                break

    dct = {
        'accounts': [x.as_dict() for x in accounts],
        'cards': [x.as_dict() for x in cards],
        'repo': repository.money
    }

    with open('data.json', 'w') as outfile:
        json.dump(dct, outfile)


if __name__ == '__main__':
    main()
'''Добавить регистрацию карт + перевести все в csv и pandas'''
