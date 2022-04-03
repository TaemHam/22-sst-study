import sys
input = sys.stdin.readline

def main():
  
    watercopy = lambda x: len([1 for d in dc if lnd[x+d]])

    N, M = map(int, input().split())
    L = N+1
    dy = (0, 0, -1, -1, -1, 0, 1, 1, 1)
    dx = (0, -1, -1, 0, 1, 1, 1, 0, -1)
    dc = (-1-L, 1-L, 1+L, -1+L)
    lnd = [0] * L*L
    cld = [N*L-L, N*L-L+1, N*L-L-L, N*L-L-L+1]
    for y in range(0, N*L, L):
        lnd[y:y+N] = map(int, input().split())

    for _ in range(M):
        dir, spd = map(int, input().split())

        '''구름 이동 페이즈'''
        prv = set()
        loc = []
        for cur in cld:
            y, x = divmod(cur, L)
            nxt = (y+dy[dir]*spd)%N*L + (x+dx[dir]*spd)%N
            loc.append(nxt)
            lnd[nxt] += 1
            prv.add(nxt)

        '''복제 마법 페이즈'''
        for nxt in loc:
            lnd[nxt] += watercopy(nxt)

        '''구름 생성 페이즈'''
        cld = []
        for y in range(0, N*L, L):
            for xy in range(y, y+N):
                if lnd[xy] > 1 and xy not in prv:
                    lnd[xy] -= 2
                    cld.append(xy)

    print(sum(lnd))
    
if __name__ == "__main__":
    main()
