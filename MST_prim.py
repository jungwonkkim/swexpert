#프림 이용한 MST
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]* V for _ in range(V)] # 인접행렬
    for i in range(E): #간선 수 만큼
        s, e, c = map(int, input().split())
        adj[s][e] = c
        adj[e][s] = c

    #key, p, mst 준비

    INF = float('inf')
    key = [INF] * V
    p = [-1] * V
    mst = [False] * V

    #시작 정점 선택

    key[0] = 0
    cnt = 0
    result = 0
    while cnt < V:
        min = INF
        u = -1
        for i in range(V):
            if not mst[i] and key[i]<min:
                min = key[i]
                u = i

        #u 를 mst로 선택
        mst[u] = True
        result += min
        #key 값 갱신
        cnt +=1

        for w in range(V):
            if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                key[w] = adj[u][w]
                p[w] = u


print('#{} {}'.format(test_case, result))


