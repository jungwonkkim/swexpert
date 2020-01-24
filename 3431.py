#3431 준환이의 운동관리 (레벨3치고 굉장히 쉬움)

T = int(input())

for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    result = 0
    if X>U:
        result = -1
    elif X<L:
        result = L-X
    else:
        result = 0
    print(f'#{test_case} {result}')