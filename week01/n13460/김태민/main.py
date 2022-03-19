import sys
input = sys.stdin.readline
def main():
    
    # 접근 방법:
    #   1. 게임판을 스캔하면서, 구슬 좌표를 네자리 숫자로(0123 이면 파랑이 0열 1행, 빨강이 2열 3행), 구멍 좌표도 두자리 숫자로 저장
    #   2. mov 배열에는 각 방향으로 기울이면 어느 위치에 멈추는지 저장 (#...# 에서 오른쪽으로 기울이는 경우는 02100)
    #   3. 방문 배열(vis)은 구슬 좌표 0000~9999까지 커버하기 위해 10000개까지 설정 하고 bfs 실행(cque, nque 배열 이용)
    #   4. 한 방향으로 기울였을 때 구슬이 겹치면, 두 구슬의 원래 위치를 비교해 바깥쪽에 있던(check 함수) 구슬을 뒤로 밀어줌
    #   5. 구슬이 구멍에 빠지는 경우는, 구멍을 초록 구슬이라고 가정했을 때, 한쪽으로 기울여서 빨강, 혹은 파랑 구슬이 초록 구슬과 겹치게 되는 경우와 같음
    #   6. ans는 -1로 초기화 한 상태로, for문이 다 돌기 전에 빨간 구슬이 구멍에 빠지면 ans를 for문의 t로 바꾸고, 아니면 그대로 탈출해서 ans를 출력

    # 어려웠던 점:
    #   1. 구슬을 dy dx로 한칸 한칸씩 움직이면 너무 느릴까봐 한 번에 이동하는 방식을 생각한건데, 구멍에 빠지는 경우를 생각 못해서 포기할 뻔했다.
    #   2. 한 번에 이동하는 방식을 쓰면서, 구슬이 구멍에 빠지는지 확인하기 이전에 방문 배열을 먼저 체크하니 반례가 생겨버렸었다. 그것도 찾는 데 한참 걸렸다.

    N, M = map(int, input().split())
    N *= 10 # 1차원 배열 저장용
    cur = 0 # 구슬 좌표
    tgt = 0 # 구멍 좌표                 
    mov = [[0] * N for _ in range(4)]   # 0이 위, 1이 아래, 2가 왼쪽, 3이 오른쪽
    mov_y = [10] * M  

    input()                             
    for y in range(10, N, 10):
        tmp = input().strip()
        mov_x = 1
        for x in range(1, M):

            if tmp[x] == '#':
                for i in range(mov_y[x], y, 10):
                    mov[1][x+i] = y - 10 - i
                for i in range(mov_x, x):
                    mov[3][y+i] = x - 1 - i
                mov_y[x] = y + 10
                mov_x = x + 1
                continue
            mov[0][y+x] = mov_y[x] - y
            mov[2][y+x] = mov_x - x

            if tmp[x] == 'R':
                cur += y + x
            elif tmp[x] == 'B':
                cur += (y + x) * 100
            elif tmp[x] == 'O':
                tgt += y + x


    bak = [10, -10, 1, -1]  # 구슬 겹치면 뒤로 보냄
    ans = -1                # 정답 저장
    vis = [0] * 10000       # 방문 체크
    vis[cur] = 1
    cque = [cur]            # deque 용도
    nque = []
    check = lambda d, a, b: (1 if a < b else 0) if d%2 else (0 if a < b else 1)

        #       |  d%2 == 1  |  d%2 == 0
        # ------|------------|------------
        # a < b |      1     |      0
        # ------|------------|------------
        # a > b |      0     |      1

    for t in range(1, 11):

        while cque:
            Bcur, Rcur = divmod(cque.pop(), 100)

            for dir in range(4):
                Bnxt = Bcur + mov[dir][Bcur]
                Rnxt = Rcur + mov[dir][Rcur]

                # 파란 구슬이 빠지는 경우
                if Bnxt == tgt + mov[dir][tgt]:
                    if check(dir, Bcur, tgt):
                        continue

                # 빨간 구슬이 빠지는 경우
                if Rnxt == tgt + mov[dir][tgt]:
                    if check(dir, Rcur, tgt):
                        ans = t
                        cque.clear()
                        nque.clear()
                        break

                # 구슬 위치가 겹치는 경우
                if Bnxt == Rnxt:
                    Rnxt += bak[dir]
                    if check(dir, Bcur, Rcur):
                        Rnxt, Bnxt = Bnxt, Rnxt

                # 방문한 위치에 있는 경우
                if vis[Bnxt * 100 + Rnxt]:
                    continue
                
                # 다음 큐에 추가
                vis[Bnxt * 100 + Rnxt] = 1
                nque.append(Bnxt * 100 + Rnxt)
            
        if not nque:
            break
        cque, nque = nque, cque
    
    print(ans)

if __name__ == "__main__":
    main()
