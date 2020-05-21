from copy import deepcopy

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    visited = [False for _ in range(1000001)]
    cnt = 0
    deque = [N]
    while True:
        flag = False
        new_queue = []
        for d in deque:
            if d == M:
                flag = True
                break
            if d+1<=1000000 and visited[d+1] == False:
                visited[d+1]= True
                new_queue.append(d+1)
            if d-1<=1000000 and visited[d-1] == False:
                visited[d-1]= True
                new_queue.append(d-1)
            if d*2<=1000000 and visited[d*2] == False:
                visited[d*2]= True
                new_queue.append(d*2)
            if d-10<=1000000 and visited[d-10] == False:
                visited[d-10]= True
                new_queue.append(d-10)
        if flag:
            break
        cnt+=1
        deque = deepcopy(new_queue)

    print('#{} {}'.format(test_case, cnt))