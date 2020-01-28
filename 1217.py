#1217.거듭제곱

def zegop(a,b):
    if b == 0:
        return 1
    elif b ==1:
        return a
    else :
        return zegop(a,b-1) * a

for test_case in range(1, 11):
    n = int(input())
    a , b = map(int, input().split())
    result = zegop(a, b)
    print(f'#{n} {result}')
