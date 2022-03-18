from collections import deque
from sys import stdin

input1 = stdin.readline
directions = (
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
)


def is_in_range(boundary, x):
    return 0 <= x < boundary


class Dice:
    def __init__(self, arr, r, c):
        self.arr: list[list[int]] = arr
        self.r, self.c = r, c
        self.n, self.m = len(self.arr), len(self.arr[0])
        self.horizontal, self.vertical = deque([0] * 4), deque([0] * 4)

    def _is_in_range(self, x, y):
        return is_in_range(self.n, x) and is_in_range(self.m, y)

    def get_top(self):
        return self.horizontal[2]

    def to_east(self):
        x, y = self.r + directions[0][0], self.c + directions[0][1]
        if not self._is_in_range(x, y):
            return False
        next_num = self.horizontal[1]
        if self.arr[x][y] == 0:
            self.arr[x][y] = next_num
        else:
            self.horizontal[1] = self.arr[x][y]
            self.arr[x][y] = 0
        self.horizontal.append(self.horizontal.popleft())
        self.vertical[0], self.vertical[2] = self.horizontal[0], self.horizontal[2]
        self.r, self.c = x, y
        return True

    def to_west(self):
        x, y = self.r + directions[1][0], self.c + directions[1][1]
        if not self._is_in_range(x, y):
            return False
        next_num = self.horizontal[3]
        if self.arr[x][y] == 0:
            self.arr[x][y] = next_num
        else:
            self.horizontal[3] = self.arr[x][y]
            self.arr[x][y] = 0
        self.horizontal.appendleft(self.horizontal.pop())
        self.vertical[0], self.vertical[2] = self.horizontal[0], self.horizontal[2]
        self.r, self.c = x, y
        return True

    def to_north(self):
        x, y = self.r + directions[2][0], self.c + directions[2][1]
        if not self._is_in_range(x, y):
            return False
        next_num = self.vertical[1]
        if self.arr[x][y] == 0:
            self.arr[x][y] = next_num
        else:
            self.vertical[1] = self.arr[x][y]
            self.arr[x][y] = 0
        self.vertical.append(self.vertical.popleft())
        self.horizontal[0], self.horizontal[2] = self.vertical[0], self.vertical[2]
        self.r, self.c = x, y
        return True

    def to_south(self):
        x, y = self.r + directions[3][0], self.c + directions[3][1]
        if not self._is_in_range(x, y):
            return False
        next_num = self.vertical[3]
        if self.arr[x][y] == 0:
            self.arr[x][y] = next_num
        else:
            self.vertical[3] = self.arr[x][y]
            self.arr[x][y] = 0
        self.vertical.appendleft(self.vertical.pop())
        self.horizontal[0], self.horizontal[2] = self.vertical[0], self.vertical[2]
        self.r, self.c = x, y
        return True


def solution():
    n, m, x, y, k = map(int, input1().split())
    arr = [list(map(int, input1().split())) for _ in range(n)]
    commands = list(map(lambda _x: int(_x) - 1, input1().split()))

    dice = Dice(arr, x, y)
    move_funcs = (
        dice.to_east,
        dice.to_west,
        dice.to_north,
        dice.to_south,
    )
    result = ''
    for command in commands:
        if move_funcs[command]():
            result += str(dice.get_top()) + '\n'
    print(result)


if __name__ == "__main__":
    solution()
