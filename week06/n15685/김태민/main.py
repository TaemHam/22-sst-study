# pypy3 112ms / python3 80
# 왔던 길을 거꾸로 탐색하며 90도 돌려서 다시 가는 그 패턴을 찾기가 어려웠던 것 같음
# 격자를 set으로 만들어 빈칸 연산 횟수를 줄여보고자 했음

import sys
input = sys.stdin.readline

def main():

    N = int(input().strip())
    mov = (1, -102, -1, 102)
    brd = set()

    for _ in range(N):
        x, y, d, g = map(int, input().split())
        cur = y*102+x
        brd.add(cur)
        cur += mov[d]
        brd.add(cur)
        stk = [(d+1)%4]
        for _ in range(g):
            for d in reversed(stk):
                cur += mov[d]
                brd.add(cur)
                stk.append((d+1)%4)

    ans = 0
    for cur in brd:
        if cur+1 in brd and cur+102 in brd and cur+103 in brd:
            ans += 1
    
    print(ans)
    
if __name__ == "__main__":
    main()
