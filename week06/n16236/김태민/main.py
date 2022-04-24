# pypy3 116ms
# 인구이동에서 배운 것처럼, 방문 배열에 시뮬레이션 횟수로 기록해 풀었음.

import sys
input = sys.stdin.readline

def main():

    N = int(input().strip())
    L = N+1
    MAX = N*L
    mov = (1, -1, L, -L)
    vis = [0] * MAX + [1000] * L
    brd = [0] * MAX
    ans = 0
    stm = 0
    siz = 2
    for y in range(0, MAX, L):
        vis[y+N] = 1000
        brd[y:y+N] = map(int, input().split())
    loc = brd.index(9)
    cque = [loc]
    brd[loc] = 0

    for v in range(1, MAX):

        eat = MAX # 먹을 물고기 좌표가 제일 작은 놈을 먹으면 됨
        for sec in range(1, MAX//2):
            nque = []
            for cur in cque:
                for d in mov:
                    if vis[cur+d] < v and brd[cur+d] <= siz:  # 격자 바깥은 방문 배열에 1000이 저장되어 있어 걸러짐
                        if 0 < brd[cur+d] < siz:
                            eat = min(eat, cur+d)
                        else:
                            vis[cur+d] = v
                            nque.append(cur+d)
            if eat != MAX:
                break
            cque = nque
        
        if eat == MAX:
            break
        
        cque = [eat]
        ans += sec
        brd[eat] = 0
        stm += 1
        if stm == siz:
            stm = 0
            siz += 1

    print(ans)
    
if __name__ == "__main__":
    main()
