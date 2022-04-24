# pypy3 224ms, 시간복잡도 O(2NMK) -> N*M 만큼 봄여름 페이즈, N*M만큼 가을겨울 페이즈, K만큼 시뮬레이션 단계
# 문제의 시간 제한이 0.3초, 시뮬레이션 단계는 최대 1000단계 -> 모든 나무를 하나하나 처리하면 시간 초과가 날 것.
# 각 칸을 딕셔너리로 만들어 같은 나이의 나무끼리는 묶어주었음.
# 봄과 여름 페이즈, 가을과 겨울 페이즈는 서로 영향을 받지 않기 때문에 묶어서 처리할 수 있지만,
# 가을 페이즈에서 번식할 나무들은 봄 페이즈에서 살아남은 나무들로 결정되기 때문에 따로 처리해야 했음.

import sys
input = sys.stdin.readline

def main():

    N, M, K = map(int, input().split())
    L = N+1                                             # 가을에 나무가 번식할 때, 격자 바깥을 판별하기 위해, s2d2 배열에 꼼수를 씀
    mov = (-1, -1-L, -L, -L+1, 1, 1+L, L, L-1)          # 2 3 2 3 2 0 <- if s2d2[좌표]: 판별문을 통해
    s2d2 = [0] * L*L                                    # 2 3 2 3 2 0    특정 좌표에서 s2d2의 값이 0이 나오면
    nutr = [5] * N*L                                    # 2 3 2 3 2 0    격자 바깥이라는 의미, 나무를 번식시키지 않음
    land = [dict() for _ in range(N*L)]                 # 2 3 2 3 2 0
    for y in range(0, N*L, L):                          # 2 3 2 3 2 0
        s2d2[y:y+N] = map(int, input().split())         # 0 0 0 0 0 0

    for _ in range(M):
        x, y, z = map(int, input().split())
        land[(x-1)*L+(y-1)][z] = 1
    
    for _ in range(K):

        '''봄, 여름 페이즈'''
        for xy in range(N*L):
            
            if land[xy]: # 특정 칸의 땅이 비어있는 딕셔너리가 아니라면 -> 그 칸에 나무가 있다면            # 예) 1살, 2살, 3살이 각 2그루씩, 양분은 10
                dead = 0                                                                              # {1:2, 2:2, 3:2}
                alive = dict()
                nutri = nutr[xy]
                
                # 나이 어린 나무부터 양분을 먹기 때문에, 나이 순으로 정렬
                for age in sorted(land[xy].keys()):
                    trees = land[xy][age]
                    # 특정 나이의 모든 나무가 먹을 양분이 남아있는 경우
                    if nutri >= age * trees:                                                          # 1살 2그루 => 필요 양분 2, 현재 양분 10, 결과 8
                        alive[age + 1] = trees                                                        # 2살 2그루 => 필요 양분 4, 현재 양분 8,  결과 4
                        nutri -= age * trees
                    # 일부 나무만 먹을 양분이 남아있거나, 어떤 나무도 먹을 양분이 없는 경우
                    else:
                        survived = nutri // age  # 남은 양분에서 나이를 나눈 몫 -> 양분 먹은 나무 그루 수 
                        if survived:                                                                  # 3살 2그루 => 필요 양분 6, 현재 양분 4, 결과 -2
                            alive[age + 1] = survived                                                 # 현재 양분 4 중 나이 3으로 나눈 몫, 1 -> 살아 남은 나무
                            nutri %= age                                                              # 현재 양분 4 중 (살아 남은 나무 1) * (나이 3)을 뺀 1이 남고,
                        dead += age // 2 * (trees - survived) # 나이를 2로 나눈 값이 양분으로 추가됨     # 나이 3을 2로 나눈 1그루의 나무, 1 만큼이 여름에 양분이 됨.

                nutr[xy] = nutri + dead
                land[xy] = alive

        '''가을, 겨울 페이즈'''
        for xy in range(N*L):

            if s2d2[xy]:
                for age in land[xy]:
                  # 나이가 5의 배수인 나무들 그루 수만큼 1의 나이를 가진 나무를 퍼뜨림
                    if not age % 5:
                        for d in mov:
                            if s2d2[xy+d]: # 격자 안의 유효한 땅이라면
                                if 1 in land[xy+d]:
                                    land[xy+d][1] += land[xy][age]
                                else:
                                    land[xy+d][1] = land[xy][age]
                                    
                nutr[xy] += s2d2[xy]

    print(sum(sum(land[xy].values()) for xy in range(N*L)))
    
if __name__ == "__main__":
    main()
