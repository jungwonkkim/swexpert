"""
swea 1247 초ㅚ적경로
code written by jungwonkim
"""
def dfs (idx, dist, x, y):
    global min_dist
    if idx == N:
        if min_dist > dist+abs(x-house_x) + abs(y-house_y):
            min_dist = dist+abs(x-house_x) + abs(y-house_y)
        return
    if min_dist < dist:
        return
    for n in range(N):
        if visited[n] == False:
            visited[n] = True
            dfs(idx+1, dist+abs(x-positions[n][0]) + abs(y - positions[n][1]), positions[n][0], positions[n][1])
            visited[n] = False


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    min_dist = 200*N
    temp = list(map(int, input().split()))
    positions = []
    visited = [False for _ in range(N)]
    office_x, office_y, house_x, house_y = temp[0], temp[1], temp[2], temp[3]
    for i in range(2, N+2):
        x, y = temp[2*i], temp[2*i+1]
        positions.append((x, y))
    dfs(0, 0, office_x, office_y)
    print('#{} {}'.format(test_case, min_dist))




