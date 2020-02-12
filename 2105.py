# 0: 오른쪽 위 1: 왼쪽 위 2: 왼쪽 아래 3:오른쪽 아래
delta = [(-1,1),(-1,-1),(1,-1),(1,1)]


def dfs(sx,sy,dir,shift):
    dx = delta[dir][0]
    dy = delta[dir][1]
    if shift == 3 and (sx,sy) == (a,b):
        counter = len(route[0]) + len(route[1]) + len(route[2]) + len(route[3])
    else:
        if shift == 0:


        elif shift == 1:
        elif shift == 2:
        elif shift == 3:

    route[shift].pop()



def max_dessert(x,y):
    if x== 0 and y == 0:
        return -1
    if x == 0 and y == N-1:
        return -1
    if x ==N-1 and y == 0:
        return -1
    if x == N-1 and y == N-1:
        return -1
    a = x
    b = y
    for dl in range(4):
        counter = -1
        global route
        route = [[],[],[],[]]
        dfs(x,y,i,0)
        if counter > max_count:
            max_count = counter
    return max_count


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    max_val = -1
    for i in range(N):
        for j in range(N):
            md = max_dessert(i, j)
            if md > max_val:
                max_val = md
    print('#{} {}'.format(test_case, max_val))
