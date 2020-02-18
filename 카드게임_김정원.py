def RSP(a, b):
    if num_list[a] == num_list[b]:
        return a
    if num_list[a] == 3 and num_list[b] == 1:
        return b
    if num_list[a] == 1 and num_list[b] == 3:
        return a
    if num_list[a] > num_list[b]:
        return a
    return b

def partition(arr):
    if len(arr)==1:
        return arr
    elif len(arr) ==2:
        res = RSP(arr[0], arr[1])
        if arr[0] == res:
            return [arr[0]]
        else:
            return [arr[1]]
    else:
        if len(arr)%2 ==0:
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2:]
        else:
            left = arr[:len(arr)//2+1]
            right = arr[len(arr)//2+1:]
        return partition(partition(left) + partition(right))

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    idx_list = [i for i in range(N)]
    result = partition(idx_list)
    print(result[0]+1)


