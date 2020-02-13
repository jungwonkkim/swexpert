#1219. [S/W 문제해결 기본] 4일차 - 길찾기


def dfs(n):
    if n == 99:
        global result
        result = 1
        return
    else:
        global visited
        visited.append(n)
        for next in route[n]:
            if next != -1 and next not in visited:
                dfs(next)
        visited.pop()


for test_case in range(1, 11):
    visited = []
    tc, V = map(int, input().split())
    route = [[-1 for _ in range(2)] for _ in range(100)]
    temp = list(map(int, input().split()))
    result = 0
    for a in range(V):
        if route[temp[2*a]][0] != -1:
            route[temp[2*a]][1] = temp[2*a+1]
        else:
            route[temp[2*a]][0] = temp[2*a+1]
    dfs(0)
    print('#{} {}'.format(tc, result))


