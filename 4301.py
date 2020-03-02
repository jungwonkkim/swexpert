#4301. 콩 많이 심기

T = int(input())
for test_case in range(1, T+1):
    M, N = map(int, input().split())
    beans = [[1 for _ in range(M)]for _ in range(N)]
    cnt = M * N
    for i in range(N):
        for j in range(M):
            if beans[i][j]:
                if i+2<N and beans[i+2][j]:
                    beans[i+2][j] = 0
                    cnt -=1
                if j+2<M and beans[i][j+2]:
                    beans[i][j+2] = 0
                    cnt -=1

    print('#{} {}'.format(test_case, cnt))