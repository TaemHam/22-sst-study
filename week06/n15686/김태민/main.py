# pypy3 144ms
# 조합 함수를 직접 만들어 쓰는 것보다 itertools 가 훨씬 빨랐다.
# 코드가 조금 길어지더라도 리스트 컴프리헨션을 사용하는 것보다 따로 포문을 돌려 돌리는 게 좀 더 빠르다는 걸 배웠다.

import sys
from itertools import combinations
input = sys.stdin.readline

def main():

    N, M = map(int, input().split())
    jip, chi = [], []
    ans = int(1e9)
    for y in range(N):
        brd = input().split()
        for x in range(N):
            if brd[x] == '1':
                jip.append((y, x))
            elif brd[x] == '2':
                chi.append((y, x))
                
    # 모든 집에서부터 모든 치킨집까지의 거리를 저장
    grp = []
    for i in range(len(jip)):
        tmp = []
        for j in range(len(chi)):
            tmp.append(abs(jip[i][0] - chi[j][0]) + abs(jip[i][1] - chi[j][1]))
        grp.append(tmp)
    
    # 살아남는 치킨집들의 조합을 구한 후, 모든 집과 치킨 집 중에서의 최솟값을 모두 더해 치킨거리를 구함
    for arr in combinations(range(len(chi)), M):
        res = 0
        for e in grp:
            mnm = int(1e9)
            for k in arr:
                mnm = min(mnm, e[k])
            res += mnm
        ans = min(ans, res)

    print(ans)

if __name__ == "__main__":
    main()
