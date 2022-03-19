import sys
input = sys.stdin.readline

def main():

    # 접근 방법:
    #   1. 게임판을 1차원 배열로 만들고 위치 역시 백의 자리 기준으로 Y좌표 X좌표 저장해줌
    #   2. 주사위의 면을 각각의 변수로 저장해서 한 번 굴릴 때 마다 스왑해줌
    #   3. 나머지는 문제 조건대로 윗 부분 출력해주고, 아랫 부분은 게임판에 숫자가 있으면 빼오고 없으면 붙여주고

    # 어려웠던 점:
    #   1. 처음에 Y와 X를 거꾸로 받아버렸는데, 왜 틀렸는지 몰라 방황했었다. 

    dd = [0, 1, -1, -100, 100]
    N, M, Y, X, _ = map(int, input().split())
    siz = 100 * N + M
    cur = 100 * Y + X
    ans = []
    brd = [0] * siz
    oob = [1] * siz
    for y in range(0, 100*N, 100):
        oob[y:y+M] = [0] * M
        brd[y:y+M] = list(map(int, input().split()))

    top, bot, lft, rgt, frt, bak = 0, 0, 0, 0, 0, 0
    
    for cmd in map(int, input().split()):
        if oob[cur + dd[cmd]]:
            continue

        cur += dd[cmd]

        if cmd == 1:
            top, lft, bot, rgt = lft, bot, rgt, top
        elif cmd == 2:
            top, lft, bot, rgt = rgt, top, lft, bot
        elif cmd == 3:
            top, frt, bot, bak = frt, bot, bak, top
        else: # cmd == 4:
            top, frt, bot, bak = bak, top, frt, bot

        ans.append(str(top))

        if not brd[cur]:
            brd[cur] = bot
        else:
            bot, brd[cur] = brd[cur], 0

    print('\n'.join(ans))

if __name__ == "__main__":
    main()
