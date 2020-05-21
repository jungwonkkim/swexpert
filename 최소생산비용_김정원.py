def backtracking(idx, cost):
    global min_cost
    global visited
    if idx >= N:
        if min_cost > cost:
            min_cost = cost
        return
    if min_cost < cost:
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        backtracking(idx+1, cost+factory[idx][i])
        visited[i] = False



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    min_cost = 100 * N * N
    backtracking(0, 0)
    print('#{} {}'.format(test_case, min_cost))