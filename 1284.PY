def sudoexp(arr_list):
    a=0
    b=0
    a = arr_list[4]*arr_list[0]
    if arr_list[4]<=arr_list[2]:
        b = arr_list[1]
    else:
        b = (arr_list[1]) + (arr_list[3]*(arr_list[4]-arr_list[2]))
    if a<b:
        return a
    else:
        return b



T = int(input())

for test_case in range(1, T + 1):
    arr = input().split()
    num_list = [int(num) for num in arr]
    expense = sudoexp(num_list)
    print(f'#{test_case} {expense}')