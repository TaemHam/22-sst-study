def main():
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
