#3260. 두 수의 덧셈

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    result = a+b
    print(f'#{test_case} {result}')