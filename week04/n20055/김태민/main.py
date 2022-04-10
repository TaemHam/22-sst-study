# pypy3 260ms
# 벨트와 로봇을 오른쪽으로 돌리는 게 아닌 시작 지점과 끝 지점을 왼쪽으로 돌려줘야하는 문제
# 어려웠던 점:
# 문제를 제대로 안읽고 같은 칸에 로봇 여러 개가 들어갈 수 있는 줄 알았었다

import sys
input = sys.stdin.readline

def main():

    N, K = map(int, input().split())
    L = 2*N
    belt = list(map(int, input().split()))
    robs = [0] * L
    stt, end = -1, N-2  # 처음에 한 번 돌려주고 난 위치
    ooo = 0             # 망가진 벨트 갯수

    for time in range(1, 4050):

        '''로봇 올리기 페이즈''' # 3번 페이즈부터 시작
        if belt[stt]:
            robs[stt] = 1
            belt[stt] -= 1

            if not belt[stt]:
                ooo += 1
                
        '''정답 체크 페이즈'''
        if ooo >= K:
            break

        '''벨트 돌리기 페이즈'''
        stt -= 1
        end -= 1
        if end < 0:
            stt %= L
            end %= L

        robs[end] = 0 # 벨트 끝지점에 로봇이 있으면 빼줌

        '''로봇 옮기기 페이즈'''
        for idx in range(end, stt+1, -1): # 벨트 끝지점부터 시작지점까지 거꾸로 돌면서

            if belt[idx] and robs[idx-1] and not robs[idx]: # 로봇이 있는 위치 다음 칸에 내구도는 있고, 로봇이 없는 경우
                belt[idx] -= 1
                robs[idx], robs[idx-1] = robs[idx-1], robs[idx]

                if not belt[idx]:
                    ooo += 1

        robs[end] = 0 # 벨트 끝지점에 로봇이 있으면 빼줌

    print(time)

if __name__ == "__main__":
    main()
