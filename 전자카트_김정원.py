"""
swea 5189 전자카트
code written by jungwonkkim
"""

def dfs(arr, sum_val):
    global min_val
    if len(arr) == N-1:
        sum_val += areas[arr[-1]][0]
        if min_val > sum_val:
            min_val = sum_val
        return
    for idx in range(1, N):
        if idx not in arr:
            arr.append(idx)
            dfs(arr, sum_val + areas[arr[-2]][arr[-1]])
            arr.pop()


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    min_val = N * 100
    areas = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        dfs([i], areas[0][i])
    print('#{} {}'.format(test_case, min_val))