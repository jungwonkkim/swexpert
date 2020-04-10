for test_case in range(10):
    V, E = map(int, input().split())
    arr = [[[] for _ in range(2)] for _ in range(V)]
    cmd = list(map(int, input().split()))
    for i in range(E):
        arr[cmd[2*i]-1][1].append(cmd[2*i+1]-1)
        arr[cmd[2*i+1]-1][0].append(cmd[2*i]-1)
    size = V
    ans = ''
    while size > 0:
        for i in range(V):
            if arr[i][0] or arr[i][1] == -1:
                continue
            else:
                ans += '{} '.format(i+1)
                size -= 1
                for ele in arr[i][1]:
                    arr[ele][0].remove(i)
                arr[i][1] = -1
    print('#{} {}'.format(test_case+1,ans[:-1]))