#1986 지그재그 숫자


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    if n %2:
        result = int((n+1)/2)
    else:
        result = int(-(n/2))
    print(f'#{test_case} {result}')
   