import copy
from sys import stdin

input1 = stdin.readline
directions = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
)


def is_in_range(n, a, b):
    return 0 <= a < n and 0 <= b < n


class BaseType:
    def get(self, i: int, j: int) -> int:
        pass

    def set(self, i: int, j: int, x: int):
        pass


class Type1(BaseType):
    def __init__(self, arr):
        self.arr = arr

    def get(self, i, j):
        return self.arr[i][j]

    def set(self, i, j, x):
        self.arr[i][j] = x


class Type2(BaseType):
    def __init__(self, arr):
        self.arr = arr

    def get(self, i, j):
        return self.arr[j][i]

    def set(self, i, j, x):
        self.arr[j][i] = x


def find_max(arr):
    return max([max(a) for a in arr])


def loop(arr, cnt):
    n = len(arr)
    if cnt == 5:
        return find_max(arr)

    result = []
    result.append(loop(to_right(copy.deepcopy(arr), n), cnt + 1))
    result.append(loop(to_down(copy.deepcopy(arr), n), cnt + 1))
    result.append(loop(to_left(copy.deepcopy(arr), n), cnt + 1))
    result.append(loop(to_top(copy.deepcopy(arr), n), cnt + 1))
    return max(result)


def to_top(arr, n):
    x = Type2(arr)
    to_something(x, 0, range(n), range(1, n), lambda _x: _x + 1)
    return x.arr


def to_left(arr, n):
    x = Type1(arr)
    to_something(x, 0, range(n), range(1, n), lambda _x: _x + 1)
    return x.arr


def to_down(arr, n):
    x = Type2(arr)
    to_something(x, n - 1, range(n), range(n - 2, -1, -1), lambda _x: _x - 1)
    return x.arr


def to_right(arr, n):
    x = Type1(arr)
    to_something(x, n - 1, range(n), range(n - 2, -1, -1), lambda _x: _x - 1)
    return x.arr


def to_something(x: BaseType, _top_idx, first_range, second_range, top_idx_set):
    for i in first_range:
        top_idx = _top_idx
        for j in second_range:
            if x.get(i, j) == 0:
                continue
            if x.get(i, j) == x.get(i, top_idx):
                x.set(i, top_idx, x.get(i, j) * 2)
                x.set(i, j, 0)
                top_idx = top_idx_set(top_idx)
            else:
                if x.get(i, top_idx) == 0:
                    x.set(i, top_idx, x.get(i, j))
                    x.set(i, j, 0)
                else:
                    top_idx = top_idx_set(top_idx)
                    if top_idx != j:
                        x.set(i, top_idx, x.get(i, j))
                        x.set(i, j, 0)


def solution():
    n = int(input1())
    arr = [list(map(int, input1().split())) for _ in range(n)]
    print(loop(copy.deepcopy(arr), 0))


if __name__ == "__main__":
    solution()
