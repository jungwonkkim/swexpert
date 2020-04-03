#피자 굽기

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    queue = [i for i in range(M)]
    queue2 = []
    for i in range(N):
        queue2.append(queue.pop(0))
    q = 0
    while True:
        pizzas[queue2[q]] //= 2
        if pizzas[queue2[q]] == 0:
            if queue:
                queue2[q] = queue.pop(0)
                q += 1
            else:
                queue2.pop(q)
            if len(queue2) == 1:
                break
        else:
            q += 1
        if q == len(queue2):
            q = 0
    print('#{} {}'.format(test_case, queue2[0] + 1))
