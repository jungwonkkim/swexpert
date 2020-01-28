#3142. 영준이와 신비한 뿔의 숲
T = int(input())

for test_case in range(1, T + 1):
    m, n = map(int,input().split())
    a= m-n
    b= n-a
    print(f'#{test_case} {b} {a}')
