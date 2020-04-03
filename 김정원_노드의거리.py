from copy import deepcopy

def bfs(start):
    global ans
    cnt = 0
    queue = [start]
    visited = [False for _ in range(V)]
    while queue:
        new_queue = []
        for q in queue:
            if q == G:
                ans = cnt
                return
            visited[q] = True
            for i in range(V):
                if graph[q][i] and visited[i]==False:
                    new_queue.append(i)
        queue = deepcopy(new_queue)
        cnt +=1
    return


T = int(input())
for test_case in range(1, T+1):
    V, E= map(int, input().split())
    graph = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a-1][b-1] = graph[b-1][a-1] = 1
    S, G = map(int, input().split())
    S -=1
    G -=1
    ans = 0
    bfs(S)
    print('#{} {}'.format(test_case, ans))