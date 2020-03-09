#4014. [모의 SW 역량테스트] 활주로 건설
def runable(arr):
    stack = []
    a = -1
    while True:
        a+=1
        if a==N:
            return True
        if a == 0 or arr[a] == arr[a-1]:
            stack.append(arr[a])
            continue
        if arr[a] > arr[a-1]+1 or arr[a] < arr[a-1]-1:
            return False
        if arr[a] == arr[a-1]+1:
            if len(stack)>= X:
                stack = [arr[a]]
                continue
            else:
                return False
        if arr[a] == arr[a-1]-1:
            for b in range(a, a+X):
                if b >= N or arr[b] != arr[a]:
                    return False
            stack = []
            a = a+X-1
            continue

T = int(input())
for test_case in range(1, T+1):
    N, X = map(int, input().split())
    runway = [list(map(int, input().split())) for _ in range(N)]
    runway_flip = [[runway[j][i] for j in range(N)] for i in range(N)]
    cnt = 0
    for i in range(N):
        if runable(runway[i]):
            cnt+=1
        if runable(runway_flip[i]):
            cnt +=1
    print('#{} {}'.format(test_case, cnt))