def route(graph, a):
    visited.append(a)
    count = 0
    if len(visited) == len(graph[0]):
        return count+1
    for i in range(len(graph)):
        if graph[a][i] ==1 and i not in visited:
            visited.append(i)
            count += 1
            route(graph, i)
    else:
        return count

def dfs(graph):



#2814. 최장 경로
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    if M == 0:
        result = 0
        break
    else: 
        graph = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(M):
            a, b = map(int, input().split())
            graph[a-1][b-1] = 1
            graph[b-1][a-1] = 1
        
