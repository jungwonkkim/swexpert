#4751. 다솔이의 다이아몬드 장식

T = int(input())

for test_case in range(1, T + 1):
    str_list = list(input())
    n = len(str_list)
    my_str_1 = '..#.'*n+'.'
    my_str_2 = '.#'*(2*n)+'.'
    my_str_3 = ''
    for char in str_list:
        my_str_3 = my_str_3+ '#.'+char+'.'
    my_str_3 = my_str_3 +'#'
    print(my_str_1)
    print(my_str_2)
    print(my_str_3)
    print(my_str_2)
    print(my_str_1)