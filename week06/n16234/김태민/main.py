# pypy3 160ms
# 그래프 탐색을 여러번 돌려야 하는 경우, 방문 배열을 계속 0으로 초기화하는 것보다, 방문 배열에 탐색 돌린 횟수를 저장해,
# 숫자가 같으면 continue, 그보다 적으면 탐색해주는 방법이 빠르다는 것을 배움.
# 문제 조건의 L이 1보다 크거나 같아, 이미 인구가 같아진 상태에서는 바로 다음날 같은 국경이 다시 열릴 수 없으므로,
# 모든 국가에서 BFS를 돌리는 것이 아닌, cque, nque 그리고 세 번째 que까지 만들어, 
# 어느쪽으로든 국경이 열리지 않았다면(que의 길이가 1이 넘지 않는다면) nque에 넘기지 않음.
# 예) 2 2 2 10 -> 2 2 6 6 -> 2 4 4 6 -> 3 3 5 5 ...

import sys
input = sys.stdin.readline

def main():

    N, L, R = map(int, input().split())
    K = N+1
    mov = (1, -1, K, -K)
    ans = 2000
    brd = [-1] * N*K
    vis = [-1] * N*K + [2000] * K
    cque = [xy for y in range(0, N*K, K) for xy in range(y, y+N)]

    for y in range(0, N*K, K):
        vis[y+N] = 2000
        brd[y:y+N] = map(int, input().split())
    
    for time in range(2000):

        nque = []
        for xy in cque:
            if vis[xy] == time:
                continue
            vis[xy] = time
            ttl = brd[xy]
            que = [xy]

            for crd in que:
                for d in mov:
                    if vis[crd+d] < time and L <= abs(brd[crd] - brd[crd+d]) <= R:
                        vis[crd+d] = time
                        ttl += brd[crd+d]
                        que.append(crd+d)
            
            if len(que) > 1:
                nque.extend(que)
                ttl //= len(que)
                for crd in que:
                    brd[crd] = ttl
        
        if not nque:
            ans = time
            break

        cque = nque
    
    print(ans)

if __name__ == "__main__":
    main()
