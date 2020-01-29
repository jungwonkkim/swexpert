#6692. 다솔이의 월급 상자

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    p_list = [0]*n
    salary = 0
    for i in range(n):
        a, b = map(float, input().split())
        p_list[i] = a*b
    for i in range(n):
        salary += p_list[i]
    print(f'#{test_case} {format(salary,".6f")}')