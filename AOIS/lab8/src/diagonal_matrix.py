from typing import List, Iterator
from src.utils import get_binary, sum_binary, compare


class DiagonalMatrix:

    def __init__(self, lst: List[int], size: int = 16):
        matrix_bin = [[0 for _ in range(size)] for _ in range(size)]
        for i, num in enumerate(lst):
            bin_num = get_binary(num)
            for j in range(len(matrix_bin)):
                matrix_bin[(i + j) % size][i] = bin_num[j]
        self.matrix = matrix_bin
        self.size = size

    def __getitem__(self, ind: int) -> List[int]:
        return [self.matrix[(j + ind) % self.size][ind] for j in range(self.size)]

    def __setitem__(self, ind: int, el: List[int]) -> None:
        for j in range(self.size):
            self.matrix[(ind + j) % self.size][ind] = el[j]

    def __iter__(self) -> Iterator[List[int]]:
        for i in range(self.size):
            yield self[i]

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return '\n'.join(' '.join([str(el) for el in line]) for line in self.matrix)

    def sum(self, lst: List[int] = None) -> None:
        if lst is None or len(lst) != 3:
            lst = [1, 0, 0]
        for i in range(self.size):
            el = self[i]
            if el[:3] != lst:
                continue
            el[11:] = sum_binary(el[3:7], el[7:11])
            self[i] = el
            return

    def sort(self, reverse=True) -> None:
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if (not compare(self[i], self[j]) and not reverse) or (compare(self[i], self[j]) and reverse):
                    self[i], self[j] = self[j], self[i]

    def bool_func_4(self, ind_1, ind_2, ind_3):
        self[ind_3] = [int(not self[ind_1][i] and self[ind_2][i]) for i in range(self.size)]

    def bool_func_6(self, ind_1, ind_2, ind_3):
        self[ind_3] = [int((not self[ind_1][i] and self[ind_2][i]) or (self[ind_1][i] and not self[ind_2][i]))
                       for i in range(self.size)]

    def bool_func_9(self, ind_1, ind_2, ind_3):
        self[ind_3] = [int((self[ind_1][i] and self[ind_2][i]) or (not self[ind_1][i] and not self[ind_2][i]))
                       for i in range(self.size)]

    def bool_func_11(self, ind_1, ind_2, ind_3):
        self[ind_3] = [int(self[ind_1][i] or not self[ind_2][i]) for i in range(self.size)]
