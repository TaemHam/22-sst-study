import copy
from sys import stdin

input1 = stdin.readline
directions = (
    (-1, 0),  # 상
    (0, 1),  # 우
    (1, 0),  # 하
    (0, -1),  # 좌
)


def is_in_range(n, m, a, b):
    return 0 <= a < n and 0 <= b < m


class Research:
    def __init__(self, r, c):
        self.r, self.c = r, c


class Warmer:
    def __init__(self, r, c, d):
        self.r, self.c = r, c
        if d == 3:
            self.d = 0
        elif d == 1:
            self.d = 1
        elif d == 4:
            self.d = 2
        else:
            self.d = 3


class WarmerDirection:
    def __init__(self, arr):
        self.arr = arr

    def set_block_pos(self, r, c, t) -> tuple[int, int]: pass
    def to_straight(self, r, c) -> tuple[int, int]: pass
    def to_left(self, r, c) -> tuple[int, int]: pass
    def to_right(self, r, c) -> tuple[int, int]: pass


class Up(WarmerDirection):
    def to_straight(self, r, c): return r - 1, c
    def to_left(self, r, c): return r - 1, c - 1
    def to_right(self, r, c): return r - 1, c + 1


class Down(WarmerDirection):
    def to_straight(self, r, c): return r + 1, c
    def to_left(self, r, c): return r + 1, c + 1
    def to_right(self, r, c): return r + 1, c - 1


class Right(WarmerDirection):
    def to_straight(self, r, c): return r, c + 1
    def to_left(self, r, c): return r - 1, c + 1
    def to_right(self, r, c): return r + 1, c + 1


class Left(WarmerDirection):
    def to_straight(self, r, c): return r, c - 1
    def to_left(self, r, c): return r + 1, c - 1
    def to_right(self, r, c): return r - 1, c - 1


def get_start_pos(r, c, d):
    a, b = directions[d]
    return r + a, c + b, d


def get_warmers_and_research(arr, m, n):
    warmers = []
    research = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 5:
                research.append(Research(i, j))
                arr[i][j] = 0
            elif arr[i][j] > 0:
                warmers.append(Warmer(i, j, arr[i][j]))
                arr[i][j] = 0
    return research, warmers


def get_wall_arr(m, n, walls):
    wall_arr = [[[True] * 4 for _ in range(m)] for _ in range(n)]
    for i in range(len(walls)):
        r, c, t = walls[i]
        if t + 1 == 0:
            wall_arr[r][c][0] = False
            if r - 1 >= 0:
                wall_arr[r - 1][c][2] = False
        else:
            wall_arr[r][c][1] = False
            if c + 1 < m:
                wall_arr[r][c + 1][3] = False
    return wall_arr


def blow(arr, wall_arr, warmer, cmd):
    n, m = len(arr), len(arr[0])
    r, c, wd = get_start_pos(warmer.r, warmer.c, warmer.d)
    if not is_in_range(n, m, r, c):
        return
    arr[r][c] += 5
    curr = {(r, c)}
    wd = warmer.d
    for i in range(4, 0, -1):
        nexts = set()
        for cr, cc in curr:
            nr, nc = cmd.to_straight(cr, cc)
            if is_in_range(n, m, nr, nc) and wall_arr[nr][nc][(wd + 2) % 4]:
                nexts.add((nr, nc))

            nr, nc = cmd.to_left(cr, cc)
            if is_in_range(n, m, nr, nc) and wall_arr[nr][nc][(wd + 2) % 4] and wall_arr[cr][cc][(wd + 3) % 4]:
                nexts.add((nr, nc))

            nr, nc = cmd.to_right(cr, cc)
            if is_in_range(n, m, nr, nc) and wall_arr[nr][nc][(wd + 2) % 4] and wall_arr[cr][cc][(wd + 1) % 4]:
                nexts.add((nr, nc))

        for nr, nc in nexts:
            arr[nr][nc] += i
        curr = nexts


def adjust(arr, wall_arr, n, m):
    def _adjust(_arr, i1, j1, i2, j2, diff):  # arr[i1][j1] < arr[i2][j2]
        _arr[i1][j1], _arr[i2][j2] = _arr[i1][j1] + diff, _arr[i2][j2] - diff
    new_arr = copy.deepcopy(arr)
    for i in range(n):
        for j in range(i % 2, m, 2):
            for k in range(4):
                a, b = directions[k]
                x, y = i + a, j + b
                if not is_in_range(n, m, x, y) or not wall_arr[i][j][k]:
                    continue
                if arr[i][j] < arr[x][y]:
                    _adjust(new_arr, i, j, x, y, (arr[x][y] - arr[i][j]) // 4)
                elif arr[i][j] > arr[x][y]:
                    _adjust(new_arr, x, y, i, j, (arr[i][j] - arr[x][y]) // 4)
    return new_arr


def cool_down(arr, n, m):
    a, b, c, d = max(0, arr[0][0] - 1), max(0, arr[n - 1][0] - 1), max(0, arr[0][m - 1] - 1), max(0, arr[n - 1][m - 1] - 1)
    for j in (0, -1):
        for i in range(n):
            arr[i][j] = max(0, arr[i][j] - 1)
    for i in (0, -1):
        for j in range(m):
            arr[i][j] = max(0, arr[i][j] - 1)
    arr[0][0], arr[n - 1][0], arr[0][m - 1], arr[n - 1][m - 1] = a, b, c, d


def temperature_check(arr, research, k):
    for i in range(len(research)):
        r, c = research[i].r, research[i].c
        if arr[r][c] < k:
            return False
    return True


def solution():
    n, m, k = map(int, input1().split())
    arr = [list(map(int, input1().split())) for _ in range(n)]
    walls = [list(map(lambda x: int(x) - 1, input1().split())) for _ in range(int(input1()))]

    wall_arr = get_wall_arr(m, n, walls)

    research, warmers = get_warmers_and_research(arr, m, n)

    cmds: list[WarmerDirection] = [Up(arr), Right(arr), Down(arr), Left(arr)]

    cnt = 0
    while not temperature_check(arr, research, k) and cnt < 101:
        cnt += 1
        for warmer in warmers:
            blow(arr, wall_arr, warmer, cmds[warmer.d])
        arr = adjust(arr, wall_arr, n, m)
        cool_down(arr, n, m)
    print(cnt)


if __name__ == "__main__":
    solution()
