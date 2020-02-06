#5356.의석이의 세로로 말해요


T = int(input())

for test_case in range(1, T + 1):
    my_str = []
    str_list = [0 for _ in range(5)]
    max_len = 0
    for i in range(5):
        str_list[i] = input()
        if len(str_list[i]) > max_len:
            max_len = len(str_list[i])
    for i in range(max_len):
        for j in range(5):
            if i <=len(str_list[j])-1:
                my_str.append(str_list[j][i])
    ans = ''.join(my_str)
    print('#{} {}'.format(test_case, ans))