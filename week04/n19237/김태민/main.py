# pypy3 176ms
# 처리해야할 정보가 많지만 시뮬레이션 자체는 간단한 문제

import sys
input = sys.stdin.readline

def main():
    
    N, M, K = map(int, input().split())
    L = N+1
    M += 1
    mov = (-L, L, -1, 1)
    pri = [[] for _ in range(M)]  # 상어 방향 우선순위 저장
    rmn = set(range(1, M))        # 청소년 상어때처럼 남아있는 상어 번호 저장
    loc = [0] * M                 # 각 상어의 위치
    brd = [0] * N*L               # 격자 현황
    odr = [0] * N*L + [-1] * L    # 남아있는 냄새 지속 시간
    who = [0] * L*L               # 냄새가 누구 냄새인지 저장
    ans = -1
    for y in range(0, N*L, L):
        odr[y+N] = -1
        brd[y:y+N] = map(int, input().split())
        for xy in range(y, y+N):
            if brd[xy]:
                loc[brd[xy]] = xy
                odr[xy] = K
                who[xy] = brd[xy]
                
    # 이 문제의 상어들은 상어 자체를 보고 움직이지 않고, 냄새를 보고 움직이므로 
    # odr 배열의 바깥칸을 -1로, 빈칸은 0으로, 그리고 나머지는 냄새가 앞으로 남아있을 수 있는 턴수로 저장
    #  0  0  0  0  4 -1    0  0  0  0  3 -1  |  0  0  0  4  3 -1    0  0  0  3  3 -1  
    #  0  4  0  0  0 -1    0  2  0  0  0 -1  |  0  3  4  0  0 -1    0  2  2  0  0 -1  
    #  4  0  0  0  4 -1    1  0  0  0  4 -1  |  3  4  0  4  3 -1    1  1  0  4  4 -1   
    #  0  0  0  0  0 -1    0  0  0  0  0 -1  |  0  0  0  0  0 -1    0  0  0  0  0 -1  
    #  0  0  0  0  0 -1    0  0  0  0  0 -1  |  0  0  0  0  0 -1    0  0  0  0  0 -1   
    # -1 -1 -1 -1 -1 -1   -1 -1 -1 -1 -1 -1  | -1 -1 -1 -1 -1 -1   -1 -1 -1 -1 -1 -1   
    #    0턴 odr 배열         0턴 who 배열    |    1턴 odr 배열         1턴 who 배열
    
    dir = [0] + list(map(lambda x: int(x)-1, input().split()))
    for i in range(1, M):
        for _ in range(4):
            pri[i].append(tuple(map(lambda x: int(x)-1, input().split())))

    for time in range(1, 1001):

        '''이동 페이즈'''
        for shk in rmn:
            brd[loc[shk]] = 0   # 격자는 일단 0으로 비워주고, 도망 페이즈 때 위치 적용할 예정.
            cnd = ()

            for i in range(4):
                nd = pri[shk][dir[shk]][i]
                nxt = loc[shk] + mov[nd]
                if not odr[nxt]:                    # odr에 냄새가 없다면
                    cnd = (nxt, nd)
                    break
                elif who[nxt] == shk and not cnd:   # odr에 냄새는 있지만 자기 냄새이고, 처음 자기 냄새가 있는 칸이 확인됐다면
                    cnd = (nxt, nd)
            
            loc[shk], dir[shk] = cnd

        '''냄새 페이즈'''
        for y in range(0, N*L, L):      # 냄새가 있는 칸을 1턴씩 지워줌
            for xy in range(y, y+N):    # 1턴 남아 있던 냄새는 자동으로 0이 되어 빈칸 처리 됨
                if odr[xy]:
                    odr[xy] -= 1

        '''도망 페이즈'''
        run = set()
        for shk in rmn:         # 낮은 번호 순서로 차례로 돌면서
            cur = loc[shk]
            if not brd[cur]:    # 위치에 상어가 없다면
                brd[cur] = shk
                who[cur] = shk
                odr[cur] = K
            else:
                run.add(shk)    # 위치에 상어가 있다 => 자신이 무조건 높은 번호 상어
        rmn -= run

        '''정답 체크 페이즈'''
        if len(rmn) == 1:       # 남은 상어가 1마리면 무조건 1만 남은거
            ans = time
            break
    
    print(ans)
  
if __name__ == "__main__":
    main()
