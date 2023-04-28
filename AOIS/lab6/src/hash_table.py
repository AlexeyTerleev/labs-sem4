from typing import List, Tuple, Any, Hashable


class HashTable:

    def __init__(self, values: List[Tuple[Hashable, Any]] = None):

        self.capacity = 1 if values is None else len(values)
        self.fullness = 0
        self.table = [[] for _ in range(self.capacity)]

        if values is not None:
            for val in values:
                self.insert(*val)

    def get_hash(self, key: Hashable):
        return hash(key) % self.capacity

    def resize(self, new_size: int) -> None:
        if new_size < len(self.table):
            raise ValueError

        lst = [element for line in self.table for element in line]
        self.capacity = new_size
        self.fullness = 0
        self.table = [[] for _ in range(new_size)]
        for element in lst:
            self.insert(*element)

    def get_index(self, key: Hashable) -> int:
        hash_key = self.get_hash(key)
        for i, key_val in enumerate(self.table[hash_key]):
            if key == key_val[0]:
                return i
        raise KeyError

    def __getitem__(self, key: Hashable) -> Any:
        return self.table[self.get_hash(key)][self.get_index(key)][1]

    def insert(self, key: Hashable, value: Any):
        try:
            self.table[self.get_hash(key)][self.get_index(key)] = value
        except KeyError:
            self.table[self.get_hash(key)].append((key, value))
            self.fullness += 1
            if self.capacity == self.fullness:
                self.resize(self.capacity * 2)

    def delete(self, key: Hashable):
        try:
            del self.table[self.get_hash(key)][self.get_index(key)]
        except KeyError:
            ...
