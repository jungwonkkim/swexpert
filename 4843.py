#4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

def bubblesort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j+1]<arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list = bubblesort(num_list)
    new_list = []
    counter = 0
    while counter<10:
        new_list.append(str(num_list[-1]))
        del num_list[-1]
        new_list.append(str(num_list[0]))
        del num_list[0]
        counter+=2
        
    result = ' '.join(new_list)
    print(f'#{test_case} {result}')