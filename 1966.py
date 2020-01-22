#1966번 숫자배열

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case}',end = ' ')
    num_list = input().split()
    num_list = [int(num) for num in num_list]
    num_list.sort()
    for num in num_list:
        print(num, end=' ')
    print()