#수 찾기
def binarysearch(arr, key):
    start = 0
    end = len(arr)-1 
    while end >= start:
        half = (start + end) // 2
        if arr[half] == key:
            return 1
        elif arr[half] > key:
            end = half-1
        else:
            start = half+1
    return 0



n = int(input())
num_list = list(map(int,input().split()))
num_list.sort()
m = int(input())
search_list = list(map(int,input().split()))
for i in range(m):
    print(binarysearch(num_list, search_list[i]))