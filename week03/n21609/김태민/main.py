import sys
input = sys.stdin.readline

def main():

    def rotate(a, b, c, d):
        brd[a], brd[b], brd[c], brd[d] = brd[b], brd[c], brd[d], brd[a]

    N, _ = map(int, input().split())
    L = N+1
    ans = 0
    dir = (L, -1, -L, 1)
    brd = [-1] * L*L
    for y in range(0, N*L, L):
        brd[y:y+N] = map(int, input().split())
    
    for _ in range(200):
        # boom 에는 블럭 그룹 좌표배열, 무지개 블럭 갯수 저장 하고, 저장된 수보다 큰게 나오면 갱신
        boom = ([0], 0)
        vis = [0] * L*L
        for y in range(0, N*L, L):
            for xy in range(y, y+N):
                if brd[xy] > 0 and not vis[xy]:
                    vis[xy] = 1
                    que = [xy]
                    rnb = []
                    for cur in que:
                        for d in dir:
                            if (brd[cur+d] == brd[xy] or brd[cur+d] == 0) and not vis[cur+d]:
                                if brd[cur+d] == 0:
                                    rnb.append(cur+d)
                                que.append(cur+d)
                                vis[cur+d] = 1
                    # max 의 키로 람다를 사용해서 블럭 그룹 갯수, 무지개 블럭 갯수, 기준 블럭 좌표 순서로 비교해 정해줌
                    boom = max(boom, (que, len(rnb)) , key= lambda x: (len(x[0]), x[1], x[0][0]))
                    # 무지개 블럭 방문 여부 리셋
                    for loc in rnb:
                        vis[loc] = 0
        # 찾은 블럭 그룹 갯수가 2 이상이면, 블럭 그룹 블럭 위치에 공백(-2)를 넣어주고, 
        if len(boom[0]) >= 2:
            ans += len(boom[0]) ** 2
            for loc in boom[0]:
                brd[loc] = -2
        else:
            break
            
        # 각 열 밑칸부터 돌면서 블럭이 나오면 포인터(cur) 위치와 스왑해주고 포인터 위치 올리고, 빈공간이 나오면 포인터 그대로 두고 하는 방식으로 중력 적용
        for x in range(N*L-L, N*L):
            cur = x
            for nxt in range(x, -1, -L):
                if brd[nxt] == -2:
                    continue
                elif brd[nxt] == -1:
                    cur = nxt - L
                else:
                    brd[cur], brd[nxt] = brd[nxt], brd[cur]
                    cur -= L
                    
        # 토네이도와 같은 방식의 로테이션
        for lvl in range(L//2):
            xy = lvl*L + lvl
            k = N-lvl*2-lvl
            lt, rt, rb, lb = xy, xy+k, xy+k*L+k, xy+k*L
            for dst in range(k):
                rotate(dst+lt, dst*L+rt, -dst+rb, -dst*L+lb)
                
        # 위와 같은 중력 적용
        for x in range(N*L-L, N*L):
            cur = x
            for nxt in range(x, -1, -L):
                if brd[nxt] == -2:
                    continue
                elif brd[nxt] == -1:
                    cur = nxt - L
                else:
                    brd[cur], brd[nxt] = brd[nxt], brd[cur]
                    cur -= L
    
    print(ans)
    
if __name__ == "__main__":
    main()
