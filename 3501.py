#3501. 순환소수 짧게 표현하기
def check(s,m):
    global q
    global tcnt
    global fcnt
    if s%m == 0:
        return True
    q = m
    while q % 2 == 0:
        q = q//2
        tcnt +=1
    while q % 5 == 0:
        q = q//5
        fcnt +=1
    if q == 1:
        return True
    if s%q == 0:
        return True
    return False

def getlength():
    n = 1
    target = 9
    while target % q !=0:
        n +=1
        target = target*10 + 9
    return n

def gcd(n1, n2):
    while n2 != 0:
        c = n1 % n2
        n1, n2 = n2, c
    return n1

T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    d  = gcd(a,b)
    a = a//d
    b = b//d
    tcnt = 0
    fcnt = 0
    sidx = 0
    if check(a,b):
        if a%b:
            print('#{} {}'.format(test_case, a/b))
        else:
            print('#{} {}'.format(test_case, a//b))
        continue
    if tcnt>fcnt:
        sidx = tcnt
    else:
        sidx = fcnt
    res = ''
    length = getlength()
    res += str(a//b)+'.'
    if sidx:
        for i in range(sidx):
            a = (a%b) * 10
            res += str(a//b)
    res += '('
    for i in range(length):
        a = (a%b) * 10
        res += str(a//b)
    res += ')'
    print('#{} {}'.format(test_case, res))



