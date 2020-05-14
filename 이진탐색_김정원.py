T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    sorted_N = sorted(list(map(int, input().split())))
    sorted_M = sorted(list(map(int, input().split())))
    cnt = 0
    for key in sorted_M:
        flag = 0
        low = 0
        high = N-1
        while low <= high:
            mid = (low + high) // 2
            if key == sorted_N[mid]:
                cnt += 1
                break
            elif key > sorted_N[mid]:
                low = mid + 1
                if flag == 1:
                    break
                flag = 1
            else:
                high = mid - 1
                if flag == -1:
                    break
                flag = -1

    print('#{} {}'.format(test_case, cnt))



