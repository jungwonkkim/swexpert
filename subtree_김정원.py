T = int(input())

for test_case in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[0,0] for i in range(E+2)]
    e_info = tuple(map(int, input().split()))
    for idx in range(E):
        if tree[e_info[2*idx]][0]:
            tree[e_info[2*idx]][1] = e_info[2*idx+1]
        else:
            tree[e_info[2*idx]][0] = e_info[2*idx+1]
    queue = [N]
    ans = 1
    while queue:
        search = queue.pop(0)
        if tree[search][0]:
            queue.append(tree[search][0])
            ans+=1
        if tree[search][1]:
            queue.append(tree[search][1])
            ans+=1
    print('#{} {}'.format(test_case, ans))
