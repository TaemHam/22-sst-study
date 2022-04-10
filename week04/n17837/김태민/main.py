# pypy3 152ms
# 어려웠던 점:
# 말이 두 파란색 칸 안에 끼어 있는 경우, 어떻게 해도 이동이 안된다 생각해서, 그 경우 일부러 빼줬었는데,
# 파랑, 빨강, 파랑 안에 끼어있고 다른 말이 빨강 칸으로 오면, 그 말이 끼어있는 말을 업고 나갈 수 있어서 틀렸었음.

import sys
input = sys.stdin.readline

def main():

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    N, K = map(int, input().split())
    flp = [1, 0, 3, 2]
    tbl = [input().split() for _ in range(N)]
    loc = []
    dir = []
    brd = [[[] for _ in range(N)] for _ in range(N)]
    stk = []
    ans = -1

    for i in range(K):
        y, x, d = map(lambda x: int(x)-1, input().split())
        loc.append((y, x))
        dir.append(d)
        brd[y][x].append(i)
    
    for t in range(1, 1001):
        for cur in range(K):
            (y, x) = loc[cur]
            
            '''방향 페이즈'''
            ny = y + dy[dir[cur]]
            nx = x + dx[dir[cur]]
            if 0 > ny or N <= ny or 0 > nx or N <= nx or tbl[ny][nx] == '2':
                dir[cur] = flp[dir[cur]]
                ny = y + dy[dir[cur]]
                nx = x + dx[dir[cur]]
                if 0 > ny or N <= ny or 0 > nx or N <= nx or tbl[ny][nx] == '2':
                    continue
                    
            '''이동 페이즈'''
            while True:
                mov = brd[y][x].pop()
                loc[mov] = (ny, nx)
                if tbl[ny][nx] == '1':
                    brd[ny][nx].append(mov)
                else:
                    stk.append(mov)
                if mov == cur:
                    while stk:
                        brd[ny][nx].append(stk.pop())
                    break
                    
            '''정담 체크 페이즈'''
            if len(brd[ny][nx]) >= 4:
                ans = t
                break
        
        if ans != -1:
            break
    
    print(ans)
  
  
if __name__ == "__main__":
    main()
