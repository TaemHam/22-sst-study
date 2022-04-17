# python3 104ms
# 조회해야하는 칸 수를 줄여보고자 기존에 구해놓은 합에 달라지는 칸의 합만 따로 구해서 더하고 빼줬는데, 시간이 너무 오래 걸렸다.

import sys
input = sys.stdin.readline

def main():
  
    def block(arr, lt, rt, rb, lb):
        arr[0] += lt + rt + rb + lb
        arr[1] -= lt
        arr[2] -= rt
        arr[3] -= rb
        arr[4] -= lb

    N = int(input().strip())
    DL, DR = N-1, N+1
    brd = []
    for _ in range(N):
        brd.extend(map(int, input().split()))
    ori = [brd[1] + brd[N] + brd[N+1] + brd[N+2] + brd[N+N+1], brd[0], sum(brd[2:N]+brd[3+N:2*N]), sum(brd[N+N:N*N:N]), sum(brd[N+N:])]
    ori[4] -= ori[3] + brd[N+N+1]
    top, rgt, bot, lft = 1, N+2, N+N+1, N
    ans = 400000

    for d1 in range(1, N-1):
        nxt = ori[:]

        for d2 in range(1, N-d1):
            que = [nxt[:]] * (N-d1-d2)

            for i in range(len(que)-1):
                que[i] = que[i][:]
                add3 = sum(brd[i+bot+N:N*N:N])
                block(que[i+1], 
                    -sum(brd[i+top:i+lft:DL]), 
                    sum(brd[i+rgt+1:i+top:-DR]), 
                    -sum(brd[i+lft:i+bot+1:DR])-add3, 
                    sum(brd[i+bot+1:i+rgt+1:-DL])+add3)

            for x in range(len(que)):
                cpy = que[x]
                ans = min(ans, max(cpy)-min(cpy))

                for xy in range(x, N*len(que)-N, N):
                    add1 = sum(brd[(d1+xy//N)*N:xy+lft])
                    add2 = sum(brd[xy+rgt+DR:((xy+rgt)//N+2)*N])
                    block(cpy,
                        -sum(brd[xy+top:xy+lft+1:DL])-add1, 
                        -sum(brd[xy+rgt:xy+top:-DR])-add2, 
                        sum(brd[xy+lft+N:xy+bot+N:DR])+add1, 
                        sum(brd[xy+bot+N:xy+rgt-1+N:-DL])+add2)
                    ans = min(ans, max(cpy)-min(cpy))
                    
            if d2 < N-d1-1:
                add3 = sum(brd[bot+N:N*N:N])
                rgt += DR
                bot += DR
                add2 = sum(brd[rgt+1:rgt+N-d1-d2-1])
                add5 = sum(brd[rgt-1:bot-1:DL]) + sum(brd[rgt:bot+1:DL])
                block(nxt, 0, -add2, -add3, add2+add3+add5)

        top += 1
        lft += N
        bot = lft+DR
        rgt = top+DR
        block(ori, -sum(brd[top-1:lft-DL:DL]), brd[top]+brd[rgt], brd[lft], sum(brd[bot:rgt:-DL]))
    
    print(ans)
  
if __name__ == "__main__":
    main()
