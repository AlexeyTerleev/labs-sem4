from src.hash_table import HashTable


def main():
    hash_table = HashTable(
        [
            ('Аня', 'волейбол'),
            ('Аня', '123456789'),
            ('Даша', 'волейбол'),
            ('Маша', 'футбол'),
            ('Катя', 'футбол'),
            ('Ира', 'баскетбол'),

            ('Витя', 'баскетбол'),
            ('Петя', 'гандбол'),
            ('Леша', 'ганбол'),
            ('Даня', 'плавание'),
            ('Ваня', 'плавание'),
        ]
    )

    print(hash_table.table)

    print(f"hash_table['Ваня'] = {hash_table['Ваня']}")
    assert hash_table['Ваня'] == 'плавание'

    print(f"hash_table.insert('Ваня', 'test')")
    hash_table.insert('Ваня', 'test')

    print(f"hash_table['Ваня'] = {hash_table['Ваня']}")
    assert hash_table['Ваня'] == 'test'

    print(f"hash_table.delete('Ваня')")
    hash_table.delete('Ваня')

    print(f"hash_table['Ваня'] = ")
    try:
        assert hash_table['Ваня'] == 'test'
    except KeyError:
        print('Нет ключа')


if __name__ == '__main__':
    main()
