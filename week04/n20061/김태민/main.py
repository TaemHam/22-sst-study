# pypy3 168ms
# 시간 절약을 위해 비트마스킹을 사용해 풀었음. 블럭이 있으면 1, 없으면 0으로 저장

import sys
input = sys.stdin.readline

def main():

    def play(brd, blk, col): # brd는 보드 종류, blk은 블럭 종류, col은 블럭이 떨어지는 열

        '''높이 확인 페이즈'''
        h = 0
        for xy in range(20+col, -1, -4):                    #     1 1 0 0
            if brd & 1<<xy:                                 #     ㄴ> 떨어질 가로 블럭
                h = xy//4+1                                 #     0 0 0 0    연한 색깔 줄
                break                                       #     0 0 0 0    연한 색깔 줄
        if blk == 2: # 가로 블럭은 오른쪽도 확인              #     0 0 0 0    3번 줄
            for xy in range(21+col, -1, -4):                #     0 0 0 1    2번 줄
                if brd & 1<<xy:                             # h-> 0 0 0 1    1번 줄
                    h = max(h, xy//4+1)                     #     0 1 1 1    0번 줄
                    break
        
        '''블럭 추가 페이즈'''
        loc = h<<2
        brd |= 1 << loc+col

        if blk == 2: # 가로 블럭은 오른쪽도 추가
            brd |= 1 << loc+col+1
            
        elif blk == 3: # 세로 블럭은 위쪽도 추가
            brd |= 1 << loc+col+4
            
            '''점수 라인 제거 페이즈'''
                                                                                #  0 0 1 0       0 0 0 0       0 0 0 0
            if not ~brd & 15 << loc+4:                                          #  0 0 1 1       0 0 0 0       0 0 0 0
                scr.append(1)                                                   #  1 1 1 1   &   0 0 0 0   =   0 0 0 0
                brd = (brd & (1 << loc+4)-1) | (brd>>4 & ~((1 << loc+4)-1))     #  0 1 1 1       1 1 1 1       0 1 1 1
                                                                                #                                 +
        if not ~brd & 15 << loc:                                                #  0 0 0 0       1 1 1 1       0 0 0 0       0 0 0 0
            scr.append(1)                                                       #  0 0 1 0       1 1 1 1       0 0 1 0       0 0 1 0
            brd = (brd & (1 << loc)-1) | (brd>>4 & ~((1 << loc)-1))             #  0 0 1 1   &   1 1 1 1   =   0 0 1 1   =   0 0 1 1
                                                                                #  1 1 1 1       0 0 0 0       0 0 0 0       0 1 1 1
        '''돌출 부분 정리 페이즈'''            
        if brd & 15 << 16:              #      0 1 0 0       0 0 0 0       0 0 0 0
            brd >>= 4                   #      0 1 0 0       1 1 1 1       0 1 0 0
            if brd & 15 << 16:          #      0 1 1 0       0 0 0 0       0 1 0 0
                brd >>= 4               #      1 1 0 0       0 0 0 0       0 1 1 0
                                        #  if  1 1 0 1   &   0 0 0 0   :   1 1 0 0
        return brd                      #      1 0 0 1       0 0 0 0       1 1 0 1

    grn = blu = 0
    swp = (0, 1, 3, 2) # 파란 격자는 가로 블록이 세로 블럭이고, 세로 블럭이 가로 블럭임
    scr = []           # 점수 더할 때마다 1을 append 해 주고 len으로 점수 합산

    for _ in range(int(input().strip())):
        t, x, y = map(int, input().split())
        grn = play(grn, t, y)
        blu = play(blu, swp[t], x)
    
    # for y in range(20, -1, -4): # 초록 파랑 보드 확인용
    #     for xy in range(y, y+4):
    #         print(1 if grn & 1<<xy else 0, end=' ')
    #     print()
    # print('위 초록 아래 파랑')
    # for y in range(20, -1, -4):
    #     for xy in range(y+3, y-1, -1):
    #         print(1 if blu & 1<<xy else 0, end= ' ')
    #     print()
    # print()

    cnt = 0
    while grn:
        grn &= grn-1
        cnt += 1
    while blu:
        blu &= blu-1
        cnt += 1

    print(str(len(scr)) + '\n' + str(cnt))
    
if __name__ == "__main__":
    main()
