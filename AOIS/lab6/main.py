from src.hash_table import HashTable


def main():
    hash_table = HashTable(
        [
            ('Аня', 'волейбол'),
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

    print(len(hash_table.table))
    print(hash_table.table)

    print(hash_table['Ваня'])


if __name__ == '__main__':
    main()
