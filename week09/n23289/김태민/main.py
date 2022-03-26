import sys
input = sys.stdin.readline

def main():

    # 어려웠던 점:
    # 벽에 막혀 온도가 안올라가는 공간은 스킵하는 걸 구현해야 하는데, 체크해야 하는 벽 위치가 방향마다 달라져서
    # 그거 구현하는데만 절반 이상 시간이 소요된 것 같다. 

    # 바람 배열(wnd)을 만들어서 모든 온풍기 돌렸을 때 더해줘야하는 온도를 미리 저장시켜 놓고, 각 횟수마다 그것만 더해줌.
    # blw 배열은 각 방향마다 진행 방향, 대각선 이동 방향, 체크해야하는 가로 벽, 세로 벽 위치가 다 달라 따로 저장해 준 것임.
    N, M, K = map(int, input().split())
    L = M + 1
    ans = 101
    chk = []
    htr = []
    cnd = []
    wnd = [0] * N*L
    brd = [0] * N*L
    oob = [1] * N*L + [0] * L
    wll = [[0] * N*L for _ in range(2)]  # 입력 거꾸로 주의! 0에는 오른쪽 벽, 1에는 윗쪽 벽
    blw = ((), (1, L, 0, 0), (-1, L, 0, -1), (-L, -1, 1, 0), (L, -1, 1, L))

    for y in range(0, N*L, L):
        oob[y+M] = 0
        for x, e in enumerate(map(int, input().split())):
            if not e:
                continue
            elif e == 5:
                chk.append(y+x)
            else:
                htr.append((y+x, e))

    for _ in range(int(input().strip())):
        y, x, t = map(lambda x: int(x)-1, input().split())
        wll[t][y*L+x] = 1
    

    # 온풍기 진행 칸 수마다 온도 낮추고, 벽에 막힌 곳은 진행하면 안되기 때문에 BFS로 큐를 관리해서 구현
    for loc, dir in htr:
        
        fwd, sde, flg, fix = blw[dir]
        vis = [0] * N*L
        wnd[loc+fwd] += 5
        cque = [loc+fwd]
        nque = []

        for heat in range(4, 0, -1):
            
            for cur in cque:
                
                if oob[cur+fwd-sde] and not wll[flg][cur-sde+fix] | wll[1-flg][cur] and not vis[cur+fwd-sde]:
                    wnd[cur+fwd-sde] += heat
                    vis[cur+fwd-sde] = 1
                    nque.append(cur+fwd-sde)

                if oob[cur+fwd] and not wll[flg][cur+fix] and not vis[cur+fwd]:
                    wnd[cur+fwd] += heat
                    vis[cur+fwd] = 1
                    nque.append(cur+fwd)

                if oob[cur+fwd+sde] and not wll[flg][cur+sde+fix] | wll[1-flg][cur+sde] and not vis[cur+fwd+sde]:
                    wnd[cur+fwd+sde] += heat
                    vis[cur+fwd+sde] = 1
                    nque.append(cur+fwd+sde)

            if not nque:
                break
            cque, nque = nque, []
    
    # wnd 배열에는 온도가 있는 칸보다 없는 칸이 많으므로 다 더해주는 건 연산 낭비, 온도가 있는 인덱스만 cnd에 따로 저장해줌
    for i in range(N*L):
        if wnd[i]:
            cnd.append(i)
 
    for choco in range(1, 101):
        
        '''온풍기 바람 페이즈'''
        for i in cnd:
            brd[i] += wnd[i]

        '''온도 조절 페이즈'''
        dif = [0] * N*L
        # 가로끼리 우측칸 비교
        for y in range(0, N*L, L):
            for xy in range(y, y+M-1):
                if not wll[0][xy] and abs(brd[xy] - brd[xy+1]) >= 4:
                    if brd[xy] > brd[xy+1]:
                        dif[xy] -= (brd[xy] - brd[xy+1])//4
                        dif[xy+1] += (brd[xy] - brd[xy+1])//4
                    else:
                        dif[xy] += (brd[xy+1] - brd[xy])//4
                        dif[xy+1] -= (brd[xy+1] - brd[xy])//4
        # 세로끼리 윗칸 비교 (벽 정보가 윗벽으로 주어지기 때문)
        for y in range(N*L-L, 0, -L):
            for xy in range(y, y+M):
                if not wll[1][xy] and abs(brd[xy] - brd[xy-L]) >= 4:
                    if brd[xy] > brd[xy-L]:
                        dif[xy] -= abs(brd[xy] - brd[xy-L])//4
                        dif[xy-L] += abs(brd[xy] - brd[xy-L])//4
                    else:
                        dif[xy] += abs(brd[xy] - brd[xy-L])//4
                        dif[xy-L] -= abs(brd[xy] - brd[xy-L])//4
        for i in range(len(dif)):
            brd[i] += dif[i]
        
        '''바깥 온도 페이즈'''
        for x in range(1, M-1):
            if brd[x]:
                brd[x] -= 1
            if brd[N*L-L+x]:
                brd[N*L-L+x] -= 1
        for y in range(0, N*L, L):
            if brd[y]:
                brd[y] -= 1
            if brd[M-1+y]:
                brd[M-1+y] -= 1
        
        '''온도 체크 페이즈'''
        for i in chk:
            if brd[i] < K:
                break
        else:
            ans = choco
            break
        
    print(ans)

if __name__ == "__main__":
    main()
