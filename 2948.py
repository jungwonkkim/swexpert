#2948. 문자열 교집합

T = int(input())
for test_case in range(1, T + 1):
    a , b  = map(int, input().split())
    list_a = set(input().split())
    list_b = set(input().split())
    set_gyo = list_a & list_b
    c = len(set_gyo)
    print(f'#{test_case} {c}')