def dijkstra(V, graph):
    INF = float('inf')
    s = [False] * V
    d = [INF] * V
    d[0] = 0
    while True:
        m = INF
        N = -1

        for j in range(V):
            if not s[j] and m > d[j]:
                m = d[j]
                N = j
        if m == INF:
            break
        s[N] = True
        for j in range(V):
            if s[j]: continue
            via = d[N] + graph[N][j]
            if d[j] > via:
                d[j] = via

    return d

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    V +=1
    INF = float('inf')
    graph = [[INF]*V for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = w
    result = dijkstra(V, graph)
    print('#{} {}'.format(test_case, result[-1]))