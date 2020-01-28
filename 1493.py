#1493. 수의 새로운 연산

standard_num = [int(i*(i-1)/2) for i in range(1,300)]

def encode(n):
    for num in range(300):
        if n>standard_num[num] and n<=standard_num[num+1]:
            k = standard_num[num+1] - n
            break
    return num+1-k,1+k

def decode(x,y):
    num = standard_num[x+y-1] -y+1
    return num

T = int(input())
for test_case in range(1, T+1):
    a,b = map(int, input().split())
    xa, ya= encode(a)
    xb, yb = encode(b)
    result = decode(xa+xb, ya+yb)
    print(f'#{test_case} {result}')