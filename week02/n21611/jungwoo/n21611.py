from sys import stdin

input1 = stdin.readline
directions = (
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
    (0, 1),  # 우
)


def is_in_range(n, a, b):
    return 0 <= a < n and 0 <= b < n


def change_direction(d):
    if d == 1:
        return 3
    elif d == 2:
        return 1
    elif d == 3:
        return 0
    else:
        return 2


class Magic:
    def __init__(self, d, s):
        self.d, self.s = change_direction(d), s


class Shark:
    def __init__(self, r, c):
        self.r, self.c = r, c


class BallInfo:
    def __init__(self, start, type, cnt):
        self.start, self.type, self.cnt, = start, type, cnt

    def set_current(self, start, type, cnt):
        self.start, self.type, self.cnt = start, type, cnt

    def __repr__(self):
        return str(self.__dict__)


def get_next_pos(r, c, d):
    return r + directions[d][0], c + directions[d][1]


def make_arr(shark, _arr):
    total_len = len(_arr) * len(_arr)
    arr = [-1]
    visit = [[False] * len(_arr) for _ in range(len(_arr))]
    visit[shark.r][shark.c] = True
    r, c, d = shark.r, shark.c, 0
    while True:
        left_nr, left_nc = get_next_pos(r, c, (d + 1) % 4)
        nr, nc = get_next_pos(r, c, d % 4)
        if is_in_range(len(_arr), left_nr, left_nc) and not visit[left_nr][left_nc]:  # 좌회전 가능시
            nr, nc, d = left_nr, left_nc, d + 1
        if not is_in_range(len(_arr), nr, nc):  # 범위 넘어가면 종료
            break
        if _arr[nr][nc] == 0:  # 다음 칸이 0이면 더 이상 진행할 필요 없음
            arr += [0] * (total_len - len(arr))
            break
        visit[nr][nc] = True
        arr.append(_arr[nr][nc])
        r, c = nr, nc
    return arr


def move_balls(arr):
    new_arr = [0] * len(arr)
    new_arr_idx = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            new_arr[new_arr_idx] = arr[i]
            new_arr_idx += 1
    return new_arr


def step1(arr, magic):
    first_idx = 2 * magic.d + 1
    idx = first_idx
    gap = first_idx + 8
    cnt = 0
    while idx < len(arr) and cnt < magic.s:
        arr[idx] = 0
        idx += gap
        gap += 8
        cnt += 1
    return move_balls(arr)


def step2(arr):
    def _blow_balls():
        for j in range(ball_info.start, i):
            arr[j] = 0
        return (i - ball_info.start) * ball_info.type

    result = False
    ball_info = BallInfo(1, arr[1], 1)
    blow_score = 0
    for i in range(2, len(arr)):
        if arr[i] == ball_info.type:
            ball_info.cnt += 1
        else:  # 이전 구슬이랑 같이 않으면
            if ball_info.cnt >= 4:  # 구슬 그룹의 수가 4개 이상일 경우 제거
                blow_score += _blow_balls()
                result = True
            ball_info.set_current(i, arr[i], 1)
    if result:
        arr = move_balls(arr)
    return result, arr, blow_score


def step3(arr):
    new_arr = [-1]
    ball_info = BallInfo(1, arr[1], 1)
    for i in range(2, len(arr)):
        if arr[i] == ball_info.type:
            ball_info.cnt += 1
        else:
            new_arr += [ball_info.cnt, ball_info.type]
            if len(new_arr) > len(arr):
                new_arr = new_arr[:-(len(new_arr) - len(arr))]
                break
            ball_info.type, ball_info.cnt = arr[i], 1
    if len(new_arr) < len(arr):
        new_arr += [0] * (len(arr) - len(new_arr))
    return new_arr


def solution():
    n, m = map(int, input1().split())
    shark = Shark(n // 2, n // 2)
    _arr = [list(map(int, input1().split())) for _ in range(n)]
    arr = make_arr(shark, _arr)
    magics: list[Magic] = [Magic(*map(int, input1().split())) for _ in range(m)]

    ball_score = 0
    for magic in magics:
        arr = step1(arr, magic)
        blow = True
        while blow:
            blow, arr, _score = step2(arr)
            ball_score += _score
        arr = step3(arr)
    print(ball_score)


if __name__ == "__main__":
    solution()
