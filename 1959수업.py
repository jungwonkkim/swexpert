def max_sum(list1, list2):
    diff = len(list1) - len(list2)
    max_val = 0
    for i in range(diff+ 1):
        value = 0
        for j in range(len(list2)):
            value += list1[j + i] * list2[j]
        if value > max_val:
            max_val = value
    return max_val


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))
    sum_val = 0
    if N > M:
        sum_val = max_sum(list_A, list_B)
    else:
        sum_val = max_sum(list_B, list_A)
    print('#{} {}'.format(test_case, sum_val))
