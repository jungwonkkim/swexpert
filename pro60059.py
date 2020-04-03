#자물쇠와 열쇠
def fit(k, l, x, y):
    N = len(l)
    M = len(k)
    right = [[False for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if l[a][b]:
                right[a][b] = True
    for i in range(x, M+x):
        if i >= N or i<0:
            continue
        for j in range(y, M+y):
            if j >=N or j<0:
                continue
            if k[i-x][j-y]:
                if right[i][j]:
                    return False
                else:
                    right[i][j] = True
    for i in range(N):
        for j in range(N):
            if right[i][j] == False:
                return False
    return True

def rotate(arr):
    M = len(arr)
    new = [[0 for _ in range(M)]for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new[i][j] = arr[M-1-j][i]
    return new


def solution(key, lock):
    N = len(lock)
    M = len(key)
    cnt = 0
    while cnt<4:
        xplus = -M+1
        while xplus < N:
            yplus = -M+1
            while yplus<N:
                if fit(key, lock, xplus, yplus):
                    return True
                else:
                    yplus+=1
            xplus+=1
        key = (rotate(key))
        cnt +=1

    return False

