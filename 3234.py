#3234. 준환이의 양팔저울

def weigh(idx, left, right):
    global cnt
    if idx == N:
        for l in left:
            if l in right:
                return
        cnt +=1
        return
    for w in weights:
        if w in left or w in right:
            continue
        if sum(left)+w <= sum(right):
            left.append(w)
            weigh(idx+1, left, right)
            left.pop()
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