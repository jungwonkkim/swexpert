"""
백준 다리만들기2
https://www.acmicpc.net/problem/17472
code written by jungwonkkim
"""

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(vertices, edges):
    for v in range(vertices):
        make_set(v)
    total = 0
    for edge in edges:
        v, u, cost = edge
        if find(v) != find(u):
            union(v, u)
            total += cost
    if total == 0:
        return -1
    p = parent[0]
    for key in parent:
        if parent[key] != p:
            return -1
    return total

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
I = 1
for n in range(N):
     for m in range(M):
        if maps[n][m] and visited[n][m] == False:
            visited[n][m] = True
            maps[n][m] = I
            stack = [(n, m)]
            while stack:
                a, b = stack.pop()
                for dl in delta:
                    na = a + dl[0]
                    nb = b + dl[1]
                    if -1<na<N and -1<nb<M and maps[na][nb] and visited[na][nb] == False:
                        visited[na][nb] = True
                        maps[na][nb] = I
                        stack.append((na, nb))
            I += 1

graph = [[float('inf') for _ in range(I-1)] for _ in range(I-1)]
edges = []
for n in range(N):
    start = 0
    dist = 0
    for m in range(M):
        if maps[n][m] == 0 :
            dist += 1
        elif maps[n][m]:
            if start == maps[n][m]:
                dist = 0
            elif start == 0:
                start = maps[n][m]
                dist = 0
            else:
                if dist == 1:
                    start = maps[n][m]
                    dist = 0
                else:
                    graph[start-1][maps[n][m]-1] = graph[maps[n][m]-1][start-1] = min(graph[maps[n][m]-1][start-1], dist)
                    start = maps[n][m]
                    dist = 0
for m in range(M):
    start = 0
    dist = 0
    for n in range(N):
        if maps[n][m] == 0:
            dist += 1
        elif maps[n][m]:
            if start == maps[n][m]:
                dist = 0
            elif start == 0:
                start = maps[n][m]
                dist = 0
            else:
                if dist == 1 or 0:
                    start = maps[n][m]
                    dist = 0
                else:
                    graph[start-1][maps[n][m]-1] = graph[maps[n][m]-1][start-1] = min(graph[maps[n][m]-1][start-1], dist)
                    start = maps[n][m]
                    dist = 0
for i in range(I-1):
    for j in range(i+1, I-1):
        if graph[i][j] != float('inf'):
            edges.append((i, j, graph[i][j]))
edges.sort(key= lambda x:x[2])
print(kruskal(I-1, edges))
