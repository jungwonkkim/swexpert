#1961 숫자 배열 회전
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    num_list = [list(input().split()) for _ in range(n)]
    print('#{}'.format(test_case))
    for j in range(n):
        my_str = ''
        for a in range(n):
            my_str += num_list[n-1-a][j]
        my_str += ' '
        for b in range(n):
            my_str+=num_list[n-1-j][n-1-b]
        my_str += ' '
        for c in range(n):
            my_str += num_list[c][n-1-j]
        print(my_str)