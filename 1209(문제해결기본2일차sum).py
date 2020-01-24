#1209. s/w 문제해결 기본 2일차 Sum

for test_case in range(1, 11):
    n = int(input())
    list_sum = 0
    d_sum = 0
    num_row = [[0 for _ in range(100)] for _ in range(100)]
    num_column = [[0 for _ in range(100)] for _ in range(100)]
    max_val = 0
    for i in range(100):
        num_list = list(map(int, input().split()))
        for j in range(100):
            num_row[i][j] = num_list[j]
    for i in range(100):
        for j in range(100):
            num_column[i][j] = num_row[j][i]
    for i in range(100):
        list_sum = sum(num_row[i])
        if list_sum>max_val:
            max_val = list_sum
    for i in range(100):
        list_sum = sum(num_column[i])
        if list_sum>max_val:
            max_val = list_sum
    for i in range(100):
        d_sum +=num_row[i][i]
    if d_sum>max_val:
        max_val = d_sum
    d_sum = 0
    for i in range(100):
        d_sum += num_row[i][99-i]
    if d_sum>max_val:
        max_val = d_sum
    print(f'#{n} {max_val}')
                          