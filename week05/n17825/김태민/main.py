#pypy3 140ms
# 각각의 말이 1~5칸을 이동해서 얻는 점수와 그 게임판의 현황을 따로따로 체크하며 푸는 백트래킹 문제
# 이지만 역시 BFS 처럼 풀었다.
# 조심해야 할 점은 여러 줄이 모이는 25~40점 칸에 하나의 말만 들어갈 수 있게 풀어야 하는 점.
# pop을 사용하기보다 cque, nque 를 사용했으면 좀 더 빨라지지 않을까 싶다.

import sys
input = sys.stdin.readline

def main():

    tbl = [[0, 
         2,  4,  6,  8, 10,
        12, 14, 16, 18, 20,
        22, 24, 26, 28, 30,
        32, 34, 36, 38, 40] + [0]*5,
        [10, 13, 16, 19, 25, 30, 35, 40] + [0]*5,
        [20, 22, 24, 25, 30, 35, 40] + [0]*5,
        [30, 28, 27, 26, 25, 30, 35, 40] + [0]*5]
    loc = [list(range(21)) + [99]*5,
        [5, 21, 22, 23, 24, 25, 26, 20] + [99]*5,
        [10, 27, 28, 24, 25, 26, 20] + [99]*5,
        [15, 29, 30, 31, 24, 25, 26, 20] + [99]*5]
    fnd = [
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (0, 6), (0, 7), (0, 8), (0, 9), (2, 0),
        (0, 11), (0, 12), (0, 13), (0, 14), (3, 0), (0, 16), (0, 17), (0, 18), (0, 19), (0, 20),
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3)]

    dgt = [1, 100, 10000, 1000000]

    nque = [(0, 0, 0)] # 점수, 말의 위치, 보드 현황 저장
    cque = []
    ans = (0, 0, 0)

    for mov in map(int, input().split()):

        nque, cque = cque, nque

        while cque:
            scr, tkn, brd = cque.pop()
            vis = set()
            for i in dgt:
                cur = tkn // i % 100
                if cur != 99 and cur not in vis:
                    vis.add(cur)
                    nxt = loc[fnd[cur][0]][fnd[cur][1] + mov]
                    if nxt != 99 and not brd & (1<<nxt):
                        nque.append((scr + tbl[fnd[nxt][0]][fnd[nxt][1]], tkn - cur*i + nxt*i, brd & ~(1<<cur) | (1<<nxt)))
                    elif nxt == 99:
                        nque.append((scr, tkn - cur*i + nxt*i, brd & ~(1<<cur)))

        ans = max(nque + [ans], key= lambda x: x[0])
    
    print(ans[0])


if __name__ == "__main__":
    main()
