#1961 숫자 배열 회전
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    meta_num_list = []
    print(f'#{test_case}')
    for i in range(1, n+1):
        num_list = input().split()
        num_list = [int(num) for num in num_list]
        meta_num_list.append(num_list)
    for j in range(n):
        my_str = ''
        for i in range(n):
            my_str += str(meta_num_list[n-1-i][j])
        my_str += ' '
        for i in range(n):
            my_str+=str(meta_num_list[n-1-j][n-1-i])
        my_str += ' '
        for i in range(n):
            my_str += str(meta_num_list[i][n-1-j])
        print(my_str)
      