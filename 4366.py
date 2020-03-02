#4366. 정식이의 은행업무
def binary_decode(num):
    res = 0
    for i in range(len(num)-1,-1,-1):
        res += int(num[i]) * (2**(len(num)-i-1))
    return res

def tri_decode(num):
    res = 0
    for i in range(len(num)-1,-1,-1):
        res += int(num[i]) * (3**(len(num)-i-1))
    return res

def binary_encode(num):
    res = ''
    while num >1:
        if num%2:
            res = '1' + res
        else:
            res = '0' + res
        num = num//2
    return int(res)


T = int(input())
for test_case in range(1, T+1):
    a = input()
    b = input()
    tri = tri_decode(b)
    cnt = 0
    for n in range(len(a)-1,-1,-1):
        if a[n] =='1':
            

    print('#{} {}'.format(test_case, result))