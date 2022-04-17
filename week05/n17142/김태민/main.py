# pypy3 156ms
# 처음에는 브루트포스로 해야할 생각 못해서 시간 꽤 잡아먹은 

import sys
input = sys.stdin.readline

def main():
    
    def comb(arr, cnt):
        if cnt == 1:
            for i in range(len(arr)):
                yield [arr[i]]
        else:
            for i in range(len(arr)):
                for nxt in comb(arr[i+1:], cnt-1):
                    yield [arr[i]] + nxt
    
    def atw(x):
        wll[x] = 1

    N, M = map(int, input().split())
    L = N+1
    mov = (1, -1, L, -L)
    vir = []
    wll = [0] * N*L + [1] * L
    air = set()
    fnc = (air.add, atw, vir.append)

    for y in range(0, N*L, L):
        wll[y+N] = 1
        for x, e in enumerate(map(int, input().split())):
            fnc[e](y+x)

    if air:
        ans = 2500
        for cque in comb(vir, M):

            vis = wll[:]
            for cur in cque:
                vis[cur] = 1
            cnt = len(air)

            for time in range(1, 2500):
                nque = []

                for cur in cque:

                    for d in mov:

                        if not vis[cur+d]:
                            vis[cur+d] = 1
                            nque.append(cur+d)

                            if cur+d in air:
                                cnt -= 1
                                if not cnt:
                                    ans = min(ans, time)
                                    nque = []
                                    cque.clear()
                                    break
                                
                if not nque:
                    break
                cque = nque
    else:
        ans = 0

    print(-1 if ans == 2500 else ans)

if __name__ == "__main__":
    main()
