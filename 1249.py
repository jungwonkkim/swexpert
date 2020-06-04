"""
swea 1249 보급로
"""
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    roads = [[int(i) for i in list(input())] for _ in range(N)]
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 0
    queue = [(0,0)]
    while queue:
        a, b = queue.pop()
        for dl in delta:
            newa = a + dl[0]
            newb = b + dl[1]
            if -1<newa<N and -1<newb<N:
                if dp[newa][newb] == -1 or dp[newa][newb] > dp[a][b] + roads[newa][newb]:
                    dp[newa][newb] = dp[a][b] + roads[newa][newb]
                    queue.append((newa, newb))
    print('#{} {}'.format(test_case, dp[N-1][N-1]))
