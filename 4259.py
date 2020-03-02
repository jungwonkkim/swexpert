#4259. 제곱수의 합 계산하기

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    res = 0
    for num in num_list:
        res += (num//10) ** (num%10)
    print('#{} {}'.format(test_case, res))
