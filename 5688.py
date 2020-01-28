#5688. 세제곱근을 찾아라

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    result = 0
    if abs(n**(1/3) - round(n**(1/3),0))<(0.000001):
        result = int(round(n**(1/3),0))
    else:
        result = -1
    print(f'#{test_case} {result}')