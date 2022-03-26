import sys
input = sys.stdin.readline

def main():
  
    # 어려웠던 점:
    # 상어가 물고기를 가장 많이 쫒을 수 있는 루트를 찾을 때, 상어가 있는 위치에는 물고기가 존재할 수 없다고 단정짓고
    # 일반 그래프 탐색처럼 상어 위치를 방문처리 하고 시작했는데, 그게 틀려서 왜 틀렸는지 찾는데 반나절 걸리고, 고치고 나니 새벽 3시 ㅠㅠ

    # 물고기 수가 백만마리가 될 수 있다는 조건에, 나무 재테크 문제에서 아이디어를 따와서
    # 각 칸에서 같은 방향으로 향하고 있는 마릿수를 8칸짜리 방향 배열에 저장함
    M, S = map(int, input().split())
    odr = [0] * 20
    brd = [[0]* 8 for _ in range(20)]
    oob = [0] * 20 + [1] * 5
    sdir = [-5, -1, 5, 1]
    fdir = [-1, -6, -5, -4, 1, 6, 5, 4]
    
    for y in range(4, 20, 5):
        oob[y] = 1

    for _ in range(M):
        y, x, d = map(lambda x: int(x)-1, input().split())
        brd[5*y+x][d] += 1
    
    y, x = map(lambda x: int(x)-1, input().split())
    shrk = 5*y+x

    for _ in range(S):

        '''물고기 이동 페이즈'''
        nbrd = [[0]*8 for _ in range(20)]
        for loc in range(20):
            if not oob[loc]:
                for d, n in enumerate(brd[loc]):
                    if n:
                        for i in range(d, d-8, -1):
                            if oob[loc+fdir[i]] or odr[loc+fdir[i]] or loc+fdir[i] == shrk:
                                continue
                            nbrd[loc+fdir[i]][i] += n
                            break
                        else:
                            nbrd[loc][d] += n
        
        '''상어 이동 페이즈'''
        # 최대 0마리 쫒아내는 경우도 있으므로 -1로 설정
        mxc = -1
            # 가장 많이 쫒아내는 루트 찾기
            # BFS, DFS, 조합 세 가지 방법을 써봤는데, 조합이 제일 빨랐다.
        for d1 in sdir:
            l1 = shrk + d1
            if oob[l1]:
                continue
            v1 = 0 | 1<<l1
            c1 = sum(nbrd[l1])
            for d2 in sdir:
                l2 = l1 + d2
                if oob[l2]:
                    continue
                v2 = v1 | 1<<l2
                c2 = c1 if v1 & 1<<l2 else c1 + sum(nbrd[l2])
                for d3 in sdir:
                    l3 = l2 + d3
                    if oob[l3]:
                        continue
                    c3 = c2 if v2 & 1<<l3 else c2 + sum(nbrd[l3])
                    if c3 > mxc:
                        mxc = c3
                        bpr = [l1, l2, l3]
            # 루트 따라가며 물고기 쫒아내기
        for loc in bpr:
            if sum(nbrd[loc]):
                nbrd[loc] = [0] * 8
                odr[loc] = 3
        shrk = bpr[-1]

        '''냄새 페이즈'''
        for i in range(20):
            if odr[i]:
                odr[i] -= 1
        
        '''복제 페이즈'''
        for i in range(20):
            if not oob[i]:
                for d in range(8):
                    nbrd[i][d] += brd[i][d]
        brd = nbrd
        
    print(sum(sum(i) for i in brd))
                    
if __name__ == "__main__":
    main()
