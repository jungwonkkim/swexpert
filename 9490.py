#9490.풍선팡

delta =[(0,1),(0,-1),(1,0),(-1,0)]
def pang(x,y):
    sum_pang = confetti[x][y]
    for a in range(1, confetti[x][y]+1):
        for dl in delta:
            dx = dl[0]*a
            dy = dl[1]*a
            if 0 <=x+dx < N and 0 <=y+dy < M:
                sum_pang += confetti[x+dx][y+dy]
    return sum_pang


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    confetti = [list(map(int, input().split())) for _ in range(N)]
    max_con = 0
    for i in range(N):
        for j in range(M):
            if confetti[i][j]:
                pom = pang(i, j)
            if pom > max_con:
                max_con = pom
    print('#{} {}'.format(test_case,max_con))
