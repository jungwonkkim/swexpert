#1860. 진기의 최고급 붕어빵

T = int(input())

for test_case in range(1, T + 1):
    n, m ,k = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()
    on_time = True
    for person in range(n):
        if (time[person]//m) *k - person-1<0:
            on_time = False
            break
    if on_time:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')
            
        
        