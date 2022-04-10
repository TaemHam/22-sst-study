# pypy3 108ms
# 백트래킹 문제이지만, 재귀를 잘 못써서 모든 정보를 큐에 저장해놓고 BFS 처럼 풀었다.

import sys
input = sys.stdin.readline

def main():
    
    floc = [[] for _ in range(17)]
    fdir = [0] * 17
    mov = [0, -5, -6, -1, 4, 5, 6, 1, -4]
    brd = [-1] * 25

    for y in range(0, 20, 5):
        tmp = list(map(int, input().split()))
        for x in range(4):
            i = x<<1
            brd[y+x] = tmp[i]
            floc[tmp[i]] = y+x
            fdir[tmp[i]] = tmp[i+1]
    
    que = [(0, fdir[brd[0]], floc, fdir, brd[0], set(range(1, 17)) - {brd[0]}, brd)]
    brd[0] = -1
    ans = 0
    
    # 격자는 총 20칸짜리 1차원 배열로, 격자 바깥칸과 상어를 -1로, 빈칸은 0으로, 나머지는 물고기 위치에 따른 물고기 번호를 저장해주었다.
    # -1  2 15  9 -1
    #  3  1 14 10 -1
    #  6 13  4 10 -1
    # 16  8  5 12 -1
    # -1 -1 -1 -1 -1
    
    # que에는 상어 위치, 상어 방향, 물고기 위치, 물고기 방향, 상어가 먹은 물고기 합, 살아남은 물고기, 격자 현황을 모두 저장
    for sloc, sdir, floc, fdir, siz, srv, brd in que:
        ans = max(ans, siz)

        '''물고기 이동 페이즈'''
        for fsh in srv:  # 살아남은 물고기는 set으로 저장해서, 죽은 물고기 빼는 것도 O(1), for문 돌리는 것도 살아 남은 것들만 번호 순으로 돌 수 있게 함 
            cur = floc[fsh]
            for _ in range(8):
                nxt = cur + mov[fdir[fsh]]
                if brd[nxt] != -1:
                    floc[fsh], floc[brd[nxt]] = nxt, cur
                    brd[cur], brd[nxt] = brd[nxt], brd[cur]
                    break
                fdir[fsh] = fdir[fsh] % 8 + 1

        '''상어 이동 페이즈'''
        for s in range(1, 4):
            nloc = sloc + mov[sdir] * s
            if brd[nloc] == -1:
                break
            if brd[nloc]:
                nbrd = brd[:]
                nbrd[sloc], nbrd[nloc] = 0, -1
                que.append((nloc, fdir[brd[nloc]], floc[:], fdir[:], siz + brd[nloc], srv - {brd[nloc]}, nbrd))
        
    print(ans)
  
if __name__ == "__main__":
    main()
