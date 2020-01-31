#6057. 그래프의 삼각형

T = int(input())

for test_case in range(1, T + 1):
    N ,M = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    triangle_counter = 0
    for i in range(M):
        x, y = map(int, input().split())
        graph[x-1][y-1] = 1
        graph[y-1][x-1] = 1
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[i][j] == graph[j][k] == graph[k][i] ==1:
                    triangle_counter +=1
    print(f'#{test_case} {int(triangle_counter/6)}')