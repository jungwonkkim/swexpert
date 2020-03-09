#3234. 준환이의 양팔저울

def weigh(idx, left, right):
    global cnt
    if idx == N:
        cnt +=1
        return
    if idx == 0:
        for w in weights:
            weigh(1, [w], [])
        return
    for w in weights:
        if w not in left and w not in right:
            left.append(w)
            weigh(idx+1, left, right)
            left.pop()
            if sum(right) + w <= sum(left):
                right.append(w)
                weigh(idx+1, left, right)
                right.pop()

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    cnt = 0
    weigh(0, [] ,[])
    print('#{} {}'.format(test_case, cnt))