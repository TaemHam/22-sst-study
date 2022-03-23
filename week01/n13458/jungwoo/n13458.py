import math
from sys import stdin

input1 = stdin.readline


def solution():
    input1()
    a = list(map(int, input1().split()))
    b, c = map(int, input1().split())

    answer = len(a)
    for i in range(len(a)):
        a[i] -= b
        if a[i] > 0:
            answer += math.ceil(a[i] / c)
    print(answer)


if __name__ == "__main__":
    solution()
