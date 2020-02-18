#4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

def dfs(x):
    global select_list
    global min_sum
    global sum_val
    if x == N:
        if min_sum>sum_val:
            min_sum = sum_val
    else:
        for j in range(N):
            if j not in select_list and num_list[x][j]+ sum_val < min_sum:
                sum_val += num_list[x][j]
                select_list.append(j)
                dfs(x+1)
                select_list.pop()
                sum_val -= num_list[x][j]



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10000
    for i in range(N):
        sum_val = num_list[0][i]
        select_list = [i]
        dfs(1)
    print('#{} {}'.format(test_case, min_sum))
