T = int(input())

for test_case in range(1, T + 1):
    a, b = input().split()
    b = int(b)
    arr = list(a)
    arr = [int(i) for i in a]
    sorted_arr = [i for i in arr]
    sorted_arr.sort()
    sorted_arr.reverse()
    for i in range(len(arr)):
        if b == 0:
            break
        if arr == sorted_arr:
            break
        sliced_arr = arr[i:]
        max_num = max(sliced_arr)
        if arr[i] == max_num:
            pass
        else:
            max_val = i
            for j in range(i+1, len(arr)):
                if arr[max_val] <= arr[j]:
                    max_val = j
            arr[i], arr[max_val] = arr[max_val], arr[i]
            b -= 1
    if b==0:
        if arr.count(max(arr))>=2:
            if arr[-1]>arr[-2]:
                arr[-1], arr[-2] = arr[-2],arr[-1]
    if b>0:
        if b%2 ==0:
            arr = sorted_arr
        else:
            for i in range(len(arr)):
                if arr.count(arr[i]) > 1:
                    arr = sorted_arr
                    break
            else:
                arr[-1],arr[-2] = arr[-2],arr[-1]
    my_str = ''.join([str(i) for i in arr])
    print(f'#{test_case} {my_str}')