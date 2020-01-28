#3233. 정삼각형 분할 놀이

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    sum = 0
    for i in range(1, int(a/b)+1):
        sum+=2*i-1
    print(f'#{test_case} {sum}')