from typing import Tuple, List
from src.utils import get_binary, sum_binary


class DiagonalMatrix:

    def __init__(self, lst: List[int], size: int = 16):
        matrix_bin = [[0 for _ in range(size)] for _ in range(size)]
        for i, num in enumerate(lst):
            bin_num = get_binary(num)
            for j in range(len(matrix_bin)):
                matrix_bin[(i + j) % size][i] = bin_num[j]
        self.matrix = matrix_bin
        self.size = size

    def __getitem__(self, ind: int):
        return [self.matrix[(j + ind) % self.size][ind] for j in range(self.size)]

    def fill(self, el: List[int], ind: int):
        for j in range(self.size):
            self.matrix[(ind + j) % self.size][ind] = el[j]

    def sum(self, lst: List[int] = None):
        if lst is None or len(lst) != 3:
            lst = [1, 0, 0]
        for i in range(self.size):
            el = self[i]
            if el[:3] != lst:
                continue
            el[11:] = sum_binary(el[3:7], el[7:11])
            self.fill(el, i)
            return

    def compare(self, ind_1: int, ind_2: int):
        for pair in zip(self.matrix[ind_1], self.matrix[ind_2]):
            if pair[0] > pair[1]:
                return True
            elif pair[1] < pair[0]:
                return False
        return False

    def sort(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                comparison_result = self.compare(i, j)
                if not comparison_result:
                    tmp = self[i]
                    self.fill(self[j], i)
                    self.fill(tmp, j)

    def func_4(self, ind_1, ind_2, ind_3):
        self.fill([not self[ind_1][i] and self[ind_2][i] for i in range(self.size)], ind_3)

    def func_6(self, ind_1, ind_2, ind_3):
        self.fill([(not self[ind_1][i] and self[ind_2][i]) or (self[ind_1][i] and not self[ind_2][i])
                   for i in range(self.size)], ind_3)

    def func_9(self, ind_1, ind_2, ind_3):
        self.fill([(self[ind_1][i] and self[ind_2][i]) or (not self[ind_1][i] and not self[ind_2][i])
                   for i in range(self.size)], ind_3)

    def func_11(self, ind_1, ind_2, ind_3):
        self.fill([self[ind_1][i] and not self[ind_2][i] for i in range(self.size)], ind_3)
