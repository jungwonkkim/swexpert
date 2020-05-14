"""
python 의 sort 메서드가 퀵정렬이라는데 sort 메서드를 쓰면
퀵 정렬을 쓴건가..라는 생각을 해보지만 아니겠져..죄송해여...
"""



def quicksort(low, high):
    if high <= low:
        return
    mid = partition(low, high)
    quicksort(low, mid-1)
    quicksort(mid, high)

def partition(low, high):
    global arr
    p = (low+high)//2
    pivot = arr[p]
    while low<=high:
        while arr[low] < pivot:
            low +=1
        while arr[high] > pivot:
            high -=1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low+1, high -1
    return low



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(0, N-1)
    print(arr)
    print('#{} {}'.format(test_case, arr[N//2]))