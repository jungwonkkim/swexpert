T = int(input())

for test_case in range(1, T + 1):
    num_list = input().split()
    number_list = [int(num) for num in num_list]
    print(f'#{test_case} {max(number_list)}')