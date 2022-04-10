# pypy3 148ms
# 승객 하나하나 각각 다른 목적의 BFS 두개를 돌려야했으며, 남은 연료 처리가 상당히 까다로웠던 문제
# 어려웠던 점:
# 같은 거리의 모든 승객 중 행과 열이 가장 작은 승객이 BFS 위, 왼쪽, 오른쪽, 아래 돌면서 가장 먼저 만난 승객인 줄 알았는데 아니었음. (거리가 2일 때 좌하가 우우보다 먼저 탐색됨)
# 빈칸을 0으로 저장해뒀는데 좌표 0으로 가는 손님을 빈칸 취급해서 오래걸림

import sys
input = sys.stdin.readline

def main():

    N, M, fuel = map(int, input().split())
    L = N+1
    brd = [-1] * L*L # 벽은 -1로, 빈칸은 -2로 저장
    for y in range(0, N*L, L):
        brd[y:y+N] = map(lambda x: int(x)-2, input().split())
    dir = (-L, -1, 1, L)
    dst = -1    # dst는 승객을 찾은 경우엔 목적지 좌표 저장, 승객 목적지 도달시 -1로 초기화.
    ans = -1
    ty, tx = map(lambda x: int(x)-1, input().split())
    cque = [ty*L+tx]

    for _ in range(M):
        sy, sx, ey, ex = map(lambda x: int(x)-1, input().split())
        brd[sy*L+sx] = ey*L+ex
        
    # 지도 각 승객 위치에 목적지 좌표를 저장
    # 목적지 자체는 빈칸과 다름 없으므로 빈칸으로 저장
    # 빈칸은 원래 -2고 벽은 -1이지만 편의상 .과 /로 표현
    
    #   .  .  /  .  .  .  /
    #   . 33  /  .  .  .  /
    #   .  .  .  .  .  .  /
    #   . 18  .  .  .  .  /
    #   .  .  .  5  /  .  /
    #   .  .  .  /  .  .  / 
    #   /  /  /  /  /  /  /

    for _ in range(M):
        
        '''승객 찾기 페이즈'''
        vis = [0] * N*L
        mnm = len(brd)    # 같은 거리의 승객 중에서, 행과 열이 가장 작은 승객 == 좌표가 가장 작은 승객
        for fuel in range(fuel, 0, -1): # 연료 자동으로 갱신
            nque = []
            for cur in cque:
                if brd[cur] >= 0 and cur < mnm:
                    mnm = cur
                    dst = brd[mnm]      # 같은 거리의 모든 승객을 확인해야 하니, 찾자마자 break 걸면 안됨

                for d in dir:
                    if brd[cur+d] != -1 and not vis[cur+d]:
                        vis[cur+d] = 1
                        nque.append(cur+d)

            if dst != -1:
                brd[mnm] = -2
                cque = [mnm]
                break
            cque = nque
            
        if dst == -1: # 다음 승객을 못찾아 목적지 갱신이 안된 경우
            break

        '''목적지 찾기 페이즈'''
        vis = [0] * N*L
        for used in range(fuel+1):  # 다 쓴 경우에도 목적지를 찾으면 2배로 차니까 +1 해줌
            nque = []
            for cur in cque:
                if cur == dst:
                    cque = [dst]
                    dst = -1
                    break

                for d in dir:
                    if brd[cur+d] != -1 and not vis[cur+d]:
                        vis[cur+d] = 1
                        nque.append(cur+d)
            
            if dst == -1:
                fuel += used
                break
            cque = nque

        if dst != -1: # 목적지를 못찾아 -1로 초기화가 안된 경우
            break
        
    else: # for문 M번 다 돈 경우 == 모든 손님을 태운 경우
        ans = fuel

    print(ans)

  
if __name__ == "__main__":
    main()
