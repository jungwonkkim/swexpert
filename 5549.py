#5549. 홀수일까 짝수일까

T = int(input())

for test_case in range(1, T + 1):
    num_list = list(input())
    result = ''
    if int(num_list[-1])%2:
        result = 'Odd'
    else:
        result = 'Even'
    print(f'#{test_case} {result}')