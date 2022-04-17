#pypy3 152ms
# 원판 돌리기는 주사위 굴리는 것과 비슷했고, 인접 숫자 구하는 것도 어렵지 않았음.
# 특별히 사용한 알고리즘은 없음.
# 시간복잡도 = T<돌리기 횟수> * (N//X*M<돌려야 하는 원판의 숫자 갯수>) * (N*M * 2 <인접 숫자 확인> + N*M<평균화 필요시>)

import sys
input = sys.stdin.readline

def main():

    N, M, T = map(int, input().split())
    dir = ((1, 0), (0, 1)) # 오른쪽이랑 밑칸만 확인해도 모든 인접칸 확인 가능
    grp = []
    ttl = 0
    for i in range(N):
        grp.append(list(map(int, input().split())))
        ttl += sum(grp[i])
    cnt = N * M # 평균값을 구할 때, 남아있는 숫자 갯수를 빠르게 구하기 위해 사용

    for _ in range(T):
        
        X, D, K = map(int, input().split())
        stk = set() # 제거할 숫자 좌표 저장. 중복 없이 지우기 위해 set을 사용함.
        
        '''돌리기 페이즈'''
        for i in range(X-1, N, X): # 돌려야하는 원판의 인덱스
            if D:
                grp[i] = grp[i][K:] + grp[i][:K]
            else:
                grp[i] = grp[i][-K:] + grp[i][:-K]

        '''인접 숫자 확인 페이즈'''
        for y in range(N):
            for x in range(M):
                if grp[y][x]:
                    for dy, dx in dir:
                        ny = y + dy
                        nx = (x + dx) % M
                        if ny < N and grp[y][x] == grp[ny][nx]:
                            stk.add((y, x))
                            stk.add((ny, nx))
                            
        '''숫자 제거 혹은 평균화'''
        if stk: # 인접한 같은 숫자가 존재한다면:
            for y, x in stk:
                ttl -= grp[y][x]
                cnt -= 1
                grp[y][x] = 0
            if not cnt:
                break
                
        else:
            avg = ttl/cnt
            for y in range(N):
                for x in range(M):
                    if grp[y][x]:
                        if grp[y][x] < avg:
                            grp[y][x] += 1
                            ttl += 1
                        elif grp[y][x] > avg:
                            grp[y][x] -= 1
                            ttl -= 1
                            
    print(ttl)

if __name__ == "__main__":
    main()
