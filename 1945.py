#1945 소인수분해

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    a =0
    b =0
    c = 0
    d =0
    e =0
    while (n%2==0):
        n=int(round(n/2,0))
        a+=1
    while (n%3==0):
        n=int(round(n/3,0))
        b+=1
    while (n%5==0):
        n=int(round(n/5,0))
        c+=1
    while (n%7==0):
        n=int(round(n/7,0))
        d+=1
    while (n%11==0):
        n=int(round(n/11,0))
        e+=1
    print(f'#{test_case} {a} {b} {c} {d} {e}')
              
        