import sys
input = sys.stdin.readline

def main():
    
    # 파이어볼 이동은 좌표 질량 속력 방향을 큐에 저장해서 시뮬레이션
    # 파이어볼 융합은 좌표를 키값으로 딕셔너리로 저장
    # 밸류에는 갯수, 질량 합, 속도 합, 방향을 2로 나눈 나머지 저장 -> 방향 2로 나눈 나머지의 합이 0이면 모두 짝수, 갯수와 같으면 모두 홀수
    N, M, K = map(int, input().split())
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    brd = dict()
    que = [list(map(int, input().split())) for _ in range(M)]
    
    for _ in range(K):
        '''이동 페이즈'''
        brd.clear()
        for y, x, m, s, d in que:
            crd = (y+dy[d]*s)%N * N + (x + dx[d]*s)%N
            if crd not in brd:
                brd[crd] = [1, m, s, d%2, d]
            else:
                brd[crd][0] += 1
                brd[crd][1] += m
                brd[crd][2] += s
                brd[crd][3] += d%2
        
        '''융합 페이즈'''
        que.clear()
        for crd, (c, m, s, n, d) in brd.items():
            y, x = divmod(crd, N)
            if c == 1:
                que.append((y, x, m, s, d))
            else:
                if not m//5:
                    continue
                que.extend((y, x, m//5, s//c, i) for i in range(1 if n%c else 0, 8, 2))

    print(sum(i[2] for i in que))
    
if __name__ == "__main__":
    main()
