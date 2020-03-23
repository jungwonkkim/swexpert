#백준 505대회 1. 스티커 붙이기
#code created by jungwonkkim
from copy import deepcopy

def rotate(arr):
    new_arr = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for a in range(len(arr[0])):
        for b in range(len(arr)):
            new_arr[a][b] = arr[len(arr)-b-1][a]
    return new_arr

def put(arr, idx):
    global max_cnt
    if idx == K:
        cnt = 0
        for a in range(N):
            for b in range(M):
                if arr[a][b] == 1:
                    cnt +=1
        if max_cnt < cnt:
            max_cnt = cnt
        return
    put(arr, idx+1)
    r = 0
    while r<4:
        stickers[idx] = rotate(stickers[idx])
        for a in range(N-len(stickers[idx])+1):
            for b in range(M-len(stickers[idx][0])+1):
                s_cnt = 0
                b_cnt = 0
                for c in range(len(stickers[idx])):
                    for d in range(len(stickers[idx][0])):
                        if stickers[idx][c][d] == 1:
                            s_cnt +=1
                            if arr[a+c][b+d] == 0:
                                b_cnt +=1
                if s_cnt == b_cnt:
                    new_arr = deepcopy(arr)
                    for c in range(len(stickers[idx])):
                        for d in range(len(stickers[idx][0])):
                            if stickers[idx][c][d] == 1:
                                new_arr[a+c][b+d] = 1
                    put(new_arr, idx+1)




N, M, K = map(int, input().split())
paper = [[0 for _ in range(M)] for _ in range(N)]
stickers = [[] for _ in range(K)]
for i in range(K):
    R, C = map(int, input().split())
    stickers[i] = [list(map(int, input().split())) for _ in range(R)]
max_cnt = 0
put(paper, 0)
print(max_cnt)



