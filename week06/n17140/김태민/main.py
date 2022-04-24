# pypy3 144ms
# 격자를 100*100으로 미리 만들어두고, 정렬 연산 후 최대 길이를 갱신시켜주며 풀었음.

import sys
input = sys.stdin.readline

def main():

    def Msort(o, a, d):
        do, da = (1, 100) if d else (100, 1)

        mxm = 0

        for i in range(0, o*do, do):

            sav = dict()
            for e in brd[i:i+a*da:da]:
                if e in sav:
                    sav[e] += 1
                else:
                    sav[e] = 1
            if 0 in sav:
                del sav[0]

            res = []
            for t in sorted(sav.items(), key= lambda x: (x[1], x[0])):
                res.extend(t)

            lim = max(a, len(res)) # 연산 후 배열이 더 짧을 경우, 뒷 숫자들을 0으로 바꿔야 하기 때문에 설정 ex) 1 1 1 1 -> 1 4 0 0
            mxm = max(mxm, len(res))
            brd[i:i+lim*da:da] = res + [0] * (lim-len(res))
        
        return mxm

    R, C, K = map(int, input().split())
    tgt = 100*R+C-101
    ans = -1
    brd = [0] * 10000
    rln, cln = 3, 3
    for y in range(0, 300, 100):
        brd[y:y+3] = map(int, input().split())
    
    for time in range(101):

        if brd[tgt] == K:
            ans = time
            break

        if rln >= cln:
            cln = Msort(rln, cln, 0)
        else:
            rln = Msort(cln, rln, 1)
    
    else:
        if brd[tgt] == K:
            ans = time
    
    print(ans)

    # for y in range(0, 100*rln, 100): # 격자 확인용
    #     print(brd[y:y+cln])
    
if __name__ == "__main__":
    main()
