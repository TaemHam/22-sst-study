import sys
input = sys.stdin.readline

def main():
    # 좌표에 -1이 있으면 (격자 밖으로 나가면) brd[-1]에 저장
    check = lambda x: -1 if brd[x] == -1 else x
    
    # 격자 바깥 표시를 위해 2칸 넓게 잡아서 -1을 저장해 주었음
    N = int(input().strip())
    L = N+2
    mov = (-1, L, 1, -L)
    # 움직여야 할 모래의 양, 앞으로 움직일 칸 수, 옆으로 움직일 칸 수
    blw = ((0.1, 1, 1), (0.07, 0, 1), (0.05, 2, 0), (0.02, 0, 2), (0.01, -1, 1))
    brd = [-1] * L*L
    brd[-1] = 0
    cur = N//2*L + N//2
    # 방향 전환을 위한 플래그 4개
    c, d = 1, 0
    flg1, flg2 = 2, 1

    for y in range(0, N*L, L):
        brd[y:y+N] = map(int, input().split())

    for _ in range(1, N**2):
        cur += mov[d]
        dif = brd[cur]

        if brd[cur] >= 10:
            for pct, fwd, sde in blw:
                if not int(brd[cur] * pct):
                    break
                fwd *= mov[d]
                sde *= mov[d-1]
                for neg in range(-1 if sde else 1, 2, 2):
                    dif -= int(brd[cur] * pct)
                    brd[check(cur+fwd+sde*neg)] += int(brd[cur] * pct)

        brd[cur] = 0
        brd[check(cur+mov[d])] += dif

        c -= 1
        if not c:
            d += 1
            d %= 4
            flg1 -= 1
            if not flg1:
                flg1 = 2
                flg2 += 1
            c = flg2
    
    print(brd[-1])

    
if __name__ == "__main__":
    main()
