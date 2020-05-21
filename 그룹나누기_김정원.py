def team_making(idx):
    global visited
    stack = [idx]
    while stack:
        i = stack.pop()
        visited[i] = True
        for j in range(N):
            if graph[i][j] and visited[j] == False:
                stack.append(j)
    return


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    visited = [False for _ in range(N)]
    application = list(map(int, input().split()))
    for i in range(M):
        a = application[2*i]-1
        b = application[2*i+1]-1
        graph[a][b] = graph[b][a] = 1
    cnt = 0
    for n in range(N):
        if visited[n] == False:
            cnt +=1
            team_making(n)
    print('#{} {}'.format(test_case, cnt))