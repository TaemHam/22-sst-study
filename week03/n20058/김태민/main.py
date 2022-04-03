import sys
input = sys.stdin.readline

def main():
    #좌표 4개를 넣으면 시계방향으로 스왑해주는 함수
    def rotate(a, b, c, d):
        brd[a], brd[b], brd[c], brd[d] = brd[d], brd[a], brd[b], brd[c]
    
    N, _ = map(int, input().split())
    N = 2**N
    M = N+1
    dir = [1, -1, M, -M]
    brd = [0] * M*M
    for y in range(0, N*M, M):
        brd[y:y+N] = map(int, input().split())
    
    for L in map(int, input().split()):

        '''돌리기 페이즈'''
        if L:
            for y in range(0, N*M, M*2**L):
                for xy in range(y, y+N, 2**L):
                    for lvl in range(2**(L-1)):
                        k = 2**L-1-2*lvl  # k는 네 좌표의 간격
                        s = xy+(M+1)*lvl  # s는 왼쪽 위 좌표
                        for dst in range(k):  # 왼쪽 위는 오른쪽으로, 오른쪽 위는 밑으로 등
                            rotate(s + dst, s+k + dst*M, s+k+k*M - dst, s+k*M - dst*M)

        '''녹이기 페이즈'''
        mlt = []
        for y in range(0, N*M, M):
            for xy in range(y, y+N):
                if not brd[xy]:
                    continue
                cnt = 0
                for d in dir:
                    if brd[xy+d]:
                        cnt += 1
                if cnt < 3:
                    mlt.append(xy)
        for xy in mlt:
            brd[xy] -= 1
    
    cnt = 0
    vis = [0] * N*M
    for y in range(0, N*M, M):
        for xy in range(y, y+N):
            if brd[xy] and not vis[xy]:
                vis[xy] = 1
                que = [xy]
                for crd in que:
                    for d in dir:
                        if brd[crd+d] and not vis[crd+d]:
                            vis[crd+d] = 1
                            que.append(crd+d)
                cnt = max(cnt, len(que))

    print(str(sum(brd)) + '\n' + str(cnt))
    
if __name__ == "__main__":
    main()
