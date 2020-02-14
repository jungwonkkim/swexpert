import sys

sys.setrecursionlimit(3000)

#백준1012. 유기농배추
def worm(i,j):
    farm[i][j] = 0
    if i< N-1 and farm[i+1][j]:
        worm(i+1,j)
    if i>0 and farm[i-1][j]:
        worm(i-1,j)
    if j>0 and farm[i][j-1]:
        worm(i, j-1)
    if j< M-1 and farm[i][j+1]:
        worm(i, j+1)


T = int(input())
for test_case in range(T):
    M, N, K = map(int, input().split())
    farm = [[0 for _ in range(M)]for _ in range(N)]
    worm_count = 0
    for c in range(K):
        X, Y = map(int,input().split())
        farm[Y][X] = 1
    for a in range(N):
        for b in range(M):
            if farm[a][b]:
                worm_count+=1
                worm(a,b)
    print(worm_count)