#2930. 힙

def max_heapify(arr,i):
    l = 2*i+1
    r = 2*i+2
    length = len(arr)
    if l <= length-1 and arr[l]>arr[i]:
        largest = l
    else:
        largest = i
    if r<=length-1 and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        arr = max_heapify(arr, largest)
        return arr
    else:
        return arr


def build_maxheap(arr):
    if len(arr)==1:
        return arr
    else :
        length = len(arr)
        for i in range(int((length-1)/2), -1, -1):
            arr = max_heapify(arr, i)
        return arr
        

T = int(input())

for test_case in range(1, T + 1):
    heap = list()
    result = list()
    n = int(input())
    for i in range(n):
        cmd = input()
        if cmd[0] =='1':
            a, b = list(map(int,cmd.split()))
            heap.append(b)
        else :
            if heap:
                heap = build_maxheap(heap)
                result.append(heap[0])
                del heap[0]
            else:    
                result.append(-1)
    re_str = ' '.join(result)
    print(f'#{test_case} {re_str}')
    print()    