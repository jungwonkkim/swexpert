T = int(input())

for test_case in range(1, T + 1):
    num_list = input().split()
    avg = 0
    for num in num_list:
        avg+=int(num)
    print(f'#{test_case} {int(round(avg/10,0))}')    