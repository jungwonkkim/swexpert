def backtracking(idx):
    global c
    global min_change
    if idx >= N:
        if min_change > c:
            min_change = c
        return
    if c >= min_change:
        return
    for i in range(idx+stations[idx], idx, -1):
        c +=1
        backtracking(i)
        c -=1



T = int(input())
for test_case in range(1, T+1):
    stations = list(map(int, input().split()))[1:]
    N = len(stations)
    c = -1
    min_change = N+1
    backtracking(0)
    print('#{} {}'.format(test_case, min_change))


