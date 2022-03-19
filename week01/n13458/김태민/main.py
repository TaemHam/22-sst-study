import sys
input = sys.stdin.readline

def main():

    # 접근 방법:
    #   1. 모든 응시자 숫자에 대응하는 배열(dic)을 만들어줌
    #   2. 계산되지 않은 응시자 숫자는 배열에 넣어주고, 이미 계산된 숫자는 배열에서 바로 빼와서 정답에 더해줌

    # 어려웠던 점:
    #   1. (응시자 수 - 총 감독관 감당 가능 수)의 값이 음수가 나오는 경우 망가지는걸 고려 안해서 틀렸었다.
    #      해결 방법으로 그 감당 가능 숫자 이하의 응시자수에 대해, 모두 1로 미리 저장해두었다.
    
    input()
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    dic = [0] + [1]*B + [0]*(1000000-B)
    ans = 0

    for a in A:

        if not dic[a]:
            i, j = divmod(a-B, C)
            dic[a] = i+2 if j else i+1

        ans += dic[a]

    print(ans)
        

if __name__ == "__main__":
    main()
