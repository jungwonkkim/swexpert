#4299. 태혁이의 사랑은 타이밍

T = int(input())

for test_case in range(1, T + 1):
    d,h,m = map(int,input().split())
    result = 0
    if m<11:
        h -=1
        m = m+49
    else:
        m= m-11
    if h<11:
        d-=1
        h= h+13
    else:
        h = h-11
    if d<11:
        result = -1
    else:
        d= d-11
        result = m+60*h + 60*24*d
    print(f'#{test_case} {result}')
        
