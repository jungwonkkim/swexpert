"""
swea 5188 최소합
code written by jungwonkkim
"""

def dfs(x, y, sum_val):
    global min_val
    sum_val += numbers[x][y]
    if x==y==N-1:
        if min_val >sum_val:
            min_val = sum_val
        return
    if x < N-1:
        dfs(x+1, y, sum_val)
    if y < N-1:
        dfs(x, y+1, sum_val)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    min_val = 16901
    numbers = [list(map(int, input().split())) for _ in range(N)]
    dfs(0, 0, 0)
    print('#{} {}'.format(test_case, min_val))
