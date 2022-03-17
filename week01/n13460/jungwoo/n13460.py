import copy
from sys import stdin

input1 = stdin.readline
directions = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
)


def is_in_range(n, a):
    return 0 <= a < n


class Obj:
    def __init__(self, r=-1, c=-1):
        self.r, self.c = r, c

    def set_pos(self, r, c):
        self.r, self.c = r, c

    def get_pos(self):
        return self.r, self.c


def go_straight(arr, r, c, a, b) -> tuple[tuple[int, int], bool]:
    n, m = len(arr), len(arr[0])
    original, last = (r, c), (r, c)
    x, y = r + a, c + b
    while is_in_range(n, x) and is_in_range(m, y) and arr[x][y] in ('.', 'O'):
        if arr[x][y] == 'O':
            arr[original[0]][original[1]] = '.'
            return (-1, -1), True
        last = (x, y)
        x, y = x + a, y + b
    arr[original[0]][original[1]], arr[last[0]][last[1]] = arr[last[0]][last[1]], arr[original[0]][original[1]]
    return last, False


def find(arr, st1: tuple[int, int], st2: tuple[int, int], ed: tuple[int, int], prev_dir, cnt):
    results = []
    for i in range(4):
        if (i + prev_dir > 1 and (i + prev_dir) % 2 == 0) or i == prev_dir:
            continue
        new_arr = copy.deepcopy(arr)
        tmp, tmp_found = go_straight(new_arr, st1[0], st1[1], directions[i][0], directions[i][1])
        last2, found2 = go_straight(new_arr, st2[0], st2[1], directions[i][0], directions[i][1])
        last1, found1 = go_straight(new_arr, tmp[0], tmp[1], directions[i][0], directions[i][1])
        if found2:
            continue
        elif tmp_found or found1:
            results.append(cnt)
        if cnt < 10:
            results.append(find(new_arr, last1, last2, ed, i, cnt + 1))
    if len(results) != 0:
        return min(results)
    else:
        return 11


def solution():
    n, m = map(int, input1().split())
    arr = [list(input1().rstrip()) for _ in range(n)]
    objs = [Obj() for _ in range(3)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                objs[0].set_pos(i, j)
            elif arr[i][j] == 'B':
                objs[1].set_pos(i, j)
            elif arr[i][j] == 'O':
                objs[2].set_pos(i, j)

    result = find(arr, objs[0].get_pos(), objs[1].get_pos(), objs[2].get_pos(), -10, 1)
    if result > 10:
        result = -1
    print(result)


if __name__ == "__main__":
    solution()
