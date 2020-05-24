
T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    V +=1
    adj = [[0] * V for _ in range(V)]
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s][e] = c
        adj[e][s] = c
    INF = float('inf')
    key = [INF] * V
    p = [-1] * V
    mst = [False] * V
    key[0] = 0
    cnt = 0
    result = 0
    while cnt < V:
        min = INF
        u = -1
        for i in range(V):
            if not mst[i] and key[i] < min:
                min = key[i]
                u = i
        mst[u] = True
        result += min
        cnt += 1
        for w in range(V):
            if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                key[w] = adj[u][w]
                p[w] = u

    print('#{} {}'.format(test_case, result))






