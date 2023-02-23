import sys


if __name__ == '__main__':

    try:
        match sys.argv[1]:
            case '-atm':
                match sys.argv[2]:
                    case '-insert_card':
                        print('Карта вставлена!')
                    case _:
                        print('err')
            case _:
                print('err')
    except IndexError:
        print('Неверное количество аргументов')