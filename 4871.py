# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

def dfs(node):
    if node == find-1:
        global result
        result = 1
        return
    else:
        global visited
        visited.append(node)
        for next in range(len(graph[node])):
            if graph[node][next] == 1 and next not in visited:
                dfs(next)
        visited.pop()


T = int(input())
for test_case in range(1, T + 1):
    result = 0
    visited = []
    V, E = map(int, input().split())
    graph = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
    S, find  = map(int, input().split())
    dfs(S-1)
    print('#{} {}'.format(test_case, result))
