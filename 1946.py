T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    b = 0
    my_str = ''
    print(f'#{test_case}')
    for num in range(1,N + 1):
        num_list = input().split()
        a = int(num_list[1])
        b+=a
        my_str+=(f'{num_list[0]}'*a)
    for i in range(b//10+1):
        print(my_str[0+10*i:10*(i+1)])
    