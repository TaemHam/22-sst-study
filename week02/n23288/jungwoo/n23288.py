from sys import stdin

input1 = stdin.readline
directions = (
    (0, 1),  # 우
    (1, 0),  # 하
    (0, -1),  # 좌
    (-1, 0),  # 상
)


def is_in_range(n, m, a, b):
    return 0 <= a < n and 0 <= b < m


class Dice:
    def __init__(self, arr, score_dp, bottom, top, right, left, front, back):
        self.arr, self.score_dp, self.n, self.m, self.r, self.c, self.d, self.score = arr, score_dp, len(arr), len(arr[0]), 0, 0, 0, 0
        self.bottom, self.top, self.right, self.left, self.front, self.back = bottom, top, right, left, front, back

    def _move(self):
        if self.d % 4 == 0:
            self._to_east()
        elif self.d % 4 == 1:
            self._to_south()
        elif self.d % 4 == 2:
            self._to_west()
        else:
            self._to_north()

    def _to_east(self):
        self.right, self.bottom, self.left, self.top = self.top, self.right, self.bottom, self.left

    def _to_west(self):
        self.right, self.bottom, self.left, self.top = self.bottom, self.left, self.top, self.right

    def _to_north(self):
        self.front, self.bottom, self.back, self.top = self.top, self.front, self.bottom, self.back

    def _to_south(self):
        self.front, self.bottom, self.back, self.top = self.bottom, self.back, self.top, self.front

    def go_to_next_pos(self):
        def get_next_pos():
            return self.r + directions[self.d % 4][0], self.c + directions[self.d % 4][1]
        r, c = get_next_pos()
        if not is_in_range(self.n, self.m, r, c):
            self.d += 2
            r, c = get_next_pos()
        self.r, self.c = r, c
        self._move()

    def change_direction(self):
        if self.bottom > self.arr[self.r][self.c]:
            self.d += 1
        elif self.bottom < self.arr[self.r][self.c]:
            self.d -= 1

    def calculate_score(self):
        self.score += self.arr[self.r][self.c] * self.score_dp[self.r][self.c]


def calculate_pre_score(arr, n, m):
    class Cnt:
        def __init__(self):
            self.cnt = 1

    def loop(_r, _c, _cnt):
        for i in range(4):
            a, b = directions[i]
            nr, nc = _r + a, _c + b
            if is_in_range(n, m, nr, nc) and arr[nr][nc] == target and not visit[nr][nc]:
                positions.append((nr, nc))
                visit[nr][nc] = True
                _cnt.cnt += 1
                loop(nr, nc, _cnt)

    dp = [[0] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if visit[r][c]:
                continue
            cnt = Cnt()
            target = arr[r][c]
            visit[r][c] = True
            positions = [(r, c)]
            loop(r, c, cnt)
            for x, y in positions:
                dp[x][y] = cnt.cnt
    return dp


def solution():
    n, m, k = map(int, input1().split())
    arr = [list(map(int, input1().split())) for _ in range(n)]

    score = calculate_pre_score(arr, n, m)
    dice = Dice(arr, score, 6, 1, 3, 4, 2, 5)
    for _ in range(k):
        dice.go_to_next_pos()
        dice.calculate_score()
        dice.change_direction()
    print(dice.score)


if __name__ == "__main__":
    solution()
