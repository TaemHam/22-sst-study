import copy
from sys import stdin

input1 = stdin.readline
sd = (
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
    (0, 1),  # 우
)
fd = (
    (0, -1),  # 좌
    (-1, -1),  # 좌상
    (-1, 0),  # 상
    (-1, 1),  # 상우
    (0, 1),  # 우
    (1, 1),  # 우하
    (1, 0),  # 하
    (1, -1),  # 하좌
)


def is_in_range(n, m, a, b):
    return 0 <= a < n and 0 <= b < m


class Animal:
    def __init__(self, arr: list[list[list[int]]], r, c, d):
        self.arr, self.r, self.c, self.d = arr, r, c, d

    def __repr__(self):
        return f'({self.__class__.__name__} {self.r} {self.c} {self.d})'

    def move_position(self, typ, nr, nc, nd):
        self.arr[nr][nc][typ] = self.arr[self.r][self.c][typ]
        self.arr[self.r][self.c][typ] = 0
        self.r, self.c, self.d = nr, nc, nd


class Shark(Animal):
    def __init__(self, arr, r, c, d):
        self.candidate_roots = init_shark_root()
        super().__init__(arr, r, c, d)

    def move(self):
        maximum_value, maximum_idx, first = 0, 0, True
        for i in range(len(self.candidate_roots)):
            r, c = self.r, self.c
            cnt, visit = 0, set()
            for d in self.candidate_roots[i]:
                x, y = r + sd[d][0], c + sd[d][1]
                new_pos = f'{x}-{y}'
                if not is_in_range(4, 4, x, y):
                    break
                if new_pos not in visit:
                    cnt += sum(self.arr[x][y][:8])
                r, c = x, y
                visit.add(new_pos)
            else:
                if maximum_value < cnt or first:
                    first = False
                    maximum_value, maximum_idx = cnt, i

        x, y = 0, 0
        r, c = self.r, self.c
        for d in self.candidate_roots[maximum_idx]:
            x, y = r + sd[d][0], c + sd[d][1]
            for i in range(8):
                self.arr[x][y][8] += self.arr[x][y][i]
                self.arr[x][y][i] = 0
            r, c = x, y
        self.move_position(10, x, y, -1)


def init_shark_root():
    roots = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                roots.append((i, j, k))
    return roots


def move_fishes(arr):
    def _can_move(x, y):
        if arr[x][y][8] or arr[x][y][9] or arr[x][y][10]:
            return False
        else:
            return True

    def _move():
        for _i in range(8):
            new_d = (k - _i) % 8
            x, y = i + fd[new_d][0], j + fd[new_d][1]
            if is_in_range(4, 4, x, y) and _can_move(x, y):
                new_arr[x][y][new_d] += arr[i][j][k]
                new_arr[i][j][k] -= arr[i][j][k]
                break

    new_arr = copy.deepcopy(arr)
    for i in range(4):
        for j in range(4):
            for k in range(8):
                if arr[i][j][k] > 0:
                    _move()
    return new_arr


def remove_fish_smell(arr):
    for i in range(4):
        for j in range(4):
            arr[i][j][9] = 0
            arr[i][j][9] = arr[i][j][8]
            arr[i][j][8] = 0


def fish_copy(arr, old_arr):
    for i in range(4):
        for j in range(4):
            for k in range(8):
                arr[i][j][k] += old_arr[i][j][k]


def count_fishes(arr):
    result = 0
    for i in range(4):
        for j in range(4):
            result += sum(arr[i][j][:8])
    return result


def solution():
    m, s = map(int, input1().split())
    arr: list[list[list[int]]] = [[[0] * 11 for _ in range(4)] for _ in range(4)]  # 0~7: fish that has each direction. 8,9: fish smell. 10: shark.
    for _ in range(m):
        x, y, d = map(lambda _x: int(_x) - 1, input1().split())
        arr[x][y][d] += 1
    x, y = map(lambda _x: int(_x) - 1, input1().split())
    shark = Shark(arr, x, y, 0)
    arr[x][y][10] = 1

    for _ in range(s):
        # 1. 복제 마법 시전
        old_arr = copy.deepcopy(arr)

        # 2. 물고기 이동
        arr = move_fishes(arr)

        # 4. 두 번 전 연습의 물고기 흔적 사라짐
        remove_fish_smell(arr)

        # 3. 상어 이동
        shark.arr = arr
        shark.move()

        # 5. 복제 마법 완료
        fish_copy(arr, old_arr)
    print(count_fishes(arr))


if __name__ == "__main__":
    solution()
