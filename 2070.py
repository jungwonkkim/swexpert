T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a,b = input().split()
    c=int(a)
    d=int(b)
    if c<d:
        print(f'#{test_case} <')
    elif c==d:
        print(f'#{test_case} =')
    else:
        print(f'#{test_case} >')