#배열 돌리기 4
import itertools
import copy

def turn (arr, command):
    global min_val
    while command:
        r, c, s = command.pop()
        for k in range(1, s+1):
            temp = arr[r-k][c-k]
            for a in range(r-k, r+k):
                arr[a][c-k] = arr[a+1][c-k]
            for b in range(c-k, c+k):
                arr[r+k][b] = arr[r+k][b+1]
            for d in range(r+k, r-k, -1):
                arr[d][c+k] = arr[d-1][c+k]
            for e in range(c+k, c-k+1, -1):
                arr[r-k][e] = arr[r-k][e-1]
            arr[r-k][c-k+1] = temp
    for row in range(N):
        sum_val = sum(arr[row])
        if min_val > sum_val:
            min_val = sum_val

N, M, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
min_val = 100 * N * M
cmd_list = []
for t in range(K):
    R, C, S = map(int, input().split())
    cmd_list.append((R-1,C-1,S))
permuted = list(map(list,itertools.permutations(cmd_list)))
for p in permuted:
    temp_array = copy.deepcopy(array)
    turn(temp_array,p)
print(min_val)