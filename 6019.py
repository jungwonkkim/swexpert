#6019. 기차 사이의 파리

T = int(input())

for test_case in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    f_dist = (D / (A+B) * F)
    print(f'#{test_case} {f_dist}')
