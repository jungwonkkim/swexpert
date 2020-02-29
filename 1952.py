#1952 수영장

def dfs(exp, idx):
    global min_val
    if idx >= 12:
        if min_val > exp:
            min_val = exp
        return
    if month[idx]*ticket[0] < ticket[1]:
        dfs(exp+month[idx]*ticket[0], idx+1)
    else:
        dfs(exp+ticket[1], idx+1)
    if month[idx]:
        dfs(exp+ticket[2], idx+3)


T = int(input())

for test_case in range(1, T+1):
    ticket = list(map(int, input().split()))
    month = list(map(int, input().split()))
    min_val = ticket[3]
    dfs(0,0)
    print('#{} {}'.format(test_case, min_val))