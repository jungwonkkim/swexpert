#4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색
# 어제 배웠던 이진탐색을 활용. 다만 두번째 end 와 start(R와 L)의 위치가 문제대로라서 조금 다른 점을 유의.

def binarysearch(arr, key):
    L = 0
    R = len(arr)-1
    counter = 0
    while R >= L:
        C = (R+L) // 2
        counter +=1
        if arr[C] == key:
            return counter
        elif arr[C] > key:
            R = C
        else:
            L = C
    return -1



T = int(input())

for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    num_list = [i+1 for i in range(N)]
    A_counter = binarysearch(num_list, A)
    B_counter = binarysearch(num_list, B)
    if A_counter< B_counter:
        result = 'A'
    elif A_counter > B_counter:
        result = 'B'
    else:
        result = 0
    print(f'#{test_case} {result}')