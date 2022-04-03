import sys
input = sys.stdin.readline

def main():
    # 어려웠던 점:
    # 학생 앉히는 조건 2, "1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다." 에서
    # "인접한 칸 중에서" 때문에 학생이 앉아있으면 그 인접한 칸들 중에서만 앉힐 수 있는 줄 알아서 왜 틀렸는지 찾는데 한참 걸렸다.
    
    N = int(input().strip())
    L = N+1
    chk = set(xy for y in range(0, L*N, L) for xy in range(y, y+N)) # 빈자리 셋
    scr = (0, 1, 10, 100, 1000)   # 좋아하는 학생 수를 인덱스로 한 점수 조회 배열
    ans = 0
    emp = [4] * L*L               # 각각의 자리에 인접한 자리 중 빈 자리의 갯수를 저장해 놓는 배열
    fnd = [0] * (N*N+1)           # 좋아하는 학생 배열 저장용 배열
    sit = [-1] * (N*N+1)          # 특정 학생이 앉는 좌표를 저장해 놓는 배열 <- 학생 앉힐 때마다 좋아하는 학생이 앉아있는지, 앉아있다면 어디에 앉아있는지 조회하기 위해 사용
    dir = (-1, 1, -L, L)
    cls = [0] * L*N + [-1] * N
    for i in range(N):
        cls[i*L+N] = -1
        emp[i] -= 1               # 바깥쪽 행들과 열들에 빈자리 갯수 1개씩 빼줌
        emp[i+L*(N-1)] -= 1
        emp[i*L] -= 1
        emp[i*L+N-1] -= 1
    # 첫 학생은 무조건 1행1열에 앉는다.
    stdt, *frnd = map(int, input().split())
    fnd[stdt] = set(frnd)
    chk.discard(L+1)
    cls[L+1] = stdt
    sit[stdt] = L+1
    for d in dir:
        emp[L+1+d] -= 1

    for _ in range(1, N*N):
        stdt, *frnd = map(int, input().split())
        fnd[stdt] = set(frnd)
        
        # 교실 각 칸을 0점으로 초기화 해 준 배열을 만들고, 
        # 좋아하는 학생 앉아있는 자리의 옆 자리들에 점수 1씩 부여,
        # 높은 점수를 가진 자리들 좌표만 cnd에 저장해 줌 
        fav = [0] * L*N
        cnd = []
        cur = 0
        for f in frnd:
            if sit[f] != -1:
                for d in dir:
                    if not cls[sit[f]+d]:
                        fav[sit[f]+d] += 1
                        if fav[sit[f]+d] > cur:
                            cur = fav[sit[f]+d]
                            cnd = [sit[f]+d]
                        elif fav[sit[f]+d] == cur:
                            cnd.append(sit[f]+d)
        # cnd 배열에 하나라도 있으면 조건에 따라 뽑아주고, 없으면 빈자리 셋(chk)중에서 인접한 빈자리 수 많은 자리 좌표 뽑아줌 
        if cnd:
            seat = max(cnd, key= lambda x: (emp[x], -x))
        else:
            seat = max(chk, key= lambda x: emp[x])

        chk.discard(seat)
        cls[seat] = stdt
        sit[stdt] = seat
        for d in dir:
            emp[seat+d] -= 1
    
    # 각 학생마다 인접한 자리에 앉은 학생들의 셋, 좋아하는 학생들의 셋, 이 두 셋의 교집합의 길이를 구해 점수를 더해줌 
    for stdt in range(1, len(sit)):
        ans += scr[len(set(cls[sit[stdt]+d] for d in dir) & fnd[stdt])]
    
    print(ans)
    
if __name__ == "__main__":
    main()
