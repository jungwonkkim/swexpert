def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global cnt
    lenl, lenr = len(left), len(right)
    sortedarr = [0 for _ in range(lenl+lenr)]
    li, ri = 0, 0
    i = 0
    if left[-1] > right[-1]:
        cnt += 1
    while li != lenl and ri != lenr:
        if left[li] <= right[ri]:
            sortedarr[i] += left[li]
            i += 1
            li += 1
        else:
            sortedarr[i] += right[ri]
            i += 1
            ri += 1
    if li != lenl:
        while li != lenl:
            sortedarr[i] += left[li]
            i += 1
            li += 1
    if ri != lenr:
        while ri != lenr:
            sortedarr[i] += right[ri]
            i += 1
            ri += 1
    return sortedarr


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = mergesort(arr)

    print('#{} {} {}'.format(test_case, arr[N//2], cnt))