# pypy3 256ms
# 격자 바깥으로 나갈 때 뒤로 돌아 가는 걸 속력과 함께 구현하는 게 힘들었음. 

import sys
input = sys.stdin.readline

def main():
  
    def catch(cur):
        for dep in range(R):
            if brd[dep][cur]:
                num = brd[dep][cur]
                del shk[num]
                brd[dep][cur] = 0
                return num
        return 0
    
    def up(r, c, s, d):
        r -= s
        if r < 0:
            r = -r
            d = 2
        return r, c, s, d

    def dwn(r, c, s, d):
        r += s
        if r >= R:
            r = rl-r
            d = 1
        return r, c, s, d

    def rgt(r, c, s, d):
        c += s
        if c >= C:
            c = cl-c
            d = 4
        return r, c, s, d

    def lft(r, c, s, d):
        c -= s
        if c < 0:
            c = -c
            d = 3
        return r, c, s, d

    R, C, M = map(int, input().split())
    rl, cl = (R-1)*2, (C-1)*2
    ans = 0
    run = []
    shk = {}
    mov = (0, up, dwn, rgt, lft)
    flp = (0, 2, 1, 4, 3)
    brd = [[0] * C for _ in range(R)]

    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        r, c = r-1, c-1
        if d//3:
            s %= cl
            if s >= C:
                s = cl-s
                d = flp[d]
        else:
            s %= rl
            if s >= R:
                s = rl-s
                d = flp[d]
        shk[z] = (r, c, s, d)
        brd[r][c] = z
    
    for cur in range(C-1):

        ans += catch(cur)

        nxt = [[0] * C for _ in range(R)]
        for z in shk:
            r, c, s, d = mov[shk[z][3]](*shk[z])
            shk[z] = (r, c, s, d)
            if nxt[r][c]:
                if nxt[r][c] < z:
                    nxt[r][c], z = z, nxt[r][c]
                run.append(z)
            else:
                nxt[r][c] = z

        while run:
            del shk[run.pop()]
        brd = nxt
    
    print(ans + catch(C-1))
  
if __name__ == "__main__":
    main()
