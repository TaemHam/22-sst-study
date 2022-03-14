from sys import stdin
from collections import deque

input1 = stdin.readline
directions = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
)


def is_in_range(n, a, b):
    return 0 <= a < n and 0 <= b < n


class Head:
    def __init__(self, r, c, idx):
        self.r, self.c = r, c
        self.idx = idx

    def set_pos(self, r, c):
        self.r, self.c = r, c

    def get_next_pos(self):
        a, b = directions[self.idx % 4]
        return self.r + a, self.c + b


def move_head(arr, head, x, y):
    result = True if arr[x][y] == -1 else False
    arr[x][y] = 1
    head.set_pos(x, y)
    return result


def move_until_next_t(arr, head: Head, current, t, snake):
    while current < t:
        x, y = head.get_next_pos()
        if not is_in_range(len(arr), x, y) or arr[x][y] == 1:
            return False, current
        is_apple = move_head(arr, head, x, y)
        snake.append((x, y))
        if not is_apple:
            del_x, del_y = snake.popleft()
            arr[del_x][del_y] = 0
        current += 1
    return True, current


def solution():
    n = int(input1())
    arr = [[0] * n for _ in range(n)]
    for _ in range(int(input1())):
        r, c = map(int, input1().split())
        arr[r - 1][c - 1] = -1

    current = 0
    head = Head(0, 0, 0)
    snake = deque([(0, 0)])
    success = True
    for _ in range(int(input1())):
        t, d = input1().split()
        t = int(t)
        success, current = move_until_next_t(arr, head, current, t, snake)
        if not success:
            break
        if d == 'L':
            head.idx -= 1
        else:
            head.idx += 1
    if success:
        success, current = move_until_next_t(arr, head, current, 10001, snake)
    print(current + 1)


if __name__ == "__main__":
    solution()
